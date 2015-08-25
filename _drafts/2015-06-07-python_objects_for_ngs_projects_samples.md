---
layout: post
title: "Python objects for NGS projects and samples"
category: research
tags: [python, oop]
---
{% include JB/setup %}

I've been using [Python programs to manage NGS sample pipelines](https://github.com/afrendeiro/pipelines) for a while, and while it started slowly, they're in a state in which the code is much more reliable and I can work much faster.

A big part of it was due to some simple object modeling of projects and samples.
Here's the basics of what I implemented. See the full code at [github](https://github.com/afrendeiro/pipelines/blob/master/pipelines/models.py).

## A *Project* object

In its simplest form, a project object holds attributes and defines and creates (if necessary) a directory structure.
Here's how I chose to structure my projects:

```
parent
|___name
    |___data
    |___results
    |   |___plots
    |___runs
       |___executables
       |___pickles
       |___logs
```

So, all the `Project` object takes as argument is `name` and `parent`. The structure is then created when `__init__` (which is called automatically upon creation of the object), calling in its turn `setProjectDirs` and `makeProjectDirs`.


```python
import os as _os


class Paths(object):
    """A class to hold paths as attributes."""
    pass


class Project(object):
    """A class to model a project.

    :param name: Project name.
    :type name: str
    :param parent: Path to where the project structure will be created.
    :type parent: str
    """
    def __init__(self, name, parent):
        super(Project, self).__init__()
        self.name = name
        self.dirs = Paths()

        self.setProjectDirs()
        self.makeProjectDirs()

    def setProjectDirs(self):
        """Atributes directories for the project."""
        self.dirs.root = _os.path.join(self.dirs.parent, self.name)
        self.dirs.runs = _os.path.join(self.dirs.root, "runs")
        self.dirs.pickles = _os.path.join(self.dirs.runs, "pickles")
        self.dirs.executables = _os.path.join(self.dirs.runs, "executables")
        self.dirs.logs = _os.path.join(self.dirs.runs, "logs")
        self.dirs.data = _os.path.join(self.dirs.root, "data")
        self.dirs.results = _os.path.join(self.dirs.root, "results")
        self.dirs.plots = _os.path.join(self.dirs.results, "plots")

    def makeProjectDirs(self):
        """Creates project directory structure if it doesn't exist."""
        for name, path in self.dirs.__dict__.items():
            if not _os.path.exists(path):
                _os.makedirs(path)

```

## A *Sample* object

I decided to have my `Sample` objects created from a Pandas `Series`, since sample annotation sheet are often in tabular form and can easily be read with Pandas.

I wanted something like:

```python
import pandas as pd

series = pd.Series(
    ["ChIP-seq", "hg19", "/data/samples/test.bam"],
    index=["technique", "genome", "unmappedBam"]
)
sample = Sample(series)
```

I first considered creating `Sample` inheriting from `pandas.Series` to take advantage of its already implemented methods, but in the end it was lacking some features (tab-completion in iPython wasn't showing the methods I defined). Also, compatibility with new Pandas versions was not guarenteed. Therefore, I simply assign the pandas `Series` attributes to a new `Sample` object.

The directory structure if sample-centric: all files from a sample are under a sample-specific directory, and then, other sub-directories hold more specific files:

```python
class Sample(object):
    """
    Class to model NGS samples.

    :param series: Pandas `Series` object.
    :type series: pandas.Series
    """
    def __init__(self, series):
        # Passed series must either be a pd.Series or a daughter class
        if not isinstance(series, _pd.Series):
            raise TypeError("Provided object is not a pandas Series.")
        super(Sample, self).__init__()

        # Set series attributes on self
        for key, value in series.to_dict().items():
            setattr(self, key, value)

        self.dirs = Paths()

    def setFilePaths(self):
        """Sets the paths of all files for this sample."""
        self.dirs.sampleRoot = _os.path.join(self.project.dirs.data, self.name)

        # Files in the root of the sample dir
        self.fastqc = self.dirs.sampleRoot
        # Unmapped: merged bam, fastq, trimmed fastq
        self.dirs.unmapped = _os.path.join(self.dirs.sampleRoot, "unmapped")
        self.unmapped = _os.path.join(self.dirs.unmapped, self.name + ".bam")
        self.fastq = _os.path.join(self.dirs.unmapped, self.name + ".fastq")
        self.trimmed = _os.path.join(self.dirs.unmapped, self.name + ".trimmed.fastq")
        # Mapped: mapped, duplicates marked, removed, reads shifted
        self.dirs.mapped = _os.path.join(self.dirs.sampleRoot, "mapped")
        self.mapped = _os.path.join(self.dirs.mapped, self.name + ".trimmed.bowtie2.bam")
        self.filtered = _os.path.join(self.dirs.mapped, self.name + ".trimmed.bowtie2.filtered.bam")

    def makeSampleDirs(self):
        """Creates sample directory structure if it doesn't exist."""
        for path in self.dirs.__dict__.values():
            if not _os.path.exists(path):
                _os.makedirs(path)

```

#### *Sample* methods
I create some useful methods for the samples.

I check if it contains required attributes and if these aren't `nan`:

```python
def checkValid(self):
    """Check if any of its important attributes is None."""
    req = ["technique", "genome", "unmappedBam"]

    if not all([hasattr(self, attr) for attr in req]):
        raise ValueError("Required values for sample do not exist.")

    if any([attr == "nan" for attr in req]):
        raise ValueError("Required values for sample are empty.")
```

I create a name for a sample from every non-`nan` attribute it might contain from a specific list:

```python
def generateName(self):
    """Generates a name for the sample by joining some of its possible attribute strings."""
    self.name = "_".join(
        [str(self.__getattribute__(attr)) for attr in [
            "cellLine", "numberCells", "technique", "ip",
            "patient", "patientID", "sampleID", "treatment", "condition",
            "biologicalReplicate", "technicalReplicate",
            "experimentName", "genome"] if hasattr(self, attr) and str(self.__getattribute__(attr)) != "nan"]
    )

```

## A *SampleSheet* object

Obviously, always creating a new Pandas `Series`, just to pass it to `Sample` does not make much sense.

I created a new class which loads a sample annotation sheet form a csv file 
and creates samples from it.

```python
class SampleSheet(object):
    """
    Class to model a sample annotation sheet.

    :param csv: Path to csv file.
    :type csv: str
    """
    def __init__(self, csv):

        super(SampleSheet, self).__init__()
        # TODO: checks on given args
        self.csv = csv
        self.samples = list()
        self.checkSheet()

    def checkSheet(self):
        """
        Check if csv file exists and has all required columns.
        """
        try:
            self.df = _pd.read_csv(self.csv)
        except IOError("Given csv file couldn't be read.") as e:
            raise e

        req = ["technique", "genome", "unmappedBam"]
        missing = [col for col in req if col not in self.df.columns]

        if len(missing) != 0:
            raise TypeError("Annotation sheet is missing columns: %s" % " ".join(missing))
```

#### *SampleSheet* methods

Obviously methods to create samples from the `SampleSheet` (either from a single pandas `Series` or from the whole sheet:

```python
    def makeSample(self, series):
        """
        Make a children of class Sample dependent on its "technique" attribute.

        :param series: Pandas `Series` object.
        :type series: pandas.Series
        :return: An object or class `Sample` or a child of that class.
        :rtype: pipelines.Sample
        """
        if technique in ["chipseq", "atac-seq"]:
            return Sample(series)
        else:
            raise TypeError("Sample is not in known technique.")

    def makeSamples(self):
        """
        Creates samples from annotation sheet dependent on technique and adds them to the project.
        """
        for i in range(len(self.df)):
            self.samples.append(self.makeSample(self.df.ix[i]))
```

Two methods to revert to a csv file (`to_csv` like in a `pandas.DataFrame`) and to get a new data frame from the already created samples (`asDataFrame`):

```python
    def asDataFrame(self):
        """
        Returns a `pandas.DataFrame` representation of self.
        """
        return _pd.DataFrame([s.asSeries() for s in self.samples])

    def to_csv(self, path, all=False):
        """
        Saves a csv annotation sheet from the samples.

        :param path: Path to csv file to be written.
        :type path: str
        :param all: If all sample attributes should be kept in the annotation sheet.
        :type all: bool
        """
        self.asDataFrame().to_csv(path, index=False)
```


## Binding them all

Ideally one would:

1. create a `Project`;
2. add a csv file to it in a new method which would create a `SampleSheet` object. This would:
    1. Make new `Sample` objects for each sample, creating its attributes and directory structure;
    2. Add the `Sample` objects to a container in `Project`.

```python
class Project(object):
    ...
    def addSampleSheet(self, csv):
        """
        Build a `SampleSheet` object from a csv file and
        add it and its samples to the project.

        :param csv: Path to csv file.
        :type csv: str
        """
        # Make SampleSheet object
        self.sheet = SampleSheet(csv)

        # pair project and sheet
        self.sheet.project = self

        # Generate sample objects from annotation sheet
        self.sheet.makeSamples()

        # Add samples to Project
        for sample in self.sheet.samples:
            self.addSample(sample)
            sample.setFilePaths()
            sample.makeSampleDirs()
```

# Practical examples

Here's a step in an example pipeline which runs Fastqc on (unmapped) bam files from all samples:

```python
from pipelines import Project, SampleSheet

def fastqc(inputBam, outputDir, sampleName):
    return "fastqc --noextract --outdir {0} {1}".format(outputDir, inputBam)

prj = Project("ngs")
prj.addSampleSheet("/projects/example/sheet.csv")

for sample in prj.samples:
    cmd = fastqc(sample.unmappedBam, sample.dirs.sampleRoot, sample.name)
    os.system(cmd)  # in real-life one wouldn't use `os.system`
    ...
```

Notice the absent use of file paths in the pipeline. Although still pretty simple, it is now much simpler to handle every file created by the pipeline for each sample.

These objects are also useful during analysis steps to quickly grab files produced by the pipeline and start an analysis right away.

Here I grab all ChIP-seq peak files from all samples and create a peak set by concatenating them all and merging:

```python
from pipelines import Project, SampleSheet
import pybedtools

prj = Project("ngs")
prj.addSampleSheet("/projects/example/sheet.csv")

for i, sample in enumerate(self.samples):
    print(sample.name)
    # Get peaks
    peaks = pybedtools.BedTool(sample.peaks)
    # Merge overlaping peaks within a sample if existing
    peaks = peaks.merge()
    if i == 0:
        sites = peaks
    else:
        # Concatenate all peaks
        sites = sites.cat(peaks)

# Merge overlaping peaks across samples
sites = sites.merge()

```
