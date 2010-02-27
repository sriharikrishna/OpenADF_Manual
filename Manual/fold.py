#!/usr/bin/env python
#-*-Mode: python;-*-

import sys,string

continChar='\\'

class FoldException(Exception):
  def __init__(self,reason):
    Exception.__init__(self,reason)
  
def processLine(line,options):
  paddingLenth=len(options.padding.expandtabs())
  paddingLenth=len(options.padding.expandtabs())
  allowedLength=options.width
  continStr=''
  if (options.continuation): 
    continStr=' '+continChar
  needCont=False
  needPadding=False
  # sanity test for first token
  tokens=line.split()
  if (len(tokens) and len(tokens[0])>allowedLength):
    msg="ERROR: first token length "+str(len(tokens[0]))+" exceeds "+str(allowedLength)+" (permitted width "+str(options.width)+" and consider padding and continuation) for "+tokens[0]
    raise FoldException, msg
  if len(line)>allowedLength:
    needCont=True; allowedLength-=len(continStr) # now we know that we need to continue
    currentPosInFolded=0
    currentPosInLine=0
    lastSpacePosInFolded=0
    lastSpacePosInLine=0
    while (currentPosInLine<len(line)):
      if (currentPosInFolded<allowedLength):
        if (line[currentPosInLine].isspace()):
          lastSpacePosInLine=currentPosInLine
          lastSpacePosInFolded=currentPosInFolded
        currentPosInFolded+=1
        currentPosInLine+=1
      else:
        if (lastSpacePosInFolded==0
            or
            (lastSpacePosInFolded!=0
             and
             currentPosInLine<len(line)
             and
             (line[currentPosInLine+1]==' '
              or
              line[currentPosInLine+1]=='\n'))): # special case when there is a token that just fits in the allowed length
          lastSpacePosInFolded=currentPosInFolded
          lastSpacePosInLine=currentPosInLine
        sys.stdout.write(line[currentPosInLine-currentPosInFolded:currentPosInLine-currentPosInFolded+lastSpacePosInFolded]+continStr+'\n')
        # now that we wrote this - check what happens next
        # sanity test for next token
        tokens=line[currentPosInLine-currentPosInFolded+lastSpacePosInFolded:].split()
        if (len(tokens) and len(tokens[0])>allowedLength):
          msg="ERROR: token length "+str(len(tokens[0]))+" exceeds "+str(allowedLength)+" (permitted width "+str(options.width)+" and consider padding and continuation) for "+tokens[0]
          raise FoldException, msg
        # do we still need to break the rest?
        if ((len(line)-currentPosInLine)<=allowedLength): 
          needCont=False; allowedLength+=len(continStr)
        # the first line isn't padded but all following lines need to be padded
        if (not needPadding):
          allowedLength-=paddingLenth
          needPadding=True
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
  opt.add_option('--inputFile',dest='inputFile',
                 help="in put file (default is stdin)",
                 metavar='<file_name>',
                 default=None)
  (options, args) = opt.parse_args()
  continued=False
  cLine="" # a continued line
  try:
    input=sys.stdin
    if (options.inputFile) :
      input=open(options.inputFile,"r")
    for line in input.readlines():
      if (options.continuation) :
        import pdb
        #pdb.set_trace()
        tokens=line.split()
        if (continued):
          firstNonSpace=0
          if (len(tokens)):
            firstNonSpace=line.find(tokens[0][0])
          line=line[firstNonSpace:]
        if (len(tokens) and tokens[-1][-1]==continChar) :
          continued=True
          if (len(tokens)>1 and len(tokens[-1][-1])==1):
            line=line[:line.rfind(tokens[-2][-1])+1]
          else: 
            line=line[:line.rfind(continChar)]
        else:
          continued=False
      if (len(cLine) and len(line) and cLine[-1]!=' ' and line[0]!=' '):
        cLine+=' ' 
      cLine+=line
      if (continued) :
        continue
      processLine(cLine,options)
      cLine=""
  except (FoldException), e:
    sys.stderr.write(str(e)+"\n")
    return -1
  if (options.inputFile) :
    input.close()
  return 0

if __name__ == "__main__":
  sys.exit(main())
