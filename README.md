# My personal website

A Jekyll powered personal website. Uses [Jekyll Bootstrap](http://jekyllbootstrap.com/)
and is hosted on [GitHub pages](https://pages.github.com/).

## Install

### Dependencies

First make sure you have the ruby package manager [bundler](https://bundler.io/bundle_install.html):

```bash
sudo apt install ruby-dev ruby-bundler
```

Now install the requirements specified in the [Gemfile](Gemfile):

```bash
bundle install
```

### The actual website

```bash
USERNAME=afrendeiro # replace with your username
git clone https://github.com/plusjade/jekyll-bootstrap.git $USERNAME.github.io
cd $USERNAME.github.io
git remote set-url origin git@github.io:${USERNAME}/${USERNAME}.github.io.git
git push origin master
```

Edit the `_config.yaml` file with your information, social networks, cv, etc...
and you're ready!

## Create pages and posts

    rake page:new name="about"
    rake post:new title="notebook"

or to make a draft and publish it only after:

    rake draft:new title="new post"
    rake draft:ready title="new post"

## Run locally

    rake preview

or

    jekyll serve

served at [http://0.0.0.0:4000/](http://0.0.0.0:4000/).

## Themes

Go to `http://themes.jekyllbootstrap.com/`, choose a theme and install it:

    rake theme:install git="https://github.com/jekyllbootstrap/theme-twitter.git"

Customize themes or create a new one from scratch.
