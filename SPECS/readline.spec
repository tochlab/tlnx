Name:           readline
Version:	8.0
Release:        1%{?dist}
Summary:	GNU Readline Library

License:	GPL
URL:		http://www.gnu.org/software/readline/
Source0:	https://ftpmirror.gnu.org/gnu/readline/readline-%{version}.tar.gz

%description

%prep
%setup -q

%build
%configure -prefix=/usr --disable-static --docdir=/usr/share/doc/readline-%{version}
for mfile in $(find "$PWD" -name 'Makefile'); do
    sed -i 's|SHLIB_LIBS =|SHLIB_LIBS = -ltinfo|g' "$mfile"
done

make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
%{__rm} -f %{buildroot}/usr/share/info/dir
mkdir %{buildroot}/lib
mv -v %{buildroot}/usr/lib/lib{readline,history}.so.* %{buildroot}/lib
chmod -v u+w %{buildroot}/lib/lib{readline,history}.so.*
ln -sfv ../../lib/$(readlink %{buildroot}/usr/lib/libreadline.so) %{buildroot}/usr/lib/libreadline.so
ln -sfv ../../lib/$(readlink %{buildroot}/usr/lib/libhistory.so ) %{buildroot}/usr/lib/libhistory.so

%files
/lib/libhistory.so.8
/lib/libhistory.so.8.0
/lib/libreadline.so.8
/lib/libreadline.so.8.0
/usr/include/readline/chardefs.h
/usr/include/readline/history.h
/usr/include/readline/keymaps.h
/usr/include/readline/readline.h
/usr/include/readline/rlconf.h
/usr/include/readline/rlstdc.h
/usr/include/readline/rltypedefs.h
/usr/include/readline/tilde.h
/usr/lib/libhistory.so
/usr/lib/libreadline.so
/usr/lib/pkgconfig/readline.pc
/usr/share/doc/readline-%{version}/CHANGES
/usr/share/doc/readline-%{version}/INSTALL
/usr/share/doc/readline-%{version}/README
/usr/share/info/history.info.gz
/usr/share/info/readline.info.gz
/usr/share/info/rluserman.info.gz
/usr/share/man/man3/history.3.gz
/usr/share/man/man3/readline.3.gz

%changelog
