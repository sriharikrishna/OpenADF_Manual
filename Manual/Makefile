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
oneMinuteExplOutput.txt \
oneMinuteReverseStatusOutput.txt \
oneMinuteReverseOutput.txt \
oneMinuteReverseTaping.f \
oneMinuteReverseAdjoint.f \
oneMinuteReverseExplOutput.txt \
goadFlags.txt \
scmStatusOutput.txt \
scmStatusFlags.txt \
openadScriptOptions.txt \
openadScriptNoAction.txt \
$(DOT2PDF) \
$(DIA2PDF) \
$(FIG2PDF) 

THISDIR=$(shell pwd)

ifndef OPENADROOT
$(error "OpenAD environment not set")
endif

ifdef NOFORCE
FORCE=
else
FORCE=FORCE
endif

$(TARGET).pdf: $(TARGET).blg $(TARGET).bbl
	# run it twice
	pdflatex $(TARGET)
	pdflatex $(TARGET)

$(TARGET).blg $(TARGET).bbl: $(TARGET).aux
	bibtex $(TARGET)

$(TARGET).aux: extraReqs $(TARGET).tex $(TARGET).bib 
	# ensure we make a .aux file
	pdflatex $(TARGET)

$(TARGET).bib: autodiff.bib local.bib
	cat local.bib autodiff.bib > $@

autodiff.bib: $(FORCE)
	./getBib.sh  $@

extraReqs: $(EXTRAREQS)
	echo $(EXTRAREQS)

openadScriptOptions.txt openadScriptOutput.txt openadScriptNoAction.txt : $(FORCE)
	./createOpenadOptionsAndOutput.sh

versionInfo.txt versionInfoOpenAD.txt : $(FORCE) 
	./createVersionInfo.sh

oneMinuteStatusOutput.txt : Examples $(FORCE)
	cd Examples/OneMinute && $(MAKE) clean
	cd Examples/OneMinute ; make toolChain | grep -v "make" > ${THISDIR}/$@

oneMinuteOutput.txt : Examples $(FORCE)
	cd Examples/OneMinute && $(MAKE)
	cd Examples/OneMinute ; ./driver > ${THISDIR}/$@

oneMinuteExplOutput.txt : Examples $(FORCE)
	cd Examples/OneMinute && $(MAKE) -B driverE | ${THISDIR}/fold.py -c -w 140 > ${THISDIR}/$@

oneMinuteReverseStatusOutput.txt : Examples $(FORCE)
	cd Examples/OneMinuteReverse && $(MAKE) clean
	cd Examples/OneMinuteReverse ; make toolChain | grep -v "make" > ${THISDIR}/$@

oneMinuteReverseOutput.txt : Examples $(FORCE)
	cd Examples/OneMinuteReverse && $(MAKE)
	cd Examples/OneMinuteReverse ; ./driver > ${THISDIR}/$@

oneMinuteReverseTaping.f : oneMinuteReverseStatusOutput.txt
	cat Examples/OneMinuteReverse/head.prepped.xb.x2w.w2f.pp.f | sed -n '/C taping/,/C taping end/p' > ${THISDIR}/$@

oneMinuteReverseAdjoint.f : oneMinuteReverseStatusOutput.txt
	cat Examples/OneMinuteReverse/head.prepped.xb.x2w.w2f.pp.f | sed -n '/C adjoint/,/C adjoint end/p' > ${THISDIR}/$@

oneMinuteReverseExplOutput.txt : Examples $(FORCE)
	cd Examples/OneMinuteReverse && $(MAKE) -B driverE | ${THISDIR}/fold.py -c -w 140 > ${THISDIR}/$@

goadFlags.txt : $(FORCE)
	cd ${OPENADROOT}; goad -h > ${THISDIR}/$@

scmStatusOutput.txt : versionInfo.txt
	cd ${OPENADROOT}; scmStatus > ${THISDIR}/$@
scmStatusFlags.txt : $(FORCE)
	cd ${OPENADROOT}; scmStatus -h > ${THISDIR}/$@

Examples :
	ln -sf ${OPENADROOT}/Examples .

clean: 
	rm -f *~ *bak $(TARGET).{toc,aux,ps,pdf,out,log,lof,lot,idx,bbl,blg,dvi,bib} index.aux
	rm -f head.{f,B,xaif,xb.x2w.B,xb.x2w.w2f.f,xb.x2w.w2f.pp.f,xb.xaif}
	rm -f iaddr.c OAD_active.f90 w2f__types.f90 openadScriptOutput.txt versionInfoOpenAD.txt
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
