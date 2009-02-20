#!/bin/sh
hg tip > /dev/null
if [ $? -ne 0 ] 
then 
  echo "vers. unknown" > versionInfo.txt.new
else
  echo -n "vers. hg:$(hg id -i):$(hg id  -n)" > versionInfo.txt.new
fi
if [ -f versionInfo.txt ] 
then
  diff versionInfo.txt.new versionInfo.txt > /dev/null
  if [ $? -eq 0 ]
  then 
    rm  versionInfo.txt.new
  else
    mv versionInfo.txt.new versionInfo.txt
  fi
else
  mv versionInfo.txt.new versionInfo.txt
fi

THISDIR=$PWD
cd $OPENADROOT
if [ -f bin/openadStatus ]
then 
  openadStatus -l >  $THISDIR/versionInfoOpenAD.txt.new
  if [ $? -ne 0 ] 
  then 
    echo "vers. unknown" > $THISDIR/versionInfoOpenAD.txt.new
  fi
else
  echo "vers. unknown" > $THISDIR/versionInfoOpenAD.txt.new
fi 
cd $THISDIR
if [ -f versionInfoOpenAD.txt ] 
then 
  diff versionInfoOpenAD.txt.new versionInfoOpenAD.txt > /dev/null
  if [ $? -eq 0 ]
  then 
    rm  versionInfoOpenAD.txt.new
  else
    mv versionInfoOpenAD.txt.new versionInfoOpenAD.txt
  fi
else
  mv versionInfoOpenAD.txt.new versionInfoOpenAD.txt
fi
