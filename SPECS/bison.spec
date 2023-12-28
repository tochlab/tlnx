Name:          	bison
Version:	3.8.2
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
%configure --prefix=/usr --libdir=/usr/lib --docdir=/usr/share/doc/bison --disable-nls
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
/usr/share/bison/skeletons/glr2.cc
/usr/share/bison/skeletons/java-skel.m4
/usr/share/bison/skeletons/java.m4
/usr/share/bison/skeletons/lalr1.cc
/usr/share/bison/skeletons/lalr1.d
/usr/share/bison/skeletons/lalr1.java
/usr/share/bison/skeletons/location.cc
/usr/share/bison/skeletons/stack.hh
/usr/share/bison/skeletons/traceon.m4
/usr/share/bison/skeletons/variant.hh
/usr/share/bison/skeletons/yacc.c
/usr/share/bison/xslt/bison.xsl
/usr/share/bison/xslt/xml2dot.xsl
/usr/share/bison/xslt/xml2text.xsl
/usr/share/bison/xslt/xml2xhtml.xsl
/usr/share/doc/bison/AUTHORS
/usr/share/doc/bison/COPYING
/usr/share/doc/bison/NEWS
/usr/share/doc/bison/README
/usr/share/doc/bison/THANKS
/usr/share/doc/bison/TODO
/usr/share/doc/bison/examples/README.md
/usr/share/doc/bison/examples/c++/Makefile
/usr/share/doc/bison/examples/c++/README.md
/usr/share/doc/bison/examples/c++/calc++/Makefile
/usr/share/doc/bison/examples/c++/calc++/README.md
/usr/share/doc/bison/examples/c++/calc++/calc++.cc
/usr/share/doc/bison/examples/c++/calc++/driver.cc
/usr/share/doc/bison/examples/c++/calc++/driver.hh
/usr/share/doc/bison/examples/c++/calc++/parser.yy
/usr/share/doc/bison/examples/c++/calc++/scanner.ll
/usr/share/doc/bison/examples/c++/simple.yy
/usr/share/doc/bison/examples/c++/variant-11.yy
/usr/share/doc/bison/examples/c++/variant.yy
/usr/share/doc/bison/examples/c/README.md
/usr/share/doc/bison/examples/c/bistromathic/Makefile
/usr/share/doc/bison/examples/c/bistromathic/README.md
/usr/share/doc/bison/examples/c/bistromathic/parse.y
/usr/share/doc/bison/examples/c/calc/Makefile
/usr/share/doc/bison/examples/c/calc/README.md
/usr/share/doc/bison/examples/c/calc/calc.y
/usr/share/doc/bison/examples/c/glr/Makefile
/usr/share/doc/bison/examples/c/glr/README.md
/usr/share/doc/bison/examples/c/glr/c++-types.y
/usr/share/doc/bison/examples/c/lexcalc/Makefile
/usr/share/doc/bison/examples/c/lexcalc/README.md
/usr/share/doc/bison/examples/c/lexcalc/parse.y
/usr/share/doc/bison/examples/c/lexcalc/scan.l
/usr/share/doc/bison/examples/c/mfcalc/Makefile
/usr/share/doc/bison/examples/c/mfcalc/calc.h
/usr/share/doc/bison/examples/c/mfcalc/mfcalc.y
/usr/share/doc/bison/examples/c/pushcalc/Makefile
/usr/share/doc/bison/examples/c/pushcalc/README.md
/usr/share/doc/bison/examples/c/pushcalc/calc.y
/usr/share/doc/bison/examples/c/reccalc/Makefile
/usr/share/doc/bison/examples/c/reccalc/README.md
/usr/share/doc/bison/examples/c/reccalc/parse.y
/usr/share/doc/bison/examples/c/reccalc/scan.l
/usr/share/doc/bison/examples/c/rpcalc/Makefile
/usr/share/doc/bison/examples/c/rpcalc/rpcalc.y
/usr/share/doc/bison/examples/d/README.md
/usr/share/doc/bison/examples/d/calc/Makefile
/usr/share/doc/bison/examples/d/calc/calc.y
/usr/share/doc/bison/examples/d/simple/Makefile
/usr/share/doc/bison/examples/d/simple/calc.y
/usr/share/doc/bison/examples/java/README.md
/usr/share/doc/bison/examples/java/calc/Calc.y
/usr/share/doc/bison/examples/java/calc/Makefile
/usr/share/doc/bison/examples/java/simple/Calc.y
/usr/share/doc/bison/examples/java/simple/Makefile
/usr/share/info/bison.info.gz
/usr/share/man/man1/bison.1.gz
/usr/share/man/man1/yacc.1.gz


%changelog
