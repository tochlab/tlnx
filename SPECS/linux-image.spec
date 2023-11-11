Name: linux-image
Version: 5.10.200
Release: 1
Summary: Linux Kernel
License: GPLv2
URL: https://www.kernel.org
Source0:	https://cdn.kernel.org/pub/linux/kernel/v5.x/linux-%{version}.tar.xz

%description

%prep
%setup -q -n linux-%{version}

%build
make x86_64_defconfig
make -j 8

%install
mkdir -p %{buildroot}/boot/
INSTALL_PATH=%{buildroot}/boot/ make install
mkdir -p %{buildroot}/lib/modules/%{version}/
INSTALL_MOD_PATH=%{buildroot}/ make modules_install
rm %{buildroot}/lib/modules/%{version}/build
rm %{buildroot}/lib/modules/%{version}/source

%files
/boot/System.map-%{version}
/boot/config-%{version}
/boot/vmlinuz-%{version}
/lib/modules/%{version}/kernel/drivers/thermal/intel/x86_pkg_temp_thermal.ko
/lib/modules/%{version}/kernel/fs/efivarfs/efivarfs.ko
/lib/modules/%{version}/kernel/net/ipv4/netfilter/iptable_nat.ko
/lib/modules/%{version}/kernel/net/ipv4/netfilter/nf_log_arp.ko
/lib/modules/%{version}/kernel/net/ipv4/netfilter/nf_log_ipv4.ko
/lib/modules/%{version}/kernel/net/ipv6/netfilter/nf_log_ipv6.ko
/lib/modules/%{version}/kernel/net/netfilter/nf_log_common.ko
/lib/modules/%{version}/kernel/net/netfilter/xt_LOG.ko
/lib/modules/%{version}/kernel/net/netfilter/xt_MASQUERADE.ko
/lib/modules/%{version}/kernel/net/netfilter/xt_addrtype.ko
/lib/modules/%{version}/kernel/net/netfilter/xt_mark.ko
/lib/modules/%{version}/kernel/net/netfilter/xt_nat.ko
/lib/modules/%{version}/modules.alias
/lib/modules/%{version}/modules.alias.bin
/lib/modules/%{version}/modules.builtin
/lib/modules/%{version}/modules.builtin.alias.bin
/lib/modules/%{version}/modules.builtin.bin
/lib/modules/%{version}/modules.builtin.modinfo
/lib/modules/%{version}/modules.dep
/lib/modules/%{version}/modules.dep.bin
/lib/modules/%{version}/modules.devname
/lib/modules/%{version}/modules.order
/lib/modules/%{version}/modules.softdep
/lib/modules/%{version}/modules.symbols
/lib/modules/%{version}/modules.symbols.bin


%post
rm -f /boot/System.map
rm -f /boot/config
rm -f /boot/vmlinuz
ln -s /boot/System.map-%{version} /boot/System.map
ln -s /boot/config-%{version} /boot/config
ln -s /boot/vmlinuz-%{version} /boot/vmlinuz

%changelog

