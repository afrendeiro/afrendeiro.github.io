---
layout: post
title: "Demo: analysis of flow cytometry data at single-cell resolution"
description: ""
category: research
tags: [flow cytometry, python]
---
{% include JB/setup %}


I'm interested in exploring flow cytometry data from a single-cell perspective. After all it is a very high throughput method that can measure a modest amount of variables in each single cell.

I decided to use the `FlowCytometryTools` Python library just to see what I could extract from those *magic* fcs files and how feature complete the library is.

I made the following Jupyter notebook:

<br>

#### Demo of exploring flow cytometry data with the FlowCytometryTools library

{% highlight python %}
# Import library
from FlowCytometryTools import FCMeasurement

{% endhighlight %}

{% highlight python %}
# load fcs file (version 3)
sample = FCMeasurement(ID='Example sample', datafile="data/example.fcs")

{% endhighlight %}

{% highlight python %}
# Let's see the number of cells measured
sample.counts

{% endhighlight %}

    156157

{% highlight python %}
# All metadata
sample.meta.items()[:10] # see only first 10 entries

{% endhighlight %}

    [(u'P13MS', u'350'),
     (u'$ETIM', u'13:21:42'),
     (u'P8DISPLAY', u'LOG'),
     (u'FSC ASF', u'0.74'),
     (u'CYTNUM', u'1'),
     (u'$ENDDATA', u'9998405            '),
     (u'P2DISPLAY', u'LIN'),
     (u'$ENDSTEXT', u'0'),
     (u'LASER2NAME', u'Red')]

{% highlight python %}
sample.channel_names

{% endhighlight %}

    (u'FSC-A',
     u'FSC-H',
     u'FSC-W',
     u'SSC-A',
     u'SSC-H',
     u'SSC-W',
     u'B/E Alexa Fluor 488-A',
     u'B/C PE-TexasRed-A',
     u'B/B PerCP-Cy5-5-A',
     u'YG/A PE-Cy7-A',
     u'R/C APC-A',
     u'R/B Alexa Fluor 700-A',
     u'R/A APC-Cy7-A',
     u'V/C Pacific Blue-A',
     u'YG/E PE-A',
     u'Time')

{% highlight python %}
sample.channels

{% endhighlight %}

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>$PnN</th>
      <th>$PnB</th>
      <th>$PnG</th>
      <th>$PnE</th>
      <th>$PnR</th>
      <th>$PnV</th>
    </tr>
    <tr>
      <th>Channel Number</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>FSC-A</td>
      <td>32</td>
      <td>1.0</td>
      <td>[0, 0]</td>
      <td>262144</td>
      <td>244</td>
    </tr>
    <tr>
      <th>2</th>
      <td>FSC-H</td>
      <td>32</td>
      <td>1.0</td>
      <td>[0, 0]</td>
      <td>262144</td>
      <td>244</td>
    </tr>
    <tr>
      <th>3</th>
      <td>FSC-W</td>
      <td>32</td>
      <td>1.0</td>
      <td>[0, 0]</td>
      <td>262144</td>
      <td>244</td>
    </tr>
    <tr>
      <th>4</th>
      <td>SSC-A</td>
      <td>32</td>
      <td>1.0</td>
      <td>[0, 0]</td>
      <td>262144</td>
      <td>276</td>
    </tr>
    <tr>
      <th>5</th>
      <td>SSC-H</td>
      <td>32</td>
      <td>1.0</td>
      <td>[0, 0]</td>
      <td>262144</td>
      <td>276</td>
    </tr>
    <tr>
      <th>6</th>
      <td>SSC-W</td>
      <td>32</td>
      <td>1.0</td>
      <td>[0, 0]</td>
      <td>262144</td>
      <td>276</td>
    </tr>
    <tr>
      <th>7</th>
      <td>B/E Alexa Fluor 488-A</td>
      <td>32</td>
      <td>1.0</td>
      <td>[0, 0]</td>
      <td>262144</td>
      <td>469</td>
    </tr>
    <tr>
      <th>8</th>
      <td>B/C PE-TexasRed-A</td>
      <td>32</td>
      <td>1.0</td>
      <td>[0, 0]</td>
      <td>262144</td>
      <td>450</td>
    </tr>
    <tr>
      <th>9</th>
      <td>B/B PerCP-Cy5-5-A</td>
      <td>32</td>
      <td>1.0</td>
      <td>[0, 0]</td>
      <td>262144</td>
      <td>462</td>
    </tr>
    <tr>
      <th>10</th>
      <td>YG/A PE-Cy7-A</td>
      <td>32</td>
      <td>1.0</td>
      <td>[0, 0]</td>
      <td>262144</td>
      <td>458</td>
    </tr>
    <tr>
      <th>11</th>
      <td>R/C APC-A</td>
      <td>32</td>
      <td>1.0</td>
      <td>[0, 0]</td>
      <td>262144</td>
      <td>586</td>
    </tr>
    <tr>
      <th>12</th>
      <td>R/B Alexa Fluor 700-A</td>
      <td>32</td>
      <td>1.0</td>
      <td>[0, 0]</td>
      <td>262144</td>
      <td>560</td>
    </tr>
    <tr>
      <th>13</th>
      <td>R/A APC-Cy7-A</td>
      <td>32</td>
      <td>1.0</td>
      <td>[0, 0]</td>
      <td>262144</td>
      <td>618</td>
    </tr>
    <tr>
      <th>14</th>
      <td>V/C Pacific Blue-A</td>
      <td>32</td>
      <td>1.0</td>
      <td>[0, 0]</td>
      <td>262144</td>
      <td>385</td>
    </tr>
    <tr>
      <th>15</th>
      <td>YG/E PE-A</td>
      <td>32</td>
      <td>1.0</td>
      <td>[0, 0]</td>
      <td>262144</td>
      <td>443</td>
    </tr>
    <tr>
      <th>16</th>
      <td>Time</td>
      <td>32</td>
      <td>0.01</td>
      <td>[0, 0]</td>
      <td>262144</td>
      <td>None</td>
    </tr>
  </tbody>
</table>
</div>

{% highlight python %}
# get forward vs side scatter of first 10 cells
sample.data[['FSC-A', 'SSC-A']][:10]

{% endhighlight %}

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>FSC-A</th>
      <th>SSC-A</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>53618.921875</td>
      <td>42435.988281</td>
    </tr>
    <tr>
      <th>1</th>
      <td>100054.664062</td>
      <td>33288.808594</td>
    </tr>
    <tr>
      <th>2</th>
      <td>60825.039062</td>
      <td>35168.011719</td>
    </tr>
    <tr>
      <th>3</th>
      <td>58227.640625</td>
      <td>37189.890625</td>
    </tr>
    <tr>
      <th>4</th>
      <td>67312.617188</td>
      <td>39781.621094</td>
    </tr>
    <tr>
      <th>5</th>
      <td>92615.437500</td>
      <td>73334.914062</td>
    </tr>
    <tr>
      <th>6</th>
      <td>51280.519531</td>
      <td>33090.449219</td>
    </tr>
    <tr>
      <th>7</th>
      <td>43725.859375</td>
      <td>36683.550781</td>
    </tr>
    <tr>
      <th>8</th>
      <td>62111.902344</td>
      <td>22713.960938</td>
    </tr>
    <tr>
      <th>9</th>
      <td>84667.843750</td>
      <td>33091.320312</td>
    </tr>
  </tbody>
</table>
</div>

{% highlight python %}
# Get all channels in one table
# this would be the main table to work on from here
sample.data.drop("Time", axis=1).head(10)  # show only first 10 cells

{% endhighlight %}

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>FSC-A</th>
      <th>FSC-H</th>
      <th>FSC-W</th>
      <th>SSC-A</th>
      <th>SSC-H</th>
      <th>SSC-W</th>
      <th>B/E Alexa Fluor 488-A</th>
      <th>B/C PE-TexasRed-A</th>
      <th>B/B PerCP-Cy5-5-A</th>
      <th>YG/A PE-Cy7-A</th>
      <th>R/C APC-A</th>
      <th>R/B Alexa Fluor 700-A</th>
      <th>R/A APC-Cy7-A</th>
      <th>V/C Pacific Blue-A</th>
      <th>YG/E PE-A</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>53618.921875</td>
      <td>46566.0</td>
      <td>75462.132812</td>
      <td>42435.988281</td>
      <td>40018.0</td>
      <td>69495.859375</td>
      <td>66.989998</td>
      <td>59.160000</td>
      <td>36.540001</td>
      <td>5453.760254</td>
      <td>2175.400146</td>
      <td>624.150024</td>
      <td>329.960022</td>
      <td>9.130000</td>
      <td>156.400009</td>
    </tr>
    <tr>
      <th>1</th>
      <td>100054.664062</td>
      <td>90369.0</td>
      <td>72560.093750</td>
      <td>33288.808594</td>
      <td>32241.0</td>
      <td>67665.867188</td>
      <td>62.639999</td>
      <td>215.759995</td>
      <td>97.440002</td>
      <td>2553.920166</td>
      <td>2539.670166</td>
      <td>579.619995</td>
      <td>252.580002</td>
      <td>14.940000</td>
      <td>720.359985</td>
    </tr>
    <tr>
      <th>2</th>
      <td>60825.039062</td>
      <td>53044.0</td>
      <td>75149.492188</td>
      <td>35168.011719</td>
      <td>33952.0</td>
      <td>67883.210938</td>
      <td>90.480003</td>
      <td>125.279999</td>
      <td>28.710001</td>
      <td>6724.280273</td>
      <td>1590.670044</td>
      <td>669.410034</td>
      <td>292.000000</td>
      <td>6.640000</td>
      <td>291.640015</td>
    </tr>
    <tr>
      <th>3</th>
      <td>58227.640625</td>
      <td>50084.0</td>
      <td>76192.140625</td>
      <td>37189.890625</td>
      <td>35568.0</td>
      <td>68524.421875</td>
      <td>69.599998</td>
      <td>334.950012</td>
      <td>139.199997</td>
      <td>2679.040039</td>
      <td>1762.950073</td>
      <td>458.440002</td>
      <td>202.210007</td>
      <td>9.960000</td>
      <td>917.239990</td>
    </tr>
    <tr>
      <th>4</th>
      <td>67312.617188</td>
      <td>57849.0</td>
      <td>76257.140625</td>
      <td>39781.621094</td>
      <td>38333.0</td>
      <td>68012.632812</td>
      <td>77.430000</td>
      <td>192.270004</td>
      <td>100.919998</td>
      <td>4035.120117</td>
      <td>1524.970093</td>
      <td>475.230011</td>
      <td>239.440002</td>
      <td>9.960000</td>
      <td>608.119995</td>
    </tr>
    <tr>
      <th>5</th>
      <td>92615.437500</td>
      <td>72473.0</td>
      <td>83750.437500</td>
      <td>73334.914062</td>
      <td>66461.0</td>
      <td>72314.242188</td>
      <td>120.059998</td>
      <td>2424.689941</td>
      <td>2306.370117</td>
      <td>253.919998</td>
      <td>237.980011</td>
      <td>241.630005</td>
      <td>66.430000</td>
      <td>34.029999</td>
      <td>6612.040039</td>
    </tr>
    <tr>
      <th>6</th>
      <td>51280.519531</td>
      <td>44760.0</td>
      <td>75083.117188</td>
      <td>33090.449219</td>
      <td>31656.0</td>
      <td>68505.679688</td>
      <td>86.129997</td>
      <td>57.420002</td>
      <td>32.189999</td>
      <td>2461.920166</td>
      <td>1025.650024</td>
      <td>365.000000</td>
      <td>151.839996</td>
      <td>43.989998</td>
      <td>80.040001</td>
    </tr>
    <tr>
      <th>7</th>
      <td>43725.859375</td>
      <td>38597.0</td>
      <td>74244.570312</td>
      <td>36683.550781</td>
      <td>35153.0</td>
      <td>68389.421875</td>
      <td>153.990005</td>
      <td>202.710007</td>
      <td>163.559998</td>
      <td>2104.040039</td>
      <td>1400.140015</td>
      <td>401.500000</td>
      <td>234.330002</td>
      <td>191.729996</td>
      <td>734.160034</td>
    </tr>
    <tr>
      <th>8</th>
      <td>62111.902344</td>
      <td>55068.0</td>
      <td>73918.890625</td>
      <td>22713.960938</td>
      <td>21820.0</td>
      <td>68221.000000</td>
      <td>73.080002</td>
      <td>46.110001</td>
      <td>81.779999</td>
      <td>4808.839844</td>
      <td>1565.119995</td>
      <td>646.049988</td>
      <td>348.940002</td>
      <td>12.450000</td>
      <td>123.279999</td>
    </tr>
    <tr>
      <th>9</th>
      <td>84667.843750</td>
      <td>75601.0</td>
      <td>73395.750000</td>
      <td>33091.320312</td>
      <td>32645.0</td>
      <td>66432.007812</td>
      <td>31.320000</td>
      <td>15.660000</td>
      <td>13.050000</td>
      <td>3248.520020</td>
      <td>1015.430054</td>
      <td>360.619995</td>
      <td>141.620010</td>
      <td>6.640000</td>
      <td>75.440002</td>
    </tr>
  </tbody>
</table>
</div>

{% highlight python %}
# Let's plot some things:

# plot with provided library wrappers
_ = sample.plot(['FSC-A', 'SSC-A'], bins=1000)

# we can obviously also plot with base matplotlib + seaborn
import matplotlib.pyplot as plt
import pylab
import seaborn as sns
sns.set_style("whitegrid")
sns.jointplot(sample.data['FSC-A'], sample.data['SSC-A'],
              xlim=(0, 250000), ylim=(0, 250000),
              alpha=0.01)

{% endhighlight %}

    <seaborn.axisgrid.JointGrid at 0x7f334e8f0b50>

<div class="centerImages">
    <img src="{{ site.url }}/data/figures/flow/flow_10_1.png"
         align="middle" style="width: 500px;"/>
</div>


<div class="centerImages">
    <img src="{{ site.url }}/data/figures/flow/flow_10_2.png"
         align="middle" style="width: 500px;"/>
</div>

{% highlight python %}
# Now let's make a gate using the interactive interface
# sample.view_interactively()

{% endhighlight %}

{% highlight python %}
from FlowCytometryTools import ThresholdGate, PolyGate

# Four threshold gates
gate1 = ThresholdGate(17500, 'FSC-A', region='above')
gate2 = ThresholdGate(60000, 'SSC-A', region='below')
gate3 = ThresholdGate(110000, 'FSC-A', region='below')
gate4 = ThresholdGate(10000, 'SSC-A', region='above')

# Similar thing with a polygon
# drawn interactively
gate5 = PolyGate(
    [(3.140e+04, 9.951e+04), (1.108e+04, 5.092e+04), (1.421e+04, 3.304e+04),
     (2.385e+04, 2.426e+04), (3.219e+04, 1.583e+04), (3.818e+04, 5.706e+03),
     (5.251e+04, 4.019e+03), (1.208e+05, 1.178e+04), (1.408e+05, 5.429e+04),
     (3.505e+04, 9.681e+04), (3.114e+04, 9.951e+04), (3.219e+04, 9.613e+04)],
    ('FSC-A', 'SSC-A'), region='in', name='gate4')
_ = sample.plot(['FSC-A', 'SSC-A'], bins=1000, gates=[gate1, gate2, gate3, gate4, gate5])

{% endhighlight %}


<div class="centerImages">
    <img src="{{ site.url }}/data/figures/flow/flow_12_0.png"
         align="middle" style="width: 500px;"/>
</div>

{% highlight python %}
# Plot channels individually
_ = sample.plot('FSC-A', bins=1000)

{% endhighlight %}


<div class="centerImages">
    <img src="{{ site.url }}/data/figures/flow/flow_13_0.png"
         align="middle" style="width: 500px;"/>
</div>

{% highlight python %}
# Log transform and plot again
_ = sample.transform('hlog', channels=['FSC-A']).plot('FSC-A', bins=1000)

{% endhighlight %}


<div class="centerImages">
    <img src="{{ site.url }}/data/figures/flow/flow_14_0.png"
         align="middle" style="width: 500px;"/>
</div>

{% highlight python %}
# Log transform and plot different channel
_ = sample.transform('hlog', channels=['R/B Alexa Fluor 700-A']).plot('R/B Alexa Fluor 700-A', bins=1000)

{% endhighlight %}

<div class="centerImages">
    <img src="{{ site.url }}/data/figures/flow/flow_15_0.png"
         align="middle" style="width: 500px;"/>
</div>

