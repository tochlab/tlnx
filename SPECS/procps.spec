Name:           procps
Version:	v3.3.17
Release:        1%{?dist}
Summary:	standard informational utilities and process-handling tools

License:	GPL-2
URL:		http://procps-ng.sourceforge.net/
Source0:	https://gitlab.com/procps-ng/procps/-/archive/%{version}/procps-%{version}.tar.gz

#BuildRequires: gettext
#Requires:

%description

%prep
%setup -q

%build
./autogen.sh
%configure  --bindir=/bin                            \
            --sbindir=/sbin                          \
            --libdir=/usr/lib                        \
            --docdir=/usr/share/doc/procps           \
            --disable-static                         \
            --disable-kill \
            --disable-nls \
            --with-pkg-config-libdir=/usr/lib/pkgconfig
            
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
%make_install
find %{buildroot} -type f -name '*.la' -delete || die

%files
/bin/free
/bin/pgrep
/bin/pidof
/bin/pkill
/bin/pmap
/bin/ps
/bin/pwdx
/bin/slabtop
/bin/tload
/bin/top
/bin/uptime
/bin/vmstat
/bin/w
/bin/watch
/bin/pwait
/sbin/sysctl
/usr/include/proc/alloc.h
/usr/include/proc/devname.h
/usr/include/proc/escape.h
/usr/include/proc/numa.h
/usr/include/proc/procps.h
/usr/include/proc/pwcache.h
/usr/include/proc/readproc.h
/usr/include/proc/sig.h
/usr/include/proc/slab.h
/usr/include/proc/sysinfo.h
/usr/include/proc/version.h
/usr/include/proc/wchan.h
/usr/include/proc/whattime.h
/usr/lib/libprocps.so
/usr/lib/libprocps.so.8
/usr/lib/libprocps.so.8.0.3
/usr/lib/pkgconfig/libprocps.pc
/usr/share/doc/procps/FAQ
/usr/share/doc/procps/bugs.md
/usr/share/man/man1/free.1.gz
/usr/share/man/man1/pgrep.1.gz
/usr/share/man/man1/pidof.1.gz
/usr/share/man/man1/pkill.1.gz
/usr/share/man/man1/pmap.1.gz
/usr/share/man/man1/procps.1.gz
/usr/share/man/man1/ps.1.gz
/usr/share/man/man1/pwdx.1.gz
/usr/share/man/man1/slabtop.1.gz
/usr/share/man/man1/tload.1.gz
/usr/share/man/man1/top.1.gz
/usr/share/man/man1/uptime.1.gz
/usr/share/man/man1/w.1.gz
/usr/share/man/man1/watch.1.gz
/usr/share/man/man3/openproc.3.gz
/usr/share/man/man3/readproc.3.gz
/usr/share/man/man3/readproctab.3.gz
/usr/share/man/man5/sysctl.conf.5.gz
/usr/share/man/man8/sysctl.8.gz
/usr/share/man/man8/vmstat.8.gz
/usr/share/man/man1/pwait.1.gz


%changelog
