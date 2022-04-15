#!/bin/sh
set -e
python genurls.py > urllist.txt
mkdir -p ./SOURCES
cd ./SOURCES
wget -c -i ../urllist.txt
