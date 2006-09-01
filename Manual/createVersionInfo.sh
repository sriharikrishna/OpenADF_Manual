#!/bin/sh
hg tip > /dev/null
if [ $? -ne 0 ] 
then 
  echo "hg: n/a by $USER" > versionInfo.txt.new
else
  echo -n "$(hg tip | grep changeset: | sed 's/changeset:[ ]*\(.*\):\(.*\)/hg:\1/'):$(hg id | sed 's/\([^ ].*\) \(.*\)/\1/')" > versionInfo.txt.new
  echo " by $(echo $USER | sed 's/_/\\_/')" >> versionInfo.txt.new  
fi
diff versionInfo.txt.new versionInfo.txt > /dev/null
if [ $? -ne 0 ]
then 
  mv versionInfo.txt.new versionInfo.txt
else 
  rm  versionInfo.txt.new
fi