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
oneMinuteReverseTaping.f90 \
oneMinuteReverseAdjoint.f90 \
oneMinuteReverseExplOutput.txt \
openadUpdateFlags.txt \
openadStatusOutput.txt \
openadStatusFlags.txt \
openadScriptOptions.txt \
openadScriptNoAction.txt \
preProcessOptions.txt \
Examples/SRCanonical/func.pre.f90 \
Examples/MaxCanonical/func.pre.f90 \
Examples/ArgExprCanonical/func.pre.f90 \
postProcessOptions.txt \
mfef90Options.txt \
whirl2fOptions.txt \
whirl2xaifOptions.txt \
xaif2whirlOptions.txt \
rtPropagationRoutines.txt \
numericalDiscrepancy.pdf \
selfAdjointDriverOutput.txt \
selfAdjointDriverADMsplitOutput.txt \
selfAdjointDriverFDOutput.txt \
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

PORTRAIT_ORIENT_BOX_WIDTH=143

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
	cd Examples/OneMinute && $(MAKE) -B driverE | ${THISDIR}/fold.py -c -w $(PORTRAIT_ORIENT_BOX_WIDTH) > ${THISDIR}/$@

oneMinuteReverseStatusOutput.txt : Examples $(FORCE)
	cd Examples/OneMinuteReverse && $(MAKE) clean
	cd Examples/OneMinuteReverse ; make toolChain | grep -v "make" > ${THISDIR}/$@

oneMinuteReverseOutput.txt : Examples $(FORCE)
	cd Examples/OneMinuteReverse && $(MAKE)
	cd Examples/OneMinuteReverse ; ./driver > ${THISDIR}/$@

oneMinuteReverseTaping.f90 : oneMinuteReverseStatusOutput.txt
	cat Examples/OneMinuteReverse/head.prepped.pre.xb.x2w.w2f.post.f90 | sed -n '/! taping/,/! taping end/p' > ${THISDIR}/$@

oneMinuteReverseAdjoint.f90 : oneMinuteReverseStatusOutput.txt
	cat Examples/OneMinuteReverse/head.prepped.pre.xb.x2w.w2f.post.f90 | sed -n '/! adjoint/,/! adjoint end/p' > ${THISDIR}/$@

oneMinuteReverseExplOutput.txt : Examples $(FORCE)
	cd Examples/OneMinuteReverse && $(MAKE) -B driverE | ${THISDIR}/fold.py -c -w $(PORTRAIT_ORIENT_BOX_WIDTH) > ${THISDIR}/$@

openadUpdateFlags.txt : $(FORCE)
	cd ${OPENADROOT}; openadUpdate -h > ${THISDIR}/$@

openadStatusOutput.txt : versionInfo.txt
	cd ${OPENADROOT}; openadStatus > ${THISDIR}/$@
openadStatusFlags.txt : $(FORCE)
	cd ${OPENADROOT}; openadStatus -h > ${THISDIR}/$@

preProcessOptions.txt : $(FORCE)
	export COLUMNS=$(PORTRAIT_ORIENT_BOX_WIDTH); ${OPENADFORTTK_BASE}/tools/SourceProcessing/preProcess.py -h | ${THISDIR}/fold.py -p '			' -w $(PORTRAIT_ORIENT_BOX_WIDTH) > ${THISDIR}/$@

Examples/SRCanonical/func.pre.f90 : Examples $(FORCE)
	cd Examples/SRCanonical && $(MAKE)

Examples/MaxCanonical/func.pre.f90 : Examples $(FORCE)
	cd Examples/MaxCanonical && $(MAKE)

Examples/ArgExprCanonical/func.pre.f90 : Examples $(FORCE)
	cd Examples/ArgExprCanonical && $(MAKE)

postProcessOptions.txt : $(FORCE)
	export COLUMNS=$(PORTRAIT_ORIENT_BOX_WIDTH); ${OPENADFORTTK_BASE}/tools/SourceProcessing/postProcess.py -h | ${THISDIR}/fold.py -p '			' -w $(PORTRAIT_ORIENT_BOX_WIDTH) > ${THISDIR}/$@

mfef90Options.txt : $(FORCE)
	${OPEN64ROOT}/crayf90/sgi/mfef90 -h | egrep '(-z|-N|-F|-f|in the Open64)' > ${THISDIR}/$@

whirl2fOptions.txt : $(FORCE)
	${OPEN64ROOT}/whirl2f/whirl2f  2>&1 | awk 'NR<=35 || (NR>=54 && NR<=59)' | ${THISDIR}/fold.py -p '	' $(PORTRAIT_ORIENT_BOX_WIDTH) > ${THISDIR}/$@

whirl2xaifOptions.txt : $(FORCE)
	${OPENADFORTTKROOT}/bin/whirl2xaif -h 2> ${THISDIR}/$@

xaif2whirlOptions.txt : $(FORCE)
	${OPENADFORTTKROOT}/bin/xaif2whirl -h 2> ${THISDIR}/$@

rtPropagationRoutines.txt : $(FORCE)
	cat ${OPENADROOT}/runTimeSupport/scalar/OAD_active.f90 | grep subroutine | grep -v convert | grep -v 'end subroutine' | grep -v 'allocateMatching' | grep -v 'shapeTest' | grep -v 'runTimeError' | grep -v 'allocateShape' | sed 's/ *subroutine //' > ${THISDIR}/$@

numericalDiscrepancy.ps : $(FORCE)
	cd ${OPENADROOT}/Regression/testRoundTrip && $(MAKE) clean
	echo "scalar tlm none" > ${OPENADROOT}/Regression/testRoundTrip/.lastRun
	cd ${OPENADROOT}/Regression/testRoundTrip && ./testAll.py -c gfortran -b boxmodel 
	- cd ${OPENADROOT}/Regression/testRoundTrip && ./numericalComparison.py -gi -t postscript -n boxmodel tmpOutput/dd.out examples/boxmodel/refOutput/dd.out tmpOutput/ad.out examples/boxmodel/refOutput/ad.out
	cp ${OPENADROOT}/Regression/testRoundTrip/plotOutput/numericalComparison-boxmodel.ps $@

selfAdjointDriverOutput.txt : Examples $(FORCE)
	cd Examples/SelfAdjoint && $(MAKE)
	cd Examples/SelfAdjoint; ./driver > ${THISDIR}/$@

selfAdjointDriverADMsplitOutput.txt : Examples $(FORCE)
	cd Examples/SelfAdjoint/ADMsplit && $(MAKE)
	cd Examples/SelfAdjoint/ADMsplit; ./driverADMsplit > ${THISDIR}/$@

selfAdjointDriverFDOutput.txt : Examples $(FORCE)
	cd Examples/SelfAdjoint/FD && $(MAKE)
	cd Examples/SelfAdjoint/FD; ./driverFD > ${THISDIR}/$@

Examples :
	ln -sf ${OPENADROOT}/Examples .

clean: 
	rm -f *~ *bak $(TARGET).{toc,aux,ps,pdf,out,log,lof,lot,idx,bbl,blg,dvi,bib} index.aux
	rm -f head.{f,B,xaif,xb.x2w.B,xb.x2w.w2f.f,xb.x2w.w2f.pp.f,xb.xaif}
	rm -f iaddr.c OAD_active.f90 w2f__types.f90 openadScriptOutput.txt versionInfoOpenAD.txt
	rm -rf $(EXTRAREQS)
	rm -f autodiff.bib.gz
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
