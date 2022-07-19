Name:           sqlite
Version:	3.38.2
Release:        1%{?dist}
Summary:	SQL database engine

License:	public domain
URL:		https://sqlite.org/
Source0:	https://www.sqlite.org/2022/sqlite-autoconf-3380200.tar.gz

#BuildRequires:
#Requires:

%description
SQL database engine

%prep
umask 022
cd %{_builddir}
rm -rf sqlite-autoconf-3380200
tar xvf %{_sourcedir}/sqlite-autoconf-3380200.tar.gz

%build
cd sqlite-autoconf-3380200
%configure --prefix=/usr --libdir=/usr/lib --with-pkg-config-libdir=/usr/lib/pkgconfig
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
cd %{_builddir}/sqlite-autoconf-3380200
%make_install
find %{buildroot} -type f -name '*.la' -delete || die


#%post
#/sbin/ldconfig
#/sbin/install-info /usr/share/info/DevIL_manual.info.gz /usr/share/info/dir 2> /dev/null || :

#%postun
#/sbin/ldconfig
#/sbin/install-info --delete /usr/share/info/DevIL_manual.info.gz /usr/share/info/dir 2> /dev/null || :

%files
/usr/bin/sqlite3
/usr/include/sqlite3.h
/usr/include/sqlite3ext.h
/usr/lib/libsqlite3.a
/usr/lib/libsqlite3.so
/usr/lib/libsqlite3.so.0
/usr/lib/libsqlite3.so.0.8.6
/usr/lib/pkgconfig/sqlite3.pc
/usr/share/man/man1/sqlite3.1.gz


%changelog
