---
layout: post
title: "NGS analysis objects with Python decorators"
description: "NGS analysis objects with Python decorators"
category: research
tags: [python, oop, decorators]
---
{% include JB/setup %}

Recently I decided to start encapsulating my analysis into an object which has methods but also holds data from a data analysis.

This is conveninent since I've [implemented classes to handle pipeline objects](2015-06-07-python_objects_for_ngs_projects_samples.md) (projects, samples, annotation sheets).

Still, nothing particularly exciting:

{% highlight python %}

from pipelines import Project

class Analysis(object):
    """
    Class to hold functions and data from analysis.
    """

    def __init__(self, data_dir, plots_dir, samples):
        self.data_dir = data_dir
        self.plots_dir = plots_dir
        self.samples = samples

    def do_some_work(self):
        ...
        self.results = results

prj = Project("testprj")
prj.addSampleSheet("metadata/sample_annotation.csv")

analysis = Analysis("data", "results/plots", prj.samples)
analysis.do_some_work()

{% endhighlight %}

## Python decorators
It would be nice if each time I run a certain functions of the `Analysis` class the class itself would be saved as a Python `pickle`.

**Enter [Python decorators](https://en.wikipedia.org/wiki/Python_syntax_and_semantics#Decorators)**.

If you're new to Python or Python decorators (I've known them for a while but seldomly use them) [here's a really nice introduction](http://simeonfranklin.com/blog/2012/jul/1/python-decorators-in-12-steps/) to *nested functions*, *clojures* and *decorators*.

In this case I write a decorator which calls the function and then performs its action, in this case, pickling the `Analysis` object:

{% highlight python %}

# decorator for some methods of Analysis class
def pickle_me(function):
    def wrapper(obj):
        function(obj)
        pickle.dump(obj, open("analysis.pickle", 'wb'))
    return wrapper

{% endhighlight %}

To apply the decorator the some methods of the class, just add `@pickle_me` to the method:

{% highlight python %}

class Analysis(object):
    ...

    @pickle_me
    def do_some_work(self):
        ...
        self.results = results

{% endhighlight %}

If I give the `Analysis` class an attribute holding where it should be pickled (`pickle_file`), then I can tell the decorator function to get it from the class itself:

{% highlight python %}

# decorator for some methods of Analysis class
def pickle_me(function):
    def wrapper(obj):
        function(obj)
        pickle.dump(obj, open(obj.pickle_file, 'wb'))
    return wrapper

class Analysis(object):
    """
    Class to hold functions and data from analysis.
    """

    def __init__(self, pickle_file, **kwargs):
        self.pickle_file = pickle_file

    @pickle_me
    def do_some_work(self):
        ...
        self.results = results

{% endhighlight %}
