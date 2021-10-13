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
./configure --prefix=/usr
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
/usr/share/locale/bg/LC_MESSAGES/psmisc.mo
/usr/share/locale/ca/LC_MESSAGES/psmisc.mo
/usr/share/locale/cs/LC_MESSAGES/psmisc.mo
/usr/share/locale/da/LC_MESSAGES/psmisc.mo
/usr/share/locale/de/LC_MESSAGES/psmisc.mo
/usr/share/locale/el/LC_MESSAGES/psmisc.mo
/usr/share/locale/eo/LC_MESSAGES/psmisc.mo
/usr/share/locale/eu/LC_MESSAGES/psmisc.mo
/usr/share/locale/fi/LC_MESSAGES/psmisc.mo
/usr/share/locale/fr/LC_MESSAGES/psmisc.mo
/usr/share/locale/hr/LC_MESSAGES/psmisc.mo
/usr/share/locale/hu/LC_MESSAGES/psmisc.mo
/usr/share/locale/id/LC_MESSAGES/psmisc.mo
/usr/share/locale/it/LC_MESSAGES/psmisc.mo
/usr/share/locale/ja/LC_MESSAGES/psmisc.mo
/usr/share/locale/nb/LC_MESSAGES/psmisc.mo
/usr/share/locale/nl/LC_MESSAGES/psmisc.mo
/usr/share/locale/pl/LC_MESSAGES/psmisc.mo
/usr/share/locale/pt/LC_MESSAGES/psmisc.mo
/usr/share/locale/pt_BR/LC_MESSAGES/psmisc.mo
/usr/share/locale/ro/LC_MESSAGES/psmisc.mo
/usr/share/locale/ru/LC_MESSAGES/psmisc.mo
/usr/share/locale/sr/LC_MESSAGES/psmisc.mo
/usr/share/locale/sv/LC_MESSAGES/psmisc.mo
/usr/share/locale/uk/LC_MESSAGES/psmisc.mo
/usr/share/locale/vi/LC_MESSAGES/psmisc.mo
/usr/share/locale/zh_CN/LC_MESSAGES/psmisc.mo
/usr/share/locale/zh_TW/LC_MESSAGES/psmisc.mo
/usr/share/man/man1/fuser.1.gz
/usr/share/man/man1/killall.1.gz
/usr/share/man/man1/peekfd.1.gz
/usr/share/man/man1/prtstat.1.gz
/usr/share/man/man1/pslog.1.gz
/usr/share/man/man1/pstree.1.gz


%changelog
* Tue May 31 2016 Adam Miller <maxamillion@fedoraproject.org>
-
