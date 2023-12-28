Name:           findutils
Version:	4.9.0
Release:        1%{?dist}
Summary:	GNU utilities for finding files

License:	GPL-3+
URL:		https://www.gnu.org/software/findutils/
Source0:	https://ftpmirror.gnu.org/gnu/findutils/findutils-%{version}.tar.xz

#BuildRequires:
#Requires:

%description

%prep
%setup -q

%build
%configure --prefix=/usr/ --disable-nls
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
%make_install
rm -rf $RPM_BUILD_ROOT/usr/share/info/dir

%files
/usr/bin/find
/usr/bin/locate
/usr/bin/updatedb
/usr/bin/xargs
/usr/libexec/frcode
/usr/share/info/find-maint.info.gz
/usr/share/info/find.info-1.gz
/usr/share/info/find.info-2.gz
/usr/share/info/find.info.gz
/usr/share/man/man1/find.1.gz
/usr/share/man/man1/locate.1.gz
/usr/share/man/man1/updatedb.1.gz
/usr/share/man/man1/xargs.1.gz
/usr/share/man/man5/locatedb.5.gz


%changelog
