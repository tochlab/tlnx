Name:           binutils
Version:	2.41
Release:        1%{?dist}
Summary:	The GNU Binutils are a collection of binary tools.

License:	GPL
URL:		https://www.gnu.org/software/binutils/
Source0:	https://ftpmirror.gnu.org/gnu/binutils/binutils-%{version}.tar.gz

%description

%prep
%setup -q

%build
mkdir -v build
cd       build
../configure --prefix=/usr --enable-gold --enable-ld=default --enable-plugins --enable-shared --disable-werror --enable-64-bit-bfd --with-system-zlib --disable-nls

make %{?_smp_mflags} tooldir=/usr

%install
rm -rf $RPM_BUILD_ROOT
cd build
make DESTDIR=%{buildroot} install
rm -rf $RPM_BUILD_ROOT/usr/share/info/dir
find %{buildroot} -type f -name '*.la' -delete || die

%files
/usr/bin/addr2line
/usr/bin/ar
/usr/bin/as
/usr/bin/c++filt
/usr/bin/dwp
/usr/bin/elfedit
/usr/bin/gprof
/usr/bin/ld
/usr/bin/ld.bfd
/usr/bin/ld.gold
/usr/bin/nm
/usr/bin/objcopy
/usr/bin/objdump
/usr/bin/ranlib
/usr/bin/readelf
/usr/bin/size
/usr/bin/strings
/usr/bin/strip
/usr/include/ansidecl.h
/usr/include/bfd.h
/usr/include/bfdlink.h
/usr/include/ctf-api.h
/usr/include/ctf.h
/usr/include/diagnostics.h
/usr/include/dis-asm.h
/usr/include/plugin-api.h
/usr/include/symcat.h
/usr/lib/libbfd-%{version}.so
/usr/lib/libbfd.a
#/usr/lib/libbfd.la
/usr/lib/libbfd.so
/usr/lib/libctf-nobfd.a
#/usr/lib/libctf-nobfd.la
/usr/lib/libctf-nobfd.so
/usr/lib/libctf-nobfd.so.0
/usr/lib/libctf-nobfd.so.0.0.0
/usr/lib/libctf.a
#/usr/lib/libctf.la
/usr/lib/libctf.so
/usr/lib/libctf.so.0
/usr/lib/libctf.so.0.0.0
/usr/lib/libopcodes-%{version}.so
/usr/lib/libopcodes.a
#/usr/lib/libopcodes.la
/usr/lib/libopcodes.so
/usr/share/info/as.info.gz
/usr/share/info/bfd.info.gz
/usr/share/info/binutils.info.gz
/usr/share/info/gprof.info.gz
/usr/share/info/ld.info.gz
/usr/share/man/man1/addr2line.1.gz
/usr/share/man/man1/ar.1.gz
/usr/share/man/man1/as.1.gz
/usr/share/man/man1/c++filt.1.gz
/usr/share/man/man1/dlltool.1.gz
/usr/share/man/man1/elfedit.1.gz
/usr/share/man/man1/gprof.1.gz
/usr/share/man/man1/ld.1.gz
/usr/share/man/man1/nm.1.gz
/usr/share/man/man1/objcopy.1.gz
/usr/share/man/man1/objdump.1.gz
/usr/share/man/man1/ranlib.1.gz
/usr/share/man/man1/readelf.1.gz
/usr/share/man/man1/size.1.gz
/usr/share/man/man1/strings.1.gz
/usr/share/man/man1/strip.1.gz
/usr/share/man/man1/windmc.1.gz
/usr/share/man/man1/windres.1.gz
/usr/x86_64-pc-linux-gnu/bin/ar
/usr/x86_64-pc-linux-gnu/bin/as
/usr/x86_64-pc-linux-gnu/bin/ld
/usr/x86_64-pc-linux-gnu/bin/ld.bfd
/usr/x86_64-pc-linux-gnu/bin/ld.gold
/usr/x86_64-pc-linux-gnu/bin/nm
/usr/x86_64-pc-linux-gnu/bin/objcopy
/usr/x86_64-pc-linux-gnu/bin/objdump
/usr/x86_64-pc-linux-gnu/bin/ranlib
/usr/x86_64-pc-linux-gnu/bin/readelf
/usr/x86_64-pc-linux-gnu/bin/strip
/usr/x86_64-pc-linux-gnu/lib/ldscripts/elf32_x86_64.x
/usr/x86_64-pc-linux-gnu/lib/ldscripts/elf32_x86_64.xbn
/usr/x86_64-pc-linux-gnu/lib/ldscripts/elf32_x86_64.xc
/usr/x86_64-pc-linux-gnu/lib/ldscripts/elf32_x86_64.xce
/usr/x86_64-pc-linux-gnu/lib/ldscripts/elf32_x86_64.xd
/usr/x86_64-pc-linux-gnu/lib/ldscripts/elf32_x86_64.xdc
/usr/x86_64-pc-linux-gnu/lib/ldscripts/elf32_x86_64.xdce
/usr/x86_64-pc-linux-gnu/lib/ldscripts/elf32_x86_64.xde
/usr/x86_64-pc-linux-gnu/lib/ldscripts/elf32_x86_64.xdw
/usr/x86_64-pc-linux-gnu/lib/ldscripts/elf32_x86_64.xdwe
/usr/x86_64-pc-linux-gnu/lib/ldscripts/elf32_x86_64.xe
/usr/x86_64-pc-linux-gnu/lib/ldscripts/elf32_x86_64.xn
/usr/x86_64-pc-linux-gnu/lib/ldscripts/elf32_x86_64.xr
/usr/x86_64-pc-linux-gnu/lib/ldscripts/elf32_x86_64.xs
/usr/x86_64-pc-linux-gnu/lib/ldscripts/elf32_x86_64.xsc
/usr/x86_64-pc-linux-gnu/lib/ldscripts/elf32_x86_64.xsce
/usr/x86_64-pc-linux-gnu/lib/ldscripts/elf32_x86_64.xse
/usr/x86_64-pc-linux-gnu/lib/ldscripts/elf32_x86_64.xsw
/usr/x86_64-pc-linux-gnu/lib/ldscripts/elf32_x86_64.xswe
/usr/x86_64-pc-linux-gnu/lib/ldscripts/elf32_x86_64.xu
/usr/x86_64-pc-linux-gnu/lib/ldscripts/elf32_x86_64.xw
/usr/x86_64-pc-linux-gnu/lib/ldscripts/elf32_x86_64.xwe
/usr/x86_64-pc-linux-gnu/lib/ldscripts/elf_i386.x
/usr/x86_64-pc-linux-gnu/lib/ldscripts/elf_i386.xbn
/usr/x86_64-pc-linux-gnu/lib/ldscripts/elf_i386.xc
/usr/x86_64-pc-linux-gnu/lib/ldscripts/elf_i386.xce
/usr/x86_64-pc-linux-gnu/lib/ldscripts/elf_i386.xd
/usr/x86_64-pc-linux-gnu/lib/ldscripts/elf_i386.xdc
/usr/x86_64-pc-linux-gnu/lib/ldscripts/elf_i386.xdce
/usr/x86_64-pc-linux-gnu/lib/ldscripts/elf_i386.xde
/usr/x86_64-pc-linux-gnu/lib/ldscripts/elf_i386.xdw
/usr/x86_64-pc-linux-gnu/lib/ldscripts/elf_i386.xdwe
/usr/x86_64-pc-linux-gnu/lib/ldscripts/elf_i386.xe
/usr/x86_64-pc-linux-gnu/lib/ldscripts/elf_i386.xn
/usr/x86_64-pc-linux-gnu/lib/ldscripts/elf_i386.xr
/usr/x86_64-pc-linux-gnu/lib/ldscripts/elf_i386.xs
/usr/x86_64-pc-linux-gnu/lib/ldscripts/elf_i386.xsc
/usr/x86_64-pc-linux-gnu/lib/ldscripts/elf_i386.xsce
/usr/x86_64-pc-linux-gnu/lib/ldscripts/elf_i386.xse
/usr/x86_64-pc-linux-gnu/lib/ldscripts/elf_i386.xsw
/usr/x86_64-pc-linux-gnu/lib/ldscripts/elf_i386.xswe
/usr/x86_64-pc-linux-gnu/lib/ldscripts/elf_i386.xu
/usr/x86_64-pc-linux-gnu/lib/ldscripts/elf_i386.xw
/usr/x86_64-pc-linux-gnu/lib/ldscripts/elf_i386.xwe
/usr/x86_64-pc-linux-gnu/lib/ldscripts/elf_iamcu.x
/usr/x86_64-pc-linux-gnu/lib/ldscripts/elf_iamcu.xbn
/usr/x86_64-pc-linux-gnu/lib/ldscripts/elf_iamcu.xc
/usr/x86_64-pc-linux-gnu/lib/ldscripts/elf_iamcu.xce
/usr/x86_64-pc-linux-gnu/lib/ldscripts/elf_iamcu.xd
/usr/x86_64-pc-linux-gnu/lib/ldscripts/elf_iamcu.xdc
/usr/x86_64-pc-linux-gnu/lib/ldscripts/elf_iamcu.xdce
/usr/x86_64-pc-linux-gnu/lib/ldscripts/elf_iamcu.xde
/usr/x86_64-pc-linux-gnu/lib/ldscripts/elf_iamcu.xdw
/usr/x86_64-pc-linux-gnu/lib/ldscripts/elf_iamcu.xdwe
/usr/x86_64-pc-linux-gnu/lib/ldscripts/elf_iamcu.xe
/usr/x86_64-pc-linux-gnu/lib/ldscripts/elf_iamcu.xn
/usr/x86_64-pc-linux-gnu/lib/ldscripts/elf_iamcu.xr
/usr/x86_64-pc-linux-gnu/lib/ldscripts/elf_iamcu.xs
/usr/x86_64-pc-linux-gnu/lib/ldscripts/elf_iamcu.xsc
/usr/x86_64-pc-linux-gnu/lib/ldscripts/elf_iamcu.xsce
/usr/x86_64-pc-linux-gnu/lib/ldscripts/elf_iamcu.xse
/usr/x86_64-pc-linux-gnu/lib/ldscripts/elf_iamcu.xsw
/usr/x86_64-pc-linux-gnu/lib/ldscripts/elf_iamcu.xswe
/usr/x86_64-pc-linux-gnu/lib/ldscripts/elf_iamcu.xu
/usr/x86_64-pc-linux-gnu/lib/ldscripts/elf_iamcu.xw
/usr/x86_64-pc-linux-gnu/lib/ldscripts/elf_iamcu.xwe
/usr/x86_64-pc-linux-gnu/lib/ldscripts/elf_x86_64.x
/usr/x86_64-pc-linux-gnu/lib/ldscripts/elf_x86_64.xbn
/usr/x86_64-pc-linux-gnu/lib/ldscripts/elf_x86_64.xc
/usr/x86_64-pc-linux-gnu/lib/ldscripts/elf_x86_64.xce
/usr/x86_64-pc-linux-gnu/lib/ldscripts/elf_x86_64.xd
/usr/x86_64-pc-linux-gnu/lib/ldscripts/elf_x86_64.xdc
/usr/x86_64-pc-linux-gnu/lib/ldscripts/elf_x86_64.xdce
/usr/x86_64-pc-linux-gnu/lib/ldscripts/elf_x86_64.xde
/usr/x86_64-pc-linux-gnu/lib/ldscripts/elf_x86_64.xdw
/usr/x86_64-pc-linux-gnu/lib/ldscripts/elf_x86_64.xdwe
/usr/x86_64-pc-linux-gnu/lib/ldscripts/elf_x86_64.xe
/usr/x86_64-pc-linux-gnu/lib/ldscripts/elf_x86_64.xn
/usr/x86_64-pc-linux-gnu/lib/ldscripts/elf_x86_64.xr
/usr/x86_64-pc-linux-gnu/lib/ldscripts/elf_x86_64.xs
/usr/x86_64-pc-linux-gnu/lib/ldscripts/elf_x86_64.xsc
/usr/x86_64-pc-linux-gnu/lib/ldscripts/elf_x86_64.xsce
/usr/x86_64-pc-linux-gnu/lib/ldscripts/elf_x86_64.xse
/usr/x86_64-pc-linux-gnu/lib/ldscripts/elf_x86_64.xsw
/usr/x86_64-pc-linux-gnu/lib/ldscripts/elf_x86_64.xswe
/usr/x86_64-pc-linux-gnu/lib/ldscripts/elf_x86_64.xu
/usr/x86_64-pc-linux-gnu/lib/ldscripts/elf_x86_64.xw
/usr/x86_64-pc-linux-gnu/lib/ldscripts/elf_x86_64.xwe
/usr/lib/bfd-plugins/libdep.so
/usr/share/info/ctf-spec.info.gz
/usr/bin/gp-archive
/usr/bin/gp-collect-app
/usr/bin/gp-display-html
/usr/bin/gp-display-src
/usr/bin/gp-display-text
/usr/bin/gprofng
/usr/etc/gprofng.rc
/usr/include/collectorAPI.h
/usr/include/libcollector.h
/usr/include/libfcollector.h
/usr/include/sframe-api.h
/usr/include/sframe.h
/usr/lib/gprofng/libgp-collector.so
/usr/lib/gprofng/libgp-collectorAPI.a
/usr/lib/gprofng/libgp-collectorAPI.so
/usr/lib/gprofng/libgp-heap.so
/usr/lib/gprofng/libgp-iotrace.so
/usr/lib/gprofng/libgp-sync.so
/usr/lib/libgprofng.a
/usr/lib/libgprofng.so
/usr/lib/libgprofng.so.0
/usr/lib/libgprofng.so.0.0.0
/usr/lib/libsframe.a
/usr/lib/libsframe.so
/usr/lib/libsframe.so.1
/usr/lib/libsframe.so.1.0.0
/usr/share/info/gprofng.info.gz
/usr/share/info/ldint.info.gz
/usr/share/info/sframe-spec.info.gz
/usr/share/man/man1/gp-archive.1.gz
/usr/share/man/man1/gp-collect-app.1.gz
/usr/share/man/man1/gp-display-html.1.gz
/usr/share/man/man1/gp-display-src.1.gz
/usr/share/man/man1/gp-display-text.1.gz
/usr/share/man/man1/gprofng.1.gz

%changelog
