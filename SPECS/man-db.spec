Name:           man-db
Version:	2.9.4
Release:        1%{?dist}
Summary:	a man replacement that utilizes berkdb instead of flat files

License:	GPL-3
URL:		http://www.nongnu.org/man-db/
Source0:	http://download.savannah.nongnu.org/releases/man-db/man-db-%{version}.tar.xz

#BuildRequires:
#Requires:

%description

%prep
%setup -q

%build
%configure --prefix=/usr                        \
	    --libdir=/usr/lib \
            --docdir=/usr/share/doc/man-db \
            --sysconfdir=/etc                    \
            --disable-setuid                     \
            --enable-cache-owner=bin             \
            --with-browser=/usr/bin/lynx         \
            --with-vgrind=/usr/bin/vgrind        \
            --with-grap=/usr/bin/grap            \
            --with-systemdtmpfilesdir=           \
            --with-systemdsystemunitdir=	\
	    --disable-nls 
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
%make_install
find %{buildroot} -type f -name '*.la' -delete || die

%files
/etc/man_db.conf
/usr/bin/apropos
/usr/bin/catman
/usr/bin/lexgrog
/usr/bin/man
/usr/bin/man-recode
/usr/bin/mandb
/usr/bin/manpath
/usr/bin/whatis
/usr/lib/man-db/libman-%{version}.so
/usr/lib/man-db/libman.so
/usr/lib/man-db/libmandb-%{version}.so
/usr/lib/man-db/libmandb.so
/usr/libexec/man-db/globbing
/usr/libexec/man-db/manconv
/usr/libexec/man-db/zsoelim
/usr/sbin/accessdb
/usr/share/doc/man-db/man-db-manual.ps
/usr/share/doc/man-db/man-db-manual.txt
/usr/share/man/man1/apropos.1.gz
/usr/share/man/man1/lexgrog.1.gz
/usr/share/man/man1/man-recode.1.gz
/usr/share/man/man1/man.1.gz
/usr/share/man/man1/manconv.1.gz
/usr/share/man/man1/manpath.1.gz
/usr/share/man/man1/whatis.1.gz
/usr/share/man/man1/zsoelim.1.gz
/usr/share/man/man5/manpath.5.gz
/usr/share/man/man8/accessdb.8.gz
/usr/share/man/man8/catman.8.gz
/usr/share/man/man8/mandb.8.gz


%changelog
