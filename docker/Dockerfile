FROM gentoo/stage3:20231113
RUN emerge-webrsync --revert=20231228
RUN emerge gentoolkit
RUN euse -D X ipv6
RUN echo "GENTOO_MIRRORS=\"http://172.17.0.1/\"" >> /etc/portage/make.conf
RUN emerge -uDN @world
RUN emerge --depclean
RUN emerge dev-vcs/git rpm vim
