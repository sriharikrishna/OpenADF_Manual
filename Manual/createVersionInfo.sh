#!/bin/sh
hg tip > /dev/null
if [ $? -ne 0 ] 
then 
  echo "vers. unknown" > versionInfo.txt.new
else
  echo -n "vers. hg:$(hg id -i):$(hg id  -n)" > versionInfo.txt.new
fi
diff versionInfo.txt.new versionInfo.txt > /dev/null
if [ $? -ne 0 ]
then 
  mv versionInfo.txt.new versionInfo.txt
else 
  rm  versionInfo.txt.new
fi

THISDIR=$PWD
cd $OPENADROOT
if [ -f bin/scmStatus ]
then 
  scmStatus -l >  $THISDIR/versionInfoOpenAD.txt.new
  if [ $? -ne 0 ] 
  then 
    echo "vers. unknown" > $THISDIR/versionInfoOpenAD.txt.new
  fi
else
  echo "vers. unknown" > $THISDIR/versionInfoOpenAD.txt.new
fi 
cd $THISDIR
diff versionInfoOpenAD.txt.new versionInfoOpenAD.txt > /dev/null
if [ $? -ne 0 ]
then 
  mv versionInfoOpenAD.txt.new versionInfoOpenAD.txt
else 
  rm  versionInfoOpenAD.txt.new
fi
