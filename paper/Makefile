TARGET=openad

$(TARGET).ps: $(TARGET).dvi $(wildcard *.eps)
	dvips  $(TARGET) -o

$(TARGET).bbl $(TARGET).aux: $(TARGET).bib 
	# ensure we make a .aux file
	latex $(TARGET)
	# use the .aux file
	bibtex $(TARGET)
	# rerun to fix up the .aux file
	latex $(TARGET)

$(TARGET).dvi: $(TARGET).tex $(TARGET).bbl $(TARGET).aux
	latex $(TARGET) 

clean: 
	rm -f *~ *bak $(TARGET).{toc,aux,pdf,ps,eps,log,lof,bbl,blg,dvi}

.PHONY: clean
