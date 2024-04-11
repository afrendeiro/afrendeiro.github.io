clean:
	bundler exec jekyll clean

update:
	python3 update_publications_resources.py

serve: clean update
	bundler exec jekyll serve --incremental
	xdg-open http://127.0.0.1:4000

web: clean update
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
