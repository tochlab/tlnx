Name:           libffi
Version:	3.3
Release:        1
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
#./configure --prefix=/usr --libdir=/usr/lib --disable-static 
%configure --libdir=/usr/lib
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
%make_install
rm $RPM_BUILD_ROOT/usr/share/info/dir
mv %{buildroot}/usr/lib64/* %{buildroot}/usr/lib

%files
/usr/include/ffi.h
/usr/include/ffitarget.h
/usr/lib/libffi.a
/usr/lib/libffi.la
/usr/lib/libffi.so
/usr/lib/libffi.so.7
/usr/lib/libffi.so.7.1.0
/usr/lib/pkgconfig/libffi.pc
/usr/share/info/libffi.info.gz
/usr/share/man/man3/ffi.3.gz
/usr/share/man/man3/ffi_call.3.gz
/usr/share/man/man3/ffi_prep_cif.3.gz
/usr/share/man/man3/ffi_prep_cif_var.3.gz


%changelog
