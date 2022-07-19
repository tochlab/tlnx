Name:           flex 
Version:	2.6.4
Release:        1%{?dist}
Summary:	The Fast Lexical Analyzer

License:	FLEX
URL:		https://flex.sourceforge.net/
Source0:	https://github.com/westes/flex/releases/download/v%{version}/flex-%{version}.tar.gz

#BuildRequires:
#Requires:

%description

%prep
%setup -q
sed -i "/math.h/a #include <malloc.h>" src/flexdef.h

%build
%configure --prefix=/usr --libdir=/usr/lib --docdir=/usr/share/doc/flex
make %{?_smp_mflags}
make check

%install
rm -rf $RPM_BUILD_ROOT
%make_install
rm -rf $RPM_BUILD_ROOT/usr/share/info/dir
find %{buildroot} -type f -name '*.la' -delete || die

%files
/usr/bin/flex
/usr/bin/flex++
/usr/include/FlexLexer.h
/usr/lib/libfl.a
/usr/lib/libfl.so
/usr/lib/libfl.so.2
/usr/lib/libfl.so.2.0.0
/usr/share/doc/flex/AUTHORS
/usr/share/doc/flex/COPYING
/usr/share/doc/flex/NEWS
/usr/share/doc/flex/ONEWS
/usr/share/doc/flex/README.md
/usr/share/locale/ca/LC_MESSAGES/flex.mo
/usr/share/locale/da/LC_MESSAGES/flex.mo
/usr/share/locale/de/LC_MESSAGES/flex.mo
/usr/share/locale/en@boldquot/LC_MESSAGES/flex.mo
/usr/share/locale/en@quot/LC_MESSAGES/flex.mo
/usr/share/locale/eo/LC_MESSAGES/flex.mo
/usr/share/locale/es/LC_MESSAGES/flex.mo
/usr/share/locale/fi/LC_MESSAGES/flex.mo
/usr/share/locale/fr/LC_MESSAGES/flex.mo
/usr/share/locale/ga/LC_MESSAGES/flex.mo
/usr/share/locale/hr/LC_MESSAGES/flex.mo
/usr/share/locale/ko/LC_MESSAGES/flex.mo
/usr/share/locale/nl/LC_MESSAGES/flex.mo
/usr/share/locale/pl/LC_MESSAGES/flex.mo
/usr/share/locale/pt_BR/LC_MESSAGES/flex.mo
/usr/share/locale/ro/LC_MESSAGES/flex.mo
/usr/share/locale/ru/LC_MESSAGES/flex.mo
/usr/share/locale/sr/LC_MESSAGES/flex.mo
/usr/share/locale/sv/LC_MESSAGES/flex.mo
/usr/share/locale/tr/LC_MESSAGES/flex.mo
/usr/share/locale/vi/LC_MESSAGES/flex.mo
/usr/share/locale/zh_CN/LC_MESSAGES/flex.mo
/usr/share/locale/zh_TW/LC_MESSAGES/flex.mo
/usr/share/man/man1/flex.1.gz
/usr/share/info/flex.info-1.gz
/usr/share/info/flex.info-2.gz
/usr/share/info/flex.info.gz

%changelog
