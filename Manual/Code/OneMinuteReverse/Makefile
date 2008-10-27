ifndef (F90C)
F90C=gfortran
endif
ifndef (CC)
CC=gcc
endif
RTSUPP=w2f__types OAD_active OAD_cp OAD_tape OAD_rev iaddr
driver: $(addsuffix .o, $(RTSUPP)) driver.o head.prepped.xb.x2w.w2f.pp.o
	${F90C} -o $@ $^
head.prepped.xb.x2w.w2f.pp.f $(addsuffix .f90, $(RTSUPP)) : toolChain 
toolChain : head.prepped.f90
	openad -c -m rj $<
%.o : %.f90
	${F90C} -o $@ -c $< 
%.o : %.f
	${F90C} -o $@ -c $< 
%.o : %.c
	${CC} -o $@ -c $< 
clean: 
	rm -f ad_template* ad_inline.f OAD_* w2f__*  iaddr* 
	rm -f head.prepped.xb* *.B *.xaif *.o *.mod driver *~ 
.PHONY: clean toolChain
