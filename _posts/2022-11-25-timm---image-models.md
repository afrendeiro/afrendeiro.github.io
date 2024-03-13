---
layout: post
title: "Timm - Image models"
description: "Timm: Torch Image Models"
category: notebook
tags: [deep learning, pytorch, programming, python]
---
{% include JB/setup %}

Timm: Torch Image Models - an amazing library to interface with a wide wide range of image models.

Honestly, it is mind blowing to me how many models are available in this library, all pre-trained on ImageNet. 

Let's dig in!

```python
import torch
import timm
from bii.datasets import get_cycif_data

model_names = timm.list_models(pretrained=True)
model_names = timm.list_models('*vit*', pretrained=True)
model_name = 'maxvit_rmlp_nano_rw_256'
model = timm.create_model(model_name, pretrained=True).eval()  # .to('cuda')

x, y, meta = get_cycif_data()
x = x / (2 ** 16 - 1)

i = np.asarray([[ch for _ in range(3)] for ch in x.values])[:, :, :256, :256]
i = torch.Tensor(i)  # .to('cuda')
with torch.no_grad():
    o = model(i).numpy()

corr = pd.DataFrame(o, index=x.channel).T.corr()
from seaborn_extensions import clustermap
grid = clustermap(corr, center=0, cmap="RdBu_r")

from sklearn.decomposition import PCA
pca = PCA(2)
lat = pca.fit_transform(o)

fig, ax = plt.subplots()
ax.scatter(*lat.T)
for i, name in enumerate(x.channel.values):
    ax.text(*lat[i], s=name)
```
