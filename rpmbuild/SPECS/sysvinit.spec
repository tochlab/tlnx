Name:           sysvinit
Version:	2.96
Release:        1%{?dist}
Summary:	/sbin/init - parent of all processes

License:	GPL-2
URL:		https://savannah.nongnu.org/projects/sysvinit
Source0:	http://download.savannah.nongnu.org/releases/sysvinit/sysvinit-%{version}.tar.xz

#BuildRequires:
#Requires:

%description

%prep
%setup -q

%build
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make ROOT=$RPM_BUILD_ROOT install

%files
/bin/pidof
/sbin/bootlogd
/sbin/fstab-decode
/sbin/halt
/sbin/init
/sbin/killall5
/sbin/logsave
/sbin/poweroff
/sbin/reboot
/sbin/runlevel
/sbin/shutdown
/sbin/sulogin
/sbin/telinit
/usr/bin/last
/usr/bin/lastb
/usr/bin/mesg
/usr/bin/readbootlog
/usr/bin/utmpdump
/usr/bin/wall
/usr/include/initreq.h
/usr/share/man/man1/last.1.gz
/usr/share/man/man1/lastb.1.gz
/usr/share/man/man1/mesg.1.gz
/usr/share/man/man1/readbootlog.1.gz
/usr/share/man/man1/utmpdump.1.gz
/usr/share/man/man1/wall.1.gz
/usr/share/man/man5/initctl.5.gz
/usr/share/man/man5/initscript.5.gz
/usr/share/man/man5/inittab.5.gz
/usr/share/man/man8/bootlogd.8.gz
/usr/share/man/man8/fstab-decode.8.gz
/usr/share/man/man8/halt.8.gz
/usr/share/man/man8/init.8.gz
/usr/share/man/man8/killall5.8.gz
/usr/share/man/man8/logsave.8.gz
/usr/share/man/man8/pidof.8.gz
/usr/share/man/man8/poweroff.8.gz
/usr/share/man/man8/reboot.8.gz
/usr/share/man/man8/runlevel.8.gz
/usr/share/man/man8/shutdown.8.gz
/usr/share/man/man8/sulogin.8.gz
/usr/share/man/man8/telinit.8.gz


%changelog
* Tue May 31 2016 Adam Miller <maxamillion@fedoraproject.org>
-

# see /usr/libexec/rpm/macros for macros
