dig  +time=5 www.autodiff.org > /dev/null
if [ $? -ne 0 ] 
then
  echo "cannot reach autodiff.org, using old file" 
  exit 0
fi
wget -O $1.gz http://www.autodiff.org/?module=Publications\&submenu=download%20all%20entries
gunzip -f $1.gz
dos2unix $1
