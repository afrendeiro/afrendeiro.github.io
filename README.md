# My personal website

A Jekyll powered personal website, hosted on [GitHub pages](https://pages.github.com/).
Built on [Bootstrap 5.3](https://getbootstrap.com/) with a light/dark/auto theme
(toggle in the navbar; your choice is remembered in `localStorage` and defaults
to the OS preference).

## Install

Dependencies: [just](https://github.com/casey/just), [uv](https://docs.astral.sh/uv/),
and Ruby with bundler (via your system package manager; on Arch: `sudo pacman -S --needed ruby ruby-bundler ruby-default-gems`).
Ruby gems are installed project-locally into `vendor/bundle`:

```bash
just install
```

### Clone

```bash
git clone git@github.com:afrendeiro/afrendeiro.github.io.git
cd afrendeiro.github.io
```

## Run locally

```bash
just serve
```

served at [http://127.0.0.1:4000/](http://127.0.0.1:4000/).

## Publications

Publications are not edited here. They are synced from the
[lab website repository](https://github.com/rendeirolab/rendeirolab.github.io)
(`content/publications.yaml`), which is the single source of truth.

```bash
just update
```

fetches the lab YAML from GitHub and writes `_data/publications.yml`,
which is rendered by `_includes/publications.html` at build time.
`just serve`/`just build`/`just web` run the sync automatically.

## Publish

```bash
just web
```

syncs publications, commits `_data/publications.yml`, `cv.pdf` and `index.md`,
and pushes to the `gh-pages` branch. GitHub Pages builds the site server-side.

## Create pages and posts

    rake page:new name="about"
    rake post:new title="notebook"

or to make a draft and publish it only after:

    rake draft:new title="new post"
    rake draft:ready title="new post"
