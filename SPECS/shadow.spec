Name:           shadow
Version:        4.11.1
Release:        1%{?dist}
Summary:        Utilities to deal with user accounts

#Group:          
License:        BSD GPL-2
URL:            https://github.com/shadow-maint/shadow
Source0:        https://github.com/shadow-maint/shadow/releases/download/v%{version}/shadow-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

#BuildRequires:  
#Requires:       

%description


%prep
%setup -q
sed -i 's/groups$(EXEEXT) //' src/Makefile.in
find man -name Makefile.in -exec sed -i 's/groups\.1 / /'   {} \;
find man -name Makefile.in -exec sed -i 's/getspnam\.3 / /' {} \;
find man -name Makefile.in -exec sed -i 's/passwd\.5 / /'   {} \;

sed -i -e 's@#ENCRYPT_METHOD DES@ENCRYPT_METHOD SHA512@' \
       -e 's@/var/spool/mail@/var/mail@' etc/login.defs
       
#sed -i 's/1000/999/' etc/useradd

%build
%configure --sysconfdir=/etc --with-group-name-max-length=32
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
find %{buildroot} -type f -name '*.la' -delete || die


%post
if [ ! -f "/etc/passwd" ]; then
    echo "root:x:0:0:root:/root:/bin/bash" > /etc/passwd
    echo "bin:x:1:1:bin:/dev/null:/bin/false" >> /etc/passwd
    echo "daemon:x:6:6:Daemon User:/dev/null:/bin/false" >> /etc/passwd
    echo "messagebus:x:18:18:D-Bus Message Daemon User:/run/dbus:/bin/false" >> /etc/passwd
    echo "uuidd:x:80:80:UUID Generation Daemon User:/dev/null:/bin/false" >> /etc/passwd
    echo "nobody:x:99:99:Unprivileged User:/dev/null:/bin/false" >> /etc/passwd
fi

if [ ! -f "/etc/group" ]; then
    echo "root:x:0:" > /etc/group
    echo "bin:x:1:daemon" >> /etc/group
    echo "sys:x:2:" >> /etc/group
    echo "kmem:x:3:" >> /etc/group
    echo "tape:x:4:" >> /etc/group
    echo "tty:x:5:" >> /etc/group
    echo "daemon:x:6:" >> /etc/group
    echo "floppy:x:7:" >> /etc/group
    echo "disk:x:8:" >> /etc/group
    echo "lp:x:9:" >> /etc/group
    echo "dialout:x:10:" >> /etc/group
    echo "audio:x:11:" >> /etc/group
    echo "video:x:12:" >> /etc/group
    echo "utmp:x:13:" >> /etc/group
    echo "usb:x:14:" >> /etc/group
    echo "cdrom:x:15:" >> /etc/group
    echo "adm:x:16:" >> /etc/group
    echo "messagebus:x:18:" >> /etc/group
    echo "input:x:24:" >> /etc/group
    echo "mail:x:34:" >> /etc/group
    echo "kvm:x:61:" >> /etc/group
    echo "uuidd:x:80:" >> /etc/group
    echo "wheel:x:97:" >> /etc/group
    echo "nogroup:x:99:" >> /etc/group
    echo "users:x:999:" >> /etc/group
fi

%clean
rm -rf $RPM_BUILD_ROOT


%files
/etc/login.defs
/etc/pam.d/chfn
/etc/pam.d/chsh
/etc/pam.d/groupmems
/etc/pam.d/login
/etc/pam.d/passwd
/etc/pam.d/su
/usr/bin/chage
/usr/bin/chfn
/usr/bin/chsh
/usr/bin/expiry
/usr/bin/faillog
/usr/bin/getsubids
/usr/bin/gpasswd
/usr/bin/lastlog
/usr/bin/login
/usr/bin/newgidmap
/usr/bin/newgrp
/usr/bin/newuidmap
/usr/bin/passwd
/usr/bin/sg
/usr/bin/su
/usr/include/shadow/subid.h
/usr/lib64/libsubid.a
/usr/lib64/libsubid.so
/usr/lib64/libsubid.so.4
/usr/lib64/libsubid.so.4.0.0
/usr/sbin/chgpasswd
/usr/sbin/chpasswd
/usr/sbin/groupadd
/usr/sbin/groupdel
/usr/sbin/groupmems
/usr/sbin/groupmod
/usr/sbin/grpck
/usr/sbin/grpconv
/usr/sbin/grpunconv
/usr/sbin/logoutd
/usr/sbin/newusers
/usr/sbin/nologin
/usr/sbin/pwck
/usr/sbin/pwconv
/usr/sbin/pwunconv
/usr/sbin/useradd
/usr/sbin/userdel
/usr/sbin/usermod
/usr/sbin/vigr
/usr/sbin/vipw
/usr/share/locale/bs/LC_MESSAGES/shadow.mo
/usr/share/locale/ca/LC_MESSAGES/shadow.mo
/usr/share/locale/cs/LC_MESSAGES/shadow.mo
/usr/share/locale/da/LC_MESSAGES/shadow.mo
/usr/share/locale/de/LC_MESSAGES/shadow.mo
/usr/share/locale/dz/LC_MESSAGES/shadow.mo
/usr/share/locale/el/LC_MESSAGES/shadow.mo
/usr/share/locale/es/LC_MESSAGES/shadow.mo
/usr/share/locale/eu/LC_MESSAGES/shadow.mo
/usr/share/locale/fi/LC_MESSAGES/shadow.mo
/usr/share/locale/fr/LC_MESSAGES/shadow.mo
/usr/share/locale/gl/LC_MESSAGES/shadow.mo
/usr/share/locale/he/LC_MESSAGES/shadow.mo
/usr/share/locale/hu/LC_MESSAGES/shadow.mo
/usr/share/locale/id/LC_MESSAGES/shadow.mo
/usr/share/locale/it/LC_MESSAGES/shadow.mo
/usr/share/locale/ja/LC_MESSAGES/shadow.mo
/usr/share/locale/kk/LC_MESSAGES/shadow.mo
/usr/share/locale/km/LC_MESSAGES/shadow.mo
/usr/share/locale/ko/LC_MESSAGES/shadow.mo
/usr/share/locale/nb/LC_MESSAGES/shadow.mo
/usr/share/locale/ne/LC_MESSAGES/shadow.mo
/usr/share/locale/nl/LC_MESSAGES/shadow.mo
/usr/share/locale/nn/LC_MESSAGES/shadow.mo
/usr/share/locale/pl/LC_MESSAGES/shadow.mo
/usr/share/locale/pt/LC_MESSAGES/shadow.mo
/usr/share/locale/pt_BR/LC_MESSAGES/shadow.mo
/usr/share/locale/ro/LC_MESSAGES/shadow.mo
/usr/share/locale/ru/LC_MESSAGES/shadow.mo
/usr/share/locale/sk/LC_MESSAGES/shadow.mo
/usr/share/locale/sq/LC_MESSAGES/shadow.mo
/usr/share/locale/sv/LC_MESSAGES/shadow.mo
/usr/share/locale/tl/LC_MESSAGES/shadow.mo
/usr/share/locale/tr/LC_MESSAGES/shadow.mo
/usr/share/locale/uk/LC_MESSAGES/shadow.mo
/usr/share/locale/vi/LC_MESSAGES/shadow.mo
/usr/share/locale/zh_CN/LC_MESSAGES/shadow.mo
/usr/share/locale/zh_TW/LC_MESSAGES/shadow.mo

%changelog
