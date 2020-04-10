Name:           make
Version:	4.3
Release:        1%{?dist}
Summary:	Standard tool to compile source trees

License:	GPL-3+
URL:		https://www.gnu.org/software/make/make.html
Source0:	https://ftp.gnu.org/gnu/make/make-%{version}.tar.gz

#BuildRequires:
#Requires:

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
/usr/bin/make
/usr/include/gnumake.h
/usr/share/info/make.info-1.gz
/usr/share/info/make.info-2.gz
/usr/share/info/make.info.gz
/usr/share/locale/be/LC_MESSAGES/make.mo
/usr/share/locale/bg/LC_MESSAGES/make.mo
/usr/share/locale/cs/LC_MESSAGES/make.mo
/usr/share/locale/da/LC_MESSAGES/make.mo
/usr/share/locale/de/LC_MESSAGES/make.mo
/usr/share/locale/es/LC_MESSAGES/make.mo
/usr/share/locale/fi/LC_MESSAGES/make.mo
/usr/share/locale/fr/LC_MESSAGES/make.mo
/usr/share/locale/ga/LC_MESSAGES/make.mo
/usr/share/locale/gl/LC_MESSAGES/make.mo
/usr/share/locale/he/LC_MESSAGES/make.mo
/usr/share/locale/hr/LC_MESSAGES/make.mo
/usr/share/locale/id/LC_MESSAGES/make.mo
/usr/share/locale/it/LC_MESSAGES/make.mo
/usr/share/locale/ja/LC_MESSAGES/make.mo
/usr/share/locale/ko/LC_MESSAGES/make.mo
/usr/share/locale/lt/LC_MESSAGES/make.mo
/usr/share/locale/nl/LC_MESSAGES/make.mo
/usr/share/locale/pl/LC_MESSAGES/make.mo
/usr/share/locale/pt/LC_MESSAGES/make.mo
/usr/share/locale/pt_BR/LC_MESSAGES/make.mo
/usr/share/locale/ru/LC_MESSAGES/make.mo
/usr/share/locale/sr/LC_MESSAGES/make.mo
/usr/share/locale/sv/LC_MESSAGES/make.mo
/usr/share/locale/tr/LC_MESSAGES/make.mo
/usr/share/locale/uk/LC_MESSAGES/make.mo
/usr/share/locale/vi/LC_MESSAGES/make.mo
/usr/share/locale/zh_CN/LC_MESSAGES/make.mo
/usr/share/locale/zh_TW/LC_MESSAGES/make.mo
/usr/share/man/man1/make.1.gz


%changelog
* Tue May 31 2016 Adam Miller <maxamillion@fedoraproject.org>
-

# see /usr/libexec/rpm/macros for macros
