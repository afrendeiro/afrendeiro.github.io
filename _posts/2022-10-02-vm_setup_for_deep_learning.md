---
layout: post
title: "VM setup for deep learning"
description: "VM setup for deep learning"
category: notebook
tags: [software, deep learning, ubuntu, pytorch, setup]
---
{% include JB/setup %}


# GPU-machine, Ubuntu 22.04

### Low-level stuff

{% highlight bash %}
# Check GPU is CUDA-compatible
lspci | grep -i nvidia

# Remove any previous installations
sudo apt-get purge nvidia*
sudo apt remove nvidia-*
sudo rm /etc/apt/sources.list.d/cuda*
sudo apt-get autoremove && sudo apt-get autoclean
sudo rm -rf /usr/local/cuda*

# Install
sudo apt-get update
sudo apt-get upgrade -y

sudo apt-get install -y \
    build-essential \
    libatlas-base-dev \
    libopencv-dev \
    libprotoc-dev \
    make \
    unzip \
    git \
    gcc \
    g++ \
    libglu1-mesa libglu1-mesa-dev \
    libcurl4-openssl-dev \
    libssl-dev \
    freeglut3-dev \
    libx11-dev \
    libxmu-dev \
    libxi-dev
{% endhighlight %}

### NVIDIA drivers

{% highlight bash %}
sudo add-apt-repository ppa:graphics-drivers/ppa
sudo apt update
sudo apt install libnvidia-common-470
sudo apt install libnvidia-gl-470
sudo apt install nvidia-driver-470
sudo apt install nvidia-settings
sudo apt install nvidia-utils-470
{% endhighlight %}

### CUDA

{% highlight bash %}

wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/cuda-ubuntu2004.pin

sudo mv cuda-ubuntu2004.pin /etc/apt/preferences.d/cuda-repository-pin-600

sudo apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/3bf863cc.pub

sudo add-apt-repository "deb https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/ /"
sudo apt-get update
sudo apt install cuda-11-3

  
# setup your paths
echo 'export PATH=/usr/local/cuda-11.3/bin:$PATH' >> ~/.bashrc
echo 'export LD_LIBRARY_PATH=/usr/local/cuda-11.3/lib64:$LD_LIBRARY_PATH' >> ~/.bashrc
source ~/.bashrc
sudo ldconfig
{% endhighlight %}

## cuDNN

{% highlight bash %}
# Download .deb for CUDA 11.3 from https://developer.nvidia.com/rdp/cudnn-download, and copy to VM via scp. Then:
# wget https://developer.nvidia.com/compute/cudnn/secure/8.5.0/local_installers/11.7/cudnn-local-repo-ubuntu2204-8.5.0.96_1.0-1_amd64.deb
sudo dpkg - i cudnn-local-repo-ubuntu2204-8.5.0.96_1.0-1_amd64.deb
{% endhighlight %}

## Python and Torch

{% highlight bash %}
# Make sure the `python` command is by default Python3 (it will be 3.10 for Ubuntu 22.04)
sudo apt install python-is-python3

# Install pip
wget https://bootstrap.pypa.io/get-pip.py
python get-pip.py

python -m pip install wheel setuptools

# Install Python scientific stack
python -m pip install \
    IPython \
    urlpath \
    tqdm \
    numpy \
    scipy \
    pandas \
    matplotlib \
    seaborn \
    anndata \
    scanpy \
    squidpy \
    statsmodels \
    scikit-learn \
    scikit-image \
    networkx \
    torch \
    torchvision \
    IPython \
    --extra-index-url https://download.pytorch.org/whl/cu113
{% endhighlight %}


# Non-GPU machine, Ubuntu 22.04

{% highlight bash %}
# Make sure VM is up-to-date
sudo apt-get update
sudo apt-get upgrade -y

# Install system libraries (not strictly required by often)
sudo apt-get install -y \
    build-essential \
    libatlas-base-dev \
    libopencv-dev \
    libprotoc-dev \
    make \
    unzip \
    git \
    gcc \
    g++ \
    libglu1-mesa libglu1-mesa-dev \
    libcurl4-openssl-dev \
    libssl-dev \
    freeglut3-dev \
    libx11-dev \
    libxmu-dev \
    libxi-dev


# Make sure the `python` command is by default Python3 (it will be 3.10 for Ubuntu 22.04)
sudo apt install python-is-python3
VERSION=`python --version`
python -c "assert '$VERSION' == 'Python 3.10.6'"

# Install pip (better to install manually than to use system's)
wget https://bootstrap.pypa.io/get-pip.py
python get-pip.py

# Install Python scientific stack
python -m pip install wheel setuptools

# Install Python scientific stack
python -m pip install \
    IPython \
    urlpath \
    tqdm \
    numpy \
    scipy \
    pandas \
    matplotlib \
    seaborn \
    anndata \
    scanpy \
    squidpy \
    statsmodels \
    scikit-learn \
    scikit-image \
    networkx \
    torch \
    torchvision \
    IPython \
    --extra-index-url https://download.pytorch.org/whl/cu113
{% endhighlight %}
