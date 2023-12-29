Name:          	pkgconf
Version:	1.8.1
Release:        1%{?dist}
Summary:	pkg-config compatible replacement with no dependencies other than ANSI C89

License:	ISC
URL:		https://git.sr.ht/~kaniini/pkgconf
Source0:	https://distfiles.dereferenced.org/pkgconf/pkgconf-%{version}.tar.gz

#BuildRequires:
#Requires:

%description

%prep
%setup -q

%build
%configure --prefix=/usr --libdir=/usr/lib
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
%make_install
find %{buildroot} -type f -name '*.la' -delete || die


%post
ln -sf /usr/bin/pkgconf /usr/bin/pkg-config

%files
/usr/bin/pkgconf
/usr/include/pkgconf/libpkgconf/bsdstubs.h
/usr/include/pkgconf/libpkgconf/iter.h
/usr/include/pkgconf/libpkgconf/libpkgconf-api.h
/usr/include/pkgconf/libpkgconf/libpkgconf.h
/usr/include/pkgconf/libpkgconf/stdinc.h
/usr/lib/libpkgconf.a
/usr/lib/libpkgconf.so
/usr/lib/libpkgconf.so.3
/usr/lib/libpkgconf.so.3.0.0
/usr/lib/pkgconfig/libpkgconf.pc
/usr/share/aclocal/pkg.m4
/usr/share/doc/pkgconf/AUTHORS
/usr/share/doc/pkgconf/README.md
/usr/share/man/man1/pkgconf.1.gz
/usr/share/man/man5/pc.5.gz
/usr/share/man/man5/pkgconf-personality.5.gz
/usr/share/man/man7/pkg.m4.7.gz


%changelog
* Tue May 31 2016 Adam Miller <maxamillion@fedoraproject.org>
-
