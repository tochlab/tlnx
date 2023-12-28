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
%configure --prefix=/usr --libdir=/usr/lib --docdir=/usr/share/doc/flex --disable-nls
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
/usr/share/man/man1/flex.1.gz
/usr/share/info/flex.info-1.gz
/usr/share/info/flex.info-2.gz
/usr/share/info/flex.info.gz

%changelog
