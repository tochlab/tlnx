#!/bin/sh
set -e
buildlist=$(cat stage1.txt)

for s in $buildlist
do
	echo ===== BUILD $s =====
	rpmbuild --clean -bb SPECS/$s 
	if [ $? -ne 0 ]; then
		echo Problem with $s 
		break;
	fi
done
