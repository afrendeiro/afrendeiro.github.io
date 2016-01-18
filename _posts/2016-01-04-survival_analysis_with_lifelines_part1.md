---
layout: post
title: "Survival analysis with lifelines - part 1"
description: "Survival analysis with lifelines - part 1"
category: research
tags: [survival, python]
---

{% include JB/setup %}

> This post is available as a [Jupiter notebook](http://jupyter.readthedocs.org/) [here](http://nbviewer.jupyter.org/github/afrendeiro/afrendeiro.github.io/blob/master/data/notebooks/lifelines_survival_part1.ipynb).

The [lifelines package](http://lifelines.readthedocs.org/) is a well documented, easy-to-use Python package for survival analysis.

I had never done any survival analysis, but  the fact that package has great documentation made me adventure in the field. From the documentation I was able to understand the key concepts of survival analysis and run a few simple analysis on clinical data gathered by our collaborators from a cohort of cancer patients. This obviously does not mean it is a replacement of proper study of the field, but nonetheless I highly recommend reading the whole documentation for begginers on the topic and the usage of the package to anyone working in the field.


### Getting our hands dirty

<small><strong>Note:</strong> In these data, although already anonymized, I have added some jitter for the actual values to differ from the real ones.</small>

Although all one needs for survival analysis is two arrays with the time duration patients were observed and whether death occured during that time, in reality you're more likely to get from clinicians an Excel file with dates of birth, diagnosis, and death along with other relevant information on the clinical cohort.

Let's read some data in and transform those fields into the time we have been observing the patient (from diagnosis to the last checkup):

<small><strong>Hint:</strong> make sure you tell pandas which columns hold dates and the format they are in for correct date parsing.</small>


{% highlight python %}

import pandas as pd

clinical = pd.read_csv(
    "clinical_data.csv",
    parse_dates=["patient_death_date", "diagnosis_date", "patient_last_checkup_date"],
    dayfirst=True)

# get duration of patient observation
clinical["duration"] = clinical["patient_last_checkup_date"] - clinical["diagnosis_date"]

clinical.head()

{% endhighlight %}


<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>patient_last_checkup_date</th>
      <th>diagnosis_date</th>
      <th>patient_death_date</th>
      <th>t1</th>
      <th>t2</th>
      <th>t3</th>
      <th>t4</th>
      <th>t5</th>
      <th>t6</th>
      <th>t7</th>
      <th>t8</th>
      <th>t9</th>
      <th>t10</th>
      <th>t11</th>
      <th>t12</th>
      <th>duration</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2011-12-05</td>
      <td>1977-08-23</td>
      <td>2011-12-19</td>
      <td>F</td>
      <td>A0</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>12522 days</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2015-01-15</td>
      <td>1997-08-06</td>
      <td>NaT</td>
      <td>M</td>
      <td>A0</td>
      <td>1</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>6371 days</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2011-11-14</td>
      <td>1987-03-11</td>
      <td>NaT</td>
      <td>F</td>
      <td>A0</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>9014 days</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2008-11-15</td>
      <td>1992-04-27</td>
      <td>2008-12-7</td>
      <td>F</td>
      <td>A0</td>
      <td>1</td>
      <td>2</td>
      <td>1</td>
      <td>True</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>6046 days</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2008-10-09</td>
      <td>1994-07-19</td>
      <td>2009-12-22</td>
      <td>M</td>
      <td>A0</td>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>5196 days</td>
    </tr>
  </tbody>
</table>
</div>



Let's check globaly how our patients are doing:


{% highlight python %}

from lifelines import KaplanMeierFitter

# Duration of patient following in months
T = [i.days / 30. for i in clinical["duration"]]
# Observation of death in boolean
# True for observed event (death);
# else False (this includes death not observed; death by other causes)
C = [True if i is not pd.NaT else False for i in clinical["patient_death_date"]]

fitter = KaplanMeierFitter()
fitter.fit(T, event_observed=C, label="all patients")
fitter.plot(show_censors=True)

{% endhighlight %}




    <matplotlib.axes._subplots.AxesSubplot at 0x7f3812afaf10>




![png](/data/figures/survival_part1/output_6_1.png)


Now we want to split our cohort according to values in several variables (*e.g.* gender, age, presence/absence of a clinical marker), and check what's the progression of survival, and if differences between groups are significant.


{% highlight python %}

import matplotlib.pyplot as plt
from lifelines.statistics import logrank_test
from matplotlib.offsetbox import AnchoredText

trait = "t1"  # we pick one trait, gender in this case

label = clinical[trait].unique()
label = label[~np.array(map(pd.isnull, label))]

fig, ax = plt.subplots(1)
# Separately for each class
# get index of patients from class
f = clinical[clinical[trait] == "F"].index.tolist()
# fit the KaplarMayer with the subset of data from the respective class
fitter.fit([T[i] for i in f], event_observed=[C[i] for i in f], label="F")
fitter.plot(ax=ax, show_censors=True)

# get index of patients from class
m = clinical[clinical[trait] == "M"].index.tolist()
# fit the KaplarMayer with the subset of data from the respective class
fitter.fit([T[i] for i in m], event_observed=[C[i] for i in m], label="M")
fitter.plot(ax=ax, show_censors=True)

# test difference between curves    
p = logrank_test(
    [T[i] for i in f], [T[i] for i in m],
    event_observed_A=[C[i] for i in f],
    event_observed_B=[C[i] for i in m]).p_value

# add p-value to plot
ax.add_artist(AnchoredText("p = %f" % round(p, 5), loc=4, frameon=False))

{% endhighlight %}




    <matplotlib.offsetbox.AnchoredText at 0x7f3813692dd0>




![png](/data/figures/survival_part1/output_8_1.png)


We can also investigate hazard over time instead of survival:


{% highlight python %}

from lifelines import NelsonAalenFitter

fitter = NelsonAalenFitter()
fitter.fit(T, event_observed=C, label="all patients")
fitter.plot(show_censors=True)

{% endhighlight %}




    <matplotlib.axes._subplots.AxesSubplot at 0x7f3812ef6fd0>




![png](/data/figures/survival_part1/output_10_1.png)


Great, so if we make the code more general and wrap it into a function, we can run see how survival or hazard of patients with certain traits differ.

We can also investigate variables with more than one class and compare them in a pairwise fashion.


{% highlight python %}

from lifelines import NelsonAalenFitter
import itertools

def survival_plot(clinical, fitter, fitter_name, feature, time):
    T = [i.days / float(30) for i in clinical[time]]  # duration of patient following
    # events:
    # True for observed event (death);
    # else False (this includes death not observed; death by other causes)
    C = [True if i is not pd.NaT else False for i in clinical["patient_death_date"]]

    fig, ax = plt.subplots(1)

    # All patients together
    fitter.fit(T, event_observed=C, label="all patients")
    fitter.plot(ax=ax, show_censors=True)

    # Filter feature types which are nan
    label = clinical[feature].unique()
    label = label[~np.array(map(pd.isnull, label))]

    # Separately for each class
    for value in label:
        # get patients from class
        s = clinical[clinical[feature] == value].index.tolist()
        fitter.fit([T[i] for i in s], event_observed=[C[i] for i in s], label=str(value))
        fitter.plot(ax=ax, show_censors=True)

    if fitter_name == "survival":
        ax.set_ylim(0, 1.05)

    # Test pairwise differences between all classes
    p_values = list()
    for a, b in itertools.combinations(label, 2):
        a_ = clinical[clinical[feature] == a].index.tolist()
        b_ = clinical[clinical[feature] == b].index.tolist()
        p = logrank_test(
            [T[i] for i in a_], [T[i] for i in b_],
            event_observed_A=[C[i] for i in a_],
            event_observed_B=[C[i] for i in b_]).p_value
        # see result of test with p.print_summary()
        p_values.append("p-value '" + " vs ".join([str(a), str(b)]) + "': %f" % p)

    # Add p-values as anchored text
    ax.add_artist(AnchoredText("\n".join(p_values), loc=8, frameon=False))

    ax.set_title("%s - %s since diagnosis" % (feature, fitter_name))

{% endhighlight %}


{% highlight python %}

features = ["t%i" % i for i in range(1, 11)]

# For each clinical feature
for feature in features:
    survival_plot(clinical, KaplanMeierFitter(), "survival", feature, "duration")
    survival_plot(clinical, NelsonAalenFitter(), "hazard", feature, "duration")

{% endhighlight %}


![png](/data/figures/survival_part1/output_13_0.png)



![png](/data/figures/survival_part1/output_13_1.png)



![png](/data/figures/survival_part1/output_13_2.png)



![png](/data/figures/survival_part1/output_13_3.png)



![png](/data/figures/survival_part1/output_13_4.png)



![png](/data/figures/survival_part1/output_13_5.png)



![png](/data/figures/survival_part1/output_13_6.png)



![png](/data/figures/survival_part1/output_13_7.png)



![png](/data/figures/survival_part1/output_13_8.png)



![png](/data/figures/survival_part1/output_13_9.png)



![png](/data/figures/survival_part1/output_13_10.png)



![png](/data/figures/survival_part1/output_13_11.png)



![png](/data/figures/survival_part1/output_13_12.png)



![png](/data/figures/survival_part1/output_13_13.png)



![png](/data/figures/survival_part1/output_13_14.png)



![png](/data/figures/survival_part1/output_13_15.png)



![png](/data/figures/survival_part1/output_13_16.png)



![png](/data/figures/survival_part1/output_13_17.png)



![png](/data/figures/survival_part1/output_13_18.png)



![png](/data/figures/survival_part1/output_13_19.png)
