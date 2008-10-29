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
goadFlags.txt \
scmStatusOutput.txt \
scmStatusFlags.txt \
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

oneMinuteStatusOutput.txt : Examples FORCE
	cd Examples/OneMinute && $(MAKE) clean
	cd Examples/OneMinute ; make toolChain | grep -v "make" > ${THISDIR}/$@

oneMinuteOutput.txt : Examples FORCE
	cd Examples/OneMinute && $(MAKE)
	cd Examples/OneMinute ; ./driver > ${THISDIR}/$@

oneMinuteReverseStatusOutput.txt : Examples FORCE
	cd Examples/OneMinuteReverse && $(MAKE) clean
	cd Examples/OneMinuteReverse ; make toolChain | grep -v "make" > ${THISDIR}/$@

oneMinuteReverseOutput.txt : Examples FORCE
	cd Examples/OneMinuteReverse && $(MAKE)
	cd Examples/OneMinuteReverse ; ./driver > ${THISDIR}/$@

oneMinuteReverseTaping.f : oneMinuteReverseStatusOutput.txt
	cat Examples/OneMinuteReverse/head.prepped.xb.x2w.w2f.pp.f | sed -n '/C taping/,/C taping end/p' > ${THISDIR}/$@

oneMinuteReverseAdjoint.f : oneMinuteReverseStatusOutput.txt
	cat Examples/OneMinuteReverse/head.prepped.xb.x2w.w2f.pp.f | sed -n '/C adjoint/,/C adjoint end/p' > ${THISDIR}/$@

goadFlags.txt : FORCE
	cd ${OPENADROOT}; goad -h > ${THISDIR}/$@

scmStatusOutput.txt : versionInfo.txt
	cd ${OPENADROOT}; scmStatus > ${THISDIR}/$@
scmStatusFlags.txt : FORCE
	cd ${OPENADROOT}; scmStatus -h > ${THISDIR}/$@

Examples :
	ln -sf ${OPENADROOT}/Examples .

clean: 
	rm -f *~ *bak $(TARGET).{toc,aux,ps,pdf,out,log,lof,lot,idx,bbl,blg,dvi} index.aux versionInfo*.txt
	rm -rf $(EXTRAREQS)
	cd Examples && $(MAKE) $@

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
