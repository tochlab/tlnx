Name:          	libtool
Version:	2.4.6
Release:        1%{?dist}
Summary:	A shared library tool for developers

License:	GPL-2
URL:		https://www.gnu.org/software/libtool/
Source0:	http://ftpmirror.gnu.org/gnu/libtool/libtool-%{version}.tar.gz

#BuildRequires:
#Requires:

%description

%prep
%setup -q

%build
%configure --prefix=/usr --libdir=/usr/lib
make %{?_smp_mflags}
#make check

%install
rm -rf $RPM_BUILD_ROOT
%make_install
rm -rf $RPM_BUILD_ROOT/usr/share/info/dir
find %{buildroot} -type f -name '*.la' -delete || die

%files
/usr/bin/libtool
/usr/bin/libtoolize
/usr/include/libltdl/lt_dlloader.h
/usr/include/libltdl/lt_error.h
/usr/include/libltdl/lt_system.h
/usr/include/ltdl.h
/usr/lib/libltdl.a
/usr/lib/libltdl.so
/usr/lib/libltdl.so.7
/usr/lib/libltdl.so.7.3.1
/usr/share/aclocal/libtool.m4
/usr/share/aclocal/ltargz.m4
/usr/share/aclocal/ltdl.m4
/usr/share/aclocal/ltoptions.m4
/usr/share/aclocal/ltsugar.m4
/usr/share/aclocal/ltversion.m4
/usr/share/aclocal/lt~obsolete.m4
/usr/share/info/libtool.info-1.gz
/usr/share/info/libtool.info-2.gz
/usr/share/info/libtool.info.gz
/usr/share/libtool/COPYING.LIB
/usr/share/libtool/Makefile.am
/usr/share/libtool/Makefile.in
/usr/share/libtool/README
/usr/share/libtool/aclocal.m4
/usr/share/libtool/build-aux/compile
/usr/share/libtool/build-aux/config.guess
/usr/share/libtool/build-aux/config.sub
/usr/share/libtool/build-aux/depcomp
/usr/share/libtool/build-aux/install-sh
/usr/share/libtool/build-aux/ltmain.sh
/usr/share/libtool/build-aux/missing
/usr/share/libtool/config-h.in
/usr/share/libtool/configure
/usr/share/libtool/configure.ac
/usr/share/libtool/libltdl/lt__alloc.h
/usr/share/libtool/libltdl/lt__argz_.h
/usr/share/libtool/libltdl/lt__dirent.h
/usr/share/libtool/libltdl/lt__glibc.h
/usr/share/libtool/libltdl/lt__private.h
/usr/share/libtool/libltdl/lt__strl.h
/usr/share/libtool/libltdl/lt_dlloader.h
/usr/share/libtool/libltdl/lt_error.h
/usr/share/libtool/libltdl/lt_system.h
/usr/share/libtool/libltdl/slist.h
/usr/share/libtool/loaders/dld_link.c
/usr/share/libtool/loaders/dlopen.c
/usr/share/libtool/loaders/dyld.c
/usr/share/libtool/loaders/load_add_on.c
/usr/share/libtool/loaders/loadlibrary.c
/usr/share/libtool/loaders/preopen.c
/usr/share/libtool/loaders/shl_load.c
/usr/share/libtool/lt__alloc.c
/usr/share/libtool/lt__argz.c
/usr/share/libtool/lt__dirent.c
/usr/share/libtool/lt__strl.c
/usr/share/libtool/lt_dlloader.c
/usr/share/libtool/lt_error.c
/usr/share/libtool/ltdl.c
/usr/share/libtool/ltdl.h
/usr/share/libtool/ltdl.mk
/usr/share/libtool/slist.c
/usr/share/man/man1/libtool.1.gz
/usr/share/man/man1/libtoolize.1.gz


%changelog
