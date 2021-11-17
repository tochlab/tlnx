Name:           shadow
Version:        4.8.1
Release:        1%{?dist}
Summary:        shadow utils

#Group:          
License:        GPL
URL:            https://github.com/shadow-maint/shadow/releases/download/4.8.1/shadow-4.8.1.tar.gz
Source0:        https://github.com/shadow-maint/shadow/releases/download/4.8.1/shadow-4.8.1.tar.gz
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
       
sed -i 's/1000/999/' etc/useradd

%build
%configure --sysconfdir=/etc --with-group-name-max-length=32
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

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
/*

%changelog
