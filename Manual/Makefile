TARGET=openad

DOTFILES=$(wildcard *.dot)
DOT2PDF=$(DOTFILES:.dot=.pdf)

DIAFILES=$(wildcard *.dia)
DIA2PDF=$(DIAFILES:.dia=.pdf)

FIGFILES=$(wildcard *.fig)
FIG2PDF=$(FIGFILES:.fig=.pdf)

EXTRAREQS= \
versionInfo.txt \
oneMinuteStatusOutput.txt \
oneMinuteOutput.txt \
oneMinuteReverseStatusOutput.txt \
oneMinuteReverseOutput.txt \
oneMinuteReverseTaping.f \
oneMinuteReverseAdjoint.f \
$(DOT2PDF) \
$(DIA2PDF) \
$(FIG2PDF) 

THISDIR=$(shell pwd)

ifndef OPENADROOT
$(error "OpenAD environment not set")
endif

$(TARGET).pdf : $(TARGET).aux $(TARGET).blg $(TARGET).bbl
# run it twice
	pdflatex $(TARGET)
	pdflatex $(TARGET)

$(TARGET).aux :  extraReqs $(TARGET).tex $(TARGET).bib 
# ensure we make a .aux file
	pdflatex $(TARGET)

$(TARGET).blg $(TARGET).bbl: $(TARGET).aux
	bibtex $(TARGET)

extraReqs: $(EXTRAREQS)
	echo $(EXTRAREQS)

versionInfo.txt : FORCE 
	./createVersionInfo.sh

oneMinuteStatusOutput.txt : FORCE
	cd Code/OneMinute && $(MAKE) clean
	cd Code/OneMinute ; make toolChain | grep -v "make" > ${THISDIR}/$@

oneMinuteOutput.txt : FORCE
	cd Code/OneMinute && $(MAKE)
	cd Code/OneMinute ; ./driver > ${THISDIR}/$@

oneMinuteReverseStatusOutput.txt : FORCE
	cd Code/OneMinuteReverse && $(MAKE) clean
	cd Code/OneMinuteReverse ; make toolChain | grep -v "make" > ${THISDIR}/$@

oneMinuteReverseOutput.txt : FORCE
	cd Code/OneMinuteReverse && $(MAKE)
	cd Code/OneMinuteReverse ; ./driver > ${THISDIR}/$@

oneMinuteReverseTaping.f : oneMinuteReverseStatusOutput.txt
	cat Code/OneMinuteReverse/head.prepped.xb.x2w.w2f.pp.f | sed -n '/C taping/,/C taping end/p' > $@

oneMinuteReverseAdjoint.f : oneMinuteReverseStatusOutput.tx
	cat Code/OneMinuteReverse/head.prepped.xb.x2w.w2f.pp.f | sed -n '/C adjoint/,/C adjoint end/p' > $@

clean: 
	rm -f *~ *bak $(TARGET).{toc,aux,ps,pdf,out,log,lof,lot,idx,bbl,blg,dvi} index.aux versionInfo*.txt
	rm -rf $(EXTRAREQS)
	cd Code/OneMinute && $(MAKE) $@
	cd Code/OneMinuteReverse && $(MAKE) $@

%.ps : %.dot
	dot -Tps2 $< -o $@

%.eps : %.dia
	dia -t eps $< -e $@

%.pdf : %.fig
	fig2dev -L pdf $< $@

%.pdf : %.ps
	ps2pdf $<

%.pdf : %.eps
	epstopdf $<


.PHONY: clean extraReqs

FORCE: 
