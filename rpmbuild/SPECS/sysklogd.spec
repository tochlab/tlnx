Name:           sysklogd
Version:	2.1.2
Release:        1%{?dist}
Summary:	Standard log daemons

License:	BSD
URL:		https://troglobit.com/sysklogd.html
Source0:	https://github.com/troglobit/sysklogd/releases/download/v%{version}/sysklogd-%{version}.tar.gz

#BuildRequires:
#Requires:

%description

%prep
%setup -q

%build
./configure --prefix=/usr --bindir=/bin --sbindir=/sbin --without-logger
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
%make_install

%files
/sbin/syslogd
/usr/include/syslog/syslog.h
/usr/lib/libsyslog.a
/usr/lib/libsyslog.la
/usr/lib/libsyslog.so
/usr/lib/libsyslog.so.0
/usr/lib/libsyslog.so.0.0.0
/usr/lib/pkgconfig/libsyslog.pc
/usr/share/doc/sysklogd/ChangeLog.md
/usr/share/doc/sysklogd/LICENSE
/usr/share/doc/sysklogd/README.md
/usr/share/doc/sysklogd/example/README.md
/usr/share/doc/sysklogd/example/example.c
/usr/share/doc/sysklogd/example/example.mk
/usr/share/doc/sysklogd/syslog.conf
/usr/share/man/man3/syslogp.3.gz
/usr/share/man/man5/syslog.conf.5.gz
/usr/share/man/man8/syslogd.8.gz


%changelog
* Tue May 31 2016 Adam Miller <maxamillion@fedoraproject.org>
-

# see /usr/libexec/rpm/macros for macros
