FROM centos:8 

RUN dnf -y install rpmdevtools \
	gcc gcc-c++ \
	m4 \
	make \
	zlib-devel \
	expat-devel \
	python38 \
	perl-ExtUtils-MakeMaker \
	glibc-langpack-en \
	ncurses-devel \
	libuuid-devel \
	libblkid-devel \
	gettext-devel \
	bison 


# Set the locale
#RUN sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen && \
#    locale-gen
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  

ENTRYPOINT [ "bash" ]
