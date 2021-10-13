Name:           inetutils
Version:	1.9.4
Release:        1%{?dist}
Summary:	Inetutils

License:	GPL
URL:		https://www.gnu.org/software/inetutils/
Source0:	https://ftpmirror.gnu.org/gnu/inetutils/inetutils-%{version}.tar.gz

#BuildRequires:
#Requires:

%description

%prep
%setup -q

%build
./configure --prefix=/usr        \
            --localstatedir=/var \
	    --bindir=/bin	 \
	    --sbindir=/sbin	 \
            --disable-logger     \
            --disable-whois      \
            --disable-rcp        \
            --disable-rexec      \
            --disable-rlogin     \
            --disable-rsh        \
	    --disable-talk	 \
            --disable-servers

make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
%make_install
rm %{buildroot}/usr/share/info/dir

%files
/bin/dnsdomainname
/bin/ftp
/bin/hostname
/bin/ifconfig
/bin/ping
/bin/ping6
/bin/telnet
/bin/tftp
/bin/traceroute
/usr/share/info/inetutils.info.gz
/usr/share/man/man1/dnsdomainname.1.gz
/usr/share/man/man1/ftp.1.gz
/usr/share/man/man1/hostname.1.gz
/usr/share/man/man1/ifconfig.1.gz
/usr/share/man/man1/ping.1.gz
/usr/share/man/man1/ping6.1.gz
/usr/share/man/man1/telnet.1.gz
/usr/share/man/man1/tftp.1.gz
/usr/share/man/man1/traceroute.1.gz


%changelog
* Tue May 31 2016 Adam Miller <maxamillion@fedoraproject.org>
-

# see /usr/libexec/rpm/macros for macros
