#!/bin/sh
mkdir ./SOURCES
find ./SPECS/ -name \*.spec -exec spectool -g -R {} \;
