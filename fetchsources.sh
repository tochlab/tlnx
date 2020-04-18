#!/bin/sh
find ./rpmbuild/SPECS/ -name \*.spec -exec spectool -g -R {} \;
