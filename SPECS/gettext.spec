Name:           gettext
Version:	0.22.4
Release:        1%{?dist}
Summary:	GNU locale utilities

License:	GPL-3
URL:		https://www.gnu.org/software/gettext/
Source0:	https://mirror.tochlab.net/pub/gnu/gettext/gettext-%{version}.tar.gz

#BuildRequires:
#Requires:

%description

%prep
%setup -q

%build
%configure --prefix=/usr    \
	    --libdir=/usr/lib \
            --disable-static \
            --docdir=/usr/share/doc/gettext \
            --datarootdir=/usr/share/gettext \
	    --disable-csharp \
	    --disable-nls
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
%make_install
rm -fr %{buildroot}/usr/share/info/dir
rm -fr %{buildroot}/usr/share/doc/gettext/examples
find %{buildroot} -type f -name '*.la' -delete || die

%files
   /usr/bin/autopoint
   /usr/bin/envsubst
   /usr/bin/gettext
   /usr/bin/gettext.sh
   /usr/bin/gettextize
   /usr/bin/msgattrib
   /usr/bin/msgcat
   /usr/bin/msgcmp
   /usr/bin/msgcomm
   /usr/bin/msgconv
   /usr/bin/msgen
   /usr/bin/msgexec
   /usr/bin/msgfilter
   /usr/bin/msgfmt
   /usr/bin/msggrep
   /usr/bin/msginit
   /usr/bin/msgmerge
   /usr/bin/msgunfmt
   /usr/bin/msguniq
   /usr/bin/ngettext
   /usr/bin/recode-sr-latin
   /usr/bin/xgettext
   /usr/include/autosprintf.h
   /usr/include/gettext-po.h
   /usr/include/textstyle.h
   /usr/include/textstyle/stdbool.h
   /usr/include/textstyle/version.h
   /usr/include/textstyle/woe32dll.h
   /usr/lib/gettext/cldr-plurals
   /usr/lib/gettext/hostname
   /usr/lib/gettext/project-id
   /usr/lib/gettext/urlget
   /usr/lib/gettext/user-email
   /usr/lib/libasprintf.so
   /usr/lib/libasprintf.so.0
   /usr/lib/libasprintf.so.0.0.0
   /usr/lib/libgettextlib-0.22.4.so
   /usr/lib/libgettextlib.so
   /usr/lib/libgettextpo.so
   /usr/lib/libgettextpo.so.0
   /usr/lib/libgettextpo.so.0.5.10
   /usr/lib/libgettextsrc-0.22.4.so
   /usr/lib/libgettextsrc.so
   /usr/lib/libtextstyle.so
   /usr/lib/libtextstyle.so.0
   /usr/lib/libtextstyle.so.0.2.1
   /usr/lib/preloadable_libintl.so
   /usr/share/aclocal/build-to-host.m4
   /usr/share/aclocal/gettext.m4
   /usr/share/aclocal/host-cpu-c-abi.m4
   /usr/share/aclocal/iconv.m4
   /usr/share/aclocal/intlmacosx.m4
   /usr/share/aclocal/lib-ld.m4
   /usr/share/aclocal/lib-link.m4
   /usr/share/aclocal/lib-prefix.m4
   /usr/share/aclocal/nls.m4
   /usr/share/aclocal/po.m4
   /usr/share/aclocal/progtest.m4
   /usr/share/doc/gettext/FAQ.html
   /usr/share/doc/gettext/autopoint.1.html
   /usr/share/doc/gettext/autosprintf_all.html
   /usr/share/doc/gettext/bind_textdomain_codeset.3.html
   /usr/share/doc/gettext/bindtextdomain.3.html
   /usr/share/doc/gettext/csharpdoc/GNU_Gettext.html
   /usr/share/doc/gettext/csharpdoc/GNU_Gettext_GettextResourceManager.html
   /usr/share/doc/gettext/csharpdoc/GNU_Gettext_GettextResourceSet.html
   /usr/share/doc/gettext/csharpdoc/begin.html
   /usr/share/doc/gettext/csharpdoc/index.html
   /usr/share/doc/gettext/csharpdoc/namespaces.html
   /usr/share/doc/gettext/envsubst.1.html
   /usr/share/doc/gettext/gettext.1.html
   /usr/share/doc/gettext/gettext.3.html
   /usr/share/doc/gettext/gettext_1.html
   /usr/share/doc/gettext/gettext_10.html
   /usr/share/doc/gettext/gettext_11.html
   /usr/share/doc/gettext/gettext_12.html
   /usr/share/doc/gettext/gettext_13.html
   /usr/share/doc/gettext/gettext_14.html
   /usr/share/doc/gettext/gettext_15.html
   /usr/share/doc/gettext/gettext_16.html
   /usr/share/doc/gettext/gettext_17.html
   /usr/share/doc/gettext/gettext_18.html
   /usr/share/doc/gettext/gettext_19.html
   /usr/share/doc/gettext/gettext_2.html
   /usr/share/doc/gettext/gettext_20.html
   /usr/share/doc/gettext/gettext_21.html
   /usr/share/doc/gettext/gettext_22.html
   /usr/share/doc/gettext/gettext_23.html
   /usr/share/doc/gettext/gettext_24.html
   /usr/share/doc/gettext/gettext_25.html
   /usr/share/doc/gettext/gettext_26.html
   /usr/share/doc/gettext/gettext_27.html
   /usr/share/doc/gettext/gettext_28.html
   /usr/share/doc/gettext/gettext_29.html
   /usr/share/doc/gettext/gettext_3.html
   /usr/share/doc/gettext/gettext_30.html
   /usr/share/doc/gettext/gettext_4.html
   /usr/share/doc/gettext/gettext_5.html
   /usr/share/doc/gettext/gettext_6.html
   /usr/share/doc/gettext/gettext_7.html
   /usr/share/doc/gettext/gettext_8.html
   /usr/share/doc/gettext/gettext_9.html
   /usr/share/doc/gettext/gettext_abt.html
   /usr/share/doc/gettext/gettext_fot.html
   /usr/share/doc/gettext/gettext_toc.html
   /usr/share/doc/gettext/gettextize.1.html
   /usr/share/doc/gettext/javadoc2/allclasses-frame.html
   /usr/share/doc/gettext/javadoc2/deprecated-list.html
   /usr/share/doc/gettext/javadoc2/gnu/gettext/GettextResource.html
   /usr/share/doc/gettext/javadoc2/gnu/gettext/package-frame.html
   /usr/share/doc/gettext/javadoc2/gnu/gettext/package-summary.html
   /usr/share/doc/gettext/javadoc2/gnu/gettext/package-tree.html
   /usr/share/doc/gettext/javadoc2/help-doc.html
   /usr/share/doc/gettext/javadoc2/index-all.html
   /usr/share/doc/gettext/javadoc2/index.html
   /usr/share/doc/gettext/javadoc2/overview-tree.html
   /usr/share/doc/gettext/javadoc2/package-list
   /usr/share/doc/gettext/javadoc2/packages.html
   /usr/share/doc/gettext/javadoc2/serialized-form.html
   /usr/share/doc/gettext/javadoc2/stylesheet.css
   /usr/share/doc/gettext/libtextstyle_1.html
   /usr/share/doc/gettext/libtextstyle_2.html
   /usr/share/doc/gettext/libtextstyle_3.html
   /usr/share/doc/gettext/libtextstyle_4.html
   /usr/share/doc/gettext/libtextstyle_5.html
   /usr/share/doc/gettext/libtextstyle_6.html
   /usr/share/doc/gettext/libtextstyle_7.html
   /usr/share/doc/gettext/libtextstyle_abt.html
   /usr/share/doc/gettext/libtextstyle_toc.html
   /usr/share/doc/gettext/msgattrib.1.html
   /usr/share/doc/gettext/msgcat.1.html
   /usr/share/doc/gettext/msgcmp.1.html
   /usr/share/doc/gettext/msgcomm.1.html
   /usr/share/doc/gettext/msgconv.1.html
   /usr/share/doc/gettext/msgen.1.html
   /usr/share/doc/gettext/msgexec.1.html
   /usr/share/doc/gettext/msgfilter.1.html
   /usr/share/doc/gettext/msgfmt.1.html
   /usr/share/doc/gettext/msggrep.1.html
   /usr/share/doc/gettext/msginit.1.html
   /usr/share/doc/gettext/msgmerge.1.html
   /usr/share/doc/gettext/msgunfmt.1.html
   /usr/share/doc/gettext/msguniq.1.html
   /usr/share/doc/gettext/ngettext.1.html
   /usr/share/doc/gettext/ngettext.3.html
   /usr/share/doc/gettext/recode-sr-latin.1.html
   /usr/share/doc/gettext/textdomain.3.html
   /usr/share/doc/gettext/tutorial.html
   /usr/share/doc/gettext/xgettext.1.html
   /usr/share/gettext-0.22.4/its/glade.loc
   /usr/share/gettext-0.22.4/its/glade1.its
   /usr/share/gettext-0.22.4/its/glade2.its
   /usr/share/gettext-0.22.4/its/gsettings.its
   /usr/share/gettext-0.22.4/its/gsettings.loc
   /usr/share/gettext-0.22.4/its/gtkbuilder.its
   /usr/share/gettext-0.22.4/its/metainfo.its
   /usr/share/gettext-0.22.4/its/metainfo.loc
   /usr/share/gettext/ABOUT-NLS
   /usr/share/gettext/archive.dir.tar.xz
   /usr/share/gettext/config.rpath
   /usr/share/gettext/gettext.h
   /usr/share/gettext/javaversion.class
   /usr/share/gettext/msgunfmt.tcl
   /usr/share/gettext/po/Makefile.in.in
   /usr/share/gettext/po/Makevars.template
   /usr/share/gettext/po/Rules-quot
   /usr/share/gettext/po/boldquot.sed
   /usr/share/gettext/po/en@boldquot.header
   /usr/share/gettext/po/en@quot.header
   /usr/share/gettext/po/insert-header.sin
   /usr/share/gettext/po/quot.sed
   /usr/share/gettext/po/remove-potcdate.sin
   /usr/share/gettext/projects/GNOME/team-address
   /usr/share/gettext/projects/GNOME/teams.html
   /usr/share/gettext/projects/GNOME/teams.url
   /usr/share/gettext/projects/GNOME/trigger
   /usr/share/gettext/projects/KDE/team-address
   /usr/share/gettext/projects/KDE/teams.html
   /usr/share/gettext/projects/KDE/teams.url
   /usr/share/gettext/projects/KDE/trigger
   /usr/share/gettext/projects/TP/team-address
   /usr/share/gettext/projects/TP/teams.html
   /usr/share/gettext/projects/TP/teams.url
   /usr/share/gettext/projects/TP/trigger
   /usr/share/gettext/projects/index
   /usr/share/gettext/projects/team-address
   /usr/share/gettext/styles/po-default.css
   /usr/share/gettext/styles/po-emacs-x.css
   /usr/share/gettext/styles/po-emacs-xterm.css
   /usr/share/gettext/styles/po-emacs-xterm16.css
   /usr/share/gettext/styles/po-emacs-xterm256.css
   /usr/share/gettext/styles/po-vim.css
   /usr/share/info/autosprintf.info.gz
   /usr/share/info/gettext.info.gz
   /usr/share/info/libtextstyle.info.gz
   /usr/share/man/man1/autopoint.1.gz
   /usr/share/man/man1/envsubst.1.gz
   /usr/share/man/man1/gettext.1.gz
   /usr/share/man/man1/gettextize.1.gz
   /usr/share/man/man1/msgattrib.1.gz
   /usr/share/man/man1/msgcat.1.gz
   /usr/share/man/man1/msgcmp.1.gz
   /usr/share/man/man1/msgcomm.1.gz
   /usr/share/man/man1/msgconv.1.gz
   /usr/share/man/man1/msgen.1.gz
   /usr/share/man/man1/msgexec.1.gz
   /usr/share/man/man1/msgfilter.1.gz
   /usr/share/man/man1/msgfmt.1.gz
   /usr/share/man/man1/msggrep.1.gz
   /usr/share/man/man1/msginit.1.gz
   /usr/share/man/man1/msgmerge.1.gz
   /usr/share/man/man1/msgunfmt.1.gz
   /usr/share/man/man1/msguniq.1.gz
   /usr/share/man/man1/ngettext.1.gz
   /usr/share/man/man1/recode-sr-latin.1.gz
   /usr/share/man/man1/xgettext.1.gz
   /usr/share/man/man3/bind_textdomain_codeset.3.gz
   /usr/share/man/man3/bindtextdomain.3.gz
   /usr/share/man/man3/dcgettext.3.gz
   /usr/share/man/man3/dcngettext.3.gz
   /usr/share/man/man3/dgettext.3.gz
   /usr/share/man/man3/dngettext.3.gz
   /usr/share/man/man3/gettext.3.gz
   /usr/share/man/man3/ngettext.3.gz
   /usr/share/man/man3/textdomain.3.gz


%changelog

