#!/bin/sh
WD=`pwd`

if [ `basename $WD` != "rpmbuild" ]; then
	echo "run me from rpmbuild!!!"
	exit
fi

docker run -it --privileged -v `pwd`:/root/rpmbuild --tmpfs /root/rpmbuild/BUILD:exec --tmpfs /root/rpmbuild/BUILDROOT:exec tlnx-stage0
