#!/bin/sh
set -e
buildlist=$(find ./SPECS/ -name \*.spec)
rm -f buildlist.txt
for s in $buildlist
do
echo $s >> buildlist.txt
done

for s in $buildlist
do
	echo ===== BUILD $s =====
	rpmbuild --clean -bb $s 
	if [ $? -ne 0 ]; then
		echo Problem with $s 
		break;
	fi
done
