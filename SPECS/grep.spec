Name:           grep
Version:	3.11
Release:        1%{?dist}
Summary:	GNU regular expression matcher

License:	GPL-3
URL:		https://www.gnu.org/software/grep/
Source0:	https://ftpmirror.gnu.org/gnu/grep/grep-%{version}.tar.xz

#BuildRequires:
#Requires:

%description

%prep
%setup -q

%build
%configure --prefix=/usr --bindir=/bin --infodir=/usr/share/info --disable-nls
make %{?_smp_mflags}
make check

%install
rm -rf $RPM_BUILD_ROOT
%make_install
rm -fr %{buildroot}/usr/share/info/dir

%files
/bin/egrep
/bin/fgrep
/bin/grep
/usr/share/info/grep.info.gz
/usr/share/man/man1/grep.1.gz

%changelog
* Tue May 31 2016 Adam Miller <maxamillion@fedoraproject.org>
-
