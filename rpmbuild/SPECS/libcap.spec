Name:          	libcap 
Version:	2.33
Release:        1%{?dist}
Summary:	POSIX 1003.1e capabilities

License:	GPL-2 BSD
URL:		https://sites.google.com/site/fullycapable/
Source0:	https://mirrors.edge.kernel.org/pub/linux/libs/security/linux-privs/libcap2/libcap-%{version}.tar.gz

#BuildRequires:
#Requires:

%description

%prep
%setup -q

%build
make lib=lib %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
%make_install lib=lib

%files
/lib/libcap.a
/lib/libcap.so
/lib/libcap.so.2
/lib/libcap.so.2.33
/lib/libpsx.a
/sbin/capsh
/sbin/getcap
/sbin/getpcaps
/sbin/setcap
/usr/include/sys/capability.h
/usr/include/sys/psx_syscall.h
/usr/lib/pkgconfig/libcap.pc
/usr/lib/pkgconfig/libpsx.pc
/usr/share/man/man1/capsh.1.gz
/usr/share/man/man3/cap_clear.3.gz
/usr/share/man/man3/cap_clear_flag.3.gz
/usr/share/man/man3/cap_compare.3.gz
/usr/share/man/man3/cap_copy_ext.3.gz
/usr/share/man/man3/cap_copy_int.3.gz
/usr/share/man/man3/cap_drop_bound.3.gz
/usr/share/man/man3/cap_dup.3.gz
/usr/share/man/man3/cap_free.3.gz
/usr/share/man/man3/cap_from_name.3.gz
/usr/share/man/man3/cap_from_text.3.gz
/usr/share/man/man3/cap_get_bound.3.gz
/usr/share/man/man3/cap_get_fd.3.gz
/usr/share/man/man3/cap_get_file.3.gz
/usr/share/man/man3/cap_get_flag.3.gz
/usr/share/man/man3/cap_get_mode.3.gz
/usr/share/man/man3/cap_get_pid.3.gz
/usr/share/man/man3/cap_get_proc.3.gz
/usr/share/man/man3/cap_get_secbits.3.gz
/usr/share/man/man3/cap_init.3.gz
/usr/share/man/man3/cap_mode_name.3.gz
/usr/share/man/man3/cap_set_fd.3.gz
/usr/share/man/man3/cap_set_file.3.gz
/usr/share/man/man3/cap_set_flag.3.gz
/usr/share/man/man3/cap_set_mode.3.gz
/usr/share/man/man3/cap_set_proc.3.gz
/usr/share/man/man3/cap_set_secbits.3.gz
/usr/share/man/man3/cap_setgroups.3.gz
/usr/share/man/man3/cap_setuid.3.gz
/usr/share/man/man3/cap_size.3.gz
/usr/share/man/man3/cap_to_name.3.gz
/usr/share/man/man3/cap_to_text.3.gz
/usr/share/man/man3/capgetp.3.gz
/usr/share/man/man3/capsetp.3.gz
/usr/share/man/man3/libcap.3.gz
/usr/share/man/man3/libpsx.3.gz
/usr/share/man/man3/psx_register.3.gz
/usr/share/man/man3/psx_syscall.3.gz
/usr/share/man/man3/psx_syscall3.3.gz
/usr/share/man/man3/psx_syscall6.3.gz
/usr/share/man/man8/getcap.8.gz
/usr/share/man/man8/getpcaps.8.gz
/usr/share/man/man8/setcap.8.gz


%changelog
* Tue May 31 2016 Adam Miller <maxamillion@fedoraproject.org>
-
