Name:           readline
Version:	8.0
Release:        1%{?dist}
Summary:	GNU Readline Library

License:	GPL
URL:		http://www.gnu.org/software/readline/
Source0:	https://ftp.gnu.org/gnu/readline/readline-%{version}.tar.gz

%description

%prep
%setup -q

%build
./configure -prefix=/usr --disable-static --docdir=/usr/share/doc/readline-8.0

make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
mkdir %{buildroot}/lib
mv -v %{buildroot}/usr/lib/lib{readline,history}.so.* %{buildroot}/lib
chmod -v u+w %{buildroot}/lib/lib{readline,history}.so.*
ln -sfv ../../lib/$(readlink %{buildroot}/usr/lib/libreadline.so) %{buildroot}/usr/lib/libreadline.so
ln -sfv ../../lib/$(readlink %{buildroot}/usr/lib/libhistory.so ) %{buildroot}/usr/lib/libhistory.so

%files
%doc
/*

%changelog
