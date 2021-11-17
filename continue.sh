#!/bin/sh
buildlist=$(cat buildlist.txt)

for s in $buildlist
do
        echo ===== BUILD $s =====
        rpmbuild --clean -bb $s
        if [ $? -ne 0 ]; then
                echo Problem with $s
                break;
        fi
done