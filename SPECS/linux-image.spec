Name: linux-image
Version: 5.10.112
Release: 1
Summary: Linux Kernel
License: GPLv2
URL: https://www.kernel.org
Source0: https://cdn.kernel.org/pub/linux/kernel/v5.x/linux-%{version}.tar.xz

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
rm %{buildroot}/lib/modules/5.10.112/build
rm %{buildroot}/lib/modules/5.10.112/source

%files
/boot/System.map-5.10.112
/boot/config-5.10.112
/boot/vmlinuz-5.10.112
/lib/modules/5.10.112/kernel/drivers/thermal/intel/x86_pkg_temp_thermal.ko
/lib/modules/5.10.112/kernel/fs/efivarfs/efivarfs.ko
/lib/modules/5.10.112/kernel/net/ipv4/netfilter/iptable_nat.ko
/lib/modules/5.10.112/kernel/net/ipv4/netfilter/nf_log_arp.ko
/lib/modules/5.10.112/kernel/net/ipv4/netfilter/nf_log_ipv4.ko
/lib/modules/5.10.112/kernel/net/ipv6/netfilter/nf_log_ipv6.ko
/lib/modules/5.10.112/kernel/net/netfilter/nf_log_common.ko
/lib/modules/5.10.112/kernel/net/netfilter/xt_LOG.ko
/lib/modules/5.10.112/kernel/net/netfilter/xt_MASQUERADE.ko
/lib/modules/5.10.112/kernel/net/netfilter/xt_addrtype.ko
/lib/modules/5.10.112/kernel/net/netfilter/xt_mark.ko
/lib/modules/5.10.112/kernel/net/netfilter/xt_nat.ko
/lib/modules/5.10.112/modules.alias
/lib/modules/5.10.112/modules.alias.bin
/lib/modules/5.10.112/modules.builtin
/lib/modules/5.10.112/modules.builtin.alias.bin
/lib/modules/5.10.112/modules.builtin.bin
/lib/modules/5.10.112/modules.builtin.modinfo
/lib/modules/5.10.112/modules.dep
/lib/modules/5.10.112/modules.dep.bin
/lib/modules/5.10.112/modules.devname
/lib/modules/5.10.112/modules.order
/lib/modules/5.10.112/modules.softdep
/lib/modules/5.10.112/modules.symbols
/lib/modules/5.10.112/modules.symbols.bin


%post
rm -f /boot/System.map
rm -f /boot/config
rm -f /boot/vmlinuz
ln -s /boot/System.map-5.10.112 /boot/System.map
ln -s /boot/config-5.10.112 /boot/config
ln -s /boot/vmlinuz-5.10.112 /boot/vmlinuz
/sbin/depmod -a

%changelog

