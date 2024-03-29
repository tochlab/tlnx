Name:           xz
Version:	5.4.5
Release:        1%{?dist}
Summary:	XZ utils

License:	public-domain LGPL-2.1+ GPL-2+
URL:		https://tukaani.org/xz/
Source0:	https://tukaani.org/xz/xz-%{version}.tar.gz

#BuildRequires:
#Requires:

%description
XZ utils

%prep
%setup -q

%build
%configure --prefix=/usr    \
	    --libdir=/usr/lib \
            --disable-static \
            --docdir=/usr/share/doc/xz \
            --with-pkg-config-libdir=/usr/lib/pkgconfig \
	    --disable-nls

make %{?_smp_mflags}
#make check

%install
rm -rf $RPM_BUILD_ROOT
%make_install
find %{buildroot} -type f -name '*.la' -delete || die
rm -fr %{buildroot}/usr/share/doc/xz/api

%files
/usr/bin/lzcat
/usr/bin/lzcmp
/usr/bin/lzdiff
/usr/bin/lzegrep
/usr/bin/lzfgrep
/usr/bin/lzgrep
/usr/bin/lzless
/usr/bin/lzma
/usr/bin/lzmadec
/usr/bin/lzmainfo
/usr/bin/lzmore
/usr/bin/unlzma
/usr/bin/unxz
/usr/bin/xz
/usr/bin/xzcat
/usr/bin/xzcmp
/usr/bin/xzdec
/usr/bin/xzdiff
/usr/bin/xzegrep
/usr/bin/xzfgrep
/usr/bin/xzgrep
/usr/bin/xzless
/usr/bin/xzmore
/usr/include/lzma.h
/usr/include/lzma/base.h
/usr/include/lzma/bcj.h
/usr/include/lzma/block.h
/usr/include/lzma/check.h
/usr/include/lzma/container.h
/usr/include/lzma/delta.h
/usr/include/lzma/filter.h
/usr/include/lzma/hardware.h
/usr/include/lzma/index.h
/usr/include/lzma/index_hash.h
/usr/include/lzma/lzma12.h
/usr/include/lzma/stream_flags.h
/usr/include/lzma/version.h
/usr/include/lzma/vli.h
/usr/lib/liblzma.so
/usr/lib/liblzma.so.5
/usr/lib/liblzma.so.%{version}
/usr/lib/pkgconfig/liblzma.pc
/usr/share/doc/xz/AUTHORS
/usr/share/doc/xz/COPYING
/usr/share/doc/xz/COPYING.GPLv2
/usr/share/doc/xz/NEWS
/usr/share/doc/xz/README
/usr/share/doc/xz/THANKS
/usr/share/doc/xz/TODO
/usr/share/doc/xz/examples/00_README.txt
/usr/share/doc/xz/examples/01_compress_easy.c
/usr/share/doc/xz/examples/02_decompress.c
/usr/share/doc/xz/examples/03_compress_custom.c
/usr/share/doc/xz/examples/04_compress_easy_mt.c
/usr/share/doc/xz/examples/Makefile
/usr/share/doc/xz/examples_old/xz_pipe_comp.c
/usr/share/doc/xz/examples_old/xz_pipe_decomp.c
/usr/share/doc/xz/faq.txt
/usr/share/doc/xz/history.txt
/usr/share/doc/xz/lzma-file-format.txt
/usr/share/doc/xz/xz-file-format.txt
/usr/share/man/man1/lzcat.1.gz
/usr/share/man/man1/lzcmp.1.gz
/usr/share/man/man1/lzdiff.1.gz
/usr/share/man/man1/lzegrep.1.gz
/usr/share/man/man1/lzfgrep.1.gz
/usr/share/man/man1/lzgrep.1.gz
/usr/share/man/man1/lzless.1.gz
/usr/share/man/man1/lzma.1.gz
/usr/share/man/man1/lzmadec.1.gz
/usr/share/man/man1/lzmainfo.1.gz
/usr/share/man/man1/lzmore.1.gz
/usr/share/man/man1/unlzma.1.gz
/usr/share/man/man1/unxz.1.gz
/usr/share/man/man1/xz.1.gz
/usr/share/man/man1/xzcat.1.gz
/usr/share/man/man1/xzcmp.1.gz
/usr/share/man/man1/xzdec.1.gz
/usr/share/man/man1/xzdiff.1.gz
/usr/share/man/man1/xzegrep.1.gz
/usr/share/man/man1/xzfgrep.1.gz
/usr/share/man/man1/xzgrep.1.gz
/usr/share/man/man1/xzless.1.gz
/usr/share/man/man1/xzmore.1.gz


%changelog
