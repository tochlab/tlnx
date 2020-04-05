Name:          	gdbm 
Version:	1.18.1
Release:        1%{?dist}
Summary:	Standard GNU database libraries

License:	GPL-3
URL:		https://www.gnu.org/software/gdbm/
Source0:	https://ftpmirror.gnu.org/gnu/gdbm/gdbm-%{version}.tar.gz

#BuildRequires:
#Requires:

%description

%prep
%setup -q

%build
./configure --prefix=/usr    \
            --disable-static \
            --enable-libgdbm-compat
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
%make_install

%files
%doc

%changelog
* Tue May 31 2016 Adam Miller <maxamillion@fedoraproject.org>
-
