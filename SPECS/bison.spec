Name:          	bison 
Version:	3.5.3
Release:        1%{?dist}
Summary:	A general-purpose (yacc-compatible) parser generator

License:	GPL-2
URL:		https://www.gnu.org/software/bison/
Source0:	https://ftpmirror.gnu.org/gnu/bison/bison-%{version}.tar.gz

#BuildRequires:
#Requires: m4

%description

%prep
%setup -q

%build
./configure --prefix=/usr --docdir=/usr/share/doc/bison-%{version}
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
%make_install
rm -fr $RPM_BUILD_ROOT/usr/share/info/dir

%files
/usr/bin/bison
/usr/bin/yacc
/usr/lib/liby.a
/usr/share/aclocal/bison-i18n.m4
/usr/share/bison/README.md
/usr/share/bison/bison-default.css
/usr/share/bison/m4sugar/foreach.m4
/usr/share/bison/m4sugar/m4sugar.m4
/usr/share/bison/skeletons/README-D.txt
/usr/share/bison/skeletons/bison.m4
/usr/share/bison/skeletons/c++-skel.m4
/usr/share/bison/skeletons/c++.m4
/usr/share/bison/skeletons/c-like.m4
/usr/share/bison/skeletons/c-skel.m4
/usr/share/bison/skeletons/c.m4
/usr/share/bison/skeletons/d-skel.m4
/usr/share/bison/skeletons/d.m4
/usr/share/bison/skeletons/glr.c
/usr/share/bison/skeletons/glr.cc
/usr/share/bison/skeletons/java-skel.m4
/usr/share/bison/skeletons/java.m4
/usr/share/bison/skeletons/lalr1.cc
/usr/share/bison/skeletons/lalr1.d
/usr/share/bison/skeletons/lalr1.java
/usr/share/bison/skeletons/location.cc
/usr/share/bison/skeletons/stack.hh
/usr/share/bison/skeletons/variant.hh
/usr/share/bison/skeletons/yacc.c
/usr/share/bison/xslt/bison.xsl
/usr/share/bison/xslt/xml2dot.xsl
/usr/share/bison/xslt/xml2text.xsl
/usr/share/bison/xslt/xml2xhtml.xsl
/usr/share/doc/bison-3.5.3/AUTHORS
/usr/share/doc/bison-3.5.3/COPYING
/usr/share/doc/bison-3.5.3/NEWS
/usr/share/doc/bison-3.5.3/README
/usr/share/doc/bison-3.5.3/THANKS
/usr/share/doc/bison-3.5.3/TODO
/usr/share/doc/bison-3.5.3/examples/README.md
/usr/share/doc/bison-3.5.3/examples/c++/Makefile
/usr/share/doc/bison-3.5.3/examples/c++/README.md
/usr/share/doc/bison-3.5.3/examples/c++/calc++/Makefile
/usr/share/doc/bison-3.5.3/examples/c++/calc++/README.md
/usr/share/doc/bison-3.5.3/examples/c++/calc++/calc++.cc
/usr/share/doc/bison-3.5.3/examples/c++/calc++/driver.cc
/usr/share/doc/bison-3.5.3/examples/c++/calc++/driver.hh
/usr/share/doc/bison-3.5.3/examples/c++/calc++/parser.yy
/usr/share/doc/bison-3.5.3/examples/c++/calc++/scanner.ll
/usr/share/doc/bison-3.5.3/examples/c++/simple.yy
/usr/share/doc/bison-3.5.3/examples/c++/variant-11.yy
/usr/share/doc/bison-3.5.3/examples/c++/variant.yy
/usr/share/doc/bison-3.5.3/examples/c/README.md
/usr/share/doc/bison-3.5.3/examples/c/calc/Makefile
/usr/share/doc/bison-3.5.3/examples/c/calc/README.md
/usr/share/doc/bison-3.5.3/examples/c/calc/calc.y
/usr/share/doc/bison-3.5.3/examples/c/lexcalc/Makefile
/usr/share/doc/bison-3.5.3/examples/c/lexcalc/README.md
/usr/share/doc/bison-3.5.3/examples/c/lexcalc/parse.y
/usr/share/doc/bison-3.5.3/examples/c/lexcalc/scan.l
/usr/share/doc/bison-3.5.3/examples/c/mfcalc/Makefile
/usr/share/doc/bison-3.5.3/examples/c/mfcalc/calc.h
/usr/share/doc/bison-3.5.3/examples/c/mfcalc/mfcalc.y
/usr/share/doc/bison-3.5.3/examples/c/reccalc/Makefile
/usr/share/doc/bison-3.5.3/examples/c/reccalc/README.md
/usr/share/doc/bison-3.5.3/examples/c/reccalc/parse.y
/usr/share/doc/bison-3.5.3/examples/c/reccalc/scan.l
/usr/share/doc/bison-3.5.3/examples/c/rpcalc/Makefile
/usr/share/doc/bison-3.5.3/examples/c/rpcalc/rpcalc.y
/usr/share/doc/bison-3.5.3/examples/d/Makefile
/usr/share/doc/bison-3.5.3/examples/d/README.md
/usr/share/doc/bison-3.5.3/examples/d/calc.y
/usr/share/doc/bison-3.5.3/examples/java/Calc.y
/usr/share/doc/bison-3.5.3/examples/java/Makefile
/usr/share/doc/bison-3.5.3/examples/java/README.md
/usr/share/info/bison.info.gz
/usr/share/locale/af/LC_MESSAGES/bison-gnulib.mo
/usr/share/locale/ast/LC_MESSAGES/bison-runtime.mo
/usr/share/locale/be/LC_MESSAGES/bison-gnulib.mo
/usr/share/locale/bg/LC_MESSAGES/bison-gnulib.mo
/usr/share/locale/bg/LC_MESSAGES/bison-runtime.mo
/usr/share/locale/bg/LC_MESSAGES/bison.mo
/usr/share/locale/ca/LC_MESSAGES/bison-gnulib.mo
/usr/share/locale/ca/LC_MESSAGES/bison-runtime.mo
/usr/share/locale/ca/LC_MESSAGES/bison.mo
/usr/share/locale/cs/LC_MESSAGES/bison-gnulib.mo
/usr/share/locale/da/LC_MESSAGES/bison-gnulib.mo
/usr/share/locale/da/LC_MESSAGES/bison-runtime.mo
/usr/share/locale/da/LC_MESSAGES/bison.mo
/usr/share/locale/de/LC_MESSAGES/bison-gnulib.mo
/usr/share/locale/de/LC_MESSAGES/bison-runtime.mo
/usr/share/locale/de/LC_MESSAGES/bison.mo
/usr/share/locale/el/LC_MESSAGES/bison-gnulib.mo
/usr/share/locale/el/LC_MESSAGES/bison-runtime.mo
/usr/share/locale/el/LC_MESSAGES/bison.mo
/usr/share/locale/eo/LC_MESSAGES/bison-gnulib.mo
/usr/share/locale/eo/LC_MESSAGES/bison-runtime.mo
/usr/share/locale/eo/LC_MESSAGES/bison.mo
/usr/share/locale/es/LC_MESSAGES/bison-gnulib.mo
/usr/share/locale/es/LC_MESSAGES/bison-runtime.mo
/usr/share/locale/es/LC_MESSAGES/bison.mo
/usr/share/locale/et/LC_MESSAGES/bison-gnulib.mo
/usr/share/locale/et/LC_MESSAGES/bison-runtime.mo
/usr/share/locale/et/LC_MESSAGES/bison.mo
/usr/share/locale/eu/LC_MESSAGES/bison-gnulib.mo
/usr/share/locale/fi/LC_MESSAGES/bison-gnulib.mo
/usr/share/locale/fi/LC_MESSAGES/bison-runtime.mo
/usr/share/locale/fi/LC_MESSAGES/bison.mo
/usr/share/locale/fr/LC_MESSAGES/bison-gnulib.mo
/usr/share/locale/fr/LC_MESSAGES/bison-runtime.mo
/usr/share/locale/fr/LC_MESSAGES/bison.mo
/usr/share/locale/ga/LC_MESSAGES/bison-gnulib.mo
/usr/share/locale/ga/LC_MESSAGES/bison-runtime.mo
/usr/share/locale/ga/LC_MESSAGES/bison.mo
/usr/share/locale/gl/LC_MESSAGES/bison-gnulib.mo
/usr/share/locale/gl/LC_MESSAGES/bison-runtime.mo
/usr/share/locale/hr/LC_MESSAGES/bison-runtime.mo
/usr/share/locale/hr/LC_MESSAGES/bison.mo
/usr/share/locale/hu/LC_MESSAGES/bison-gnulib.mo
/usr/share/locale/hu/LC_MESSAGES/bison-runtime.mo
/usr/share/locale/ia/LC_MESSAGES/bison-runtime.mo
/usr/share/locale/id/LC_MESSAGES/bison-runtime.mo
/usr/share/locale/id/LC_MESSAGES/bison.mo
/usr/share/locale/it/LC_MESSAGES/bison-gnulib.mo
/usr/share/locale/it/LC_MESSAGES/bison-runtime.mo
/usr/share/locale/it/LC_MESSAGES/bison.mo
/usr/share/locale/ja/LC_MESSAGES/bison-gnulib.mo
/usr/share/locale/ja/LC_MESSAGES/bison-runtime.mo
/usr/share/locale/ja/LC_MESSAGES/bison.mo
/usr/share/locale/ko/LC_MESSAGES/bison-gnulib.mo
/usr/share/locale/ky/LC_MESSAGES/bison-runtime.mo
/usr/share/locale/lt/LC_MESSAGES/bison-runtime.mo
/usr/share/locale/lv/LC_MESSAGES/bison-runtime.mo
/usr/share/locale/ms/LC_MESSAGES/bison-gnulib.mo
/usr/share/locale/ms/LC_MESSAGES/bison-runtime.mo
/usr/share/locale/ms/LC_MESSAGES/bison.mo
/usr/share/locale/nb/LC_MESSAGES/bison-gnulib.mo
/usr/share/locale/nb/LC_MESSAGES/bison-runtime.mo
/usr/share/locale/nb/LC_MESSAGES/bison.mo
/usr/share/locale/nl/LC_MESSAGES/bison-gnulib.mo
/usr/share/locale/nl/LC_MESSAGES/bison-runtime.mo
/usr/share/locale/nl/LC_MESSAGES/bison.mo
/usr/share/locale/pl/LC_MESSAGES/bison-gnulib.mo
/usr/share/locale/pl/LC_MESSAGES/bison-runtime.mo
/usr/share/locale/pl/LC_MESSAGES/bison.mo
/usr/share/locale/pt/LC_MESSAGES/bison-gnulib.mo
/usr/share/locale/pt/LC_MESSAGES/bison-runtime.mo
/usr/share/locale/pt/LC_MESSAGES/bison.mo
/usr/share/locale/pt_BR/LC_MESSAGES/bison-gnulib.mo
/usr/share/locale/pt_BR/LC_MESSAGES/bison-runtime.mo
/usr/share/locale/pt_BR/LC_MESSAGES/bison.mo
/usr/share/locale/ro/LC_MESSAGES/bison-gnulib.mo
/usr/share/locale/ro/LC_MESSAGES/bison-runtime.mo
/usr/share/locale/ro/LC_MESSAGES/bison.mo
/usr/share/locale/ru/LC_MESSAGES/bison-gnulib.mo
/usr/share/locale/ru/LC_MESSAGES/bison-runtime.mo
/usr/share/locale/ru/LC_MESSAGES/bison.mo
/usr/share/locale/rw/LC_MESSAGES/bison-gnulib.mo
/usr/share/locale/sk/LC_MESSAGES/bison-gnulib.mo
/usr/share/locale/sl/LC_MESSAGES/bison-gnulib.mo
/usr/share/locale/sl/LC_MESSAGES/bison-runtime.mo
/usr/share/locale/sq/LC_MESSAGES/bison-runtime.mo
/usr/share/locale/sr/LC_MESSAGES/bison-gnulib.mo
/usr/share/locale/sr/LC_MESSAGES/bison-runtime.mo
/usr/share/locale/sr/LC_MESSAGES/bison.mo
/usr/share/locale/sv/LC_MESSAGES/bison-gnulib.mo
/usr/share/locale/sv/LC_MESSAGES/bison-runtime.mo
/usr/share/locale/sv/LC_MESSAGES/bison.mo
/usr/share/locale/th/LC_MESSAGES/bison-runtime.mo
/usr/share/locale/tr/LC_MESSAGES/bison-gnulib.mo
/usr/share/locale/tr/LC_MESSAGES/bison-runtime.mo
/usr/share/locale/tr/LC_MESSAGES/bison.mo
/usr/share/locale/uk/LC_MESSAGES/bison-gnulib.mo
/usr/share/locale/uk/LC_MESSAGES/bison-runtime.mo
/usr/share/locale/uk/LC_MESSAGES/bison.mo
/usr/share/locale/vi/LC_MESSAGES/bison-gnulib.mo
/usr/share/locale/vi/LC_MESSAGES/bison-runtime.mo
/usr/share/locale/vi/LC_MESSAGES/bison.mo
/usr/share/locale/zh_CN/LC_MESSAGES/bison-gnulib.mo
/usr/share/locale/zh_CN/LC_MESSAGES/bison-runtime.mo
/usr/share/locale/zh_CN/LC_MESSAGES/bison.mo
/usr/share/locale/zh_TW/LC_MESSAGES/bison-gnulib.mo
/usr/share/locale/zh_TW/LC_MESSAGES/bison-runtime.mo
/usr/share/locale/zh_TW/LC_MESSAGES/bison.mo
/usr/share/man/man1/bison.1.gz
/usr/share/man/man1/yacc.1.gz


%changelog
* Tue May 31 2016 Adam Miller <maxamillion@fedoraproject.org>
-
