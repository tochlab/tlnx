Name:           libpsl
Version:	0.21.1
Release:        1%{?dist}
Summary:	C library for the Public Suffix List

License:	MIT
URL:		https://github.com/rockdaboot/libpsl
Source0:	https://github.com/rockdaboot/libpsl/releases/download/%{version}/libpsl-%{version}.tar.gz

#BuildRequires:
#Requires:

%description

%prep
%setup -q

%build
%configure --libdir=/usr/lib --with-pkg-config-libdir=/usr/lib/pkgconfig
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
%make_install
%{__rm} -f %{buildroot}/usr/share/info/dir
find %{buildroot} -type f -name '*.la' -delete || die

#%post
#/sbin/ldconfig
#/sbin/install-info /usr/share/info/DevIL_manual.info.gz /usr/share/info/dir 2> /dev/null || :

#%postun
#/sbin/ldconfig
#/sbin/install-info --delete /usr/share/info/DevIL_manual.info.gz /usr/share/info/dir 2> /dev/null || :

%files
/usr/bin/psl
/usr/include/libpsl.h
/usr/lib/libpsl.a
/usr/lib/libpsl.so
/usr/lib/libpsl.so.5
/usr/lib/libpsl.so.5.3.3
/usr/lib/pkgconfig/libpsl.pc
/usr/share/man/man1/psl-make-dafsa.1.gz
/usr/share/man/man1/psl.1.gz

%changelog
