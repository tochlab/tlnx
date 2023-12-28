Name:           diffutils
Version:	3.8
Release:        1%{?dist}
Summary:	Tools to make diffs and compare files

License:	GPL-2
URL:		https://www.gnu.org/software/diffutils/
Source0:	https://ftpmirror.gnu.org/gnu/diffutils/diffutils-%{version}.tar.xz

#BuildRequires:
#Requires:

%description

%prep
%setup -q

%build
%configure --prefix=/usr --disable-nls
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
%make_install
rm -f $RPM_BUILD_ROOT/usr/share/info/dir

%files
/usr/bin/cmp
/usr/bin/diff
/usr/bin/diff3
/usr/bin/sdiff
/usr/share/info/diffutils.info.gz
/usr/share/man/man1/cmp.1.gz
/usr/share/man/man1/diff.1.gz
/usr/share/man/man1/diff3.1.gz
/usr/share/man/man1/sdiff.1.gz



%changelog
* Tue May 31 2016 Adam Miller <maxamillion@fedoraproject.org>
-

# see /usr/libexec/rpm/macros for macros
