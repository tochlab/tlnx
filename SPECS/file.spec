Name:           file
Version:	5.45
Release:        1%{?dist}
Summary:	File utility

License:	MIT
URL:		https://astron.com/
Source0:	https://astron.com/pub/file/file-%{version}.tar.gz

%description
File utility

%prep
%setup -q

%build
%configure --prefix=/usr --libdir=/usr/lib
make %{?_smp_mflags}
make check

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
find %{buildroot} -type f -name '*.la' -delete || die

%files
/usr/bin/file
/usr/include/magic.h
/usr/lib/libmagic.so
/usr/lib/libmagic.so.1
/usr/lib/libmagic.so.1.0.0
/usr/lib/pkgconfig/libmagic.pc
/usr/share/man/man1/file.1.gz
/usr/share/man/man3/libmagic.3.gz
/usr/share/man/man4/magic.4.gz
/usr/share/misc/magic.mgc

%changelog
