Name:           make
Version:	4.3
Release:        1%{?dist}
Summary:	Standard tool to compile source trees

License:	GPL-3+
URL:		https://www.gnu.org/software/make/make.html
Source0:	https://ftpmirror.gnu.org/gnu/make/make-%{version}.tar.gz

#BuildRequires:
#Requires:

%description

%prep
%setup -q

%build
%configure --prefix=/usr --without-guile --disable-nls
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
%make_install
rm -rf $RPM_BUILD_ROOT/usr/share/info/dir

%files
/usr/bin/make
/usr/include/gnumake.h
/usr/share/info/make.info-1.gz
/usr/share/info/make.info-2.gz
/usr/share/info/make.info.gz
/usr/share/man/man1/make.1.gz


%changelog
* Tue May 31 2016 Adam Miller <maxamillion@fedoraproject.org>
-

# see /usr/libexec/rpm/macros for macros
