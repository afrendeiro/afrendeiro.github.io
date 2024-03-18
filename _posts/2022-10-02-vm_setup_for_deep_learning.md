---
layout: post
title: "VM setup for deep learning"
description: "VM setup for deep learning"
category: notebook
tags: [software, deep learning, ubuntu, pytorch, setup]
---
{% include JB/setup %}


# GPU-machine, Ubuntu 22.04

```bash
# Get latest version strings
UBUNTU_VERSION=ubuntu2204
ARCH=amd64
DRIVER_VERSION=$(apt-cache search nvidia-driver- | grep "^nvidia-driver" | grep -v open | sort | tail -n 1 | sed "s/ .*//g" | sed -r 's/.*-([0-9]+)/\1/g')
CUDA_VERSION=$(apt-cache search cuda- | grep "^cuda-[0-9]" | sort | tail -n 1 | sed "s/ .*//g" | sed -r 's/.*-([0-9]+-[0-9])/\1/g')
CUDDN_VERSION=9.0.0

# Clean up old installs
sudo apt-get -y purge nvidia*
sudo apt-get -y remove nvidia-*
sudo rm /etc/apt/sources.list.d/cuda*
sudo apt-get -y autoremove && sudo apt-get -y autoclean
sudo rm -rf /usr/local/cuda*

# Update
sudo apt-get update
sudo apt-get upgrade -y

# Install base libs
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

# Install NVIDIA drivers
sudo add-apt-repository ppa:graphics-drivers/ppa
sudo apt-get update
sudo apt-get install -y libnvidia-common-${DRIVER_VERSION}
sudo apt-get install -y libnvidia-gl-${DRIVER_VERSION}
sudo apt-get install -y nvidia-driver-${DRIVER_VERSION}
sudo apt-get install -y nvidia-settings
sudo apt-get install -y nvidia-utils-${DRIVER_VERSION}

# Install CUDA
wget https://developer.download.nvidia.com/compute/cuda/repos/${UBUNTU_VERSION}/x86_64/cuda-${UBUNTU_VERSION}.pin
sudo mv cuda-${UBUNTU_VERSION}.pin /etc/apt/preferences.d/cuda-repository-pin-600
sudo apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/cuda/repos/${UBUNTU_VERSION}/x86_64/3bf863cc.pub
sudo add-apt-repository "deb https://developer.download.nvidia.com/compute/cuda/repos/${UBUNTU_VERSION}/x86_64/ /"
sudo apt-get update
sudo apt-get install -y cuda-${CUDA_VERSION}

# setup CUDA paths (TODO: test if this has already been added)
__export='
# CUDA
if [ -d "/usr/local/cuda/bin/" ]; then
    export PATH=/usr/local/cuda/bin${PATH:+:${PATH}}
    export LD_LIBRARY_PATH=/usr/local/cuda/lib64${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}
    export LD_LIBRARY_PATH=/opt/cuda/lib64${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}
    export LD_LIBRARY_PATH=/opt/cuda/include${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}
    export LD_LIBRARY_PATH=/usr/lib/x86_64-linux-gnu${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}
    export LD_LIBRARY_PATH=/usr/local/cuda/targets/x86_64-linux/include${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}
    export CUDA_HOME=/usr/local/cuda
fi
'
echo "$__export" >> ~/.bashrc
source ~/.bashrc
sudo ldconfig

# Install CuDNN: https://developer.nvidia.com/rdp/cudnn-download
wget https://developer.download.nvidia.com/compute/cudnn/${CUDDN_VERSION}/local_installers/cudnn-local-repo-${UBUNTU_VERSION}-${CUDDN_VERSION}_1.0-1_${ARCH}.deb
sudo dpkg -i cudnn-local-repo-${UBUNTU_VERSION}-${CUDDN_VERSION}_1.0-1_${ARCH}.deb
sudo cp /var/cudnn-local-repo-${UBUNTU_VERSION}-${CUDDN_VERSION}/cudnn-*-keyring.gpg /usr/share/keyrings/
sudo apt-get update
sudo apt-get -y install cudnn

# Reboot!
sudo reboot
```


# Non-GPU machine, Ubuntu 22.04

```bash
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
```
