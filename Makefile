build:
	mkdocs build --clean
	cp -r slides/* site
	cp -r notebooks site
	cp -r demos site

all: build
	rsync -a --delete site/* /export/home/caodg/public_html/course/ic/
