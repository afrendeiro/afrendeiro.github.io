---
layout: post
title: "MapReduce-like operations across jobs in cluster"
description: ""
category: research
tags: [programming, python, slurm, cluster]
---
{% include JB/setup %}

MapReduce operations allow parallelization of tasks taking advantage of aditional available cpus. However, one might want to use processors across several nodes in a computing cluster and while several options exist to perform this (with very different aims and scallability options), I didn't feel like there was an option which would allow doing this interactively (for example during a `IPython` session) in a Slurm cluster and without requiring diving into lots of documentation. So obviously, here's my custom solution.

The strategy I followed splits input in pools which are submitted in parallel through jobs to the cluster, each one of them is further processed in parallel using the `multiprocessing` library. This is a middle term between mapping all inputs to different jobs (clogging the cluster) and using only the CPUs available in one machine/node, by controlling the number of jobs that are submitted to the cluster and the size of each pool submitted. This approach was inspired by conversations with Michael Schuster and Nathan Sheffield in my lab.

I create an `object` to manage tasks which can include huge amounts of independent data to process the same way. Each task's input is split in equal(ish)-sized pools and submitted to Slurm as jobs when wanted. For now I take care of tasks using a dict by I will expand this to make a `Task(object)` class, which would take care of them.

I use `subprocess` to keep track of the job IDs Slurm gives to the jobs and this way I can track if they're finished or still running.
Now the task going to be called is written in a separate script that is called by the Slurm job.

The basic usage would be something like this:

{% highlight python %}
slurm = DivideAndSlurm() 			# create instance of object
regions = [promoters, genes]		# data is iterable with iterables - each is a separate task with multiple regions
											
for region in regions:				# Add several tasks:
	taskNumber = slurm.task(region, 20, bamFile) 	# Add new task - syntax: data, fractions, *aditional arguments
	slurm.submit(taskNumber)		# Submit new task

slurm.is_ready(taskNumber)			# check if task is done
output = slurm.collect_distances(taskNumber)	# collect output
{% endhighlight %}

This would submit 20 jobs per task, which would each take further advantage of parallel processing.

The essential code for the class is here:

{% highlight python %}
import os
import time
import subprocess
import cPickle as pickle

class DivideAndSlurm(object):
	"""DivideAndSlurm is a class to handle a map-reduce style submission of jobs to a Slurm cluster."""
	def __init__(self):
		self.tasks = dict()
 
	def _slurmHeader(self):
		command = """			#!/bin/bash
			# Start running the job
			hostname
			date

		""" 
		return command
 
	def _slurmFooter(self):
		command = """
			date # Job end
		"""
		 return command
 
	def _slurmSubmitJob(self, jobFile):
		"""Submit command to shell."""
		command = "sbatch %s" % jobFile
		p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
		return p.communicate()
 
	def _split_data(self, taskName, data, fractions):
		"""Split data in fractions and create pickle objects with them."""
		chunkify = lambda lst,n: [lst[i::n] for i in xrange(n)]
 
		groups = chunkify(data, fractions)
		ids = [taskName + "_" + str(i) for i in xrange(len(groups))]
		files = [os.path.join(self.tmpDir, ID) for ID in ids]
		
		groups = zip(ids, groups, files)				# keep track of groups in self
 
		# serialize groups
		for i in xrange(len(groups)):
			pickle.dump(groups[i][1],					# actual group of objects
				open(groups[i][2] + ".pickle", 'wb'),	# group pickle file
				protocol=pickle.HIGHEST_PROTOCOL
			)
		return groups
 
	def task(self, data, fractions, bam_file, strand_wise=True, fragment_size=1):
		"""Add task to be performed with data."""
		now = string.join([time.strftime("%Y%m%d%H%M%S", time.localtime()) str(random.randint(1,1000))], sep="_")
		taskName = "task_name_{0}".format(now)
		log = taskName + ".log"
 
		# check data is iterable
		if type(data) == dict or type(data) == OrderedDict:
			data = data.items()
 
		# split data in fractions
		groups = self._split_data(taskName, data, fractions)
 
		# make jobs with groups of data
		jobs = list()
		jobFiles = list()
 
		for i in xrange(len(groups)):
			jobFile = groups[i][2] + "_task_name.sh"
			input_pickle = groups[i][2] + ".pickle"
			output_pickle = groups[i][2] + ".output.pickle"
 
			# assemble command for job
			task = "    python perform_task_parallel.py {0} {1} {2} ".format(input_pickle, output_pickle, bam_file)
 
			if strand_wise:
				task += "--strand-wise "
			task += "--fragment-size {0}".format(fragment_size)
 
			# assemble job file
			job = self._slurmHeader(groups[i][0], log, queue=self.queue, userMail=self.userMail) + task + self._slurmFooter()
 
			# keep track of jobs and their files
			jobs.append(job)
			jobFiles.append(jobFile)
 
			# write job file to disk
			with open(jobFile, 'w') as handle:
				handle.write(textwrap.dedent(job))
 
		# save task in object
		taskNumber = len(self.tasks)
		self.tasks[taskNumber] = {  # don't keep track of data
			"name" : taskName,
			"groups" : groups,
			"jobs" : jobs,
			"jobFiles" : jobFiles,
			"log" : log
		}
		# return taskNumber so that it can be used later
		return taskNumber
 
	def submit(self, taskNumber):
		"""Submit slurm jobs with each fraction of data."""
		jobIDs = list()
		for i in xrange(len(self.tasks[taskNumber]["jobs"])):
			output, err = self._slurmSubmitJob(self.tasks[taskNumber]["jobFiles"][i])
			jobIDs.append(re.sub("\D", "", output))
		self.tasks[taskNumber]["submission_time"] = time.time()
		self.tasks[taskNumber]["jobIDs"] = jobIDs

	def collect_output(self, taskNumber):
		"""If self.is_ready(taskNumber), return joined data."""
		if taskNumber not in self.tasks:
			raise KeyError("Task number not in object's tasks.")
 
		if "output" in self.tasks[taskNumber]: # if output is already stored, just return it
			return self.tasks[taskNumber]["output"]
 
		# load all pickles into list
		groups = self.tasks[taskNumber]["groups"]
		outputs = [pickle.load(open(groups[i][2] + ".output.pickle", 'r')) for i in xrange(len(groups))]
		# if all are counters, and their elements are counters, sum them
		if all([type(outputs[i]) == Counter for i in range(len(outputs))]):
			output = reduce(lambda x, y: x + y, outputs) # reduce
			if type(output) == Counter:
				self.tasks[taskNumber]["output"] = output    # store output in object
				return self.tasks[taskNumber]["output"]
 
{% endhighlight %}

In a second level of parallelization, a regular map-reduce operation is also employed. Here I request the help of the `parmap` module (a wrapper to `multiprocessing`), since `multiprocessing.map()` does not allow several arguments passed to the function:

{% highlight python %}

import multiprocessing
import parmap
from collections import Counter

def task(singleFeature, bamFile):
	"""Computes something with reads present in a single, specific interval.Returns Counter."""
	# ...
	return Counter

output = reduce(
		lambda x, y: x + y,
		parmap.map(task, features, bamFile
		)
	)

{% endhighlight %}

Also, `collections.Counter` objects are really usefull and one can reduce them by summation.

# Complete example:
I illustrate the complete implementation of the Class with an example which takes several genomic regions (combinations of H3K4me3 or H3K27me3 peaks) and compute an output (coverage, density, etc...) under those peaks.

I add more functions to the main Object to perform tasks such as removal of temporary files (pickles, sh file, logs...) and to check if job is finished and output is of the right form.

{% gist b5e97b429ff7363f5574 %}