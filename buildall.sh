#!/bin/sh
for s in $(find ./rpmbuild/SPECS/ -name \*.spec)
do
	rpmbuild --clean -bb $s 
	if [ $? -ne 0 ]; then
		echo Problem with $s 
		break;
	fi
done
