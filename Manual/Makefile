TARGET=openad

# dot converts to PS and ps2pdf converts to pdf (see below)
PDF_FROM_DOT=$(basename $(wildcard *.dot))

# dia exports to eps and epstopdf converts to pdf:
PDF_FROM_DIA=$(basename $(wildcard *.dia))

# directly exported from xfig to pdf:
PDF_FROM_FIG=$(basename $(wildcard *.fig))

$(TARGET).pdf: $(addsuffix .pdf,$(PDF_FROM_DOT) $(PDF_FROM_DIA) $(PDF_FROM_FIG)) versionInfo.txt $(TARGET).tex $(TARGET).bbl $(TARGET).aux
	pdflatex $(TARGET) 

versionInfo.txt : FORCE 
	./createVersionInfo.sh

$(TARGET).bbl $(TARGET).aux: $(TARGET).bib 
	# ensure we make a .aux file
	pdflatex $(TARGET)
	# use the .aux file
	bibtex $(TARGET)
	# rerun to fix up the .aux file
	pdflatex $(TARGET)

clean: 
	rm -f *~ *bak $(TARGET).{toc,aux,ps,pdf,out,log,lof,bbl,blg,dvi} versionInfo.*

%.ps : %.dot
	dot -Tps2 $< -o $@

%.pdf : %.ps
	ps2pdf $<

%.pdf : %.eps
	epstopdf $<

.PHONY: clean

FORCE: 