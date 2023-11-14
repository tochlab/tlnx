Name:           rpm
Version:	4.19.0
Release:        1%{?dist}
Summary:	Red Hat Package Management Utils

License:	GPL-2 LGPL-2
URL:		https://rpm.org
Source0:	http://ftp.rpm.org/releases/rpm-4.19.x/rpm-%{version}.tar.bz2

#BuildRequires:
#Requires:

%description

%prep
%setup -q

%build
mkdir rpm-build
cd rpm-build
cmake .. -DWITH_AUDIT=OFF -DWITH_DBUS=OFF -DWITH_SELINUX=OFF -DWITH_INTERNAL_OPENPGP=ON -DCMAKE_INSTALL_PREFIX:PATH=/usr -DCMAKE_INSTALL_LIBDIR:PATH=/usr/lib
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
cd rpm-build
%make_install
mkdir %{buildroot}/root
cp %{_sourcedir}/rpmmacros %{buildroot}/root/.rpmmacros
cp %{_sourcedir}/rpmrc %{buildroot}/root/.rpmrc
find %{buildroot} -type f -name '*.la' -delete || die


%files
/root/.rpmmacros
/root/.rpmrc
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
/usr/include/rpm/rpmver.h
/usr/lib/librpm.so
/usr/lib/librpm.so.10
/usr/lib/librpm.so.10.0.0
/usr/lib/librpmbuild.so
/usr/lib/librpmbuild.so.10
/usr/lib/librpmbuild.so.10.0.0
/usr/lib/librpmio.so
/usr/lib/librpmio.so.10
/usr/lib/librpmio.so.10.0.0
/usr/lib/librpmsign.so
/usr/lib/librpmsign.so.10
/usr/lib/librpmsign.so.10.0.0
/usr/lib/pkgconfig/rpm.pc
/usr/lib/rpm-plugins/prioreset.so
/usr/lib/rpm-plugins/syslog.so
/usr/lib/rpm/brp-compress
/usr/lib/rpm/brp-strip
/usr/lib/rpm/brp-strip-comment-note
/usr/lib/rpm/brp-strip-static-archive
/usr/lib/rpm/check-buildroot
/usr/lib/rpm/check-files
/usr/lib/rpm/check-prereqs
/usr/lib/rpm/check-rpaths
/usr/lib/rpm/check-rpaths-worker
/usr/lib/rpm/elfdeps
/usr/lib/rpm/fileattrs/debuginfo.attr
/usr/lib/rpm/fileattrs/desktop.attr
/usr/lib/rpm/fileattrs/elf.attr
/usr/lib/rpm/fileattrs/font.attr
/usr/lib/rpm/fileattrs/metainfo.attr
/usr/lib/rpm/fileattrs/ocaml.attr
/usr/lib/rpm/fileattrs/perl.attr
/usr/lib/rpm/fileattrs/perllib.attr
/usr/lib/rpm/fileattrs/pkgconfig.attr
/usr/lib/rpm/fileattrs/script.attr
/usr/lib/rpm/find-lang.sh
/usr/lib/rpm/find-provides
/usr/lib/rpm/find-requires
/usr/lib/rpm/fontconfig.prov
/usr/lib/rpm/macros
/usr/lib/rpm/ocamldeps.sh
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
/usr/lib/rpm/platform/armv8hl-linux/macros
/usr/lib/rpm/platform/armv8l-linux/macros
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
/usr/lib/rpm/rpm.daily
/usr/lib/rpm/rpm.log
/usr/lib/rpm/rpm.supp
/usr/lib/rpm/rpm2cpio.sh
/usr/lib/rpm/rpmdb_dump
/usr/lib/rpm/rpmdb_load
/usr/lib/rpm/rpmdeps
/usr/lib/rpm/rpmpopt-4.19.0
/usr/lib/rpm/rpmrc
/usr/lib/rpm/script.req
/usr/lib/rpm/tgpg
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
/usr/share/man/man1/gendiff.1.gz
/usr/share/man/man8/rpm-misc.8.gz
/usr/share/man/man8/rpm-plugin-prioreset.8.gz
/usr/share/man/man8/rpm-plugin-syslog.8.gz
/usr/share/man/man8/rpm-plugins.8.gz
/usr/share/man/man8/rpm.8.gz
/usr/share/man/man8/rpm2archive.8.gz
/usr/share/man/man8/rpm2cpio.8.gz
/usr/share/man/man8/rpmbuild.8.gz
/usr/share/man/man8/rpmdb.8.gz
/usr/share/man/man8/rpmdeps.8.gz
/usr/share/man/man8/rpmgraph.8.gz
/usr/share/man/man8/rpmkeys.8.gz
/usr/share/man/man8/rpmsign.8.gz
/usr/share/man/man8/rpmspec.8.gz
/usr/lib/rpm/brp-elfperms
/usr/lib/rpm/brp-remove-la-files
/usr/share/locale/gu/LC_MESSAGES/rpm.mo
/usr/share/locale/he/LC_MESSAGES/rpm.mo
/usr/share/locale/pa/LC_MESSAGES/rpm.mo
/usr/share/locale/si/LC_MESSAGES/rpm.mo


