---
layout: post
title: "Building Python manywheels"
description: "Building Python manywheels"
category: notebook
tags: [python, programming]
---
{% include JB/setup %}

# Building Python manywheels

Manywheeels are a way to distribute pre-compiled wheels for Python packages that are compatible with manylinux. This is a great way to distribute packages that depend on C-extensions, as it allows the user to install the package without having to compile the C-extensions themselves. 

Building them is a bit of a pain, but not as much as I thought.

Here's an example of a script that I use to build manylinux wheels for the `forceatlas2` package. 


{% highlight bash %}
# Build manylinux wheel for a package

PACKAGE_NAME=fa2
GIT_URL=git@github.com:bhargavchippada/forceatlas2.git
GIT_NAME=forceatlas2
PACKAGE_VERSION=0.3.5
ARCH=linux_x86_64
PYTHON_VERSION=cp310
INTERPRETER=python3.10
WHEEL_PREFIX="${PACKAGE_NAME}-${PACKAGE_VERSION}-${PYTHON_VERSION}-${PYTHON_VERSION}"

# Print commands and exit on error
set -ex

clean () {
    rm -rf build
    rm -rf dist
    rm -rf *.whl
    rm -rf *.egg-info
    rm -rf wheelhouse
    rm -rf */__pycache__
    rm -rf */*.so
    rm -rf forceatlas2
}

echo "Building wheel for ${PACKAGE_NAME} package"

echo "Cloning repository"
rm -rf $GIT_NAME
# git clone --depth 1 --branch v$PACKAGE_VERSION $GIT_URL
git clone $GIT_URL
cd $GIT_NAME

echo "Making sure build tools are up to date"
$INTERPRETER -m pip install --upgrade pip
$INTERPRETER -m pip install --upgrade setuptools wheel auditwheel

# Build wheel
echo "Building wheel"
$INTERPRETER -m pip wheel -w wheelhouse .

# Make manylinux compliant
echo "Making manylinux compliant wheel"
$INTERPRETER -m auditwheel repair wheelhouse/${WHEEL_PREFIX}-${ARCH}.whl

# Test installation
echo "Testing installation"
$INTERPRETER -m pip install wheelhouse/${WHEEL_PREFIX}-manylinux*.whl
echo "Removing package"
$INTERPRETER -m pip uninstall ${PACKAGE_NAME} -y

# Cleanup
echo "Cleaning up"
clean
{% endhighlight %}
