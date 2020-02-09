Name:           glibc
Version:	2.29
Release:        1
Summary:	GNU libc

License:	GPL
URL:		https://www.gnu.org/software/libc/
Source0:	glibc-2.29.tar.xz

%description
GNU C library

%prep
%setup -q

%build
mkdir build
cd build
../configure --prefix=/usr --enable-kernel=3.2.0 --enable-obsolete-rpc --enable-stack-protector=strong libc_cv_slibdir=/lib
make -j 16
#make check

%install
cd build
mkdir -pv %{buildroot}/etc/
touch %{buildroot}/etc/ld.so.conf
make DESTDIR=%{buildroot} install
cp -v ../nscd/nscd.conf %{buildroot}/etc/nscd.conf
mkdir -pv %{buildroot}/var/cache/nscd
echo /usr/local/lib > %{buildroot}/etc/ld.so.conf
echo /opt/lib >> %{buildroot}/etc/ld.so.conf
#rm -rf $RPM_BUILD_ROOT

%files
/*

%changelog
* Tue May 31 2016 Adam Miller <maxamillion@fedoraproject.org>
-