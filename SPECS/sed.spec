Name:           sed
Version:	4.8
Release:        1%{?dist}
Summary:	Super-useful stream editor

License:	GPL-3
URL:		http://sed.sourceforge.net/
Source0:	https://ftpmirror.gnu.org/gnu/sed/sed-%{version}.tar.gz

#BuildRequires:
#Requires:

%description

%prep
%setup -q

%build
%configure --prefix=/usr --bindir=/bin --disable-nls
make %{?_smp_mflags}
#make check

%install
rm -rf $RPM_BUILD_ROOT
%make_install
rm -rf $RPM_BUILD_ROOT/usr/share/info/dir

%files
/bin/sed
/usr/share/info/sed.info.gz
/usr/share/man/man1/sed.1.gz

%changelog
* Tue May 31 2016 Adam Miller <maxamillion@fedoraproject.org>
-
