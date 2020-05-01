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
./configure --prefix=/usr --libdir=/lib/ --64
make %{?_smp_mflags}
make check

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=%{buildroot}


%files
/*

%changelog
#