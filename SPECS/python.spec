Name:          	python
Version:	3.8.8
Release:        1%{?dist}
Summary:	An interpreted, interactive, object-oriented programming language

License:	PSF-2
URL:		https://www.python.org/
Source0:	https://www.python.org/ftp/python/%{version}/Python-%{version}.tar.xz

#BuildRequires:
#Requires:

%description

%prep
#%setup -q
umask 022
cd %{_builddir}
rm -rf Python-%{version}
tar xvf %{_sourcedir}/Python-%{version}.tar.xz


%build
cd %{_builddir}/Python-%{version}
%configure --prefix=/usr       \
            --enable-shared     \
            --with-system-expat \
            --with-system-ffi   \
            --with-ensurepip=yes
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
cd %{_builddir}/Python-%{version}
%make_install

%post
ln -s /usr/bin/python3 /usr/bin/python

%files
/*

%changelog
* Tue May 31 2016 Adam Miller <maxamillion@fedoraproject.org>
-

# see /usr/libexec/rpm/macros for macros
