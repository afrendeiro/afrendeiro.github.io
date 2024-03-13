---
layout: post
title: "Fast.ai and its tricks"
description: "Fast.ai and its amazing tricks"
category: notebook
tags: [deep learning, fastai, programming, python]
---
{% include JB/setup %}

Oh fast.ai, how I love thee.

How easy it is to get started and train a model.

But sometimes, you are a pain in the neck.

The documentation isn't really there and the source code is not readable.

I hear the forums are very helpful but it's not quite a format I have time for.

Ultimately fasta.ai will only get you started, but I have immense respect and admiration for Howard, Sylvain, and the other people behind it.

Sometimes there is a true spark of genius in the way they do things, going above what many academics do and what other libraries provide (e.g. lr_find).

Let's check out one of my favourite tricks: using a ResNet as an encoder in an autoencoder.


### Sources:

- https://colab.research.google.com/drive/1t9dn6qIdKc6rdF-A02KMdJ8UVGYPFh4v#scrollTo=e9dnMvm7q5q4

```python
from pathlib import Path

import numpy as np
import imageio
import torch
import torchvision
from fastai.vision.all import (
    L,
    DataBlock,
    ImageBlock,
    CategoryBlock,
    aug_transforms,
    vision_learner,
    create_body,
    Resize,
    PixelShuffle_ICNR,
    ConvLayer,
    nn,
    Module,
    SigmoidRange,
    Tensor,
    xresnet18,
    Learner,
    MSELossFlat
)

def get_class(x):
    return x.stem.split("-")[-1]


def get_self(x):
    return x

# Make dummy dataset
dataset_dir = Path("datasets") / "dummy_resize"
dataset_dir.mkdir(exist_ok=True, parents=True)
(dataset_dir / "train").mkdir(exist_ok=True)
(dataset_dir / "valid").mkdir(exist_ok=True)

for i in range(10):
    for c in ["a", "b"]:
        img = np.random.randint(0, 255, (32, 32, 3)).astype("uint8")
        imageio.imwrite(dataset_dir / "train" / f"{i}-{c}.jpg", img)
        imageio.imwrite(dataset_dir / "valid" / f"{i}-{c}.jpg", img)
files = L(dataset_dir.glob("*/*.jpg"))

# Define model architecture
class UpsampleBlock(Module):
    def __init__(
        self,
        up_in_c: int,
        final_div: bool = True,
        blur: bool = False,
        leaky: float = None,
        **kwargs,
    ):
        self.shuf = PixelShuffle_ICNR(up_in_c, up_in_c // 2, blur=blur, **kwargs)
        ni = up_in_c // 2
        nf = ni if final_div else ni // 2
        self.conv1 = ConvLayer(ni, nf, **kwargs)
        self.conv2 = ConvLayer(nf, nf, **kwargs)
        self.relu = nn.ReLU()

    def forward(self, up_in: Tensor) -> Tensor:
        up_out = self.shuf(up_in)
        cat_x = self.relu(up_out)
        return self.conv2(self.conv1(cat_x))

def decoder_resnet(y_range, n_out=3):
    return nn.Sequential(
        UpsampleBlock(512),
        UpsampleBlock(256),
        UpsampleBlock(128),
        UpsampleBlock(64),
        UpsampleBlock(32),
        nn.Conv2d(16, n_out, 1),
        SigmoidRange(*y_range),
    )

def autoencoder(encoder, y_range):
    return nn.Sequential(encoder, decoder_resnet(y_range))

# Make dataloader
btfms = aug_transforms()
block = DataBlock(
    blocks=[ImageBlock(), ImageBlock()],
    get_y=get_self,
    batch_tfms=btfms,
    item_tfms=Resize(32),
)
dls = block.dataloaders(files, path=dataset_dir, bs=12)
x, y = dls.one_batch()

# Build model and check
encoder = create_body(xresnet18(), n_in=3).cuda()
encoder(x).shape
y_range = (-3.0, 3.0)
ac_resnet = autoencoder(encoder, y_range).cuda()
assert x.shape == ac_resnet(x).shape
decoder = decoder_resnet(y_range).cuda()
assert x.shape == decoder(encoder(x)).shape

# Train
learn = Learner(dls, ac_resnet, loss_func=MSELossFlat())
```
