Name:           automake 
Version:	1.16.1
Release:        1%{?dist}
Summary:	Used to generate Makefile.in from Makefile.am

License:	GPL-2
URL:		https://www.gnu.org/software/automake/
Source0:	https://mirror.tochlab.net/pub/gnu/automake/automake-%{version}.tar.gz

#BuildRequires:
#Requires:

%description

%prep
%setup -q

%build
./configure --prefix=/usr --docdir=/usr/share/doc/automake-%{version}
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
%make_install

%files
/usr/bin/aclocal
/usr/bin/aclocal-1.16
/usr/bin/automake
/usr/bin/automake-1.16
/usr/share/aclocal-1.16/amversion.m4
/usr/share/aclocal-1.16/ar-lib.m4
/usr/share/aclocal-1.16/as.m4
/usr/share/aclocal-1.16/auxdir.m4
/usr/share/aclocal-1.16/cond-if.m4
/usr/share/aclocal-1.16/cond.m4
/usr/share/aclocal-1.16/depend.m4
/usr/share/aclocal-1.16/depout.m4
/usr/share/aclocal-1.16/dmalloc.m4
/usr/share/aclocal-1.16/extra-recurs.m4
/usr/share/aclocal-1.16/gcj.m4
/usr/share/aclocal-1.16/init.m4
/usr/share/aclocal-1.16/install-sh.m4
/usr/share/aclocal-1.16/internal/ac-config-macro-dirs.m4
/usr/share/aclocal-1.16/lead-dot.m4
/usr/share/aclocal-1.16/lex.m4
/usr/share/aclocal-1.16/lispdir.m4
/usr/share/aclocal-1.16/maintainer.m4
/usr/share/aclocal-1.16/make.m4
/usr/share/aclocal-1.16/missing.m4
/usr/share/aclocal-1.16/mkdirp.m4
/usr/share/aclocal-1.16/obsolete.m4
/usr/share/aclocal-1.16/options.m4
/usr/share/aclocal-1.16/prog-cc-c-o.m4
/usr/share/aclocal-1.16/python.m4
/usr/share/aclocal-1.16/runlog.m4
/usr/share/aclocal-1.16/sanity.m4
/usr/share/aclocal-1.16/silent.m4
/usr/share/aclocal-1.16/strip.m4
/usr/share/aclocal-1.16/substnot.m4
/usr/share/aclocal-1.16/tar.m4
/usr/share/aclocal-1.16/upc.m4
/usr/share/aclocal-1.16/vala.m4
/usr/share/aclocal/README
/usr/share/automake-1.16/Automake/ChannelDefs.pm
/usr/share/automake-1.16/Automake/Channels.pm
/usr/share/automake-1.16/Automake/Condition.pm
/usr/share/automake-1.16/Automake/Config.pm
/usr/share/automake-1.16/Automake/Configure_ac.pm
/usr/share/automake-1.16/Automake/DisjConditions.pm
/usr/share/automake-1.16/Automake/FileUtils.pm
/usr/share/automake-1.16/Automake/General.pm
/usr/share/automake-1.16/Automake/Getopt.pm
/usr/share/automake-1.16/Automake/Item.pm
/usr/share/automake-1.16/Automake/ItemDef.pm
/usr/share/automake-1.16/Automake/Language.pm
/usr/share/automake-1.16/Automake/Location.pm
/usr/share/automake-1.16/Automake/Options.pm
/usr/share/automake-1.16/Automake/Rule.pm
/usr/share/automake-1.16/Automake/RuleDef.pm
/usr/share/automake-1.16/Automake/VarDef.pm
/usr/share/automake-1.16/Automake/Variable.pm
/usr/share/automake-1.16/Automake/Version.pm
/usr/share/automake-1.16/Automake/Wrap.pm
/usr/share/automake-1.16/Automake/XFile.pm
/usr/share/automake-1.16/COPYING
/usr/share/automake-1.16/INSTALL
/usr/share/automake-1.16/am/check.am
/usr/share/automake-1.16/am/check2.am
/usr/share/automake-1.16/am/clean-hdr.am
/usr/share/automake-1.16/am/clean.am
/usr/share/automake-1.16/am/compile.am
/usr/share/automake-1.16/am/configure.am
/usr/share/automake-1.16/am/data.am
/usr/share/automake-1.16/am/dejagnu.am
/usr/share/automake-1.16/am/depend.am
/usr/share/automake-1.16/am/depend2.am
/usr/share/automake-1.16/am/distdir.am
/usr/share/automake-1.16/am/footer.am
/usr/share/automake-1.16/am/header-vars.am
/usr/share/automake-1.16/am/header.am
/usr/share/automake-1.16/am/inst-vars.am
/usr/share/automake-1.16/am/install.am
/usr/share/automake-1.16/am/java.am
/usr/share/automake-1.16/am/lang-compile.am
/usr/share/automake-1.16/am/lex.am
/usr/share/automake-1.16/am/library.am
/usr/share/automake-1.16/am/libs.am
/usr/share/automake-1.16/am/libtool.am
/usr/share/automake-1.16/am/lisp.am
/usr/share/automake-1.16/am/ltlib.am
/usr/share/automake-1.16/am/ltlibrary.am
/usr/share/automake-1.16/am/mans-vars.am
/usr/share/automake-1.16/am/mans.am
/usr/share/automake-1.16/am/program.am
/usr/share/automake-1.16/am/progs.am
/usr/share/automake-1.16/am/python.am
/usr/share/automake-1.16/am/remake-hdr.am
/usr/share/automake-1.16/am/scripts.am
/usr/share/automake-1.16/am/subdirs.am
/usr/share/automake-1.16/am/tags.am
/usr/share/automake-1.16/am/texi-vers.am
/usr/share/automake-1.16/am/texibuild.am
/usr/share/automake-1.16/am/texinfos.am
/usr/share/automake-1.16/am/vala.am
/usr/share/automake-1.16/am/yacc.am
/usr/share/automake-1.16/ar-lib
/usr/share/automake-1.16/compile
/usr/share/automake-1.16/config.guess
/usr/share/automake-1.16/config.sub
/usr/share/automake-1.16/depcomp
/usr/share/automake-1.16/install-sh
/usr/share/automake-1.16/mdate-sh
/usr/share/automake-1.16/missing
/usr/share/automake-1.16/mkinstalldirs
/usr/share/automake-1.16/py-compile
/usr/share/automake-1.16/tap-driver.sh
/usr/share/automake-1.16/test-driver
/usr/share/automake-1.16/texinfo.tex
/usr/share/automake-1.16/ylwrap
/usr/share/doc/automake-1.16.1/amhello-1.0.tar.gz
/usr/share/info/automake-history.info.gz
/usr/share/info/automake.info-1.gz
/usr/share/info/automake.info-2.gz
/usr/share/info/automake.info.gz
/usr/share/man/man1/aclocal-1.16.1.gz
/usr/share/man/man1/aclocal.1.gz
/usr/share/man/man1/automake-1.16.1.gz
/usr/share/man/man1/automake.1.gz


%changelog
* Tue May 31 2016 Adam Miller <maxamillion@fedoraproject.org>
-

# see /usr/libexec/rpm/macros for macros