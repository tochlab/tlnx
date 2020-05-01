#!/bin/sh
for s in $(find ./RPMS/ -name \*.rpm)
do
	echo ===== INSTALL $s to $1 =====
	rpm -i --nodeps --nopost --root=/home/toch/tmp/ $s
	if [ $? -ne 0 ]; then
		echo Problem with $s 
		break;
	fi
done
