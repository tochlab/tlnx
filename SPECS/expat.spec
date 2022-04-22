Name:           expat
Version:	2.2.9
Release:        1%{?dist}
Summary:	Stream-oriented XML parser library

License:	MIT
URL:		https://libexpat.github.io/
Source0:	https://github.com/libexpat/libexpat/releases/download/R_2_2_9/expat-%{version}.tar.xz

#BuildRequires:
#Requires:

%description

%prep
%setup -q

%build
%configure --prefix=/usr    \
	    --libdir=/usr/lib \
            --disable-static \
            --docdir=/usr/share/doc/expat-%{version} \
            --with-pkg-config-libdir=/usr/lib/pkgconfig
            
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
%make_install

%files
/usr/bin/xmlwf
/usr/include/expat.h
/usr/include/expat_config.h
/usr/include/expat_external.h
#/usr/lib/libexpat.la
/usr/lib/libexpat.so
/usr/lib/libexpat.so.1
/usr/lib/libexpat.so.1.6.11
/usr/lib/pkgconfig/expat.pc
/usr/share/doc/expat-2.2.9/AUTHORS
/usr/share/doc/expat-2.2.9/changelog


%changelog
* Tue May 31 2016 Adam Miller <maxamillion@fedoraproject.org>
-

# see /usr/libexec/rpm/macros for macros
