ifndef (F90C)
F90C=gfortran
endif
RTSUPP=w2f__types OAD_active
driver: $(addsuffix .o, $(RTSUPP)) driver.o head.prepped.xb.x2w.w2f.pp.o
	${F90C} -o $@ $^
head.prepped.xb.x2w.w2f.pp.f $(addsuffix .f90, $(RTSUPP)) : head.prepped.f90
	openad -c -m f $<
%.o : %.f90
	${F90C} -o $@ -c $< 
%.o : %.f
	${F90C} -o $@ -c $< 
clean: 
	rm -f ad_template* OAD_* w2f__*  iaddr* 
	rm -f head.prepped.xb* *.B *.xaif *.o *.mod oad_tr_* driver *~ 
.PHONY: clean
