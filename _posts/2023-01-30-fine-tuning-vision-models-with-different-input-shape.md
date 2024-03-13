---
layout: post
title: "Fine tuning vision models with different input shape"
description: "Fine tuning vision models with different input shape"
category: notebook
tags: [deep learning, pytorch, programming, python]
---
{% include JB/setup %}

Oh vision models, how I love thee.

But sometimes, you are a pain in the neck. 

The beauty of pre-training on ImageNet is that we have weights for several architechtures which somehow are relatable across architectures and therefore also across datasets (with some tricks).

However, if our dataset is not a natural image (i.e. photography/simple microscopy encoded in 3 channels), we need to do some tricks to make it work.

Here are some tricks I've learned along the way.


## Different channel number or different XY size

### Sources

- https://www.kaggle.com/code/iafoss/pretrained-resnet34-with-rgby-0-460-public-lb/notebook
- https://forums.fast.ai/t/how-to-do-transfer-learning-with-different-inputs/28395/5
- https://forums.fast.ai/t/feeding-different-sized-images-to-fine-tune-resnet34/58712/5


```python
from pathlib import Path
from argparse import ArgumentParser

import numpy as np
import imageio
import torch
import torchvision
import fastai
from fastai.vision.all import (
    L,
    DataBlock,
    ImageBlock,
    CategoryBlock,
    aug_transforms,
    vision_learner,
    error_rate,
)
from fastai.callback.tracker import SaveModelCallback


def get_class(x):
    return x.stem.split("-")[-1]

# Make dummy dataset
dataset_dir = Path("datasets") / "dummy_resize"
dataset_dir.mkdir(exist_ok=True, parents=True)
(dataset_dir / "train").mkdir(exist_ok=True)
(dataset_dir / "valid").mkdir(exist_ok=True)

for i in range(10):
    for c in ['a', 'b']:
        img = np.random.randint(0, 255, (32, 32, 3)).astype('uint8')
        imageio.imwrite(dataset_dir / "train" / f"{i}-{c}.jpg", img)
        imageio.imwrite(dataset_dir / "valid" / f"{i}-{c}.jpg", img)

# Make dataloader
block = DataBlock(blocks=[ImageBlock, CategoryBlock], get_y=get_class)
dls = block.dataloaders(L(dataset_dir.glob("*/*.jpg")), path=dataset_dir, bs=4)

# Get model
model_name = 'resnet50'
fa = getattr(torchvision.models, model_name)
learn = vision_learner(dls, fa)
learn.model = learn.eval()

# Compare architectures
rn = fa(weights="DEFAULT").eval()
learn.model

# Check size adjusts
x = torch.from_numpy(img.transpose((2, 0, 1))[np.newaxis, ...]) / 255
with torch.no_grad():
    y0 = rn(x)

with torch.no_grad():
    y1 = learn.model(x)
# both work, but eval() mode is required

# Train
learn.model = learn.train()
learn.fine_tune(10)

```