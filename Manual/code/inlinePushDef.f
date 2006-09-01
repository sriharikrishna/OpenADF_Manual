subroutine push(x)
C$openad$ inline DECLS
  use OpenAD_tape
  implicit none
  double precision :: x
C$openad$ end DECLS
  double_tape(double_tape_pointer)=x
  double_tape_pointer=double_tape_pointer+1
end subroutine 
