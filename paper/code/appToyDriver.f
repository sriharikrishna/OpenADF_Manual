program driver
  use OpenAD_active
  external head
  type(active):: x, y
  read *, x%v    
  x%d=1.0
  call head(x,y)
  write (*,*) "J(1,1)=",y%d
end program driver
