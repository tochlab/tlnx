Name:           gmp
Version:	6.2.1
Release:        1%{?dist}
Summary:	The GMP package contains math libraries. These have useful functions for arbitrary precision arithmetic.

License:	GPL
URL:		https://gmplib.org/
Source0:	https://ftpmirror.gnu.org/gnu/gmp/gmp-%{version}.tar.bz2

%description

%prep
%setup -q

%build
%configure --prefix=/usr --libdir=/usr/lib --enable-cxx --disable-static --docdir=/usr/share/doc/gmp
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
%make_install
%{__rm} -f %{buildroot}/usr/share/info/dir
find %{buildroot} -type f -name '*.la' -delete || die


%files
/usr/include/gmp.h
/usr/include/gmpxx.h
/usr/lib/libgmp.so
/usr/lib/libgmp.so.10
/usr/lib/libgmp.so.10.4.1
/usr/lib/libgmpxx.so
/usr/lib/libgmpxx.so.4
/usr/lib/libgmpxx.so.4.6.1
/usr/lib/pkgconfig/gmp.pc
/usr/lib/pkgconfig/gmpxx.pc
/usr/share/info/gmp.info-1.gz
/usr/share/info/gmp.info-2.gz
/usr/share/info/gmp.info.gz

%changelog
