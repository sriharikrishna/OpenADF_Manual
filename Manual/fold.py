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
  opt.add_option('-p','--padding',dest='padding',
                 help="padding string after the line break (default is \'\\t\')",
                 default='\t')
  (options, args) = opt.parse_args()
  paddingLenth=len(options.padding.expandtabs())
  for line in sys.stdin.readlines():
    if len(line)>options.width:
      currentPosInFolded=0
      currentPosInLine=0
      lastSpacePosInFolded=0
      lastSpacePosInLine=0
      allowedLength=options.width
      while (currentPosInLine<len(line)):
        if (currentPosInFolded<allowedLength):
          if (line[currentPosInLine].isspace()):
            lastSpacePosInLine=currentPosInLine
            lastSpacePosInFolded=currentPosInFolded
          currentPosInFolded+=1
          currentPosInLine+=1
        else:
          sys.stdout.write(line[currentPosInLine-currentPosInFolded:currentPosInLine-currentPosInFolded+lastSpacePosInFolded]+'\n')
          if (allowedLength!=options.width-paddingLenth):
            allowedLength-=paddingLenth
          sys.stdout.write(options.padding)
          currentPosInLine=lastSpacePosInLine
          while (currentPosInLine<len(line) and line[currentPosInLine].isspace()):
            currentPosInLine+=1
          lastSpacePosInFolded=0
          currentPosInFolded=0
      if (currentPosInFolded>0):    
        sys.stdout.write(line[currentPosInLine-currentPosInFolded:currentPosInLine])
    else:
      sys.stdout.write(line)

if __name__ == "__main__":
  sys.exit(main())
