STAGE_ARCHIVE_NAME=tlnx0-stage1.tar.gz
tar -C tmp -c -f $STAGE_ARCHIVE_NAME .

#docker import $STAGE_ARCHIVE_NAME tlnx0/stage1

