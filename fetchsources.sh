#!/bin/sh
python genurls.py > urllist.txt
mkdir ./SOURCES
cd ./SOURCES
wget -c -i ../urllist.txt
