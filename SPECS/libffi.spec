Name:           libffi
Version:	3.4.2
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
%configure --libdir=/usr/lib --with-pkg-config-libdir=/usr/lib/pkgconfig
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
%make_install
mv %{buildroot}/usr/lib64/* %{buildroot}/usr/lib
rm -f $RPM_BUILD_ROOT/usr/share/info/dir
find %{buildroot} -type f -name '*.la' -delete || die

%files
/usr/include/ffi.h
/usr/include/ffitarget.h
/usr/lib/libffi.a
/usr/lib/libffi.so
/usr/lib/libffi.so.8
/usr/lib/libffi.so.8.1.0
/usr/lib/pkgconfig/libffi.pc
/usr/share/info/libffi.info.gz
/usr/share/man/man3/ffi.3.gz
/usr/share/man/man3/ffi_call.3.gz
/usr/share/man/man3/ffi_prep_cif.3.gz
/usr/share/man/man3/ffi_prep_cif_var.3.gz


%changelog
