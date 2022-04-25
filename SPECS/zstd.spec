Name:           zstd
Version:	1.5.2
Release:        1%{?dist}
Summary:	zstd fast compression library

License:	BSD GPL-2
URL:		https://facebook.github.io/zstd/
Source0:	https://github.com/facebook/zstd/releases/download/v%{version}/zstd-%{version}.tar.gz

#BuildRequires:
#Requires:

%description

%prep
%setup -q

%build
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make prefix=%{buildroot}/usr install

%post
ldconfig

%files
/usr/bin/unzstd
/usr/bin/zstd
/usr/bin/zstdcat
/usr/bin/zstdgrep
/usr/bin/zstdless
/usr/bin/zstdmt
/usr/include/zdict.h
/usr/include/zstd.h
/usr/include/zstd_errors.h
/usr/lib/libzstd.a
/usr/lib/libzstd.so
/usr/lib/libzstd.so.1
/usr/lib/libzstd.so.%{version}
/usr/lib/pkgconfig/libzstd.pc
/usr/share/man/man1/unzstd.1.gz
/usr/share/man/man1/zstd.1.gz
/usr/share/man/man1/zstdcat.1.gz
/usr/share/man/man1/zstdgrep.1.gz
/usr/share/man/man1/zstdless.1.gz

%doc

%changelog
