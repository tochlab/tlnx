Name:           zlib
Version:	1.2.12
Release:        1%{?dist}
Summary:	Zlib

License:	ZLIB
URL:		https://www.zlib.net/
Source0:	https://www.zlib.net/zlib-%{version}.tar.gz

%description
Zlib compress library

%prep
%setup -q

%build
./configure --prefix=/usr --sharedlibdir=/lib/ --64 --shared --with-pkg-config-libdir=/usr/lib/pkgconfig
make %{?_smp_mflags}
make check

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=%{buildroot}
rm -fv %{buildroot}/usr/lib/libz.a

%files
/lib/libz.so
/lib/libz.so.1
/lib/libz.so.1.2.12
/usr/include/zconf.h
/usr/include/zlib.h
/usr/lib/pkgconfig/zlib.pc
/usr/share/man/man3/zlib.3.gz

%changelog
#
