Name:           mpfr
Version:        4.0.2
Release:        1%{?dist}
Summary:        mpfr lib

#Group:          
License:        GPL
URL:            https://www.mpfr.org/
Source0:        https://mirror.tochlab.net/pub/gnu/mpfr/mpfr-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

#BuildRequires:  
#Requires:       

%description
MPFR Library

%prep
%setup -q


%build
%configure --prefix=/usr        \
            --disable-static     \
            --enable-thread-safe \
            --docdir=/usr/share/doc/mpfr-%{version}
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
%{__rm}  %{buildroot}/usr/share/info/dir

%clean
rm -rf $RPM_BUILD_ROOT


%files
/usr/include/mpf2mpfr.h
/usr/include/mpfr.h
/usr/lib/libmpfr.la
/usr/lib/libmpfr.so
/usr/lib/libmpfr.so.6
/usr/lib/libmpfr.so.6.0.2
/usr/lib/pkgconfig/mpfr.pc
/usr/share/doc/mpfr-4.0.2/AUTHORS
/usr/share/doc/mpfr-4.0.2/BUGS
/usr/share/doc/mpfr-4.0.2/COPYING
/usr/share/doc/mpfr-4.0.2/COPYING.LESSER
/usr/share/doc/mpfr-4.0.2/FAQ.html
/usr/share/doc/mpfr-4.0.2/NEWS
/usr/share/doc/mpfr-4.0.2/TODO
/usr/share/doc/mpfr-4.0.2/examples/ReadMe
/usr/share/doc/mpfr-4.0.2/examples/can_round.c
/usr/share/doc/mpfr-4.0.2/examples/divworst.c
/usr/share/doc/mpfr-4.0.2/examples/rndo-add.c
/usr/share/doc/mpfr-4.0.2/examples/sample.c
/usr/share/doc/mpfr-4.0.2/examples/version.c
/usr/share/info/mpfr.info.gz

%changelog
