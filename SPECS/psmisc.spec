Name:         	psmisc 
Version:	23.4
Release:        1%{?dist}
Summary:	A set of tools that use the proc filesystem

License:	GPL-2
URL:		http://psmisc.sourceforge.net/
Source0:	https://mirror.yandex.ru/gentoo-distfiles/distfiles/psmisc-%{version}.tar.xz

#BuildRequires:
#Requires: ncurses

%description

%prep
%setup -q

%build
LDFLAGS="-Wl,--build-id" ./configure --prefix=/usr --disable-nls
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
%make_install

%files
/usr/bin/fuser
/usr/bin/killall
/usr/bin/peekfd
/usr/bin/prtstat
/usr/bin/pslog
/usr/bin/pstree
/usr/bin/pstree.x11
/usr/share/man/man1/fuser.1.gz
/usr/share/man/man1/killall.1.gz
/usr/share/man/man1/peekfd.1.gz
/usr/share/man/man1/prtstat.1.gz
/usr/share/man/man1/pslog.1.gz
/usr/share/man/man1/pstree.1.gz
/usr/share/man/de/man1/fuser.1.gz
/usr/share/man/de/man1/killall.1.gz
/usr/share/man/de/man1/peekfd.1.gz
/usr/share/man/de/man1/prtstat.1.gz
/usr/share/man/de/man1/pslog.1.gz
/usr/share/man/de/man1/pstree.1.gz
/usr/share/man/fr/man1/fuser.1.gz
/usr/share/man/fr/man1/killall.1.gz
/usr/share/man/fr/man1/peekfd.1.gz
/usr/share/man/fr/man1/prtstat.1.gz
/usr/share/man/fr/man1/pslog.1.gz
/usr/share/man/fr/man1/pstree.1.gz
/usr/share/man/pt_BR/man1/fuser.1.gz
/usr/share/man/pt_BR/man1/killall.1.gz
/usr/share/man/pt_BR/man1/peekfd.1.gz
/usr/share/man/pt_BR/man1/prtstat.1.gz
/usr/share/man/pt_BR/man1/pslog.1.gz
/usr/share/man/pt_BR/man1/pstree.1.gz
/usr/share/man/ru/man1/fuser.1.gz
/usr/share/man/ru/man1/killall.1.gz
/usr/share/man/ru/man1/peekfd.1.gz
/usr/share/man/ru/man1/prtstat.1.gz
/usr/share/man/ru/man1/pslog.1.gz
/usr/share/man/ru/man1/pstree.1.gz
/usr/share/man/uk/man1/fuser.1.gz
/usr/share/man/uk/man1/killall.1.gz
/usr/share/man/uk/man1/peekfd.1.gz
/usr/share/man/uk/man1/prtstat.1.gz
/usr/share/man/uk/man1/pslog.1.gz
/usr/share/man/uk/man1/pstree.1.gz

%changelog
* Tue May 31 2016 Adam Miller <maxamillion@fedoraproject.org>
-
