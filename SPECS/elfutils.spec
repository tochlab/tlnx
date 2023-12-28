Name:           elfutils
Version:        0.186
Release:        1%{?dist}
Summary:	Libraries/utilities to handle ELF objects (drop in replacement for libelf)

License:	GPL LGPL
URL:		http://elfutils.org/
Source0:	https://sourceware.org/elfutils/ftp/%{version}/elfutils-%{version}.tar.bz2

#BuildRequires:
#Requires:

%description

%prep
%setup -q

%build
./configure --prefix=/usr --disable-libdebuginfod --disable-debuginfod --with-pkg-config-libdir=/usr/lib/pkgconfig --disable-nls
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
%make_install

%files
/usr/bin/eu-addr2line
/usr/bin/eu-ar
/usr/bin/eu-elfclassify
/usr/bin/eu-elfcmp
/usr/bin/eu-elfcompress
/usr/bin/eu-elflint
/usr/bin/eu-findtextrel
/usr/bin/eu-make-debug-archive
/usr/bin/eu-nm
/usr/bin/eu-objdump
/usr/bin/eu-ranlib
/usr/bin/eu-readelf
/usr/bin/eu-size
/usr/bin/eu-stack
/usr/bin/eu-strings
/usr/bin/eu-strip
/usr/bin/eu-unstrip
/usr/include/dwarf.h
/usr/include/elfutils/elf-knowledge.h
/usr/include/elfutils/known-dwarf.h
/usr/include/elfutils/libasm.h
/usr/include/elfutils/libdw.h
/usr/include/elfutils/libdwelf.h
/usr/include/elfutils/libdwfl.h
/usr/include/elfutils/version.h
/usr/include/gelf.h
/usr/include/libelf.h
/usr/include/nlist.h
/usr/lib/libasm-0.186.so
/usr/lib/libasm.a
/usr/lib/libasm.so
/usr/lib/libasm.so.1
/usr/lib/libdw-0.186.so
/usr/lib/libdw.a
/usr/lib/libdw.so
/usr/lib/libdw.so.1
/usr/lib/libelf-0.186.so
/usr/lib/libelf.a
/usr/lib/libelf.so
/usr/lib/libelf.so.1
/usr/lib/pkgconfig/libdw.pc
/usr/lib/pkgconfig/libelf.pc
/usr/share/man/man1/eu-elfclassify.1.gz
/usr/share/man/man1/eu-readelf.1.gz
/usr/share/man/man3/elf_begin.3.gz
/usr/share/man/man3/elf_clone.3.gz
/usr/share/man/man3/elf_getdata.3.gz
/usr/share/man/man3/elf_update.3.gz

%changelog
