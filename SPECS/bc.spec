Name:           bc
Version:	1.07.1
Release:        1%{?dist}
Summary:	bc is an arbitrary precision numeric processing language.

License:	GPL
URL:		http://www.gnu.org/software/bc/
Source0:	https://ftpmirror.gnu.org/gnu/bc/bc-1.07.1.tar.gz

%description

%prep
%setup -q
cat > bc/fix-libmath_h << "EOF"
#! /bin/bash
sed -e '1   s/^/{"/' \
    -e     's/$/",/' \
    -e '2,$ s/^/"/'  \
    -e   '$ d'       \
    -i libmath.h

sed -e '$ s/$/0}/' \
    -i libmath.h
EOF

%build
sed -i -e '/flex/s/as_fn_error/: ;; # &/' configure
./configure --prefix=/usr --with-readline --mandir=/usr/share/man --infodir=/usr/share/info
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
rm -rf $RPM_BUILD_ROOT/usr/share/info/dir


%files
/usr/bin/bc
/usr/bin/dc
/usr/share/info/bc.info.gz
/usr/share/info/dc.info.gz
/usr/share/man/man1/bc.1.gz
/usr/share/man/man1/dc.1.gz

