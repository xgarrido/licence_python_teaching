# -*- mode: makefile; -*-
EMACS=emacs
BATCH=$(EMACS) --batch --no-init-file									\
  --eval "(require 'org)"										\
  --eval "(org-babel-do-load-languages 'org-babel-load-languages					\
        '((shell . t)))"										\
  --eval "(setq org-babel-use-quick-and-dirty-noweb-expansion t)"                                       \
  --eval "(setq org-confirm-babel-evaluate nil)"							\
  --eval "(setq c-standard-font-lock-fontify-region-function 'font-lock-default-fontify-region)"	\
  --eval '(org-babel-load-file   "./README.org")'                                                       \
  --eval '(org-babel-tangle-file "./README.org")'							\

SUBDIRS_ALL = td slides

all: html

html: pdf
	@echo "NOTICE: Generating html documentation..."
	@mkdir -p doc/html/pdf
	@for dir in $(SUBDIRS_ALL); do cp $$dir/[0-9]*.pdf doc/html/pdf/.; done
	@cp -r slides/figures/cover.png doc/html/.
	@$(BATCH) --visit "README.org"> /dev/null 2>&1
	@rm -f README.el *.sty

publish: html
	@(cd doc/html; tar czvf /tmp/org-python-publish.tar.gz .)
	@git checkout gh-pages
	@tar xzvf /tmp/org-python-publish.tar.gz
	@if [ -n "`git status --porcelain`" ]; then git commit -am "update doc" && git push; fi
	@git checkout master

pdf:
	@for dir in $(SUBDIRS_ALL); do $(MAKE) -C $$dir || exit $$?; done

clean:
	@rm -rf doc *.sty logo.* *.el

clean-all: clean
	@for dir in $(SUBDIRS_ALL); do $(MAKE) -C $$dir clean || exit $$?; done
