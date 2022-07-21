#!/bin/sh
set -e
buildlist=$(find ./SPECS/ -name \*.spec)
mkdir -p ./SOURCES
for spec in $buildlist; do
rpmspec -P $spec | grep Source.: | cut -f 2 >> sourcelist.txt
rpmspec -P $spec | grep Patch.: | cut -f 2 >> sourcelist.txt
done

sourcelist=$(cat sourcelist.txt)
for src in $sourcelist; do
    dstfile=$(basename $src)
    if [ -f ./SOURCES/$dstfile ]; then
	echo "File $dstfile exists"
    else
    wget $src --directory-prefix=./SOURCES/
    fi
done
