update:
	python3 update_publications_resources.py

serve: update
	bundler exec jekyll serve --incremental

web: update
	# Update website: "afrendeiro.github.io"
	git add \
		publications.csv \
		publication_resources.csv \
		cv.pdf \
		index.md; \
	git commit -m 'update publications'; \
	git push origin gh-pages

all: update serve

.DEFAULT_GOAL := all
