Name:          	gdbm
Version:	1.23
Release:        1%{?dist}
Summary:	Standard GNU database libraries

License:	GPL-3
URL:		https://www.gnu.org/software/gdbm/
Source0:	https://ftpmirror.gnu.org/gnu/gdbm/gdbm-%{version}.tar.gz

#BuildRequires:
#Requires:

%description

%prep
%setup -q

%build
%configure --prefix=/usr    \
	    --libdir=/usr/lib \
            --disable-static \
            --enable-libgdbm-compat
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
#make install DESTDIR=%{?buildroot}
%make_install
%{__rm} -f %{buildroot}/usr/share/info/dir
find %{buildroot} -type f -name '*.la' -delete || die


#%post
#/sbin/ldconfig
#/sbin/install-info /usr/share/info/gdbm.info.gz /usr/share/info/dir 2> /dev/null || :

%files
/usr/bin/gdbm_dump
/usr/bin/gdbm_load
/usr/bin/gdbmtool
/usr/include/dbm.h
/usr/include/gdbm.h
/usr/include/ndbm.h
/usr/lib/libgdbm.so
/usr/lib/libgdbm.so.6
/usr/lib/libgdbm.so.6.0.0
/usr/lib/libgdbm_compat.so
/usr/lib/libgdbm_compat.so.4
/usr/lib/libgdbm_compat.so.4.0.0
/usr/share/info/gdbm.info.gz
/usr/share/man/man1/gdbm_dump.1.gz
/usr/share/man/man1/gdbm_load.1.gz
/usr/share/man/man1/gdbmtool.1.gz
/usr/share/man/man3/gdbm.3.gz
/usr/share/locale/da/LC_MESSAGES/gdbm.mo
/usr/share/locale/de/LC_MESSAGES/gdbm.mo
/usr/share/locale/eo/LC_MESSAGES/gdbm.mo
/usr/share/locale/es/LC_MESSAGES/gdbm.mo
/usr/share/locale/fi/LC_MESSAGES/gdbm.mo
/usr/share/locale/fr/LC_MESSAGES/gdbm.mo
/usr/share/locale/ja/LC_MESSAGES/gdbm.mo
/usr/share/locale/pl/LC_MESSAGES/gdbm.mo
/usr/share/locale/pt_BR/LC_MESSAGES/gdbm.mo
/usr/share/locale/ru/LC_MESSAGES/gdbm.mo
/usr/share/locale/sr/LC_MESSAGES/gdbm.mo
/usr/share/locale/sv/LC_MESSAGES/gdbm.mo
/usr/share/locale/uk/LC_MESSAGES/gdbm.mo
/usr/share/locale/vi/LC_MESSAGES/gdbm.mo


%changelog
