Name:           popt
Version:	1.19
Release:        1%{?dist}
Summary:	Parse Options - Command line parser

License:	MIT
URL:		https://github.com/rpm-software-management/popt
Source0:	http://ftp.rpm.org/popt/releases/popt-1.x/popt-%{version}.tar.gz

#BuildRequires:
#Requires:

%description

%prep
%setup -q

%build
./autogen.sh
%configure --libdir=/usr/lib --with-pkg-config-libdir=/usr/lib/pkgconfig --disable-nls
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
%make_install
%{__rm} -f %{buildroot}/usr/share/info/dir
find %{buildroot} -type f -name '*.la' -delete || die

#%post
#/sbin/ldconfig
#/sbin/install-info /usr/share/info/DevIL_manual.info.gz /usr/share/info/dir 2> /dev/null || :

#%postun
#/sbin/ldconfig
#/sbin/install-info --delete /usr/share/info/DevIL_manual.info.gz /usr/share/info/dir 2> /dev/null || :

%files
/usr/include/popt.h
/usr/lib/libpopt.a
/usr/lib/libpopt.so
/usr/lib/libpopt.so.0
/usr/lib/libpopt.so.0.0.2
/usr/lib/pkgconfig/popt.pc
/usr/share/man/man3/popt.3.gz

%doc

%changelog
