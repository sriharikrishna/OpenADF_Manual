subroutine head(x,y,k)
double precision x(2),y(k)
integer i,k

  y(k)=sin(x(1)*x(2)) 
  k=k+1 
  if (imod(k,2) .eq. 1) then  
    y(k)=2*y(k-1)  
  else  
    do i=1,k  
      t1=x(1)+x(2)  
      t2=t1*sin(x(1))  
      x(1)=cos(t1*t2)  
      x(2)=-sqrt(t2)  
    end do  
  end if   
  y(k)=y(k)+x(1)*x(2)
end subroutine
