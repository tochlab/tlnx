Name:           ca-certificates
Version:	20230311
Release:        1%{?dist}
Summary:	Common CA Certificates PEM files

License:	MPL-1.1
URL:		https://packages.debian.org/sid/ca-certificates
Source0:	http://ftp.debian.org/debian/pool/main/c/ca-certificates/ca-certificates_%{version}.tar.xz
#Patch0:	ca-certificates-20211016.3.72-no-cryptography.patch

#BuildRequires:
#Requires:

%description

%prep
tar xvf %{_sourcedir}/ca-certificates_%{version}.tar.xz
cd work
#%patch -p1

%build
cd work
make 

%install
rm -rf $RPM_BUILD_ROOT
cd work
mkdir -p %{buildroot}/usr/share/ca-certificates/mozilla/
mkdir -p %{buildroot}/usr/sbin/
%make_install

%post
find /usr/share/ca-certificates/ -name \*.crt >> /etc/ssl/certs/ca-certificates.crt

#%postun
#/sbin/ldconfig
#/sbin/install-info --delete /usr/share/info/DevIL_manual.info.gz /usr/share/info/dir 2> /dev/null || :

%files
/*
