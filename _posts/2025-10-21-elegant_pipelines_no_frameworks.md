---
layout: post
title: "Elegant processing pipelines with no frameworks"
description: "A minimalist pattern for scalable, reproducible, and concurrency-safe data processing using uv, Zarr, and plain Python - no workflow managers, no containers, minimizing technical debt."
category: engineering
tags: ["python", "reproducibility", "pipelines", "uv", "zarr", "hpc", "minimalism"]
---
{% include JB/setup %}

# Elegant processing pipelines with no frameworks: just `uv`, Zarr, and Python

Large-scale analysis pipelines are often complex, brittle, and fragmented across multiple tools.
They grow organically - one more dependency here, a helper script there, a bash script to submit the job, a YAML configuration to glue it all together - suddenly, you have a system that no one understands, no even future you.

In practice, if you are not making a software package for reuse by others, most of that complexity adds little scientific or engineering value. It only makes the code harder to reason about, harder to reproduce, and harder to maintain.

The cost of that complexity is enormous:

- **Technical debt** accumulates invisibly. Each new "framework" or "helper utility" promises order but instead creates another layer to maintain.
- **Dependency drift** means that six months later, half the code no longer runs because upstream libraries changed APIs or stopped supporting your Python version. (in scientific programming, most data analysis code won't be run by others so environment abstractions via frameworks rarely pay off).
- **Cognitive overhead** explodes: to re-start working or to fix a bug, you first need to remember which workflow manager or config file actually controls execution. How do we specify that? Add one more file/document to glue it all together. Ups.
- **Human frustration** follows: you open your old repository and think, *who was the idiot who wrote this mess?* - before realizing it was you.

For most exploratory or iterative scientific work, the real goal is not to build software infrastructure; it is to **run analyses quickly, clearly, and reproducibly**.
And for that, simplicity is not a luxury — it is an essential design principle.

This post describes a pattern for **scalable, concurrent-safe processing** that is:

- a **single-file**: everything in one portable script
- **robust**: no race conditions, no overwrites, no half-written files
- **scalable**: trivially parallelizable across HPC jobs
- **lightweight**: no external workflow managers or container layers
- and above all, **beautifully simple**

---

## 1. Inline dependencies with `uv`

The traditional advice is to maintain a `requirements.txt`, a `pyproject.toml`, or a Docker container with pinned dependencies.
This is reproducible, but cumbersome — and most importantly, it breaks the principle of *locality*: the code and its dependencies are not in the same place.

[`uv`](https://docs.astral.sh/uv/) fixes this.
Dependencies can be defined directly at the top of the script:

```python
#!/usr/bin/env uv --script
# /// script
# dependencies = ["numpy", "pandas", "zarr", "fasteners"]
# ///
```

That’s it.
Now the script can be executed anywhere with:

```bash
uv run --script process_images.py
```

or if made executable with:

```bash
chmod +x process_images.py  # run once only
./process_images.py
```

No virtual environments to activate, no requirements.txt, no container rebuilds.
The script is self-contained, portable, and reproducible by default.

## 2. Zarr: concurrency-friendly storage

Many pipelines still rely on writing large .h5ad, .npy, or .csv outputs, serialized and rewritten each time.
That design collapses once you distribute work across multiple jobs — it’s fragile, slow, and error-prone.

`Zarr` solves this elegantly.
It stores data as chunked arrays in directories, meaning:

- jobs can write different parts of the dataset concurrently;
- partial results are immediately available;
- failures don’t corrupt the entire dataset;
- and the format is portable across languages and environments.

In other words, Zarr lets you treat disk like a database for large-scale numeric data — perfect for incremental, parallel feature extraction.

## 3. Randomized order and lock files

Traditional HPC workflows try to control parallelism explicitly using SLURM array indices or workflow DAGs.
These approaches create coordination overhead: each job must know which subset to process and where to write.

Instead, randomization and lightweight locks are enough:

```python
np.random.shuffle(files)
np.random.shuffle(model_names)
```

Each worker processes items in random order, minimizing collisions.
When a write must be exclusive (e.g., creating a new Zarr group), a simple interprocess lock ensures safety:

import fasteners
with fasteners.InterProcessLock(lock_file):
    # write metadata or create array


No central controller, no global scheduler, no external state.
Just Python files operating independently, safely, and efficiently.

## 4. Cluster submission: one clean command

People often rely on workflow managers (Snakemake, Nextflow, Cromwell) for job orchestration.
They work well for static pipelines, but for exploratory computational research, they introduce overhead — complex configuration files, extra abstraction layers, and a steep maintenance cost.

Here, we use a single command embedded inside the Python script docstring, so the whole pipeline lives in one place:

```python
"""
Run in cluster with:

echo 'for ID in {00..79}; do
  sbatch --job-name histo.$ID \
         --qos tinyq -p tinyq --time 02:00:00 -c 8 --mem 48G \
         --output logs/processing/tinyq.$ID.log \
         --wrap "uv run --frozen --no-sync python process_images.py"
done' | at now + 2 hours
"""
```

This approach avoids queuing hundreds of jobs simultaneously.
The scheduler stays healthy, you stay in control, and there is still zero Bash boilerplate beyond this one line.

## 5. Why this works better

| Aspect                | Conventional approach                    | This pattern                           |
| --------------------- | ---------------------------------------- | -------------------------------------- |
| Dependency management | `requirements.txt`, Conda, or containers | Inline dependencies via `uv`           |
| Workflow control      | Snakemake / Nextflow / Bash scripts      | Self-contained randomized for-loops    |
| Data output           | Multiple serialized files (.csv, .h5)    | Concurrent-safe Zarr store             |
| Parallelization       | Overhead to setup job arrays with explicit indices         | Randomized distribution across workers |
| Safety                | Risk of overwrite or corruption          | Interprocess locks                     |
| Complexity            | Multiple moving parts                    | One script                             |
| Reproducibility       | Environment files and containers         | Single versioned script                |

This design does not compete with heavy frameworks - it replaces them when you need something simpler, faster, and more reliable.


## 6. A philosophy of simplicity

Modern research software often drifts toward overengineering.
But scaling should not require frameworks within frameworks.

There is beauty in solving large-scale problems with the smallest, most transparent system possible.
This pattern embodies that principle: locality, minimalism, reproducibility.

No workflow managers.
No bash gymnastics.
Just Python, done right.


## 7. Code appendix: minimal runnable example

Below is a minimal, self-contained implementation using uv, zarr, and fasteners.
It demonstrates randomized processing, concurrency-safe writes, and a single embedded job submission snippet.

```python
#!/usr/bin/env uv --script
# /// script
# dependencies = ["numpy", "pandas", "zarr", "fasteners"]
# ///

"""
Minimal example for distributed image processing with uv + Zarr.

Submit a wave of jobs (one-time execution) on the cluster:

echo 'for ID in {00..79}; do
  sbatch --job-name histo.$ID --qos tinyq -p tinyq --time 02:00:00 -c 8 --mem 48G \
         --output logs/processing/tinyq.$ID.log \
         --wrap "uv run --frozen --no-sync python process_images.py"
done' | at now + 2 hours
"""

from pathlib import Path
import numpy as np
import pandas as pd
import zarr
import fasteners


data_dir = Path("data"); data_dir.mkdir(exist_ok=True)
store_dir = Path("processed") / "images.zarr"; store_dir.parent.mkdir(parents=True, exist_ok=True)
locks_dir = Path("locks"); locks_dir.mkdir(exist_ok=True)

# pretend input files
files = sorted(data_dir.glob("*.tif"))
np.random.shuffle(files)

# open or create a Zarr store
root = zarr.open_group(store_dir, mode="a")

def main() -> None:
    for f in files:
        extract(f)

def extract(file: Path) -> None:
    """Process one file and append to Zarr in a concurrency-safe way."""
    arr_name = file.stem
    lock = fasteners.InterProcessLock(locks_dir / f"{arr_name}.lock")
    if arr_name in root:
        print(f"Skip {file.name}: already processed")  # this will be written to log by slurm
        return

    # Simulate some heavy processing
    feats = np.random.rand(4096).astype("float32")
    meta = {"filename": file.name}

    with lock:
        root.create_dataset(arr_name, data=feats, chunks=(512,), overwrite=False)
        root[arr_name].attrs.update(meta)

    print(f"Processed {file.name}")  # this will be written to log by slurm

if __name__ == "__main__":
    main()
```
### Notes:

- uv run with `--frozen` and `--no-sync` ensure deterministic environments across nodes.
- Locks are only used for short metadata operations — heavy computation happens outside.
- Zarr chunking lets you scale I/O efficiently and resume interrupted jobs.


## 8. Final thoughts

This pattern has served me remarkably well for various pipelines that need to run in high-throughput (tens of thousands of tasks, each lasting hours).
It demonstrates that robust, distributed computation does not require complex infrastructure — only careful design.

In many cases, the best workflow manager is none at all.
