Name:           gmp
Version:	6.1.2
Release:        1%{?dist}
Summary:	The GMP package contains math libraries. These have useful functions for arbitrary precision arithmetic.

License:	GPL
URL:		https://gmplib.org/
Source0:	gmp-6.1.2.tar.bz2

%description

%prep
%setup -q

%build
./configure --prefix=/usr --enable-cxx --disable-static --docdir=/usr/share/doc/gmp-%{version}
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
%make_install

%files
/*

%changelog
