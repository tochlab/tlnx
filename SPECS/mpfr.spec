Name:           mpfr
Version:        4.1.0
Release:        1%{?dist}
Summary:        mpfr lib

#Group:          
License:        GPL
URL:            https://www.mpfr.org/
Source0:        https://ftpmirror.gnu.org/mpfr/mpfr-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

#BuildRequires:  
#Requires:       

%description
MPFR Library

%prep
%setup -q


%build
%configure --prefix=/usr        \
	    --libdir=/usr/lib   \
            --disable-static     \
            --enable-thread-safe \
            --docdir=/usr/share/doc/mpfr \
            --with-pkg-config-libdir=/usr/lib/pkgconfig
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
rm -fr %{buildroot}/usr/share/info/dir

%clean
rm -rf $RPM_BUILD_ROOT


%files
/usr/include/mpf2mpfr.h
/usr/include/mpfr.h
/usr/lib/libmpfr.so
/usr/lib/libmpfr.so.6
/usr/lib/libmpfr.so.6.1.0
/usr/lib/pkgconfig/mpfr.pc
/usr/share/doc/mpfr/AUTHORS
/usr/share/doc/mpfr/BUGS
/usr/share/doc/mpfr/COPYING
/usr/share/doc/mpfr/COPYING.LESSER
/usr/share/doc/mpfr/FAQ.html
/usr/share/doc/mpfr/NEWS
/usr/share/doc/mpfr/TODO
/usr/share/doc/mpfr/examples/ReadMe
/usr/share/doc/mpfr/examples/can_round.c
/usr/share/doc/mpfr/examples/divworst.c
/usr/share/doc/mpfr/examples/rndo-add.c
/usr/share/doc/mpfr/examples/sample.c
/usr/share/doc/mpfr/examples/version.c
/usr/share/doc/mpfr/examples/threads.c
/usr/share/info/mpfr.info.gz

%changelog
