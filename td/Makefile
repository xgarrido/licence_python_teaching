# -*- mode: makefile; -*-
files_ipynb = $(wildcard *.ipynb)
files_pdf = $(files_ipynb:.ipynb=.pdf)
files_binder = $(addprefix ../binder-sandbox/, $(files_ipynb))

all: $(files_pdf)

%.pdf: %.ipynb .td.tex.j2
	@echo "NOTICE: Exporting $< to pdf..."
	@jupyter nbconvert --to latex --template-file .td.tex.j2 --no-input $< --TagRemovePreprocessor.remove_cell_tags="correction"
	@xelatex -shell-escape $(<:.ipynb=.tex)

ipynb: $(files_binder)

../binder-sandbox/%.ipynb: %.ipynb
	@echo "NOTICE: Running $<..."
ifndef with-correction
	jq 'del(.cells[] | select(.metadata[] == ["skip"] or .metadata[] == ["correction"]))' $< > $@
else
	jupyter nbconvert --execute --to notebook --inplace $<
	jq 'del(.cells[] | select(.metadata[] == ["skip"] or .metadata[] == ["reponse"]))' $< > $@
	sed -i -e 's/\(.*\)\("toc-hr-collapsed":\).*/\1\2 false,/' -e 's/\(.*\)\("toc-nb-collapsed":\).*/\1\2 false/' $@

endif

clean:
	@rm -rf	latex.d *.tex *.aux *.pdf *.fdb* *~ _minted* *.toc *.out *.log svg-inkscape
