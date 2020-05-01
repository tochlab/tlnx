Name:           findutils
Version:	4.7.0
Release:        1%{?dist}
Summary:	GNU utilities for finding files

License:	GPL-3+
URL:		https://www.gnu.org/software/findutils/
Source0:	https://ftp.gnu.org/gnu/findutils/findutils-%{version}.tar.xz

#BuildRequires:
#Requires:

%description

%prep
%setup -q

%build
%configure --prefix=/usr/
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
%make_install
rm -rf $RPM_BUILD_ROOT/usr/share/info/dir

%files
/usr/bin/find
/usr/bin/locate
/usr/bin/updatedb
/usr/bin/xargs
/usr/libexec/frcode
/usr/share/info/find-maint.info.gz
/usr/share/info/find.info-1.gz
/usr/share/info/find.info-2.gz
/usr/share/info/find.info.gz
/usr/share/locale/be/LC_MESSAGES/findutils.mo
/usr/share/locale/bg/LC_MESSAGES/findutils.mo
/usr/share/locale/ca/LC_MESSAGES/findutils.mo
/usr/share/locale/cs/LC_MESSAGES/findutils.mo
/usr/share/locale/da/LC_MESSAGES/findutils.mo
/usr/share/locale/de/LC_MESSAGES/findutils.mo
/usr/share/locale/el/LC_MESSAGES/findutils.mo
/usr/share/locale/eo/LC_MESSAGES/findutils.mo
/usr/share/locale/es/LC_MESSAGES/findutils.mo
/usr/share/locale/et/LC_MESSAGES/findutils.mo
/usr/share/locale/fi/LC_MESSAGES/findutils.mo
/usr/share/locale/fr/LC_MESSAGES/findutils.mo
/usr/share/locale/ga/LC_MESSAGES/findutils.mo
/usr/share/locale/gl/LC_MESSAGES/findutils.mo
/usr/share/locale/hr/LC_MESSAGES/findutils.mo
/usr/share/locale/hu/LC_MESSAGES/findutils.mo
/usr/share/locale/id/LC_MESSAGES/findutils.mo
/usr/share/locale/it/LC_MESSAGES/findutils.mo
/usr/share/locale/ja/LC_MESSAGES/findutils.mo
/usr/share/locale/ko/LC_MESSAGES/findutils.mo
/usr/share/locale/lg/LC_MESSAGES/findutils.mo
/usr/share/locale/lt/LC_MESSAGES/findutils.mo
/usr/share/locale/ms/LC_MESSAGES/findutils.mo
/usr/share/locale/nb/LC_MESSAGES/findutils.mo
/usr/share/locale/nl/LC_MESSAGES/findutils.mo
/usr/share/locale/pl/LC_MESSAGES/findutils.mo
/usr/share/locale/pt/LC_MESSAGES/findutils.mo
/usr/share/locale/pt_BR/LC_MESSAGES/findutils.mo
/usr/share/locale/ro/LC_MESSAGES/findutils.mo
/usr/share/locale/ru/LC_MESSAGES/findutils.mo
/usr/share/locale/sk/LC_MESSAGES/findutils.mo
/usr/share/locale/sl/LC_MESSAGES/findutils.mo
/usr/share/locale/sr/LC_MESSAGES/findutils.mo
/usr/share/locale/sv/LC_MESSAGES/findutils.mo
/usr/share/locale/tr/LC_MESSAGES/findutils.mo
/usr/share/locale/uk/LC_MESSAGES/findutils.mo
/usr/share/locale/vi/LC_MESSAGES/findutils.mo
/usr/share/locale/zh_CN/LC_MESSAGES/findutils.mo
/usr/share/locale/zh_TW/LC_MESSAGES/findutils.mo
/usr/share/man/man1/find.1.gz
/usr/share/man/man1/locate.1.gz
/usr/share/man/man1/updatedb.1.gz
/usr/share/man/man1/xargs.1.gz
/usr/share/man/man5/locatedb.5.gz


%changelog
* Tue May 31 2016 Adam Miller <maxamillion@fedoraproject.org>
-

# see /usr/libexec/rpm/macros for macros
