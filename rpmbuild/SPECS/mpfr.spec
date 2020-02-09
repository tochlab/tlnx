Name:           mpfr
Version:        4.0.2
Release:        1%{?dist}
Summary:        mpfr lib

#Group:          
License:        GPL
URL:            https://www.mpfr.org/
Source0:        https://mirror.tochlab.net/pub/gnu/mpfr/mpfr-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

#BuildRequires:  
#Requires:       

%description
MPFR Library

%prep
%setup -q


%build
./configure --prefix=/usr        \
            --disable-static     \
            --enable-thread-safe \
            --docdir=/usr/share/doc/mpfr-%{version}
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT


%files
/*


%changelog
