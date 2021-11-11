Name:           libnsl
Version:	1.3.0
Release:        1%{?dist}
Summary:	Library contains the public client interface for NIS(YP) and NIS+ in a IPv6 ready version 

License:	LGPL-2.1
URL:		https://github.com/thkukuk/libnsl
Source0:	https://github.com/thkukuk/libnsl/releases/download/v%{version}/libnsl-%{version}.tar.xz

#BuildRequires:
#Requires:

%description
Public client interface for NIS(YP) and NIS+ in a IPv6 ready version

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
%make_install
%{__rm} -f %{buildroot}/usr/share/info/dir

#%post
#/sbin/ldconfig
#/sbin/install-info /usr/share/info/DevIL_manual.info.gz /usr/share/info/dir 2> /dev/null || :

#%postun
#/sbin/ldconfig
#/sbin/install-info --delete /usr/share/info/DevIL_manual.info.gz /usr/share/info/dir 2> /dev/null || :

%files
/usr/include/rpcsvc/nis.h
/usr/include/rpcsvc/nis.x
/usr/include/rpcsvc/nis_callback.h
/usr/include/rpcsvc/nis_callback.x
/usr/include/rpcsvc/nis_object.x
/usr/include/rpcsvc/nis_tags.h
/usr/include/rpcsvc/nislib.h
/usr/include/rpcsvc/yp.h
/usr/include/rpcsvc/yp.x
/usr/include/rpcsvc/yp_prot.h
/usr/include/rpcsvc/ypclnt.h
/usr/include/rpcsvc/yppasswd.h
/usr/include/rpcsvc/yppasswd.x
/usr/include/rpcsvc/ypupd.h
/usr/lib64/libnsl.a
/usr/lib64/libnsl.la
/usr/lib64/libnsl.so
/usr/lib64/libnsl.so.2
/usr/lib64/libnsl.so.2.0.1
/usr/lib64/pkgconfig/libnsl.pc

%doc

%changelog
* Tue May 31 2016 Adam Miller <maxamillion@fedoraproject.org>
-

# see /usr/libexec/rpm/macros for macros
