Name:           libxcrypt
Version:	4.4.28
Release:        1%{?dist}
Summary:	Extended crypt library for descrypt, md5crypt, bcrypt, and others

License:	LGPL 2.1
URL:		https://github.com/besser82/libxcrypt
Source0:	https://github.com/besser82/libxcrypt/releases/download/v%{version}/libxcrypt-%{version}.tar.xz

#BuildRequires:
#Requires:

%description
Extended crypt library for descrypt, md5crypt, bcrypt, and others

%prep
%setup -q

%build
%configure --libdir=/lib --disable-xcrypt-compat-files  --enable-obsolete-api=no --with-pkg-config-libdir=/usr/lib/pkgconfig
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
%make_install
%{__rm} -f %{buildroot}/usr/share/info/dir
%{__rm} %{buildroot}/usr/share/man/man3/crypt.3
#%{__rm} %{buildroot}/usr/include/crypt.h
mkdir %{buildroot}/usr/lib/
cd %{buildroot}
ln -s /lib/libcrypt.so.2.0.0 /lib/libcrypt.so.1
mv %{buildroot}/lib/pkgconfig %{buildroot}/usr/lib/
find %{buildroot} -type f -name '*.la' -delete || die

#%post
#/sbin/ldconfig
#/sbin/install-info /usr/share/info/DevIL_manual.info.gz /usr/share/info/dir 2> /dev/null || :

#%postun
#/sbin/ldconfig
#/sbin/install-info --delete /usr/share/info/DevIL_manual.info.gz /usr/share/info/dir 2> /dev/null || :

%files
/lib/libcrypt.a
#/lib/libcrypt.la
/lib/libcrypt.so
/lib/libcrypt.so.1
/lib/libcrypt.so.2
/lib/libcrypt.so.2.0.0
/usr/lib/pkgconfig/libcrypt.pc
/usr/lib/pkgconfig/libxcrypt.pc
/usr/share/man/man3/crypt_checksalt.3.gz
/usr/share/man/man3/crypt_gensalt.3.gz
/usr/share/man/man3/crypt_gensalt_ra.3.gz
/usr/share/man/man3/crypt_gensalt_rn.3.gz
/usr/share/man/man3/crypt_preferred_method.3.gz
/usr/share/man/man3/crypt_r.3.gz
/usr/share/man/man3/crypt_ra.3.gz
/usr/share/man/man3/crypt_rn.3.gz
/usr/share/man/man5/crypt.5.gz
/usr/include/crypt.h

%doc

%changelog
* Tue May 31 2016 Adam Miller <maxamillion@fedoraproject.org>
-

# see /usr/libexec/rpm/macros for macros
