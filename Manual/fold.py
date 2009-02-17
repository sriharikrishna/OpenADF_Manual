#!/usr/bin/env python
#-*-Mode: python;-*-

import sys,string

def main():
  from optparse import OptionParser
  usage = '%prog [options]\n\t fold long lines'
  opt = OptionParser(usage=usage)
  opt.add_option('-w','--width',dest='width',
                 help="width to be respected (default 132)",
                 type="int",default=132)
  opt.add_option('-c','--continuation',dest='continuation',
                 help="use \'\\\' as continuation character",
                 action='store_true',default=False)
  (options, args) = opt.parse_args()
  for line in sys.stdin.readlines():
    if len(line)>options.width:
       words = string.split(line)
       cWord=0
       sWord=0
       while True :
           if cWord==len(words)-1:
               sys.stdout.write(words[cWord]+"\n")
               break
           tl=0
           while tl<=options.width and cWord<len(words)-1:
               tl+=len(words[cWord])
               cWord+=1
           if (tl>options.width and cWord>sWord+1):
              cWord-=1
           for i in range(sWord,cWord):
               sys.stdout.write(words[i])
               sys.stdout.write(' ')
           if cWord<len(words):
             if (options.continuation):
               sys.stdout.write("\\")
             sys.stdout.write("\n\t")
           sWord=cWord
    else:
        sys.stdout.write(line)
       

if __name__ == "__main__":
  sys.exit(main())
