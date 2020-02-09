Name:           file
Version:	5.37
Release:        1%{?dist}
Summary:	File utility

License:	MIT?
URL:		ftp://ftp.astron.com/pub/file/
Source0:	file-5.37.tar.gz

%description
File utility

%prep
%setup -q

%build
%configure --prefix=/usr
make %{?_smp_mflags}
make check

%install
rm -rf $RPM_BUILD_ROOT
%make_install

%files
/usr/bin/file
/usr/include/magic.h
/usr/lib64/libmagic.la
/usr/lib64/libmagic.so
/usr/lib64/libmagic.so.1
/usr/lib64/libmagic.so.1.0.0
/usr/share/man/man1/file.1.gz
/usr/share/man/man3/libmagic.3.gz
/usr/share/man/man4/magic.4.gz
/usr/share/misc/magic.mgc

%changelog
