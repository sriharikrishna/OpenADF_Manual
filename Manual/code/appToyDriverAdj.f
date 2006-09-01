program driver
  use OpenAD_active
  use OpenAD_rev
  external head
  type(active):: x, y
  read *, x%v    
  y%d=1.0  
  our_rev_mode%tape=.TRUE.
  our_rev_mode%adjoint=.TRUE.
  call head(x,y)
  write (*,*) "J(1,1)=",x%d
end program driver
