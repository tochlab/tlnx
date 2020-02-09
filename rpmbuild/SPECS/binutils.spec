Name:           binutils
Version:	2.34
Release:        1%{?dist}
Summary:	The GNU Binutils are a collection of binary tools.

License:	GPL
URL:		https://www.gnu.org/software/binutils/
Source0:	https://ftp.gnu.org/gnu/binutils/binutils-2.34.tar.gz

%description

%prep
%setup -q

%build
mkdir -v build
cd       build
../configure --prefix=/usr --enable-gold --enable-ld=default --enable-plugins --enable-shared --disable-werror --enable-64-bit-bfd --with-system-zlib

make %{?_smp_mflags} tooldir=/usr

%install
rm -rf $RPM_BUILD_ROOT
cd build
make DESTDIR=%{buildroot} install

%files
/*

%changelog
