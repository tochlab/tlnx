Name:           patch
Version:	2.7.6
Release:        1%{?dist}
Summary:	Utility to apply diffs to files

License:	GPL-3+
URL:		https://www.gnu.org/software/patch/patch.html
Source0:	https://ftpmirror.gnu.org/gnu/patch/patch-%{version}.tar.gz

#BuildRequires:
#Requires:

%description

%prep
%setup -q

%build
%configure --prefix=/usr
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
%make_install

%files
/usr/bin/patch
/usr/share/man/man1/patch.1.gz

%changelog
