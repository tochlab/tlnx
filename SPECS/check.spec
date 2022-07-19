Name:           check
Version:	0.15.2
Release:        1%{?dist}
Summary:	A unit test framework for C

License:	LGPL-2.1+
URL:		https://libcheck.github.io/check/
Source0:	https://github.com/libcheck/check/releases/download/%{version}/check-%{version}.tar.gz

#BuildRequires:
#Requires:

%description

%prep
%setup -q

%build
%configure --prefix=/usr --libdir=/usr/lib --with-pkg-config-libdir=/usr/lib/pkgconfig
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
%make_install
rm -rf $RPM_BUILD_ROOT/usr/share/info/dir
find %{buildroot} -type f -name '*.la' -delete || die

%files
/usr/bin/checkmk
/usr/include/check.h
/usr/include/check_stdint.h
/usr/lib/libcheck.a
#/usr/lib/libcheck.la
/usr/lib/libcheck.so
/usr/lib/libcheck.so.0
/usr/lib/libcheck.so.0.0.0
/usr/lib/pkgconfig/check.pc
/usr/share/aclocal/check.m4
/usr/share/doc/check/COPYING.LESSER
/usr/share/doc/check/ChangeLog
/usr/share/doc/check/NEWS
/usr/share/doc/check/README
/usr/share/doc/check/example/Makefile.am
/usr/share/doc/check/example/README
/usr/share/doc/check/example/configure.ac
/usr/share/doc/check/example/src/Makefile.am
/usr/share/doc/check/example/src/main.c
/usr/share/doc/check/example/src/money.1.c
/usr/share/doc/check/example/src/money.1.h
/usr/share/doc/check/example/src/money.2.h
/usr/share/doc/check/example/src/money.3.c
/usr/share/doc/check/example/src/money.4.c
/usr/share/doc/check/example/src/money.5.c
/usr/share/doc/check/example/src/money.6.c
/usr/share/doc/check/example/src/money.c
/usr/share/doc/check/example/src/money.h
/usr/share/doc/check/example/tests/Makefile.am
/usr/share/doc/check/example/tests/check_money.1.c
/usr/share/doc/check/example/tests/check_money.2.c
/usr/share/doc/check/example/tests/check_money.3.c
/usr/share/doc/check/example/tests/check_money.6.c
/usr/share/doc/check/example/tests/check_money.7.c
/usr/share/doc/check/example/tests/check_money.c
/usr/share/info/check.info.gz
/usr/share/man/man1/checkmk.1.gz


%changelog
