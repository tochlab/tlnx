Name:           less 
Version:	551
Release:        1%{?dist}
Summary:	Excellent text file viewer

License:	GPL-3 BSD
URL:		http://www.greenwoodsoftware.com/less/
Source0:	http://www.greenwoodsoftware.com/less/less-%{version}.tar.gz

#BuildRequires:
#Requires:

%description

%prep
%setup -q

%build
%configure --prefix=/usr --sysconfdir=/etc
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
%make_install

%files
/usr/bin/less
/usr/bin/lessecho
/usr/bin/lesskey
/usr/share/man/man1/less.1.gz
/usr/share/man/man1/lessecho.1.gz
/usr/share/man/man1/lesskey.1.gz

%changelog
* Tue May 31 2016 Adam Miller <maxamillion@fedoraproject.org>
-

# see /usr/libexec/rpm/macros for macros
