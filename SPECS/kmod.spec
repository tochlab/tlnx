Name:           kmod
Version:	29
Release:        1%{?dist}
Summary:	library and tools for managing linux kernel modules

License:	LGPL-2
URL:		https://git.kernel.org/?p=utils/kernel/kmod/kmod.git
Source0:	https://www.kernel.org/pub/linux/utils/kernel/kmod/kmod-%{version}.tar.gz

#BuildRequires:
#Requires:

%description

%prep
%setup -q

%build
%configure --prefix=/usr          \
            --bindir=/bin          \
            --sysconfdir=/etc      \
            --with-rootlibdir=/lib \
	    --libdir=/usr/lib      \
            --with-xz              \
            --with-zlib \
            --with-pkg-config-libdir=/usr/lib/pkgconfig
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
%make_install

%files
/bin/kmod
/lib/libkmod.so.2
/lib/libkmod.so.2.3.7
/usr/include/libkmod.h
/usr/lib/libkmod.so
/usr/lib/pkgconfig/libkmod.pc
/usr/share/bash-completion/completions/kmod
/usr/share/man/man5/depmod.d.5.gz
/usr/share/man/man5/modprobe.d.5.gz
/usr/share/man/man5/modules.dep.5.gz
/usr/share/man/man5/modules.dep.bin.5.gz
/usr/share/man/man8/depmod.8.gz
/usr/share/man/man8/insmod.8.gz
/usr/share/man/man8/kmod.8.gz
/usr/share/man/man8/lsmod.8.gz
/usr/share/man/man8/modinfo.8.gz
/usr/share/man/man8/modprobe.8.gz
/usr/share/man/man8/rmmod.8.gz

%post
ln -sf /bin/kmod /sbin/depmod
ln -sf /bin/kmod /sbin/modprobe
ln -sf /bin/kmod /sbin/insmod
ln -sf /bin/kmod /sbin/rmmod

%changelog

