FROM gentoo/stage3:20231106
RUN emerge-webrsync --revert=20231107
RUN eselect profile set default/linux/amd64/17.1/no-multilib
RUN emerge gentoolkit
RUN euse -D X ipv6
RUN echo "GENTOO_MIRRORS=\"http://172.17.0.1/\"" >> /etc/portage/make.conf
RUN emerge -uDN @world
RUN emerge --depclean
RUN emerge dev-vcs/git rpm vim tmux
RUN cd ~; git clone https://github.com/tochlab/tlnx.git ~/rpmbuild
RUN cd ~/rpmbuild/; ./fetchsources.sh
#RUN cp ~/rpmbuild/SOURCES/rpmrc ~/.rpmrc
#RUN cp ~/rpmbuild/SOURCES/rpmmacros ~/.rpmmacros
#RUN cd ~/rpmbuild; ./build-stage1.sh
#RUN ls -lRa ~/rpmbuild/RPMS/
