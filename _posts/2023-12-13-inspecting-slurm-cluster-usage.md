---
layout: post
title: "Inspecting SLURM cluster usage"
description: "Inspecting SLURM cluster usage"
category: notebook
tags: [slurm, bash]
---
{% include JB/setup %}

As in many academic institutions, we have an HPC cluster with the SLURM scheduler.
While we are fortunate enough to not be limited by the amount of jobs we can submit (and usually) also not by the resources we can use, it is good to be mindful of the resources we use and the efficiency of our jobs in order to save resources for others and to be mindful of the environment.

The `sacct` command can be used to inspect the resources used by a set of jobs, but it is not very convenient to use to get a summary of the usage of the cluster over long periods of time.

I wanted to get a summary of the usage of the cluster for the lab and for each user and partition. To do this, I wrote a simple bash script that runs `sshare` to get the usage of the cluster for all users and partitions and then wrote a python script to process the output and plot the usage. This can be run as a cron job every week to get a timestamped summary of the usage of the cluster over time.

```bash
#!/usr/bin/env bash

mkdir -p ~/cluster_usage/
USERS=$(ls -p /home/ | tr '\n' ',' | sed 's/\///g')
DATE=$(date +%F)
sshare -u $USERS -m -p > ~/cluster_usage/${DATE}.txt
```

```python
#!/usr/bin/env python

from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data_dir = Path("~/cluster_usage").expanduser()
lab_name = "rendeiro_lab"

_df = list()
for f in sorted(data_dir.glob("*.txt")):
    df = pd.read_csv(f, sep="|")
    n = df.isnull().all()
    df = df.loc[:, ~n].dropna()
    for col in df.columns[df.dtypes == "object"]:
        df[col] = df[col].str.strip()
    df = df.assign(date=pd.to_datetime(f.stem))
    _df.append(df)

dfs = pd.concat(_df)
dfs.to_csv(data_dir / "summary.csv", index=False)
dfs = pd.read_csv(data_dir / "summary.csv")

# Plotting (only last date)
df = df.loc[df["RawUsage"] > 0]
labs = df["Account"].unique()
sel_labs = labs[df.groupby("Account")["EffectvUsage"].mean().sort_values() > 0.01]
colors = dict(zip(sel_labs, sns.color_palette("tab20") + sns.color_palette("Paired")))

df = df.loc[df["Account"].isin(sel_labs)]

fig, ax = plt.subplots()
for lab in sel_labs:
    p = df.loc[df["Account"] == lab]
    ax.scatter(p["RawUsage"], p["EffectvUsage"], label=lab, color=colors[lab])
    ax.set(xlabel="RawUsage", ylabel="EffectvUsage", xscale="log")
ax.legend()
fig.savefig(data_dir / "summary.svg", bbox_inches="tight", dpi=300)


queues = df["Partition"].unique()

fig, axes = plt.subplots(1, len(queues), figsize=(5 * len(queues), 5), sharey=True)
for ax, queue in zip(fig.axes, queues):
    for lab in sel_labs:
        p = df.query(f"Account == '{lab}' & Partition == '{queue}'")
        ax.scatter(p["RawUsage"], p["EffectvUsage"], label=lab, color=colors[lab])
        ax.set(xlabel="RawUsage", ylabel="EffectvUsage", xscale="log", title=queue)
    if queue == queues[-1]:
        ax.legend(bbox_to_anchor=(1.05, 1), loc="upper left")
fig.savefig(data_dir / "summary.per_queue.svg", bbox_inches="tight", dpi=300)

df = df.loc[df["Account"].isin([lab_name])]
df["id"] = df["User"] + " " + df["Partition"]
colors = dict(
    zip(df["id"].unique(), sns.color_palette("tab20") + sns.color_palette("Paired"))
)
fig, ax = plt.subplots()
for q in df["id"].unique():
    p = df.loc[df["id"] == q]
    ax.scatter(p["RawUsage"], p["EffectvUsage"], label=q, color=colors[q])
    ax.set(xlabel="RawUsage", ylabel="EffectvUsage", xscale="log")
ax.legend()
fig.savefig(data_dir / f"summary.{lab_name}.svg", bbox_inches="tight", dpi=300)
```
