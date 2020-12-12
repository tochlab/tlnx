Name:           libseccomp
Version:	2.4.4
Release:        1%{?dist}
Summary:	High level interface to Linux seccomp filter

License:	LGPL-2.1
URL:		https://github.com/seccomp/libseccomp
Source0:	https://github.com/seccomp/libseccomp/releases/download/v%{version}/libseccomp-%{version}.tar.gz

#BuildRequires:
#Requires:

%description

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
%make_install
%{__rm} -f %{buildroot}/usr/share/info/dir

#%post
#/sbin/ldconfig
#/sbin/install-info /usr/share/info/DevIL_manual.info.gz /usr/share/info/dir 2> /dev/null || :

#%postun
#/sbin/ldconfig
#/sbin/install-info --delete /usr/share/info/DevIL_manual.info.gz /usr/share/info/dir 2> /dev/null || :

%files
/usr/bin/scmp_sys_resolver
/usr/include/seccomp-syscalls.h
/usr/include/seccomp.h
/usr/lib64/libseccomp.a
/usr/lib64/libseccomp.la
/usr/lib64/libseccomp.so
/usr/lib64/libseccomp.so.2
/usr/lib64/libseccomp.so.%{version}
/usr/lib64/pkgconfig/libseccomp.pc
/usr/share/man/man1/scmp_sys_resolver.1.gz
/usr/share/man/man3/seccomp_api_get.3.gz
/usr/share/man/man3/seccomp_api_set.3.gz
/usr/share/man/man3/seccomp_arch_add.3.gz
/usr/share/man/man3/seccomp_arch_exist.3.gz
/usr/share/man/man3/seccomp_arch_native.3.gz
/usr/share/man/man3/seccomp_arch_remove.3.gz
/usr/share/man/man3/seccomp_arch_resolve_name.3.gz
/usr/share/man/man3/seccomp_attr_get.3.gz
/usr/share/man/man3/seccomp_attr_set.3.gz
/usr/share/man/man3/seccomp_export_bpf.3.gz
/usr/share/man/man3/seccomp_export_pfc.3.gz
/usr/share/man/man3/seccomp_init.3.gz
/usr/share/man/man3/seccomp_load.3.gz
/usr/share/man/man3/seccomp_merge.3.gz
/usr/share/man/man3/seccomp_release.3.gz
/usr/share/man/man3/seccomp_reset.3.gz
/usr/share/man/man3/seccomp_rule_add.3.gz
/usr/share/man/man3/seccomp_rule_add_array.3.gz
/usr/share/man/man3/seccomp_rule_add_exact.3.gz
/usr/share/man/man3/seccomp_rule_add_exact_array.3.gz
/usr/share/man/man3/seccomp_syscall_priority.3.gz
/usr/share/man/man3/seccomp_syscall_resolve_name.3.gz
/usr/share/man/man3/seccomp_syscall_resolve_name_arch.3.gz
/usr/share/man/man3/seccomp_syscall_resolve_name_rewrite.3.gz
/usr/share/man/man3/seccomp_syscall_resolve_num_arch.3.gz
/usr/share/man/man3/seccomp_version.3.gz

%doc

%changelog
* Tue May 31 2016 Adam Miller <maxamillion@fedoraproject.org>
-

# see /usr/libexec/rpm/macros for macros
