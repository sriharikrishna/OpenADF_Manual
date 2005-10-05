TARGET=openad

$(TARGET).pdf: $(TARGET).tex $(TARGET).bbl $(TARGET).aux
	pdflatex $(TARGET) 

$(TARGET).bbl $(TARGET).aux: $(TARGET).bib 
	# ensure we make a .aux file
	pdflatex $(TARGET)
	# use the .aux file
	bibtex $(TARGET)
	# rerun to fix up the .aux file
	pdflatex $(TARGET)

clean: 
	rm -f *~ *bak $(TARGET).{toc,aux,ps,pdf,out,log,lof,bbl,blg,dvi}

.PHONY: clean
