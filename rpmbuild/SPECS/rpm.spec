Name:           rpm
Version:	4.14.3
Release:        1%{?dist}
Summary:	Red Hat Package Management Utils

License:	GPL-2 LGPL-2
URL:		https://rpm.org
Source0:	http://ftp.rpm.org/releases/rpm-4.14.x/rpm-%{version}.tar.bz2	

#BuildRequires:
#Requires:

%description

%prep
%setup -q

%build
%configure --without-lua
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
%make_install

%files
/usr/bin/gendiff
/usr/bin/rpm
/usr/bin/rpm2archive
/usr/bin/rpm2cpio
/usr/bin/rpmbuild
/usr/bin/rpmdb
/usr/bin/rpmgraph
/usr/bin/rpmkeys
/usr/bin/rpmquery
/usr/bin/rpmsign
/usr/bin/rpmspec
/usr/bin/rpmverify
/usr/include/rpm/argv.h
/usr/include/rpm/header.h
/usr/include/rpm/rpmarchive.h
/usr/include/rpm/rpmbase64.h
/usr/include/rpm/rpmbuild.h
/usr/include/rpm/rpmcallback.h
/usr/include/rpm/rpmcli.h
/usr/include/rpm/rpmdb.h
/usr/include/rpm/rpmds.h
/usr/include/rpm/rpmfc.h
/usr/include/rpm/rpmfi.h
/usr/include/rpm/rpmfiles.h
/usr/include/rpm/rpmfileutil.h
/usr/include/rpm/rpmio.h
/usr/include/rpm/rpmkeyring.h
/usr/include/rpm/rpmlib.h
/usr/include/rpm/rpmlog.h
/usr/include/rpm/rpmmacro.h
/usr/include/rpm/rpmpgp.h
/usr/include/rpm/rpmpol.h
/usr/include/rpm/rpmprob.h
/usr/include/rpm/rpmps.h
/usr/include/rpm/rpmsign.h
/usr/include/rpm/rpmspec.h
/usr/include/rpm/rpmsq.h
/usr/include/rpm/rpmstring.h
/usr/include/rpm/rpmstrpool.h
/usr/include/rpm/rpmsw.h
/usr/include/rpm/rpmtag.h
/usr/include/rpm/rpmtd.h
/usr/include/rpm/rpmte.h
/usr/include/rpm/rpmts.h
/usr/include/rpm/rpmtypes.h
/usr/include/rpm/rpmurl.h
/usr/include/rpm/rpmutil.h
/usr/include/rpm/rpmvf.h
/usr/lib/rpm/brp-compress
/usr/lib/rpm/brp-java-gcjcompile
/usr/lib/rpm/brp-python-bytecompile
/usr/lib/rpm/brp-python-hardlink
/usr/lib/rpm/brp-strip
/usr/lib/rpm/brp-strip-comment-note
/usr/lib/rpm/brp-strip-shared
/usr/lib/rpm/brp-strip-static-archive
/usr/lib/rpm/check-buildroot
/usr/lib/rpm/check-files
/usr/lib/rpm/check-prereqs
/usr/lib/rpm/check-rpaths
/usr/lib/rpm/check-rpaths-worker
/usr/lib/rpm/config.guess
/usr/lib/rpm/config.sub
/usr/lib/rpm/debugedit
/usr/lib/rpm/debuginfo.prov
/usr/lib/rpm/desktop-file.prov
/usr/lib/rpm/elfdeps
/usr/lib/rpm/fileattrs/debuginfo.attr
/usr/lib/rpm/fileattrs/desktop.attr
/usr/lib/rpm/fileattrs/elf.attr
/usr/lib/rpm/fileattrs/font.attr
/usr/lib/rpm/fileattrs/libtool.attr
/usr/lib/rpm/fileattrs/metainfo.attr
/usr/lib/rpm/fileattrs/mono.attr
/usr/lib/rpm/fileattrs/ocaml.attr
/usr/lib/rpm/fileattrs/perl.attr
/usr/lib/rpm/fileattrs/perllib.attr
/usr/lib/rpm/fileattrs/pkgconfig.attr
/usr/lib/rpm/fileattrs/python.attr
/usr/lib/rpm/fileattrs/script.attr
/usr/lib/rpm/find-debuginfo.sh
/usr/lib/rpm/find-lang.sh
/usr/lib/rpm/find-provides
/usr/lib/rpm/find-requires
/usr/lib/rpm/fontconfig.prov
/usr/lib/rpm/libtooldeps.sh
/usr/lib/rpm/macros
/usr/lib/rpm/macros.perl
/usr/lib/rpm/macros.php
/usr/lib/rpm/macros.python
/usr/lib/rpm/metainfo.prov
/usr/lib/rpm/mkinstalldirs
/usr/lib/rpm/mono-find-provides
/usr/lib/rpm/mono-find-requires
/usr/lib/rpm/ocaml-find-provides.sh
/usr/lib/rpm/ocaml-find-requires.sh
/usr/lib/rpm/perl.prov
/usr/lib/rpm/perl.req
/usr/lib/rpm/pkgconfigdeps.sh
/usr/lib/rpm/platform/aarch64-linux/macros
/usr/lib/rpm/platform/alpha-linux/macros
/usr/lib/rpm/platform/alphaev5-linux/macros
/usr/lib/rpm/platform/alphaev56-linux/macros
/usr/lib/rpm/platform/alphaev6-linux/macros
/usr/lib/rpm/platform/alphaev67-linux/macros
/usr/lib/rpm/platform/alphapca56-linux/macros
/usr/lib/rpm/platform/amd64-linux/macros
/usr/lib/rpm/platform/armv3l-linux/macros
/usr/lib/rpm/platform/armv4b-linux/macros
/usr/lib/rpm/platform/armv4l-linux/macros
/usr/lib/rpm/platform/armv5tejl-linux/macros
/usr/lib/rpm/platform/armv5tel-linux/macros
/usr/lib/rpm/platform/armv5tl-linux/macros
/usr/lib/rpm/platform/armv6hl-linux/macros
/usr/lib/rpm/platform/armv6l-linux/macros
/usr/lib/rpm/platform/armv7hl-linux/macros
/usr/lib/rpm/platform/armv7hnl-linux/macros
/usr/lib/rpm/platform/armv7l-linux/macros
/usr/lib/rpm/platform/athlon-linux/macros
/usr/lib/rpm/platform/geode-linux/macros
/usr/lib/rpm/platform/i386-linux/macros
/usr/lib/rpm/platform/i486-linux/macros
/usr/lib/rpm/platform/i586-linux/macros
/usr/lib/rpm/platform/i686-linux/macros
/usr/lib/rpm/platform/ia32e-linux/macros
/usr/lib/rpm/platform/ia64-linux/macros
/usr/lib/rpm/platform/m68k-linux/macros
/usr/lib/rpm/platform/mips-linux/macros
/usr/lib/rpm/platform/mips64-linux/macros
/usr/lib/rpm/platform/mips64el-linux/macros
/usr/lib/rpm/platform/mips64r6-linux/macros
/usr/lib/rpm/platform/mips64r6el-linux/macros
/usr/lib/rpm/platform/mipsel-linux/macros
/usr/lib/rpm/platform/mipsr6-linux/macros
/usr/lib/rpm/platform/mipsr6el-linux/macros
/usr/lib/rpm/platform/noarch-linux/macros
/usr/lib/rpm/platform/pentium3-linux/macros
/usr/lib/rpm/platform/pentium4-linux/macros
/usr/lib/rpm/platform/ppc-linux/macros
/usr/lib/rpm/platform/ppc32dy4-linux/macros
/usr/lib/rpm/platform/ppc64-linux/macros
/usr/lib/rpm/platform/ppc64iseries-linux/macros
/usr/lib/rpm/platform/ppc64le-linux/macros
/usr/lib/rpm/platform/ppc64p7-linux/macros
/usr/lib/rpm/platform/ppc64pseries-linux/macros
/usr/lib/rpm/platform/ppc8260-linux/macros
/usr/lib/rpm/platform/ppc8560-linux/macros
/usr/lib/rpm/platform/ppciseries-linux/macros
/usr/lib/rpm/platform/ppcpseries-linux/macros
/usr/lib/rpm/platform/riscv64-linux/macros
/usr/lib/rpm/platform/s390-linux/macros
/usr/lib/rpm/platform/s390x-linux/macros
/usr/lib/rpm/platform/sh-linux/macros
/usr/lib/rpm/platform/sh3-linux/macros
/usr/lib/rpm/platform/sh4-linux/macros
/usr/lib/rpm/platform/sh4a-linux/macros
/usr/lib/rpm/platform/sparc-linux/macros
/usr/lib/rpm/platform/sparc64-linux/macros
/usr/lib/rpm/platform/sparc64v-linux/macros
/usr/lib/rpm/platform/sparcv8-linux/macros
/usr/lib/rpm/platform/sparcv9-linux/macros
/usr/lib/rpm/platform/sparcv9v-linux/macros
/usr/lib/rpm/platform/x86_64-linux/macros
/usr/lib/rpm/python-macro-helper
/usr/lib/rpm/pythondeps.sh
/usr/lib/rpm/pythondistdeps.py
/usr/lib/rpm/rpm.daily
/usr/lib/rpm/rpm.log
/usr/lib/rpm/rpm.supp
/usr/lib/rpm/rpm2cpio.sh
/usr/lib/rpm/rpmdb_loadcvt
/usr/lib/rpm/rpmdeps
/usr/lib/rpm/rpmpopt-4.14.3
/usr/lib/rpm/rpmrc
/usr/lib/rpm/script.req
/usr/lib/rpm/sepdebugcrcfix
/usr/lib/rpm/tgpg
/usr/lib64/librpm.la
/usr/lib64/librpm.so
/usr/lib64/librpm.so.8
/usr/lib64/librpm.so.8.2.0
/usr/lib64/librpmbuild.la
/usr/lib64/librpmbuild.so
/usr/lib64/librpmbuild.so.8
/usr/lib64/librpmbuild.so.8.2.0
/usr/lib64/librpmio.la
/usr/lib64/librpmio.so
/usr/lib64/librpmio.so.8
/usr/lib64/librpmio.so.8.2.0
/usr/lib64/librpmsign.la
/usr/lib64/librpmsign.so
/usr/lib64/librpmsign.so.8
/usr/lib64/librpmsign.so.8.2.0
/usr/lib64/pkgconfig/rpm.pc
/usr/lib64/rpm-plugins/ima.la
/usr/lib64/rpm-plugins/ima.so
/usr/lib64/rpm-plugins/prioreset.la
/usr/lib64/rpm-plugins/prioreset.so
/usr/lib64/rpm-plugins/syslog.la
/usr/lib64/rpm-plugins/syslog.so
/usr/lib64/rpm-plugins/systemd_inhibit.la
/usr/lib64/rpm-plugins/systemd_inhibit.so
/usr/share/locale/ar/LC_MESSAGES/rpm.mo
/usr/share/locale/br/LC_MESSAGES/rpm.mo
/usr/share/locale/ca/LC_MESSAGES/rpm.mo
/usr/share/locale/cmn/LC_MESSAGES/rpm.mo
/usr/share/locale/cs/LC_MESSAGES/rpm.mo
/usr/share/locale/da/LC_MESSAGES/rpm.mo
/usr/share/locale/de/LC_MESSAGES/rpm.mo
/usr/share/locale/el/LC_MESSAGES/rpm.mo
/usr/share/locale/eo/LC_MESSAGES/rpm.mo
/usr/share/locale/es/LC_MESSAGES/rpm.mo
/usr/share/locale/fi/LC_MESSAGES/rpm.mo
/usr/share/locale/fr/LC_MESSAGES/rpm.mo
/usr/share/locale/id/LC_MESSAGES/rpm.mo
/usr/share/locale/is/LC_MESSAGES/rpm.mo
/usr/share/locale/it/LC_MESSAGES/rpm.mo
/usr/share/locale/ja/LC_MESSAGES/rpm.mo
/usr/share/locale/ko/LC_MESSAGES/rpm.mo
/usr/share/locale/ms/LC_MESSAGES/rpm.mo
/usr/share/locale/nb/LC_MESSAGES/rpm.mo
/usr/share/locale/nl/LC_MESSAGES/rpm.mo
/usr/share/locale/pl/LC_MESSAGES/rpm.mo
/usr/share/locale/pt/LC_MESSAGES/rpm.mo
/usr/share/locale/pt_BR/LC_MESSAGES/rpm.mo
/usr/share/locale/ru/LC_MESSAGES/rpm.mo
/usr/share/locale/sk/LC_MESSAGES/rpm.mo
/usr/share/locale/sl/LC_MESSAGES/rpm.mo
/usr/share/locale/sr/LC_MESSAGES/rpm.mo
/usr/share/locale/sr@latin/LC_MESSAGES/rpm.mo
/usr/share/locale/sv/LC_MESSAGES/rpm.mo
/usr/share/locale/te/LC_MESSAGES/rpm.mo
/usr/share/locale/tr/LC_MESSAGES/rpm.mo
/usr/share/locale/uk/LC_MESSAGES/rpm.mo
/usr/share/locale/vi/LC_MESSAGES/rpm.mo
/usr/share/locale/zh_CN/LC_MESSAGES/rpm.mo
/usr/share/locale/zh_TW/LC_MESSAGES/rpm.mo
/usr/share/man/fr/man8/rpm.8.gz
/usr/share/man/ja/man8/rpm.8.gz
/usr/share/man/ja/man8/rpm2cpio.8.gz
/usr/share/man/ja/man8/rpmbuild.8.gz
/usr/share/man/ja/man8/rpmgraph.8.gz
/usr/share/man/ko/man8/rpm.8.gz
/usr/share/man/ko/man8/rpm2cpio.8.gz
/usr/share/man/man1/gendiff.1.gz
/usr/share/man/man8/rpm-misc.8.gz
/usr/share/man/man8/rpm-plugin-systemd-inhibit.8.gz
/usr/share/man/man8/rpm.8.gz
/usr/share/man/man8/rpm2cpio.8.gz
/usr/share/man/man8/rpmbuild.8.gz
/usr/share/man/man8/rpmdb.8.gz
/usr/share/man/man8/rpmdeps.8.gz
/usr/share/man/man8/rpmgraph.8.gz
/usr/share/man/man8/rpmkeys.8.gz
/usr/share/man/man8/rpmsign.8.gz
/usr/share/man/man8/rpmspec.8.gz
/usr/share/man/pl/man1/gendiff.1.gz
/usr/share/man/pl/man8/rpm.8.gz
/usr/share/man/pl/man8/rpm2cpio.8.gz
/usr/share/man/pl/man8/rpmbuild.8.gz
/usr/share/man/pl/man8/rpmdeps.8.gz
/usr/share/man/pl/man8/rpmgraph.8.gz
/usr/share/man/ru/man8/rpm.8.gz
/usr/share/man/ru/man8/rpm2cpio.8.gz
/usr/share/man/sk/man8/rpm.8.gz


%changelog
* Tue May 31 2016 Adam Miller <maxamillion@fedoraproject.org>
-

# see /usr/libexec/rpm/macros for macros
