Name:           libnsl
Version:	2.0.0
Release:        1%{?dist}
Summary:	Public client interface for NIS(YP) in a IPv6 ready version

License:	LGPL-2.1+
URL:		https://github.com/thkukuk/libnsl
Source0:	https://github.com/thkukuk/libnsl/releases/download/v%{version}/libnsl-%{version}.tar.xz

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
/usr/include/rpcsvc/yp.h
/usr/include/rpcsvc/yp.x
/usr/include/rpcsvc/yp_prot.h
/usr/include/rpcsvc/ypclnt.h
/usr/include/rpcsvc/yppasswd.h
/usr/include/rpcsvc/yppasswd.x
/usr/include/rpcsvc/ypupd.h
/usr/lib/libnsl.a
/usr/lib/libnsl.so
/usr/lib/libnsl.so.3
/usr/lib/libnsl.so.3.0.0
/usr/lib/pkgconfig/libnsl.pc


%doc

%changelog
