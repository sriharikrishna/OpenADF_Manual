#!/usr/bin/env python
#-*-Mode: python;-*-

import sys,string

def main():
  for line in sys.stdin.readlines():
    if len(line)>132:
       words = string.split(line)
       cWord=0
       sWord=0
       while True :
           if cWord==len(words)-1:
               sys.stdout.write(words[cWord]+"\n")
               break
           tl=0
           while tl<=132 and cWord<len(words)-1:
               tl+=len(words[cWord])
               cWord+=1
           if (tl>132 and cWord>sWord+1):
              cWord-=1
           for i in range(sWord,cWord):
               sys.stdout.write(words[i])
               sys.stdout.write(' ')
           if cWord<len(words):
               sys.stdout.write("\\\n\t")
           sWord=cWord
    else:
        sys.stdout.write(line)
       

if __name__ == "__main__":
  sys.exit(main())
