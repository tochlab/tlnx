#!/bin/sh
find ./SPECS/ -name \*.spec -exec spectool -g -R {} \;
