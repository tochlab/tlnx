Name:          	Python
Version:	3.11.6
Release:        1%{?dist}
Summary:	An interpreted, interactive, object-oriented programming language

License:	PSF-2
URL:		https://www.python.org/
Source0:	https://www.python.org/ftp/python/%{version}/Python-%{version}.tar.xz

#BuildRequires:
#Requires:

%description

%prep
%setup -q


%build
%configure --prefix=/usr       \
	    --libdir=/usr/lib \
            --enable-shared     \
            --with-system-expat \
            --with-system-ffi   \
	    --without-ensurepip \
	    --with-pkg-config-libdir=/usr/lib/pkgconfig \
	    --enable-optimizations
make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -name "__pycache__" -print0 | xargs -r0 -- rm -r

%post
ln -s /usr/bin/python3 /usr/bin/python

%files

%changelog
