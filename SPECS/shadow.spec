Name:           shadow
Version:        4.8.1
Release:        2%{?dist}
Summary:        shadow utils

#Group:          
License:        GPL
URL:            https://github.com/shadow-maint/shadow/releases/download/4.8.1/shadow-4.8.1.tar.gz
Source0:        https://github.com/shadow-maint/shadow/releases/download/4.8.1/shadow-4.8.1.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

#BuildRequires:  
#Requires:       

%description


%prep
%setup -q
sed -i 's/groups$(EXEEXT) //' src/Makefile.in
find man -name Makefile.in -exec sed -i 's/groups\.1 / /'   {} \;
find man -name Makefile.in -exec sed -i 's/getspnam\.3 / /' {} \;
find man -name Makefile.in -exec sed -i 's/passwd\.5 / /'   {} \;

sed -i -e 's@#ENCRYPT_METHOD DES@ENCRYPT_METHOD SHA512@' \
       -e 's@/var/spool/mail@/var/mail@' etc/login.defs
       
sed -i 's/1000/999/' etc/useradd

%build
%configure --sysconfdir=/etc --with-group-name-max-length=32
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT


%files
/*

%changelog
