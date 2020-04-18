Name:           libffi 
Version:	3.3
Release:        1%{?dist}
Summary:	a portable, high level programming interface to various calling conventions

License:	MIT
URL:		https://sourceware.org/libffi
Source0:	https://github.com/libffi/libffi/releases/download/v%{version}/libffi-%{version}.tar.gz

#BuildRequires:
#Requires:

%description

%prep
%setup -q

%build
./configure --prefix=/usr --disable-static
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
%make_install
rm $RPM_BUILD_ROOT/usr/share/info/dir

%files
/usr/include/ffi.h
/usr/include/ffitarget.h
/usr/lib64/libffi.la
/usr/lib64/libffi.so
/usr/lib64/libffi.so.7
/usr/lib64/libffi.so.7.1.0
/usr/lib/pkgconfig/libffi.pc
/usr/share/info/libffi.info.gz
/usr/share/man/man3/ffi.3.gz
/usr/share/man/man3/ffi_call.3.gz
/usr/share/man/man3/ffi_prep_cif.3.gz
/usr/share/man/man3/ffi_prep_cif_var.3.gz

%changelog
* Tue May 31 2016 Adam Miller <maxamillion@fedoraproject.org>
-

# see /usr/libexec/rpm/macros for macros
