---
layout: post
title: "Torch basics"
description: "Torch basics from scratch to Pytorch lightning step-by-step"
category: notebook
tags: [deep learning, pytorch, programming, python]
---
{% include JB/setup %}


# Torch basics

Pytorch, the essential deep learning library. It is flexible and easy to use - what a breath of fresh air compared to TensorFlow. 

Let's dig in!


## Linear regression from scratch:
```python
import torch as t

def get_data():
    x = t.randn((100, 1))
    real_m = 0.5
    real_b = 20
    y = x * real_m + real_b + (t.rand_like(x) / 5)
    return x, y

def linear_regression(x, params):
    return x * params[0] + params[1]

def absolute_error(y, pred):
    return (y - pred).abs().sum()

def report(i, params, loss):
    if i == 0:
        print("step\tm\tb\tloss")
    if i % 50 == 0:
        print(f"{i}\t{params[0].item():.3f}\t{params[1].item():.3f}\t{loss.item():.3f}")

t.manual_seed(0)

x, y = get_data()
params = t.zeros(2, requires_grad=True)

eps = 1e-5
# eps = 1e-8
for i in range(1_000):
    pred = linear_regression(x, params)
    loss = absolute_error(y, pred)
    report(i, params, loss)

    # Calculate loss
    loss.backward()

    # step
    with t.no_grad():
        params = (params - params.grad * eps).requires_grad_(True)

```

## Using an optimizer:
```python
from torch.optim import SGD

x, y = get_data()
params = t.zeros(2, requires_grad=True)
eps = 1e-5
optim = SGD([params], eps)

for i in range(1_000):
    pred = linear_regression(x, params)
    loss = absolute_error(y, pred)
    report(i, params, loss)

    loss.backward()
    optim.step()
    optim.zero_grad()
```

```python
from torch.optim import Adam

x, y = get_data()
params = t.zeros(2, requires_grad=True)
eps = 1e-2
optim = Adam([params], eps)

for i in range(1_000):
    pred = linear_regression(x, params)
    loss = absolute_error(y, pred)
    report(i, params, loss)

    loss.backward()
    optim.step()
    optim.zero_grad()
```

## Pytorch lightning:
```python

import pytorch_lightning as pl
import torch.nn as nn
from pytorch_lightning.callbacks.early_stopping import EarlyStopping

class LinearRegressor(pl.LightningModule):
    def __init__(self):
        super().__init__()
        self.layer1 = nn.Linear(1, 1)

    def forward(self, x):
        return self.layer1(x)

    def loss_fn(self, y, pred):
        return (y - pred).abs().sum()

    def training_step(self, batch, batch_idx):
        x, y = batch
        # with autocast():
        y_hat = self.forward(x)
        loss = self.loss_fn(y, y_hat)
        self.log("train_loss", loss)
        return loss

    def validation_step(self, batch, batch_idx):
        x, y = batch
        y_hat = self.forward(x)
        loss = self.loss_fn(y_hat, y)
        return loss

    def configure_optimizers(self):
        optimizer = torch.optim.SGD(self.parameters(), lr=1e-2)
        return optimizer

pl.seed_everything(0)
model = LinearRegressor()
trainer = pl.Trainer()
x, y = get_data()
trainer.fit(model, train_dataloaders=(x, y))

# Using callbacks
early_stop = EarlyStopping(monitor="train_loss", mode="min")
trainer = pl.Trainer(callbacks=[early_stop])
trainer.fit(model, train_dataloaders=(x, y))
```
## Dataset, Dataloader and vision models:
```python
from pathlib import Path
import numpy as np
import imageio
from torch.utils.data import Dataset
from torch.utils.data import DataLoader
from torchvision.io import read_image
import pytorch_lightning as pl
import torch.nn as nn
from pytorch_lightning.callbacks.early_stopping import EarlyStopping

def get_image_data() -> tuple[np.ndarray, np.ndarray]:
    x = np.random.randint(0, 255, (100, 224, 224, 3), dtype="uint8")
    x[:50, ..., -1] = 0
    y = np.asarray([0] * 50 + [1] * 50)
    return x, y

def write_dataset_to_disk(x: np.ndarray, y: np.ndarray, output_dir: Path) -> None:
    output_dir.mkdir(exist_ok=True, parents=True)
    for i, (x_, y_) in enumerate(zip(x, y)):
        f = output_dir / f"{str(i).zfill(3)}.{y_}.jpg"
        imageio.imwrite(f, x_)

class ImageDataset(Dataset):
    def __init__(self, data_dir: Path):
        self.data_dir = data_dir
        self.filenames = sorted(data_dir.glob("*.jpg"))

    def __len__(self) -> int:
        return len(self.filenames)

    def __getitem__(self, idx: int) -> tuple[t.Tensor, int]:
        image = read_image(self.filenames[idx].as_posix()) / 255
        label = int(self.filenames[idx].stem.split(".")[1])
        return image, label

class VisionModel(pl.LightningModule):
    def __init__(self):
        super().__init__()
        self.layer1 = nn.AvgPool2d(224)
        self.layer2 = nn.Linear(3, 1)
        self.layer3 = nn.Sigmoid()

    def forward(self, x):
        x = self.layer1(x)
        x = t.transpose(x, 1, -1)
        x = self.layer2(x)
        x = self.layer3(x)
        return x

    def loss_fn(self, y, pred):
        return (y - pred).abs().sum()

    def training_step(self, batch, batch_idx):
        x, y = batch
        # with autocast():
        y_hat = self.forward(x)
        loss = self.loss_fn(y, y_hat)
        self.log("train_loss", loss)
        return loss

    def validation_step(self, batch, batch_idx):
        x, y = batch
        y_hat = self.forward(x)
        loss = self.loss_fn(y_hat, y)
        return loss

    def configure_optimizers(self):
        optimizer = torch.optim.SGD(self.parameters(), lr=1e-2)
        return optimizer

pl.seed_everything(0)

x, y = get_image_data()
output_dir = Path("test_dataset")
write_dataset_to_disk(x, y, output_dir)

data = ImageDataset(output_dir)
dataloader = DataLoader(data, batch_size=4)

model = VisionModel()
trainer = pl.Trainer()
early_stop = EarlyStopping(monitor="train_loss", mode="min")
trainer = pl.Trainer(callbacks=[early_stop])
trainer.fit(model, train_dataloaders=dataloader)

# Inference
with torch.no_grad():
    res = np.asarray([(y, model(x[np.newaxis, ...]).item()) for x, y in data])
```
