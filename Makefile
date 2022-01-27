# 
# Makefile für die Generierung von Scripten an der BFS
#
SPHINXOPTS    = -j auto -q
SPHINXBUILD   = sphinx-build
SPHINXPROJ    = umlaut-issue
SOURCEDIR     = source
# 
# Die Module von welchen kopiert werden soll müssen vorher eingehängt werden.
# z.B.
# git submodule add -f git@32840.bfs-kaelte-klima.de:scripte-de/modul-2-wien.git copyfrom/modul-2-wien
# die folgende Zeile muss dann angepasst werden xxx -> copyfrom/modul-2-wien
#
COPYFROM      = copyfrom/xxx
COPYFROM2     = copyfrom
BUILDDIR      = build
HTDIR         = htdocs
HTFILES		  = $(BUILDDIR)/html/
SINGLEDIR     = $(BUILDDIR)/singlehtml
DEPLOYDIR     = /home/gitlab-runner/autoscript/$(SPHINXPROJ)

export PYTHONPATH := $(shell pwd):$(PYTHONPATH)

DATE := $(shell date)
USER := $(shell whoami)
#TAG  := $(shell git tag)

GITVERSION := $(BFS_VERSION)
GITMESSAGE := $(BFS_MESSAGE)




all :
	echo "GITVERSION = $(GITVERSION)"
	echo "GITMESSAGE = $(GITMESSAGE)"
	echo "TAG = $(TAG)"
	make pdf

ifeq "$(strip $(USER))"  "gitlab-runner"
deploy:
	rm -rf $(DEPLOYDIR)
	mkdir -p $(DEPLOYDIR)
	mkdir -p $(DEPLOYDIR)/html
	mv $(HTFILES)/* $(DEPLOYDIR)/html
	cp build/latex/$(SPHINXPROJ).pdf $(DEPLOYDIR)/$(SPHINXPROJ).pdf
	cp build/singlehtml/index.docx $(DEPLOYDIR)/$(SPHINXPROJ).docx
	echo "Neu erstelltes Script wurde auf den Windows server kopiert"
else
deploy:
	echo "__$(USER)__ is not gitlab-runner, so no deployment"
endif
#
# In dem update müssen Befehle zum synchronisieren sein
# Zwei Beispiele sind auskommentiert
#
update:
	git submodule foreach git pull origin master
	#rsync -auv --exclude 'index.rst' --exclude 'version.rst' $(COPYFROM)/source/*.rst $(SOURCEDIR)
	#rsync -auv $(COPYFROM)/source/_bilder     $(SOURCEDIR)

copypdf:
	cp build/latex/$(SPHINXPROJ).pdf source/$(SPHINXPROJ).pdf
	cp build/latex/$(SPHINXPROJ).pdf public/$(SPHINXPROJ).pdf

graupdf:
	gs -sOutputFile=build/latex/$(SPHINXPROJ)_grau.pdf -sDEVICE=pdfwrite -sColorConversionStrategy=Gray \
	-dProcessColorModel=/DeviceGray -dCompatibilityLevel=1.4 -dNOPAUSE -dBATCH build/latex/$(SPHINXPROJ).pdf 
	cp build/latex/$(SPHINXPROJ)_grau.pdf $(DEPLOYDIR)/$(SPHINXPROJ)_grau.pdf

copydocx:
	cp build/singlehtml/index.docx source/$(SPHINXPROJ).docx
	cp build/singlehtml/index.docx public/$(SPHINXPROJ).docx

copyhtml:
	cp -r build/html/ public/

nopublic:
	rm -rf public/*

pdf:
	sphinx-build -M latexpdf  source build  -c source/pdf_conf

compresspdf:
	mv build/latex/$(SPHINXPROJ).pdf build/latex/$(SPHINXPROJ)-big.pdf
	ps2pdf build/latex/$(SPHINXPROJ)-big.pdf build/latex/$(SPHINXPROJ).pdf
	rm build/latex/$(SPHINXPROJ)-big.pdf

version:
	echo $(USER)
	python makeversion.py
	
docx:
	cd build/singlehtml && pandoc -o index.docx index.html

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile

htdocs:
	rsync -rupE "$(HTFILES)" "$(HTDIR)"
	
# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)



	