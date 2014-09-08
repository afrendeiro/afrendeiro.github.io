# Open Science notebook

A Jekyll powered blog hosted on GitHub pages.
Based on the [Jekyll Bootstrap](http://jekyllbootstrap.com/) boilerplate.

## Install
```bash
USERNAME=afrendeiro # replace with your username
git clone https://github.com/plusjade/jekyll-bootstrap.git $USERNAME.github.io
cd $USERNAME.github.io
git remote set-url origin git@github.io:${USERNAME}/${USERNAME}.github.io.git
git push origin master
```
Edit `_config.yml` and you're ready to go.

## Create pages and post
    rake page name="about"
    rake post title="notebook"

## Run locally
    jekyll serve

see pages on `http://0.0.0.0:4000/`.

## Edit configuration
Edit the `_config.yaml` file with your information, social networks, licence, etc...

## Customize

### Install theme
Go to `http://themes.jekyllbootstrap.com/`, choose a theme and install it:
    
    rake theme:install git="https://github.com/jekyllbootstrap/theme-twitter.git"

Customize it or create new from scratch.