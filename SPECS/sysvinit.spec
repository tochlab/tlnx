Name:           sysvinit
Version:	3.03
Release:        1%{?dist}
Summary:	/sbin/init - parent of all processes

License:	GPL-2
URL:		https://savannah.nongnu.org/projects/sysvinit
Source0:	https://github.com/slicer69/sysvinit/releases/download/%{version}/sysvinit-%{version}.tar.xz

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
%{__rm} -f %{buildroot}/bin/pidof
%{__rm} -f %{buildroot}/sbin/logsave
%{__rm} -f %{buildroot}/sbin/sulogin
%{__rm} -f %{buildroot}/usr/bin/last
%{__rm} -f %{buildroot}/usr/bin/lastb
%{__rm} -f %{buildroot}/usr/bin/mesg
%{__rm} -f %{buildroot}/usr/bin/utmpdump
%{__rm} -f %{buildroot}/usr/share/man/man8/pidof.8
%{__rm} -f %{buildroot}/usr/share/man/man8/logsave.8
%{__rm} -f %{buildroot}/usr/share/man/man8/sulogin.8
%{__rm} -f %{buildroot}/usr/share/man/man1/last.1
%{__rm} -f %{buildroot}/usr/share/man/man1/lastb.1
%{__rm} -f %{buildroot}/usr/share/man/man1/mesg.1
%{__rm} -f %{buildroot}/usr/share/man/man1/utmpdump.1

%files
/sbin/bootlogd
/sbin/fstab-decode
/sbin/halt
/sbin/init
/sbin/killall5
/sbin/poweroff
/sbin/reboot
/sbin/runlevel
/sbin/shutdown
/sbin/telinit
/usr/bin/readbootlog
/usr/bin/wall
/usr/include/initreq.h
/usr/share/man/man1/readbootlog.1.gz
/usr/share/man/man1/wall.1.gz
/usr/share/man/man5/initctl.5.gz
/usr/share/man/man5/initscript.5.gz
/usr/share/man/man5/inittab.5.gz
/usr/share/man/man8/bootlogd.8.gz
/usr/share/man/man8/fstab-decode.8.gz
/usr/share/man/man8/halt.8.gz
/usr/share/man/man8/init.8.gz
/usr/share/man/man8/killall5.8.gz
/usr/share/man/man8/poweroff.8.gz
/usr/share/man/man8/reboot.8.gz
/usr/share/man/man8/runlevel.8.gz
/usr/share/man/man8/shutdown.8.gz
/usr/share/man/man8/telinit.8.gz


%changelog
