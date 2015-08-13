---
layout: post
title: "Python objects for NGS projects and samples"
category: research
tags: [python]
---
{% include JB/setup %}

I've been using [Python programs to manage NGS sample pipelines](https://github.com/afrendeiro/pipelines) for a while, and while it started slowly and very 
They're in a state in which the code is much more reliable and I can work much faster.


A big part of it was due to some simple object modeling of projects and samples.
Here's the basics of what I implemented:

#### A *Project* object

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
So, all the `Project` object takes as argument is `name` and `parent`. The structure is then created when `__init__` (which is called automatically upon creation of the object) calls in its turn `setProjectDirs` and `makeProjectDirs`.


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

#### A Sample object



Sample centric


```python
import pandas as pd

series = pd.Series(
    ["ChIP-seq", "hg19", "/data/samples/test.bam"],
    index=["technique", "genome", "unmappedBam"]
)
sample = Sample(series)
```





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

        self.checkValid()
        self.generateName()
        self.getReadType()

        self.dirs = Paths()

    def checkValid(self):
        """Check if any of its important attributes is None."""
        req = ["technique", "genome", "unmappedBam"]

        if not all([hasattr(self, attr) for attr in req]):
            raise ValueError("Required values for sample do not exist.")

        if any([attr == "nan" for attr in req]):
            raise ValueError("Required values for sample are empty.")

    def generateName(self):
        """Generates a name for the sample by joining some of its possible attribute strings."""
        self.name = "_".join(
            [str(self.__getattribute__(attr)) for attr in [
                "cellLine", "numberCells", "technique", "ip",
                "patient", "patientID", "sampleID", "treatment", "condition",
                "biologicalReplicate", "technicalReplicate",
                "experimentName", "genome"] if hasattr(self, attr) and str(self.__getattribute__(attr)) != "nan"]
        )

    def setFilePaths(self):
        """Sets the paths of all files for this sample."""
        self.dirs.sampleRoot = _os.path.join(self.project.dirs.data, self.name)

        # Files in the root of the sample dir
        self.fastqc = self.dirs.sampleRoot
        self.trimlog = _os.path.join(self.dirs.sampleRoot, self.name + ".trimlog.txt")
        self.alnRates = _os.path.join(self.dirs.sampleRoot, self.name + ".alnRates.txt")
        self.alnMetrics = _os.path.join(self.dirs.sampleRoot, self.name + ".alnMetrics.txt")
        self.dupsMetrics = _os.path.join(self.dirs.sampleRoot, self.name + ".duplicates.txt")

        # Unmapped: merged bam, fastq, trimmed fastq
        self.dirs.unmapped = _os.path.join(self.dirs.sampleRoot, "unmapped")
        self.unmapped = _os.path.join(self.dirs.unmapped, self.name + ".bam")
        if self.readType == "SE":
            self.fastq = _os.path.join(self.dirs.unmapped, self.name + ".fastq")
        else:
            self.fastq1 = _os.path.join(self.dirs.unmapped, self.name + ".1.fastq")
            self.fastq2 = _os.path.join(self.dirs.unmapped, self.name + ".2.fastq")
            self.fastqUnpaired = _os.path.join(self.dirs.unmapped, self.name + ".unpaired.fastq")
        if self.readType == "SE":
            self.trimmed = _os.path.join(self.dirs.unmapped, self.name + ".trimmed.fastq")
        else:
            self.trimmed1 = _os.path.join(self.dirs.unmapped, self.name + ".1.trimmed.fastq")
            self.trimmed2 = _os.path.join(self.dirs.unmapped, self.name + ".2.trimmed.fastq")
            self.trimmed1Unpaired = _os.path.join(self.dirs.unmapped, self.name + ".1_unpaired.trimmed.fastq")
            self.trimmed2Unpaired = _os.path.join(self.dirs.unmapped, self.name + ".2_unpaired.trimmed.fastq")

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

```

class Paths(object):
    """
    A class to hold paths as attributes.
    """
    pass
```



```python
    def getReadType(self):
        """Gets the read type and length of bam file."""
        ...
        self.readLength = [0-9]+
        self.readType = ["SE", "PE"]
        self.paired = [False, True]
```
