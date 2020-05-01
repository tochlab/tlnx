Name:          	pkg-config 
Version:	0.29.2
Release:        1%{?dist}
Summary:	Package config system that manages compile/link flags

License:	GPL-2
URL:		https://pkgconfig.freedesktop.org/wiki/
Source0:	https://pkgconfig.freedesktop.org/releases/pkg-config-%{version}.tar.gz

#BuildRequires:
#Requires:

%description

%prep
%setup -q

%build
./configure --prefix=/usr              \
            --with-internal-glib       \
            --disable-host-tool        \
            --docdir=/usr/share/doc/pkg-config-%{version}
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
%make_install

%files
/usr/bin/pkg-config
/usr/share/aclocal/pkg.m4
/usr/share/doc/pkg-config-0.29.2/pkg-config-guide.html
/usr/share/man/man1/pkg-config.1.gz

%changelog
* Tue May 31 2016 Adam Miller <maxamillion@fedoraproject.org>
-
