Name:           intltool
Version:	0.51.0
Release:        1%{?dist}
Summary:	Internationalization Tool Collection

License:	GPL-2
URL:		https://launchpad.net/intltool/
Source0:	https://launchpad.net/intltool/trunk/%{version}/+download/intltool-%{version}.tar.gz

#BuildRequires:
#Requires:

%description

%prep
%setup -q

%build
sed -i 's:\\\${:\\\$\\{:' intltool-update.in
%configure --prefix=/usr
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
%make_install

%files
/usr/bin/intltool-extract
/usr/bin/intltool-merge
/usr/bin/intltool-prepare
/usr/bin/intltool-update
/usr/bin/intltoolize
/usr/share/aclocal/intltool.m4
/usr/share/intltool/Makefile.in.in
/usr/share/man/man8/intltool-extract.8.gz
/usr/share/man/man8/intltool-merge.8.gz
/usr/share/man/man8/intltool-prepare.8.gz
/usr/share/man/man8/intltool-update.8.gz
/usr/share/man/man8/intltoolize.8.gz

%changelog
* Tue May 31 2016 Adam Miller <maxamillion@fedoraproject.org>
-

# see /usr/libexec/rpm/macros for macros
