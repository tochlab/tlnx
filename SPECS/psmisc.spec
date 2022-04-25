Name:         	psmisc
Version:	v23.4
Release:        1%{?dist}
Summary:	A set of tools that use the proc filesystem

License:	GPL-2
URL:		http://psmisc.sourceforge.net/
Source0:	https://gitlab.com/psmisc/psmisc/-/archive/%{version}/psmisc-%{version}.tar.gz

#BuildRequires:
#Requires: ncurses

%description

%prep
%setup -q

%build
./autogen.sh
LDFLAGS="-Wl,--build-id" ./configure --prefix=/usr --disable-nls
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
%make_install

%files
/usr/bin/fuser
/usr/bin/killall
/usr/bin/peekfd
/usr/bin/prtstat
/usr/bin/pslog
/usr/bin/pstree
/usr/bin/pstree.x11
/usr/share/man/man1/fuser.1.gz
/usr/share/man/man1/killall.1.gz
/usr/share/man/man1/peekfd.1.gz
/usr/share/man/man1/prtstat.1.gz
/usr/share/man/man1/pslog.1.gz
/usr/share/man/man1/pstree.1.gz

%changelog
