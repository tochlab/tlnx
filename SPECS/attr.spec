Name:           attr 
Version:	2.4.48
Release:        1%{?dist}
Summary:	Extended attributes tools

License:	GPL
URL:		https://savannah.nongnu.org/projects/attr
Source0:	https://download-mirror.savannah.gnu.org/releases/attr/attr-2.4.48.tar.gz

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
            --docdir=/usr/share/doc/attr-%{version}
make %{?_smp_mflags}
#make check

%install
rm -rf $RPM_BUILD_ROOT
%make_install

%files
/bin/attr
/bin/getfattr
/bin/setfattr
/etc/xattr.conf
/usr/include/attr/attributes.h
/usr/include/attr/error_context.h
/usr/include/attr/libattr.h
#/usr/lib/libattr.la
/usr/lib/libattr.so
/usr/lib/libattr.so.1
/usr/lib/libattr.so.1.1.2448
/usr/lib/pkgconfig/libattr.pc
/usr/share/doc/attr-2.4.48/CHANGES
/usr/share/doc/attr-2.4.48/COPYING
/usr/share/doc/attr-2.4.48/COPYING.LGPL
/usr/share/doc/attr-2.4.48/PORTING
/usr/share/locale/cs/LC_MESSAGES/attr.mo
/usr/share/locale/de/LC_MESSAGES/attr.mo
/usr/share/locale/en@boldquot/LC_MESSAGES/attr.mo
/usr/share/locale/en@quot/LC_MESSAGES/attr.mo
/usr/share/locale/es/LC_MESSAGES/attr.mo
/usr/share/locale/fr/LC_MESSAGES/attr.mo
/usr/share/locale/gl/LC_MESSAGES/attr.mo
/usr/share/locale/nl/LC_MESSAGES/attr.mo
/usr/share/locale/pl/LC_MESSAGES/attr.mo
/usr/share/locale/sv/LC_MESSAGES/attr.mo
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
* Tue May 31 2016 Adam Miller <maxamillion@fedoraproject.org>
-
