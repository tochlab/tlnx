Name:           mpc
Version:        1.2.1
Release:        1%{?dist}
Summary:        mpc lib

Group:          System Environment/Libraries
License:        GPL
#URL:            
Source0:        https://ftpmirror.gnu.org/mpc/mpc-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

#BuildRequires:  
#Requires:       

%description


%prep
%setup -q


%build
%configure --prefix=/usr    \
            --disable-static \
	    --libdir=/usr/lib \
            --docdir=/usr/share/doc/mpc-%{version}
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
%{__rm} -f %{buildroot}/usr/share/info/dir

%clean
rm -rf $RPM_BUILD_ROOT


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
/usr/include/mpc.h
/usr/lib/libmpc.so
/usr/lib/libmpc.so.3
/usr/lib/libmpc.so.3.2.1
/usr/share/info/mpc.info.gz

%changelog
