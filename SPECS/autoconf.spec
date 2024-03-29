Name:           autoconf
Version:	2.71
Release:        1%{?dist}
Summary:        Used to create autoconfiguration files

License:	GPL-3
URL:		https://www.gnu.org/software/autoconf/autoconf.html
Source0:	https://ftpmirror.gnu.org/gnu/autoconf/autoconf-%{version}.tar.gz

#BuildRequires:
#Requires:

%description

%prep
%setup -q

%build
%configure --prefix=/usr
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
%make_install
rm -fr $RPM_BUILD_ROOT/usr/share/info/dir

%files
/usr/bin/autoconf
/usr/bin/autoheader
/usr/bin/autom4te
/usr/bin/autoreconf
/usr/bin/autoscan
/usr/bin/autoupdate
/usr/bin/ifnames
/usr/share/autoconf/Autom4te/C4che.pm
/usr/share/autoconf/Autom4te/ChannelDefs.pm
/usr/share/autoconf/Autom4te/Channels.pm
/usr/share/autoconf/Autom4te/Configure_ac.pm
/usr/share/autoconf/Autom4te/FileUtils.pm
/usr/share/autoconf/Autom4te/General.pm
/usr/share/autoconf/Autom4te/Getopt.pm
/usr/share/autoconf/Autom4te/Request.pm
/usr/share/autoconf/Autom4te/XFile.pm
/usr/share/autoconf/INSTALL
/usr/share/autoconf/autoconf/autoconf.m4
/usr/share/autoconf/autoconf/autoconf.m4f
/usr/share/autoconf/autoconf/autoheader.m4
/usr/share/autoconf/autoconf/autoscan.m4
/usr/share/autoconf/autoconf/autotest.m4
/usr/share/autoconf/autoconf/autoupdate.m4
/usr/share/autoconf/autoconf/c.m4
/usr/share/autoconf/autoconf/erlang.m4
/usr/share/autoconf/autoconf/fortran.m4
/usr/share/autoconf/autoconf/functions.m4
/usr/share/autoconf/autoconf/general.m4
/usr/share/autoconf/autoconf/go.m4
/usr/share/autoconf/autoconf/headers.m4
/usr/share/autoconf/autoconf/lang.m4
/usr/share/autoconf/autoconf/libs.m4
/usr/share/autoconf/autoconf/oldnames.m4
/usr/share/autoconf/autoconf/programs.m4
/usr/share/autoconf/autoconf/specific.m4
/usr/share/autoconf/autoconf/status.m4
/usr/share/autoconf/autoconf/types.m4
/usr/share/autoconf/autom4te.cfg
/usr/share/autoconf/autoscan/autoscan.list
/usr/share/autoconf/autotest/autotest.m4
/usr/share/autoconf/autotest/autotest.m4f
/usr/share/autoconf/autotest/general.m4
/usr/share/autoconf/autotest/specific.m4
/usr/share/autoconf/m4sugar/foreach.m4
/usr/share/autoconf/m4sugar/m4sh.m4
/usr/share/autoconf/m4sugar/m4sh.m4f
/usr/share/autoconf/m4sugar/m4sugar.m4
/usr/share/autoconf/m4sugar/m4sugar.m4f
/usr/share/autoconf/m4sugar/version.m4
/usr/share/info/autoconf.info.gz
/usr/share/info/standards.info.gz
/usr/share/man/man1/autoconf.1.gz
/usr/share/man/man1/autoheader.1.gz
/usr/share/man/man1/autom4te.1.gz
/usr/share/man/man1/autoreconf.1.gz
/usr/share/man/man1/autoscan.1.gz
/usr/share/man/man1/autoupdate.1.gz
/usr/share/man/man1/ifnames.1.gz
/usr/share/autoconf/Autom4te/Config.pm
/usr/share/autoconf/autoconf/trailer.m4
/usr/share/autoconf/build-aux/config.guess
/usr/share/autoconf/build-aux/config.sub
/usr/share/autoconf/build-aux/install-sh


%changelog
