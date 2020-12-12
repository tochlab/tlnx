Name:           zlib
Version:	1.2.11
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
./configure --prefix=/usr --sharedlibdir=/lib/ --64
make %{?_smp_mflags}
make check

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=%{buildroot}


%files
/lib/libz.so
/lib/libz.so.1
/lib/libz.so.1.2.11
/usr/include/zconf.h
/usr/include/zlib.h
/usr/lib/libz.a
/usr/lib/pkgconfig/zlib.pc
/usr/share/man/man3/zlib.3.gz

%changelog
#
