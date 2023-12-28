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
cmake .. -DWITH_OPENSSL=ON -DWITH_AUDIT=OFF -DWITH_DBUS=OFF -DWITH_SELINUX=OFF -DWITH_INTERNAL_OPENPGP=ON -DCMAKE_INSTALL_PREFIX:PATH=/usr -DCMAKE_INSTALL_LIBDIR:PATH=/usr/lib
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
cd rpm-build
%make_install
mkdir %{buildroot}/root
cp %{_sourcedir}/rpmmacros %{buildroot}/root/.rpmmacros
cp %{_sourcedir}/rpmrc %{buildroot}/root/.rpmrc
find %{buildroot} -type f -name '*.la' -delete || die
rm -fr %{buildroot}/usr/share/locale


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
   /usr/bin/rpmlua
   /usr/bin/rpmsort
   /usr/include/rpm/rpmcrypto.h
   /usr/lib/cmake/rpm/rpm-config-version.cmake
   /usr/lib/cmake/rpm/rpm-config.cmake
   /usr/lib/cmake/rpm/rpm-targets-noconfig.cmake
   /usr/lib/cmake/rpm/rpm-targets.cmake
   /usr/lib/python3.11/site-packages/rpm-4.19.0-py3.11.egg-info
   /usr/lib/python3.11/site-packages/rpm/__init__.py
   /usr/lib/python3.11/site-packages/rpm/_rpm.so
   /usr/lib/python3.11/site-packages/rpm/transaction.py
   /usr/lib/rpm-plugins/fapolicyd.so
   /usr/lib/rpm/fileattrs/rpm_macro.attr
   /usr/lib/rpm/fileattrs/sysusers.attr
   /usr/lib/rpm/fileattrs/usergroup.attr
   /usr/lib/rpm/platform/loongarch64-linux/macros
   /usr/lib/rpm/platform/x86_64_v2-linux/macros
   /usr/lib/rpm/platform/x86_64_v3-linux/macros
   /usr/lib/rpm/platform/x86_64_v4-linux/macros
   /usr/lib/rpm/rpm_macros_provides.sh
   /usr/lib/rpm/rpmuncompress
   /usr/lib/rpm/sysusers.sh
   /usr/share/doc/rpm/API/Doxyheader_8h_source.html
   /usr/share/doc/rpm/API/annotated.html
   /usr/share/doc/rpm/API/argv_8h.html
   /usr/share/doc/rpm/API/argv_8h__dep__incl.map
   /usr/share/doc/rpm/API/argv_8h__dep__incl.md5
   /usr/share/doc/rpm/API/argv_8h__dep__incl.png
   /usr/share/doc/rpm/API/argv_8h__incl.map
   /usr/share/doc/rpm/API/argv_8h__incl.md5
   /usr/share/doc/rpm/API/argv_8h__incl.png
   /usr/share/doc/rpm/API/argv_8h_source.html
   /usr/share/doc/rpm/API/bc_s.png
   /usr/share/doc/rpm/API/bc_sd.png
   /usr/share/doc/rpm/API/bdwn.png
   /usr/share/doc/rpm/API/classes.html
   /usr/share/doc/rpm/API/closed.png
   /usr/share/doc/rpm/API/deprecated.html
   /usr/share/doc/rpm/API/dir_29c936d9388d655265625f80756ba99c.html
   /usr/share/doc/rpm/API/dir_29c936d9388d655265625f80756ba99c_dep.map
   /usr/share/doc/rpm/API/dir_29c936d9388d655265625f80756ba99c_dep.md5
   /usr/share/doc/rpm/API/dir_29c936d9388d655265625f80756ba99c_dep.png
   /usr/share/doc/rpm/API/dir_7253c2499f67487bf77ad55bc4b19891.html
   /usr/share/doc/rpm/API/dir_d44c64559bbebec7f509842c48db8b23.html
   /usr/share/doc/rpm/API/doc.png
   /usr/share/doc/rpm/API/docd.png
   /usr/share/doc/rpm/API/doxygen.css
   /usr/share/doc/rpm/API/doxygen.svg
   /usr/share/doc/rpm/API/dynsections.js
   /usr/share/doc/rpm/API/files.html
   /usr/share/doc/rpm/API/folderclosed.png
   /usr/share/doc/rpm/API/folderopen.png
   /usr/share/doc/rpm/API/functions.html
   /usr/share/doc/rpm/API/functions_vars.html
   /usr/share/doc/rpm/API/globals.html
   /usr/share/doc/rpm/API/globals_b.html
   /usr/share/doc/rpm/API/globals_c.html
   /usr/share/doc/rpm/API/globals_defs.html
   /usr/share/doc/rpm/API/globals_enum.html
   /usr/share/doc/rpm/API/globals_eval.html
   /usr/share/doc/rpm/API/globals_eval_c.html
   /usr/share/doc/rpm/API/globals_eval_f.html
   /usr/share/doc/rpm/API/globals_eval_i.html
   /usr/share/doc/rpm/API/globals_eval_l.html
   /usr/share/doc/rpm/API/globals_eval_p.html
   /usr/share/doc/rpm/API/globals_eval_q.html
   /usr/share/doc/rpm/API/globals_eval_r.html
   /usr/share/doc/rpm/API/globals_eval_s.html
   /usr/share/doc/rpm/API/globals_eval_t.html
   /usr/share/doc/rpm/API/globals_eval_u.html
   /usr/share/doc/rpm/API/globals_eval_v.html
   /usr/share/doc/rpm/API/globals_eval_x.html
   /usr/share/doc/rpm/API/globals_f.html
   /usr/share/doc/rpm/API/globals_func.html
   /usr/share/doc/rpm/API/globals_func_f.html
   /usr/share/doc/rpm/API/globals_func_h.html
   /usr/share/doc/rpm/API/globals_func_p.html
   /usr/share/doc/rpm/API/globals_func_r.html
   /usr/share/doc/rpm/API/globals_func_s.html
   /usr/share/doc/rpm/API/globals_func_u.html
   /usr/share/doc/rpm/API/globals_h.html
   /usr/share/doc/rpm/API/globals_i.html
   /usr/share/doc/rpm/API/globals_l.html
   /usr/share/doc/rpm/API/globals_m.html
   /usr/share/doc/rpm/API/globals_p.html
   /usr/share/doc/rpm/API/globals_q.html
   /usr/share/doc/rpm/API/globals_r.html
   /usr/share/doc/rpm/API/globals_s.html
   /usr/share/doc/rpm/API/globals_t.html
   /usr/share/doc/rpm/API/globals_type.html
   /usr/share/doc/rpm/API/globals_u.html
   /usr/share/doc/rpm/API/globals_v.html
   /usr/share/doc/rpm/API/globals_vars.html
   /usr/share/doc/rpm/API/globals_x.html
   /usr/share/doc/rpm/API/graph_legend.html
   /usr/share/doc/rpm/API/graph_legend.md5
   /usr/share/doc/rpm/API/graph_legend.png
   /usr/share/doc/rpm/API/group__buildsign.html
   /usr/share/doc/rpm/API/group__buildsign.map
   /usr/share/doc/rpm/API/group__buildsign.md5
   /usr/share/doc/rpm/API/group__buildsign.png
   /usr/share/doc/rpm/API/group__datatypes.html
   /usr/share/doc/rpm/API/group__datatypes.map
   /usr/share/doc/rpm/API/group__datatypes.md5
   /usr/share/doc/rpm/API/group__datatypes.png
   /usr/share/doc/rpm/API/group__header.html
   /usr/share/doc/rpm/API/group__header.map
   /usr/share/doc/rpm/API/group__header.md5
   /usr/share/doc/rpm/API/group__header.png
   /usr/share/doc/rpm/API/group__headquery.html
   /usr/share/doc/rpm/API/group__headquery.map
   /usr/share/doc/rpm/API/group__headquery.md5
   /usr/share/doc/rpm/API/group__headquery.png
   /usr/share/doc/rpm/API/group__install.html
   /usr/share/doc/rpm/API/group__install.map
   /usr/share/doc/rpm/API/group__install.md5
   /usr/share/doc/rpm/API/group__install.png
   /usr/share/doc/rpm/API/group__io.html
   /usr/share/doc/rpm/API/group__io.map
   /usr/share/doc/rpm/API/group__io.md5
   /usr/share/doc/rpm/API/group__io.png
   /usr/share/doc/rpm/API/group__rpmargv.html
   /usr/share/doc/rpm/API/group__rpmargv.map
   /usr/share/doc/rpm/API/group__rpmargv.md5
   /usr/share/doc/rpm/API/group__rpmargv.png
   /usr/share/doc/rpm/API/group__rpmbuild.html
   /usr/share/doc/rpm/API/group__rpmbuild.map
   /usr/share/doc/rpm/API/group__rpmbuild.md5
   /usr/share/doc/rpm/API/group__rpmbuild.png
   /usr/share/doc/rpm/API/group__rpmcallback.html
   /usr/share/doc/rpm/API/group__rpmcallback.map
   /usr/share/doc/rpm/API/group__rpmcallback.md5
   /usr/share/doc/rpm/API/group__rpmcallback.png
   /usr/share/doc/rpm/API/group__rpmcli.html
   /usr/share/doc/rpm/API/group__rpmcli.map
   /usr/share/doc/rpm/API/group__rpmcli.md5
   /usr/share/doc/rpm/API/group__rpmcli.png
   /usr/share/doc/rpm/API/group__rpmcrypto.html
   /usr/share/doc/rpm/API/group__rpmdb.html
   /usr/share/doc/rpm/API/group__rpmdb.map
   /usr/share/doc/rpm/API/group__rpmdb.md5
   /usr/share/doc/rpm/API/group__rpmdb.png
   /usr/share/doc/rpm/API/group__rpmds.html
   /usr/share/doc/rpm/API/group__rpmds.map
   /usr/share/doc/rpm/API/group__rpmds.md5
   /usr/share/doc/rpm/API/group__rpmds.png
   /usr/share/doc/rpm/API/group__rpmfc.html
   /usr/share/doc/rpm/API/group__rpmfc.map
   /usr/share/doc/rpm/API/group__rpmfc.md5
   /usr/share/doc/rpm/API/group__rpmfc.png
   /usr/share/doc/rpm/API/group__rpmfi.html
   /usr/share/doc/rpm/API/group__rpmfiles.html
   /usr/share/doc/rpm/API/group__rpmfileutil.html
   /usr/share/doc/rpm/API/group__rpmfileutil.map
   /usr/share/doc/rpm/API/group__rpmfileutil.md5
   /usr/share/doc/rpm/API/group__rpmfileutil.png
   /usr/share/doc/rpm/API/group__rpmio.html
   /usr/share/doc/rpm/API/group__rpmio.map
   /usr/share/doc/rpm/API/group__rpmio.md5
   /usr/share/doc/rpm/API/group__rpmio.png
   /usr/share/doc/rpm/API/group__rpmkeyring.html
   /usr/share/doc/rpm/API/group__rpmlog.html
   /usr/share/doc/rpm/API/group__rpmmacro.html
   /usr/share/doc/rpm/API/group__rpmpgp.html
   /usr/share/doc/rpm/API/group__rpmprob.html
   /usr/share/doc/rpm/API/group__rpmprob.map
   /usr/share/doc/rpm/API/group__rpmprob.md5
   /usr/share/doc/rpm/API/group__rpmprob.png
   /usr/share/doc/rpm/API/group__rpmps.html
   /usr/share/doc/rpm/API/group__rpmps.map
   /usr/share/doc/rpm/API/group__rpmps.md5
   /usr/share/doc/rpm/API/group__rpmps.png
   /usr/share/doc/rpm/API/group__rpmrc.html
   /usr/share/doc/rpm/API/group__rpmrc.map
   /usr/share/doc/rpm/API/group__rpmrc.md5
   /usr/share/doc/rpm/API/group__rpmrc.png
   /usr/share/doc/rpm/API/group__rpmsign.html
   /usr/share/doc/rpm/API/group__rpmsign.map
   /usr/share/doc/rpm/API/group__rpmsign.md5
   /usr/share/doc/rpm/API/group__rpmsign.png
   /usr/share/doc/rpm/API/group__rpmsq.html
   /usr/share/doc/rpm/API/group__rpmsq.map
   /usr/share/doc/rpm/API/group__rpmsq.md5
   /usr/share/doc/rpm/API/group__rpmsq.png
   /usr/share/doc/rpm/API/group__rpmstring.html
   /usr/share/doc/rpm/API/group__rpmstring.map
   /usr/share/doc/rpm/API/group__rpmstring.md5
   /usr/share/doc/rpm/API/group__rpmstring.png
   /usr/share/doc/rpm/API/group__rpmstrpool.html
   /usr/share/doc/rpm/API/group__rpmstrpool.map
   /usr/share/doc/rpm/API/group__rpmstrpool.md5
   /usr/share/doc/rpm/API/group__rpmstrpool.png
   /usr/share/doc/rpm/API/group__rpmsw.html
   /usr/share/doc/rpm/API/group__rpmsw.map
   /usr/share/doc/rpm/API/group__rpmsw.md5
   /usr/share/doc/rpm/API/group__rpmsw.png
   /usr/share/doc/rpm/API/group__rpmtag.html
   /usr/share/doc/rpm/API/group__rpmtag.map
   /usr/share/doc/rpm/API/group__rpmtag.md5
   /usr/share/doc/rpm/API/group__rpmtag.png
   /usr/share/doc/rpm/API/group__rpmtd.html
   /usr/share/doc/rpm/API/group__rpmtd.map
   /usr/share/doc/rpm/API/group__rpmtd.md5
   /usr/share/doc/rpm/API/group__rpmtd.png
   /usr/share/doc/rpm/API/group__rpmte.html
   /usr/share/doc/rpm/API/group__rpmte.map
   /usr/share/doc/rpm/API/group__rpmte.md5
   /usr/share/doc/rpm/API/group__rpmte.png
   /usr/share/doc/rpm/API/group__rpmts.html
   /usr/share/doc/rpm/API/group__rpmts.map
   /usr/share/doc/rpm/API/group__rpmts.md5
   /usr/share/doc/rpm/API/group__rpmts.png
   /usr/share/doc/rpm/API/group__rpmtypes.html
   /usr/share/doc/rpm/API/group__rpmtypes.map
   /usr/share/doc/rpm/API/group__rpmtypes.md5
   /usr/share/doc/rpm/API/group__rpmtypes.png
   /usr/share/doc/rpm/API/group__rpmurl.html
   /usr/share/doc/rpm/API/group__rpmurl.map
   /usr/share/doc/rpm/API/group__rpmurl.md5
   /usr/share/doc/rpm/API/group__rpmurl.png
   /usr/share/doc/rpm/API/group__rpmver.html
   /usr/share/doc/rpm/API/group__rpmver.map
   /usr/share/doc/rpm/API/group__rpmver.md5
   /usr/share/doc/rpm/API/group__rpmver.png
   /usr/share/doc/rpm/API/group__rpmvf.html
   /usr/share/doc/rpm/API/group__rpmvf.map
   /usr/share/doc/rpm/API/group__rpmvf.md5
   /usr/share/doc/rpm/API/group__rpmvf.png
   /usr/share/doc/rpm/API/group__signature.html
   /usr/share/doc/rpm/API/group__signature.map
   /usr/share/doc/rpm/API/group__signature.md5
   /usr/share/doc/rpm/API/group__signature.png
   /usr/share/doc/rpm/API/header_8h.html
   /usr/share/doc/rpm/API/header_8h__dep__incl.map
   /usr/share/doc/rpm/API/header_8h__dep__incl.md5
   /usr/share/doc/rpm/API/header_8h__dep__incl.png
   /usr/share/doc/rpm/API/header_8h__incl.map
   /usr/share/doc/rpm/API/header_8h__incl.md5
   /usr/share/doc/rpm/API/header_8h__incl.png
   /usr/share/doc/rpm/API/header_8h_source.html
   /usr/share/doc/rpm/API/index.html
   /usr/share/doc/rpm/API/jquery.js
   /usr/share/doc/rpm/API/menu.js
   /usr/share/doc/rpm/API/menudata.js
   /usr/share/doc/rpm/API/modules.html
   /usr/share/doc/rpm/API/nav_f.png
   /usr/share/doc/rpm/API/nav_fd.png
   /usr/share/doc/rpm/API/nav_g.png
   /usr/share/doc/rpm/API/nav_h.png
   /usr/share/doc/rpm/API/nav_hd.png
   /usr/share/doc/rpm/API/open.png
   /usr/share/doc/rpm/API/pages.html
   /usr/share/doc/rpm/API/rpmarchive_8h.html
   /usr/share/doc/rpm/API/rpmarchive_8h__dep__incl.map
   /usr/share/doc/rpm/API/rpmarchive_8h__dep__incl.md5
   /usr/share/doc/rpm/API/rpmarchive_8h__dep__incl.png
   /usr/share/doc/rpm/API/rpmarchive_8h_source.html
   /usr/share/doc/rpm/API/rpmbase64_8h.html
   /usr/share/doc/rpm/API/rpmbase64_8h__incl.map
   /usr/share/doc/rpm/API/rpmbase64_8h__incl.md5
   /usr/share/doc/rpm/API/rpmbase64_8h__incl.png
   /usr/share/doc/rpm/API/rpmbase64_8h_source.html
   /usr/share/doc/rpm/API/rpmbuild_8h.html
   /usr/share/doc/rpm/API/rpmbuild_8h__incl.map
   /usr/share/doc/rpm/API/rpmbuild_8h__incl.md5
   /usr/share/doc/rpm/API/rpmbuild_8h__incl.png
   /usr/share/doc/rpm/API/rpmbuild_8h_source.html
   /usr/share/doc/rpm/API/rpmcallback_8h.html
   /usr/share/doc/rpm/API/rpmcallback_8h__dep__incl.map
   /usr/share/doc/rpm/API/rpmcallback_8h__dep__incl.md5
   /usr/share/doc/rpm/API/rpmcallback_8h__dep__incl.png
   /usr/share/doc/rpm/API/rpmcallback_8h__incl.map
   /usr/share/doc/rpm/API/rpmcallback_8h__incl.md5
   /usr/share/doc/rpm/API/rpmcallback_8h__incl.png
   /usr/share/doc/rpm/API/rpmcallback_8h_source.html
   /usr/share/doc/rpm/API/rpmcli_8h.html
   /usr/share/doc/rpm/API/rpmcli_8h__dep__incl.map
   /usr/share/doc/rpm/API/rpmcli_8h__dep__incl.md5
   /usr/share/doc/rpm/API/rpmcli_8h__dep__incl.png
   /usr/share/doc/rpm/API/rpmcli_8h__incl.map
   /usr/share/doc/rpm/API/rpmcli_8h__incl.md5
   /usr/share/doc/rpm/API/rpmcli_8h__incl.png
   /usr/share/doc/rpm/API/rpmcli_8h_source.html
   /usr/share/doc/rpm/API/rpmcrypto_8h_source.html
   /usr/share/doc/rpm/API/rpmdb_8h.html
   /usr/share/doc/rpm/API/rpmdb_8h__incl.map
   /usr/share/doc/rpm/API/rpmdb_8h__incl.md5
   /usr/share/doc/rpm/API/rpmdb_8h__incl.png
   /usr/share/doc/rpm/API/rpmdb_8h_source.html
   /usr/share/doc/rpm/API/rpmds_8h.html
   /usr/share/doc/rpm/API/rpmds_8h__dep__incl.map
   /usr/share/doc/rpm/API/rpmds_8h__dep__incl.md5
   /usr/share/doc/rpm/API/rpmds_8h__dep__incl.png
   /usr/share/doc/rpm/API/rpmds_8h__incl.map
   /usr/share/doc/rpm/API/rpmds_8h__incl.md5
   /usr/share/doc/rpm/API/rpmds_8h__incl.png
   /usr/share/doc/rpm/API/rpmds_8h_source.html
   /usr/share/doc/rpm/API/rpmfc_8h.html
   /usr/share/doc/rpm/API/rpmfc_8h__incl.map
   /usr/share/doc/rpm/API/rpmfc_8h__incl.md5
   /usr/share/doc/rpm/API/rpmfc_8h__incl.png
   /usr/share/doc/rpm/API/rpmfc_8h_source.html
   /usr/share/doc/rpm/API/rpmfi_8h.html
   /usr/share/doc/rpm/API/rpmfi_8h__dep__incl.map
   /usr/share/doc/rpm/API/rpmfi_8h__dep__incl.md5
   /usr/share/doc/rpm/API/rpmfi_8h__dep__incl.png
   /usr/share/doc/rpm/API/rpmfi_8h__incl.map
   /usr/share/doc/rpm/API/rpmfi_8h__incl.md5
   /usr/share/doc/rpm/API/rpmfi_8h__incl.png
   /usr/share/doc/rpm/API/rpmfi_8h_source.html
   /usr/share/doc/rpm/API/rpmfiles_8h.html
   /usr/share/doc/rpm/API/rpmfiles_8h__dep__incl.map
   /usr/share/doc/rpm/API/rpmfiles_8h__dep__incl.md5
   /usr/share/doc/rpm/API/rpmfiles_8h__dep__incl.png
   /usr/share/doc/rpm/API/rpmfiles_8h__incl.map
   /usr/share/doc/rpm/API/rpmfiles_8h__incl.md5
   /usr/share/doc/rpm/API/rpmfiles_8h__incl.png
   /usr/share/doc/rpm/API/rpmfiles_8h_source.html
   /usr/share/doc/rpm/API/rpmfileutil_8h.html
   /usr/share/doc/rpm/API/rpmfileutil_8h__dep__incl.map
   /usr/share/doc/rpm/API/rpmfileutil_8h__dep__incl.md5
   /usr/share/doc/rpm/API/rpmfileutil_8h__dep__incl.png
   /usr/share/doc/rpm/API/rpmfileutil_8h__incl.map
   /usr/share/doc/rpm/API/rpmfileutil_8h__incl.md5
   /usr/share/doc/rpm/API/rpmfileutil_8h__incl.png
   /usr/share/doc/rpm/API/rpmfileutil_8h_source.html
   /usr/share/doc/rpm/API/rpmio_8h.html
   /usr/share/doc/rpm/API/rpmio_8h__dep__incl.map
   /usr/share/doc/rpm/API/rpmio_8h__dep__incl.md5
   /usr/share/doc/rpm/API/rpmio_8h__dep__incl.png
   /usr/share/doc/rpm/API/rpmio_8h__incl.map
   /usr/share/doc/rpm/API/rpmio_8h__incl.md5
   /usr/share/doc/rpm/API/rpmio_8h__incl.png
   /usr/share/doc/rpm/API/rpmio_8h_source.html
   /usr/share/doc/rpm/API/rpmkeyring_8h.html
   /usr/share/doc/rpm/API/rpmkeyring_8h__incl.map
   /usr/share/doc/rpm/API/rpmkeyring_8h__incl.md5
   /usr/share/doc/rpm/API/rpmkeyring_8h__incl.png
   /usr/share/doc/rpm/API/rpmkeyring_8h_source.html
   /usr/share/doc/rpm/API/rpmlib_8h.html
   /usr/share/doc/rpm/API/rpmlib_8h__dep__incl.map
   /usr/share/doc/rpm/API/rpmlib_8h__dep__incl.md5
   /usr/share/doc/rpm/API/rpmlib_8h__dep__incl.png
   /usr/share/doc/rpm/API/rpmlib_8h__incl.map
   /usr/share/doc/rpm/API/rpmlib_8h__incl.md5
   /usr/share/doc/rpm/API/rpmlib_8h__incl.png
   /usr/share/doc/rpm/API/rpmlib_8h_source.html
   /usr/share/doc/rpm/API/rpmlog_8h.html
   /usr/share/doc/rpm/API/rpmlog_8h__incl.map
   /usr/share/doc/rpm/API/rpmlog_8h__incl.md5
   /usr/share/doc/rpm/API/rpmlog_8h__incl.png
   /usr/share/doc/rpm/API/rpmlog_8h_source.html
   /usr/share/doc/rpm/API/rpmmacro_8h.html
   /usr/share/doc/rpm/API/rpmmacro_8h__dep__incl.map
   /usr/share/doc/rpm/API/rpmmacro_8h__dep__incl.md5
   /usr/share/doc/rpm/API/rpmmacro_8h__dep__incl.png
   /usr/share/doc/rpm/API/rpmmacro_8h__incl.map
   /usr/share/doc/rpm/API/rpmmacro_8h__incl.md5
   /usr/share/doc/rpm/API/rpmmacro_8h__incl.png
   /usr/share/doc/rpm/API/rpmmacro_8h_source.html
   /usr/share/doc/rpm/API/rpmpgp_8h.html
   /usr/share/doc/rpm/API/rpmpgp_8h__dep__incl.map
   /usr/share/doc/rpm/API/rpmpgp_8h__dep__incl.md5
   /usr/share/doc/rpm/API/rpmpgp_8h__dep__incl.png
   /usr/share/doc/rpm/API/rpmpgp_8h__incl.map
   /usr/share/doc/rpm/API/rpmpgp_8h__incl.md5
   /usr/share/doc/rpm/API/rpmpgp_8h__incl.png
   /usr/share/doc/rpm/API/rpmpgp_8h_source.html
   /usr/share/doc/rpm/API/rpmprob_8h.html
   /usr/share/doc/rpm/API/rpmprob_8h__dep__incl.map
   /usr/share/doc/rpm/API/rpmprob_8h__dep__incl.md5
   /usr/share/doc/rpm/API/rpmprob_8h__dep__incl.png
   /usr/share/doc/rpm/API/rpmprob_8h__incl.map
   /usr/share/doc/rpm/API/rpmprob_8h__incl.md5
   /usr/share/doc/rpm/API/rpmprob_8h__incl.png
   /usr/share/doc/rpm/API/rpmprob_8h_source.html
   /usr/share/doc/rpm/API/rpmps_8h.html
   /usr/share/doc/rpm/API/rpmps_8h__dep__incl.map
   /usr/share/doc/rpm/API/rpmps_8h__dep__incl.md5
   /usr/share/doc/rpm/API/rpmps_8h__dep__incl.png
   /usr/share/doc/rpm/API/rpmps_8h__incl.map
   /usr/share/doc/rpm/API/rpmps_8h__incl.md5
   /usr/share/doc/rpm/API/rpmps_8h__incl.png
   /usr/share/doc/rpm/API/rpmps_8h_source.html
   /usr/share/doc/rpm/API/rpmsign_8h.html
   /usr/share/doc/rpm/API/rpmsign_8h__incl.map
   /usr/share/doc/rpm/API/rpmsign_8h__incl.md5
   /usr/share/doc/rpm/API/rpmsign_8h__incl.png
   /usr/share/doc/rpm/API/rpmsign_8h_source.html
   /usr/share/doc/rpm/API/rpmspec_8h.html
   /usr/share/doc/rpm/API/rpmspec_8h__dep__incl.map
   /usr/share/doc/rpm/API/rpmspec_8h__dep__incl.md5
   /usr/share/doc/rpm/API/rpmspec_8h__dep__incl.png
   /usr/share/doc/rpm/API/rpmspec_8h__incl.map
   /usr/share/doc/rpm/API/rpmspec_8h__incl.md5
   /usr/share/doc/rpm/API/rpmspec_8h__incl.png
   /usr/share/doc/rpm/API/rpmspec_8h_source.html
   /usr/share/doc/rpm/API/rpmsq_8h.html
   /usr/share/doc/rpm/API/rpmsq_8h__incl.map
   /usr/share/doc/rpm/API/rpmsq_8h__incl.md5
   /usr/share/doc/rpm/API/rpmsq_8h__incl.png
   /usr/share/doc/rpm/API/rpmsq_8h_source.html
   /usr/share/doc/rpm/API/rpmstring_8h.html
   /usr/share/doc/rpm/API/rpmstring_8h__dep__incl.map
   /usr/share/doc/rpm/API/rpmstring_8h__dep__incl.md5
   /usr/share/doc/rpm/API/rpmstring_8h__dep__incl.png
   /usr/share/doc/rpm/API/rpmstring_8h__incl.map
   /usr/share/doc/rpm/API/rpmstring_8h__incl.md5
   /usr/share/doc/rpm/API/rpmstring_8h__incl.png
   /usr/share/doc/rpm/API/rpmstring_8h_source.html
   /usr/share/doc/rpm/API/rpmstrpool_8h.html
   /usr/share/doc/rpm/API/rpmstrpool_8h__incl.map
   /usr/share/doc/rpm/API/rpmstrpool_8h__incl.md5
   /usr/share/doc/rpm/API/rpmstrpool_8h__incl.png
   /usr/share/doc/rpm/API/rpmstrpool_8h_source.html
   /usr/share/doc/rpm/API/rpmsw_8h.html
   /usr/share/doc/rpm/API/rpmsw_8h__dep__incl.map
   /usr/share/doc/rpm/API/rpmsw_8h__dep__incl.md5
   /usr/share/doc/rpm/API/rpmsw_8h__dep__incl.png
   /usr/share/doc/rpm/API/rpmsw_8h__incl.map
   /usr/share/doc/rpm/API/rpmsw_8h__incl.md5
   /usr/share/doc/rpm/API/rpmsw_8h__incl.png
   /usr/share/doc/rpm/API/rpmsw_8h_source.html
   /usr/share/doc/rpm/API/rpmtag_8h.html
   /usr/share/doc/rpm/API/rpmtag_8h__dep__incl.map
   /usr/share/doc/rpm/API/rpmtag_8h__dep__incl.md5
   /usr/share/doc/rpm/API/rpmtag_8h__dep__incl.png
   /usr/share/doc/rpm/API/rpmtag_8h__incl.map
   /usr/share/doc/rpm/API/rpmtag_8h__incl.md5
   /usr/share/doc/rpm/API/rpmtag_8h__incl.png
   /usr/share/doc/rpm/API/rpmtag_8h_source.html
   /usr/share/doc/rpm/API/rpmtd_8h.html
   /usr/share/doc/rpm/API/rpmtd_8h__dep__incl.map
   /usr/share/doc/rpm/API/rpmtd_8h__dep__incl.md5
   /usr/share/doc/rpm/API/rpmtd_8h__dep__incl.png
   /usr/share/doc/rpm/API/rpmtd_8h__incl.map
   /usr/share/doc/rpm/API/rpmtd_8h__incl.md5
   /usr/share/doc/rpm/API/rpmtd_8h__incl.png
   /usr/share/doc/rpm/API/rpmtd_8h_source.html
   /usr/share/doc/rpm/API/rpmte_8h.html
   /usr/share/doc/rpm/API/rpmte_8h__dep__incl.map
   /usr/share/doc/rpm/API/rpmte_8h__dep__incl.md5
   /usr/share/doc/rpm/API/rpmte_8h__dep__incl.png
   /usr/share/doc/rpm/API/rpmte_8h__incl.map
   /usr/share/doc/rpm/API/rpmte_8h__incl.md5
   /usr/share/doc/rpm/API/rpmte_8h__incl.png
   /usr/share/doc/rpm/API/rpmte_8h_source.html
   /usr/share/doc/rpm/API/rpmts_8h.html
   /usr/share/doc/rpm/API/rpmts_8h__dep__incl.map
   /usr/share/doc/rpm/API/rpmts_8h__dep__incl.md5
   /usr/share/doc/rpm/API/rpmts_8h__dep__incl.png
   /usr/share/doc/rpm/API/rpmts_8h__incl.map
   /usr/share/doc/rpm/API/rpmts_8h__incl.md5
   /usr/share/doc/rpm/API/rpmts_8h__incl.png
   /usr/share/doc/rpm/API/rpmts_8h_source.html
   /usr/share/doc/rpm/API/rpmtypes_8h.html
   /usr/share/doc/rpm/API/rpmtypes_8h__dep__incl.map
   /usr/share/doc/rpm/API/rpmtypes_8h__dep__incl.md5
   /usr/share/doc/rpm/API/rpmtypes_8h__dep__incl.png
   /usr/share/doc/rpm/API/rpmtypes_8h__incl.map
   /usr/share/doc/rpm/API/rpmtypes_8h__incl.md5
   /usr/share/doc/rpm/API/rpmtypes_8h__incl.png
   /usr/share/doc/rpm/API/rpmtypes_8h_source.html
   /usr/share/doc/rpm/API/rpmurl_8h.html
   /usr/share/doc/rpm/API/rpmurl_8h__dep__incl.map
   /usr/share/doc/rpm/API/rpmurl_8h__dep__incl.md5
   /usr/share/doc/rpm/API/rpmurl_8h__dep__incl.png
   /usr/share/doc/rpm/API/rpmurl_8h_source.html
   /usr/share/doc/rpm/API/rpmutil_8h.html
   /usr/share/doc/rpm/API/rpmutil_8h__dep__incl.map
   /usr/share/doc/rpm/API/rpmutil_8h__dep__incl.md5
   /usr/share/doc/rpm/API/rpmutil_8h__dep__incl.png
   /usr/share/doc/rpm/API/rpmutil_8h__incl.map
   /usr/share/doc/rpm/API/rpmutil_8h__incl.md5
   /usr/share/doc/rpm/API/rpmutil_8h__incl.png
   /usr/share/doc/rpm/API/rpmutil_8h_source.html
   /usr/share/doc/rpm/API/rpmver_8h_source.html
   /usr/share/doc/rpm/API/search/all_0.js
   /usr/share/doc/rpm/API/search/all_1.js
   /usr/share/doc/rpm/API/search/all_10.js
   /usr/share/doc/rpm/API/search/all_11.js
   /usr/share/doc/rpm/API/search/all_12.js
   /usr/share/doc/rpm/API/search/all_13.js
   /usr/share/doc/rpm/API/search/all_14.js
   /usr/share/doc/rpm/API/search/all_15.js
   /usr/share/doc/rpm/API/search/all_2.js
   /usr/share/doc/rpm/API/search/all_3.js
   /usr/share/doc/rpm/API/search/all_4.js
   /usr/share/doc/rpm/API/search/all_5.js
   /usr/share/doc/rpm/API/search/all_6.js
   /usr/share/doc/rpm/API/search/all_7.js
   /usr/share/doc/rpm/API/search/all_8.js
   /usr/share/doc/rpm/API/search/all_9.js
   /usr/share/doc/rpm/API/search/all_a.js
   /usr/share/doc/rpm/API/search/all_b.js
   /usr/share/doc/rpm/API/search/all_c.js
   /usr/share/doc/rpm/API/search/all_d.js
   /usr/share/doc/rpm/API/search/all_e.js
   /usr/share/doc/rpm/API/search/all_f.js
   /usr/share/doc/rpm/API/search/classes_0.js
   /usr/share/doc/rpm/API/search/classes_1.js
   /usr/share/doc/rpm/API/search/classes_2.js
   /usr/share/doc/rpm/API/search/close.svg
   /usr/share/doc/rpm/API/search/defines_0.js
   /usr/share/doc/rpm/API/search/defines_1.js
   /usr/share/doc/rpm/API/search/enums_0.js
   /usr/share/doc/rpm/API/search/enums_1.js
   /usr/share/doc/rpm/API/search/enums_2.js
   /usr/share/doc/rpm/API/search/enums_3.js
   /usr/share/doc/rpm/API/search/enums_4.js
   /usr/share/doc/rpm/API/search/enumvalues_0.js
   /usr/share/doc/rpm/API/search/enumvalues_1.js
   /usr/share/doc/rpm/API/search/enumvalues_2.js
   /usr/share/doc/rpm/API/search/enumvalues_3.js
   /usr/share/doc/rpm/API/search/enumvalues_4.js
   /usr/share/doc/rpm/API/search/enumvalues_5.js
   /usr/share/doc/rpm/API/search/enumvalues_6.js
   /usr/share/doc/rpm/API/search/enumvalues_7.js
   /usr/share/doc/rpm/API/search/enumvalues_8.js
   /usr/share/doc/rpm/API/search/enumvalues_9.js
   /usr/share/doc/rpm/API/search/enumvalues_a.js
   /usr/share/doc/rpm/API/search/enumvalues_b.js
   /usr/share/doc/rpm/API/search/enumvalues_c.js
   /usr/share/doc/rpm/API/search/files_0.js
   /usr/share/doc/rpm/API/search/files_1.js
   /usr/share/doc/rpm/API/search/files_2.js
   /usr/share/doc/rpm/API/search/functions_0.js
   /usr/share/doc/rpm/API/search/functions_1.js
   /usr/share/doc/rpm/API/search/functions_2.js
   /usr/share/doc/rpm/API/search/functions_3.js
   /usr/share/doc/rpm/API/search/functions_4.js
   /usr/share/doc/rpm/API/search/functions_5.js
   /usr/share/doc/rpm/API/search/functions_6.js
   /usr/share/doc/rpm/API/search/groups_0.js
   /usr/share/doc/rpm/API/search/groups_1.js
   /usr/share/doc/rpm/API/search/groups_10.js
   /usr/share/doc/rpm/API/search/groups_11.js
   /usr/share/doc/rpm/API/search/groups_2.js
   /usr/share/doc/rpm/API/search/groups_3.js
   /usr/share/doc/rpm/API/search/groups_4.js
   /usr/share/doc/rpm/API/search/groups_5.js
   /usr/share/doc/rpm/API/search/groups_6.js
   /usr/share/doc/rpm/API/search/groups_7.js
   /usr/share/doc/rpm/API/search/groups_8.js
   /usr/share/doc/rpm/API/search/groups_9.js
   /usr/share/doc/rpm/API/search/groups_a.js
   /usr/share/doc/rpm/API/search/groups_b.js
   /usr/share/doc/rpm/API/search/groups_c.js
   /usr/share/doc/rpm/API/search/groups_d.js
   /usr/share/doc/rpm/API/search/groups_e.js
   /usr/share/doc/rpm/API/search/groups_f.js
   /usr/share/doc/rpm/API/search/mag.svg
   /usr/share/doc/rpm/API/search/mag_d.svg
   /usr/share/doc/rpm/API/search/mag_sel.svg
   /usr/share/doc/rpm/API/search/mag_seld.svg
   /usr/share/doc/rpm/API/search/pages_0.js
   /usr/share/doc/rpm/API/search/pages_1.js
   /usr/share/doc/rpm/API/search/pages_2.js
   /usr/share/doc/rpm/API/search/search.css
   /usr/share/doc/rpm/API/search/search.js
   /usr/share/doc/rpm/API/search/searchdata.js
   /usr/share/doc/rpm/API/search/typedefs_0.js
   /usr/share/doc/rpm/API/search/typedefs_1.js
   /usr/share/doc/rpm/API/search/typedefs_2.js
   /usr/share/doc/rpm/API/search/typedefs_3.js
   /usr/share/doc/rpm/API/search/typedefs_4.js
   /usr/share/doc/rpm/API/search/typedefs_5.js
   /usr/share/doc/rpm/API/search/variables_0.js
   /usr/share/doc/rpm/API/search/variables_1.js
   /usr/share/doc/rpm/API/search/variables_10.js
   /usr/share/doc/rpm/API/search/variables_2.js
   /usr/share/doc/rpm/API/search/variables_3.js
   /usr/share/doc/rpm/API/search/variables_4.js
   /usr/share/doc/rpm/API/search/variables_5.js
   /usr/share/doc/rpm/API/search/variables_6.js
   /usr/share/doc/rpm/API/search/variables_7.js
   /usr/share/doc/rpm/API/search/variables_8.js
   /usr/share/doc/rpm/API/search/variables_9.js
   /usr/share/doc/rpm/API/search/variables_a.js
   /usr/share/doc/rpm/API/search/variables_b.js
   /usr/share/doc/rpm/API/search/variables_c.js
   /usr/share/doc/rpm/API/search/variables_d.js
   /usr/share/doc/rpm/API/search/variables_e.js
   /usr/share/doc/rpm/API/search/variables_f.js
   /usr/share/doc/rpm/API/splitbar.png
   /usr/share/doc/rpm/API/splitbard.png
   /usr/share/doc/rpm/API/structARGI__s-members.html
   /usr/share/doc/rpm/API/structARGI__s.html
   /usr/share/doc/rpm/API/structpgpPktCdata__s-members.html
   /usr/share/doc/rpm/API/structpgpPktCdata__s.html
   /usr/share/doc/rpm/API/structpgpPktEdata__s-members.html
   /usr/share/doc/rpm/API/structpgpPktEdata__s.html
   /usr/share/doc/rpm/API/structpgpPktKeyV3__s-members.html
   /usr/share/doc/rpm/API/structpgpPktKeyV3__s.html
   /usr/share/doc/rpm/API/structpgpPktKeyV4__s-members.html
   /usr/share/doc/rpm/API/structpgpPktKeyV4__s.html
   /usr/share/doc/rpm/API/structpgpPktLdata__s-members.html
   /usr/share/doc/rpm/API/structpgpPktLdata__s.html
   /usr/share/doc/rpm/API/structpgpPktOnepass__s-members.html
   /usr/share/doc/rpm/API/structpgpPktOnepass__s.html
   /usr/share/doc/rpm/API/structpgpPktPubkey__s-members.html
   /usr/share/doc/rpm/API/structpgpPktPubkey__s.html
   /usr/share/doc/rpm/API/structpgpPktSigV3__s-members.html
   /usr/share/doc/rpm/API/structpgpPktSigV3__s.html
   /usr/share/doc/rpm/API/structpgpPktSigV4__s-members.html
   /usr/share/doc/rpm/API/structpgpPktSigV4__s.html
   /usr/share/doc/rpm/API/structpgpPktSymkey__s-members.html
   /usr/share/doc/rpm/API/structpgpPktSymkey__s.html
   /usr/share/doc/rpm/API/structpgpPktTrust__s-members.html
   /usr/share/doc/rpm/API/structpgpPktTrust__s.html
   /usr/share/doc/rpm/API/structpgpPktUid__s-members.html
   /usr/share/doc/rpm/API/structpgpPktUid__s.html
   /usr/share/doc/rpm/API/structrpmBuildArguments__s-members.html
   /usr/share/doc/rpm/API/structrpmBuildArguments__s.html
   /usr/share/doc/rpm/API/structrpmInstallArguments__s-members.html
   /usr/share/doc/rpm/API/structrpmInstallArguments__s.html
   /usr/share/doc/rpm/API/structrpmInstallArguments__s__coll__graph.map
   /usr/share/doc/rpm/API/structrpmInstallArguments__s__coll__graph.md5
   /usr/share/doc/rpm/API/structrpmInstallArguments__s__coll__graph.png
   /usr/share/doc/rpm/API/structrpmQVKArguments__s-members.html
   /usr/share/doc/rpm/API/structrpmQVKArguments__s.html
   /usr/share/doc/rpm/API/structrpmQVKArguments__s__coll__graph.map
   /usr/share/doc/rpm/API/structrpmQVKArguments__s__coll__graph.md5
   /usr/share/doc/rpm/API/structrpmQVKArguments__s__coll__graph.png
   /usr/share/doc/rpm/API/structrpmRelocation__s-members.html
   /usr/share/doc/rpm/API/structrpmRelocation__s.html
   /usr/share/doc/rpm/API/structrpmSignArgs-members.html
   /usr/share/doc/rpm/API/structrpmSignArgs.html
   /usr/share/doc/rpm/API/structrpmop__s-members.html
   /usr/share/doc/rpm/API/structrpmop__s.html
   /usr/share/doc/rpm/API/structrpmop__s__coll__graph.map
   /usr/share/doc/rpm/API/structrpmop__s__coll__graph.md5
   /usr/share/doc/rpm/API/structrpmop__s__coll__graph.png
   /usr/share/doc/rpm/API/structrpmsw__s-members.html
   /usr/share/doc/rpm/API/structrpmsw__s.html
   /usr/share/doc/rpm/API/structrpmtd__s-members.html
   /usr/share/doc/rpm/API/structrpmtd__s.html
   /usr/share/doc/rpm/API/sync_off.png
   /usr/share/doc/rpm/API/sync_on.png
   /usr/share/doc/rpm/API/tab_a.png
   /usr/share/doc/rpm/API/tab_ad.png
   /usr/share/doc/rpm/API/tab_b.png
   /usr/share/doc/rpm/API/tab_bd.png
   /usr/share/doc/rpm/API/tab_h.png
   /usr/share/doc/rpm/API/tab_hd.png
   /usr/share/doc/rpm/API/tab_s.png
   /usr/share/doc/rpm/API/tab_sd.png
   /usr/share/doc/rpm/API/tabs.css
   /usr/share/doc/rpm/API/todo.html
   /usr/share/doc/rpm/API/unionpgpPktKey__u-members.html
   /usr/share/doc/rpm/API/unionpgpPktKey__u.html
   /usr/share/doc/rpm/API/unionpgpPktKey__u__coll__graph.map
   /usr/share/doc/rpm/API/unionpgpPktKey__u__coll__graph.md5
   /usr/share/doc/rpm/API/unionpgpPktKey__u__coll__graph.png
   /usr/share/doc/rpm/API/unionpgpPktPre__u-members.html
   /usr/share/doc/rpm/API/unionpgpPktPre__u.html
   /usr/share/doc/rpm/API/unionpgpPktPre__u__coll__graph.map
   /usr/share/doc/rpm/API/unionpgpPktPre__u__coll__graph.md5
   /usr/share/doc/rpm/API/unionpgpPktPre__u__coll__graph.png
   /usr/share/doc/rpm/API/unionpgpPktSig__u-members.html
   /usr/share/doc/rpm/API/unionpgpPktSig__u.html
   /usr/share/doc/rpm/API/unionpgpPktSig__u__coll__graph.map
   /usr/share/doc/rpm/API/unionpgpPktSig__u__coll__graph.md5
   /usr/share/doc/rpm/API/unionpgpPktSig__u__coll__graph.png
   /usr/share/doc/rpm/CONTRIBUTING.md
   /usr/share/doc/rpm/COPYING
   /usr/share/doc/rpm/CREDITS
   /usr/share/doc/rpm/INSTALL
   /usr/share/doc/rpm/README
   /usr/share/doc/rpm/arch_dependencies.md
   /usr/share/doc/rpm/autosetup.md
   /usr/share/doc/rpm/boolean_dependencies.md
   /usr/share/doc/rpm/buildprocess.md
   /usr/share/doc/rpm/conditionalbuilds.md
   /usr/share/doc/rpm/dependencies.md
   /usr/share/doc/rpm/dependency_generators.md
   /usr/share/doc/rpm/devel_documentation.md
   /usr/share/doc/rpm/dynamic_specs.md
   /usr/share/doc/rpm/examples/rpmls.py
   /usr/share/doc/rpm/examples/rpmunpack.py
   /usr/share/doc/rpm/examples/srpmspec.py
   /usr/share/doc/rpm/file_triggers.md
   /usr/share/doc/rpm/format.md
   /usr/share/doc/rpm/hregions.md
   /usr/share/doc/rpm/index.md
   /usr/share/doc/rpm/large_files.md
   /usr/share/doc/rpm/lua.md
   /usr/share/doc/rpm/macros.md
   /usr/share/doc/rpm/more_dependencies.md
   /usr/share/doc/rpm/plugins.md
   /usr/share/doc/rpm/queryformat.md
   /usr/share/doc/rpm/relocatable.md
   /usr/share/doc/rpm/scriptlet_expansion.md
   /usr/share/doc/rpm/signatures_digests.md
   /usr/share/doc/rpm/spec.md
   /usr/share/doc/rpm/tags.md
   /usr/share/doc/rpm/triggers.md
   /usr/share/doc/rpm/tsort.md
   /usr/share/man/man8/rpm-plugin-fapolicyd.8.gz
   /usr/share/man/man8/rpmlua.8.gz
   /usr/share/man/man8/rpmsort.8.gz
