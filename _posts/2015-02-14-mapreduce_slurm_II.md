---
layout: post
title: "MapReduce-like operations across jobs in cluster - part II"
description: ""
category: research
tags: [programming, python, slurm, cluster]
---
{% include JB/setup %}

In [my previous post](/_posts/2015-02-02-mapreduce_slurm.md) concerning interactive (*e.g.* during a `IPython` session) parallelization of tasks with a MapReduce-like aproach across nodes in a cluster, I created an object which interfaces Slurm and the interactive session I'm working on, by splitting an input in pools and submitting each pool as a job that would be further processed in parallel.

Since the class was performing two distinct functions (handling jobs, splitting input in a task-dependent manner), I split it into two classes: `DivideAndSlurm` - which takes care of job processing; `Task` which is a meta-class for different tasks which can be parallelized this way.

`Task` subclasses should be created for a particular class, inheriting from the meta one, allowing little effort when writing new classes, since basically what changes between tasks is (1) the location of the script which actually will compute the output, and (2) how the output is reduced when collected, since different output objects should be reduced differently (*e.g.* `collections.Counter` objects can be reduced by summation, but `list` or `dict` ones no (although here I might get smarter and write general colllection methods for different output types).

The basic usage now looks like this:

{% highlight python %}
from divideAndSlurm import DivideAndSlurm, Task

slurm = DivideAndSlurm() # create instance of object
regions = [promoters, genes] # data is iterable with iterables - each is a separate task with multiple regions

for region in regions: # Add several tasks:
	task = Task(region, 20, bamFile) # Add new task - syntax: data, fractions, *aditional arguments
    slurm.add_task(task)  # Add task to slurm invokes the splitting of the data, and talk between objects
	slurm.submit(task)  # Submit the task

regionsOutput = dict()
for task in slurm.tasks:
    if task.is_ready():
        regionsOutput[task] = task.collect()

{% endhighlight %}

The meta class `Task` accepts args and kwargs, so inheriting sub-classes can use task-specific options.

I further included many more functions and attributes to handle tasks (`slurm.tasks` or `task.log` attributes) faulty job executions (*e.g.* allowing collection of output even if some jobs would fail - `task.permissive` attribute - off by default), status checking (`task.is_running()`, `task.is_ready()`, `task.has_output()`, `task.failed()`) and handling tasks (`slurm.cancel_task(task)`, `slurm.cancel_all_tasks()`, `slurm.remove_task(task)`).


### Repository
The small library is called [divideAndSlurm](https://github.com/afrendeiro/divideAndSlurm) and includes a setup.py to install.
