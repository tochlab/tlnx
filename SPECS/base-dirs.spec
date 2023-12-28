Name: base-dirs
Version: 1
Release: 1
Summary: Base dirs for /
License: GPLv2
BuildArch: noarch

%description
Contains base tree for initial work

%prep
# Nothing here

%build
# And here

%install
    rm -fr %{buildroot}
    mkdir -pv %{buildroot}/{bin,boot,etc/{opt,sysconfig},home,lib/firmware,mnt,opt}
    mkdir -pv %{buildroot}/{media/{floppy,cdrom},sbin,srv,var,proc,dev}
    mkdir -pvm 0750 %{buildroot}/root
    mkdir -pvm 1777 %{buildroot}/tmp 
    mkdir -pvm 1777 %{buildroot}/var/tmp
    mkdir -pv %{buildroot}/usr/{,local/}{bin,include,lib,sbin,src}
    mkdir -pv %{buildroot}/usr/{,local/}share/{color,dict,doc,info,locale,man}
    mkdir -v  %{buildroot}/usr/{,local/}share/{misc,terminfo,zoneinfo}
    mkdir -v  %{buildroot}/usr/libexec
    mkdir -pv %{buildroot}/usr/{,local/}share/man/man{1..8}
    cd %{buildroot}; ln -s lib lib64

    mkdir -v %{buildroot}/var/{log,mail,spool}
    #ln -sv run var/run
    #ln -sv run/lock var/lock
    mkdir -pv %{buildroot}/var/{opt,cache,lib/{color,misc,locate},local}
    echo 127.0.0.1 localhost black > %{buildroot}/etc/hosts

    echo "set +h" > %{buildroot}/root/.bashrc
    echo "umask 022" >> %{buildroot}/root/.bashrc
    echo "LC_ALL=C" >> %{buildroot}/root/.bashrc
    echo "LANG=C" >> %{buildroot}/root/.bashrc
    echo "PATH=/bin:/sbin:/usr/bin:/usr/sbin" >>  %{buildroot}/root/.bashrc
    echo "export LC_ALL LANG PATH" >> %{buildroot}/root/.bashrc
    cp %{_sourcedir}/profile %{buildroot}/etc/profile
    echo "NAME=TLNX" > %{buildroot}/etc/os-release
    echo "ID=tlnx" >> %{buildroot}/etc/os-release
    echo "PRETTY_NAME=\"Tochlab Linux\""  >> %{buildroot}/etc/os-release
    echo "ANSI_COLOR=\"1;32\"" >> %{buildroot}/etc/os-release
    echo "HOME_URL=\"https://www.tlnx.org/\"" >> %{buildroot}/etc/os-release
    echo "SUPPORT_URL=\"https://www.tlnx.org/support/\"" >> %{buildroot}/etc/os-release
    echo "BUG_REPORT_URL=\"https://bugs.tlnx.org/\"" >> %{buildroot}/etc/os-release
    echo "VERSION_ID=\"0.0\"" >> %{buildroot}/etc/os-release

###    mknod -m 600 %{buildroot}/dev/console c 5 1
###    mknod -m 666 %{buildroot}/dev/null c 1 3

%files
/*
# No files at all

%changelog
# Nothin here
