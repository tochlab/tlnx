#!/bin/sh
INSTALL_DESTDIR=/home/tlnx/tmp/
mkdir $INSTALL_DESTDIR/dev
mkdir $INSTALL_DESTDIR/proc
mount --bind /dev/ $INSTALL_DESTDIR/dev
mount --bind /proc/ $INSTALL_DESTDIR/proc
for s in $(find ./RPMS/ -name \*.rpm)
do
	echo ===== INSTALL $s to $INSTALL_DESTDIR =====
	rpm --force --reinstall --nodeps --root=$INSTALL_DESTDIR $s
	if [ $? -ne 0 ]; then
		echo Problem with $s 
		break;
	fi
done
	echo root:x:0:0:root:/root:/bin/bash > $INSTALL_DESTDIR/etc/passwd
	echo root:x:0:root > $INSTALL_DESTDIR/etc/group
#	cp profile $INSTALL_DESTDIR/etc
