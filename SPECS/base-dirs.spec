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
    mkdir -pv %{buildroot}/{media/{floppy,cdrom},sbin,srv,var,proc}
    mkdir -m 0750 %{buildroot}/root
    mkdir -m 1777 %{buildroot}/tmp 
    mkdir -m 1777 %{buildroot}/var/tmp
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

%files
/*
# No files at all

%changelog
# Nothin here
