Name:           gperf
Version:	3.1
Release:        1%{?dist}
Summary:	A perfect hash function generator

License:	GPL-2
URL:		https://www.gnu.org/software/gperf/
Source0:	https://ftpmirror.gnu.org/gnu/gperf/gperf-%{version}.tar.gz

#BuildRequires:
#Requires:

%description

%prep
%setup -q

%build
./configure --prefix=/usr --docdir=/usr/share/doc/gperf-%{version}
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
%make_install

%files
/usr/bin/gperf
/usr/share/doc/gperf-3.1/gperf.html
/usr/share/info/gperf.info.gz
/usr/share/man/man1/gperf.1.gz


%changelog
* Tue May 31 2016 Adam Miller <maxamillion@fedoraproject.org>
-

# see /usr/libexec/rpm/macros for macros
