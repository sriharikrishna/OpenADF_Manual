subroutine head(x,y) 
  double precision,intent(in) :: x
  double precision,intent(out) :: y
c$openad INDEPENDENT(x)
  y=sin(x*x)
c$openad DEPENDENT(y)
end subroutine
