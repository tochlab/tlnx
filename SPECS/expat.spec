Name:           expat
Version:	2.4.8
Release:        1%{?dist}
Summary:	Stream-oriented XML parser library

License:	MIT
URL:		https://libexpat.github.io/
Source0:	https://github.com/libexpat/libexpat/releases/download/R_2_4_8/expat-2.4.8.tar.xz

#BuildRequires:
#Requires:

%description

%prep
%setup -q

%build
%configure --prefix=/usr    \
	    --libdir=/usr/lib \
            --disable-static \
            --docdir=/usr/share/doc/expat \
            --with-pkg-config-libdir=/usr/lib/pkgconfig
            
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
%make_install
rm -fr %{buildroot}/usr/lib/cmake
find %{buildroot} -type f -name '*.la' -delete || die

%files
/usr/bin/xmlwf
/usr/include/expat.h
/usr/include/expat_config.h
/usr/include/expat_external.h
/usr/lib/libexpat.so
/usr/lib/libexpat.so.1
/usr/lib/libexpat.so.1.8.8
/usr/lib/pkgconfig/expat.pc
/usr/share/doc/expat/AUTHORS
/usr/share/doc/expat/changelog


%changelog
