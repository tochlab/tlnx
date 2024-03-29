Name:           m4
Version:	1.4.19
Release:        1%{?dist}
Summary:	M4 is an implementation of the traditional Unix macro processor.

License:	GPL
URL:		http://www.gnu.org/software/m4/
Source0:	https://ftpmirror.gnu.org/gnu/m4/m4-%{version}.tar.gz

%description

%prep
%setup -q


%build
%configure --prefix=/usr --disable-nls
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
%{__rm} -f %{buildroot}/usr/share/info/dir

%files
/usr/bin/m4
/usr/share/info/m4.info-1.gz
/usr/share/info/m4.info-2.gz
/usr/share/info/m4.info.gz
/usr/share/man/man1/m4.1.gz

%changelog
