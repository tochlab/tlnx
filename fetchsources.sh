#!/bin/sh
find . -name \*.spec -exec spectool -g -R {} \;
