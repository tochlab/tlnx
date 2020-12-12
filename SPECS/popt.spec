Name:           popt
Version:	1.18
Release:        1%{?dist}
Summary:	Parse Options - Command line parser

License:	MIT
URL:		https://github.com/rpm-software-management/popt
Source0:	http://ftp.rpm.org/popt/releases/popt-1.x/popt-%{version}.tar.gz

#BuildRequires:
#Requires:

%description

%prep
%setup -q

%build
./autogen.sh
%configure
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
%make_install
%{__rm} -f %{buildroot}/usr/share/info/dir

#%post
#/sbin/ldconfig
#/sbin/install-info /usr/share/info/DevIL_manual.info.gz /usr/share/info/dir 2> /dev/null || :

#%postun
#/sbin/ldconfig
#/sbin/install-info --delete /usr/share/info/DevIL_manual.info.gz /usr/share/info/dir 2> /dev/null || :

%files
/usr/include/popt.h
/usr/lib64/libpopt.a
/usr/lib64/libpopt.la
/usr/lib64/libpopt.so
/usr/lib64/libpopt.so.0
/usr/lib64/libpopt.so.0.0.1
/usr/lib64/pkgconfig/popt.pc
/usr/share/locale/cs/LC_MESSAGES/popt.mo
/usr/share/locale/da/LC_MESSAGES/popt.mo
/usr/share/locale/de/LC_MESSAGES/popt.mo
/usr/share/locale/eo/LC_MESSAGES/popt.mo
/usr/share/locale/es/LC_MESSAGES/popt.mo
/usr/share/locale/fi/LC_MESSAGES/popt.mo
/usr/share/locale/fr/LC_MESSAGES/popt.mo
/usr/share/locale/ga/LC_MESSAGES/popt.mo
/usr/share/locale/gl/LC_MESSAGES/popt.mo
/usr/share/locale/hu/LC_MESSAGES/popt.mo
/usr/share/locale/id/LC_MESSAGES/popt.mo
/usr/share/locale/is/LC_MESSAGES/popt.mo
/usr/share/locale/it/LC_MESSAGES/popt.mo
/usr/share/locale/ja/LC_MESSAGES/popt.mo
/usr/share/locale/ko/LC_MESSAGES/popt.mo
/usr/share/locale/lv/LC_MESSAGES/popt.mo
/usr/share/locale/nb/LC_MESSAGES/popt.mo
/usr/share/locale/nl/LC_MESSAGES/popt.mo
/usr/share/locale/pl/LC_MESSAGES/popt.mo
/usr/share/locale/pt/LC_MESSAGES/popt.mo
/usr/share/locale/ro/LC_MESSAGES/popt.mo
/usr/share/locale/ru/LC_MESSAGES/popt.mo
/usr/share/locale/sk/LC_MESSAGES/popt.mo
/usr/share/locale/sl/LC_MESSAGES/popt.mo
/usr/share/locale/sv/LC_MESSAGES/popt.mo
/usr/share/locale/th/LC_MESSAGES/popt.mo
/usr/share/locale/tr/LC_MESSAGES/popt.mo
/usr/share/locale/uk/LC_MESSAGES/popt.mo
/usr/share/locale/vi/LC_MESSAGES/popt.mo
/usr/share/locale/wa/LC_MESSAGES/popt.mo
/usr/share/locale/zh_CN/LC_MESSAGES/popt.mo
/usr/share/locale/zh_TW/LC_MESSAGES/popt.mo
/usr/share/man/man3/popt.3.gz

%doc

%changelog
* Tue May 31 2016 Adam Miller <maxamillion@fedoraproject.org>
-

# see /usr/libexec/rpm/macros for macros
