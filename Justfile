default: serve

# Install dependencies (Arch Linux: system packages + Ruby gems, project-local)
install:
    sudo pacman -S --needed ruby ruby-bundler ruby-default-gems
    bundle config set --local path vendor/bundle
    bundle install

# Clean the built site
clean:
    bundler exec jekyll clean

# Sync publications from the lab website: fetches content/publications.yaml
# from rendeirolab.github.io (main branch) and writes _data/publications.yml.
# The lab YAML is the single source of truth - edit publications there, not here.
update:
    uv run --script sync_publications.py

# Build the site locally (into _site/)
build: clean update
    bundler exec jekyll build

# Serve the site locally at http://127.0.0.1:4000
serve: clean update
    bundler exec jekyll serve --incremental

# Sync publications and publish: commits the generated publications data,
# the CV and the homepage, then pushes to the gh-pages branch.
# GitHub Pages builds the site server-side from that branch.
web: clean update
    git add _data/publications.yml cv.pdf index.md
    git commit -m 'update publications'
    git push origin gh-pages
