Name:           attr 
Version:	2.5.1
Release:        1%{?dist}
Summary:	Extended attributes tools

License:	GPL
URL:		https://savannah.nongnu.org/projects/attr
Source0:	https://download-mirror.savannah.gnu.org/releases/attr/attr-%{version}.tar.gz

#BuildRequires:
#Requires:

%description

%prep
%setup -q

%build
%configure --prefix=/usr     \
	    --libdir=/usr/lib \
            --bindir=/bin     \
            --disable-static  \
            --sysconfdir=/etc \
            --docdir=/usr/share/doc/attr \
            --with-pkg-config-libdir=/usr/lib/pkgconfig \
	    --disable-nls
make %{?_smp_mflags}
#make check

%install
rm -rf $RPM_BUILD_ROOT
%make_install
find %{buildroot} -type f -name '*.la' -delete || die

%files
/bin/attr
/bin/getfattr
/bin/setfattr
/etc/xattr.conf
/usr/include/attr/attributes.h
/usr/include/attr/error_context.h
/usr/include/attr/libattr.h
/usr/lib/libattr.so
/usr/lib/libattr.so.1
/usr/lib/libattr.so.1.1.2501
/usr/lib/pkgconfig/libattr.pc
/usr/share/doc/attr/CHANGES
/usr/share/doc/attr/COPYING
/usr/share/doc/attr/COPYING.LGPL
/usr/share/doc/attr/PORTING
/usr/share/man/man1/attr.1.gz
/usr/share/man/man1/getfattr.1.gz
/usr/share/man/man1/setfattr.1.gz
/usr/share/man/man3/attr_get.3.gz
/usr/share/man/man3/attr_getf.3.gz
/usr/share/man/man3/attr_list.3.gz
/usr/share/man/man3/attr_listf.3.gz
/usr/share/man/man3/attr_multi.3.gz
/usr/share/man/man3/attr_multif.3.gz
/usr/share/man/man3/attr_remove.3.gz
/usr/share/man/man3/attr_removef.3.gz
/usr/share/man/man3/attr_set.3.gz
/usr/share/man/man3/attr_setf.3.gz


%changelog
