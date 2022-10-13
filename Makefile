

update:
	python update_publications_resources.py

serve: update
	bundler exec jekyll serve

all: update serve

.DEFAULT_GOAL := all
