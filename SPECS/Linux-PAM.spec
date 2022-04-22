Name:		Linux-PAM
Version:	1.5.2
Release:        1%{?dist}
Summary:	Linux PAM (Pluggable Authentication Modules for Linux) project

License:	BSD
URL:		https://github.com/linux-pam/linux-pam
Source0:	https://github.com/linux-pam/linux-pam/releases/download/v%{version}/Linux-PAM-%{version}.tar.xz

#BuildRequires:
#Requires:

%description
Linux PAM (Pluggable Authentication Modules for Linux) project 

%prep
%setup -q

%build
%configure --includedir=/usr/include/security --libdir=/lib --sbindir=/sbin --bindir=/bin --with-pkg-config-libdir=/usr/lib/pkgconfig
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
%make_install
%{__rm} -f %{buildroot}/usr/share/info/dir
%{__rm} -f %{buildroot}/usr/lib/systemd/system/pam_namespace.service

#%post
#/sbin/ldconfig
#/sbin/install-info /usr/share/info/DevIL_manual.info.gz /usr/share/info/dir 2> /dev/null || :

#%postun
#/sbin/ldconfig
#/sbin/install-info --delete /usr/share/info/DevIL_manual.info.gz /usr/share/info/dir 2> /dev/null || :

%files
/etc/environment
/etc/security/access.conf
/etc/security/faillock.conf
/etc/security/group.conf
/etc/security/limits.conf
/etc/security/namespace.conf
/etc/security/namespace.init
/etc/security/pam_env.conf
/etc/security/time.conf
#/lib/libpam.la
/lib/libpam.so
/lib/libpam.so.0
/lib/libpam.so.0.85.1
#/lib/libpam_misc.la
/lib/libpam_misc.so
/lib/libpam_misc.so.0
/lib/libpam_misc.so.0.82.1
#/lib/libpamc.la
/lib/libpamc.so
/lib/libpamc.so.0
/lib/libpamc.so.0.82.1
/lib/pkgconfig/pam.pc
/lib/pkgconfig/pam_misc.pc
/lib/pkgconfig/pamc.pc
#/lib/security/pam_access.la
/lib/security/pam_access.so
#/lib/security/pam_debug.la
/lib/security/pam_debug.so
#/lib/security/pam_deny.la
/lib/security/pam_deny.so
#/lib/security/pam_echo.la
/lib/security/pam_echo.so
#/lib/security/pam_env.la
/lib/security/pam_env.so
#/lib/security/pam_exec.la
/lib/security/pam_exec.so
#/lib/security/pam_faildelay.la
/lib/security/pam_faildelay.so
#/lib/security/pam_faillock.la
/lib/security/pam_faillock.so
#/lib/security/pam_filter.la
/lib/security/pam_filter.so
/lib/security/pam_filter/upperLOWER
#/lib/security/pam_ftp.la
/lib/security/pam_ftp.so
#/lib/security/pam_group.la
/lib/security/pam_group.so
#/lib/security/pam_issue.la
/lib/security/pam_issue.so
#/lib/security/pam_keyinit.la
/lib/security/pam_keyinit.so
#/lib/security/pam_lastlog.la
/lib/security/pam_lastlog.so
#/lib/security/pam_limits.la
/lib/security/pam_limits.so
#/lib/security/pam_listfile.la
/lib/security/pam_listfile.so
#/lib/security/pam_localuser.la
/lib/security/pam_localuser.so
#/lib/security/pam_loginuid.la
/lib/security/pam_loginuid.so
#/lib/security/pam_mail.la
/lib/security/pam_mail.so
#/lib/security/pam_mkhomedir.la
/lib/security/pam_mkhomedir.so
#/lib/security/pam_motd.la
/lib/security/pam_motd.so
#/lib/security/pam_namespace.la
/lib/security/pam_namespace.so
#/lib/security/pam_nologin.la
/lib/security/pam_nologin.so
#/lib/security/pam_permit.la
/lib/security/pam_permit.so
#/lib/security/pam_pwhistory.la
/lib/security/pam_pwhistory.so
#/lib/security/pam_rhosts.la
/lib/security/pam_rhosts.so
#/lib/security/pam_rootok.la
/lib/security/pam_rootok.so
#/lib/security/pam_securetty.la
/lib/security/pam_securetty.so
#/lib/security/pam_setquota.la
/lib/security/pam_setquota.so
#/lib/security/pam_shells.la
/lib/security/pam_shells.so
#/lib/security/pam_stress.la
/lib/security/pam_stress.so
#/lib/security/pam_succeed_if.la
/lib/security/pam_succeed_if.so
#/lib/security/pam_time.la
/lib/security/pam_time.so
#/lib/security/pam_timestamp.la
/lib/security/pam_timestamp.so
#/lib/security/pam_umask.la
/lib/security/pam_umask.so
#/lib/security/pam_unix.la
/lib/security/pam_unix.so
#/lib/security/pam_userdb.la
/lib/security/pam_userdb.so
#/lib/security/pam_usertype.la
/lib/security/pam_usertype.so
#/lib/security/pam_warn.la
/lib/security/pam_warn.so
#/lib/security/pam_wheel.la
/lib/security/pam_wheel.so
#/lib/security/pam_xauth.la
/lib/security/pam_xauth.so
/sbin/faillock
/sbin/mkhomedir_helper
/sbin/pam_namespace_helper
/sbin/pam_timestamp_check
/sbin/pwhistory_helper
/sbin/unix_chkpwd
/sbin/unix_update
/usr/include/security/_pam_compat.h
/usr/include/security/_pam_macros.h
/usr/include/security/_pam_types.h
/usr/include/security/pam_appl.h
/usr/include/security/pam_client.h
/usr/include/security/pam_ext.h
/usr/include/security/pam_filter.h
/usr/include/security/pam_misc.h
/usr/include/security/pam_modules.h
/usr/include/security/pam_modutil.h
/usr/share/doc/Linux-PAM/draft-morgan-pam-current.txt
/usr/share/doc/Linux-PAM/index.html
/usr/share/doc/Linux-PAM/rfc86.0.txt
/usr/share/locale/af/LC_MESSAGES/Linux-PAM.mo
/usr/share/locale/am/LC_MESSAGES/Linux-PAM.mo
/usr/share/locale/ar/LC_MESSAGES/Linux-PAM.mo
/usr/share/locale/as/LC_MESSAGES/Linux-PAM.mo
/usr/share/locale/az/LC_MESSAGES/Linux-PAM.mo
/usr/share/locale/be/LC_MESSAGES/Linux-PAM.mo
/usr/share/locale/bg/LC_MESSAGES/Linux-PAM.mo
/usr/share/locale/bn/LC_MESSAGES/Linux-PAM.mo
/usr/share/locale/bn_IN/LC_MESSAGES/Linux-PAM.mo
/usr/share/locale/bs/LC_MESSAGES/Linux-PAM.mo
/usr/share/locale/ca/LC_MESSAGES/Linux-PAM.mo
/usr/share/locale/cs/LC_MESSAGES/Linux-PAM.mo
/usr/share/locale/cy/LC_MESSAGES/Linux-PAM.mo
/usr/share/locale/da/LC_MESSAGES/Linux-PAM.mo
/usr/share/locale/de/LC_MESSAGES/Linux-PAM.mo
/usr/share/locale/de_CH/LC_MESSAGES/Linux-PAM.mo
/usr/share/locale/el/LC_MESSAGES/Linux-PAM.mo
/usr/share/locale/eo/LC_MESSAGES/Linux-PAM.mo
/usr/share/locale/es/LC_MESSAGES/Linux-PAM.mo
/usr/share/locale/et/LC_MESSAGES/Linux-PAM.mo
/usr/share/locale/eu/LC_MESSAGES/Linux-PAM.mo
/usr/share/locale/fa/LC_MESSAGES/Linux-PAM.mo
/usr/share/locale/fi/LC_MESSAGES/Linux-PAM.mo
/usr/share/locale/fr/LC_MESSAGES/Linux-PAM.mo
/usr/share/locale/ga/LC_MESSAGES/Linux-PAM.mo
/usr/share/locale/gl/LC_MESSAGES/Linux-PAM.mo
/usr/share/locale/gu/LC_MESSAGES/Linux-PAM.mo
/usr/share/locale/he/LC_MESSAGES/Linux-PAM.mo
/usr/share/locale/hi/LC_MESSAGES/Linux-PAM.mo
/usr/share/locale/hr/LC_MESSAGES/Linux-PAM.mo
/usr/share/locale/hu/LC_MESSAGES/Linux-PAM.mo
/usr/share/locale/ia/LC_MESSAGES/Linux-PAM.mo
/usr/share/locale/id/LC_MESSAGES/Linux-PAM.mo
/usr/share/locale/is/LC_MESSAGES/Linux-PAM.mo
/usr/share/locale/it/LC_MESSAGES/Linux-PAM.mo
/usr/share/locale/ja/LC_MESSAGES/Linux-PAM.mo
/usr/share/locale/ka/LC_MESSAGES/Linux-PAM.mo
/usr/share/locale/kk/LC_MESSAGES/Linux-PAM.mo
/usr/share/locale/km/LC_MESSAGES/Linux-PAM.mo
/usr/share/locale/kn/LC_MESSAGES/Linux-PAM.mo
/usr/share/locale/ko/LC_MESSAGES/Linux-PAM.mo
/usr/share/locale/kw_GB/LC_MESSAGES/Linux-PAM.mo
/usr/share/locale/ky/LC_MESSAGES/Linux-PAM.mo
/usr/share/locale/lt/LC_MESSAGES/Linux-PAM.mo
/usr/share/locale/lv/LC_MESSAGES/Linux-PAM.mo
/usr/share/locale/mk/LC_MESSAGES/Linux-PAM.mo
/usr/share/locale/ml/LC_MESSAGES/Linux-PAM.mo
/usr/share/locale/mn/LC_MESSAGES/Linux-PAM.mo
/usr/share/locale/mr/LC_MESSAGES/Linux-PAM.mo
/usr/share/locale/ms/LC_MESSAGES/Linux-PAM.mo
/usr/share/locale/my/LC_MESSAGES/Linux-PAM.mo
/usr/share/locale/nb/LC_MESSAGES/Linux-PAM.mo
/usr/share/locale/ne/LC_MESSAGES/Linux-PAM.mo
/usr/share/locale/nl/LC_MESSAGES/Linux-PAM.mo
/usr/share/locale/nn/LC_MESSAGES/Linux-PAM.mo
/usr/share/locale/or/LC_MESSAGES/Linux-PAM.mo
/usr/share/locale/pa/LC_MESSAGES/Linux-PAM.mo
/usr/share/locale/pl/LC_MESSAGES/Linux-PAM.mo
/usr/share/locale/pt/LC_MESSAGES/Linux-PAM.mo
/usr/share/locale/pt_BR/LC_MESSAGES/Linux-PAM.mo
/usr/share/locale/ro/LC_MESSAGES/Linux-PAM.mo
/usr/share/locale/ru/LC_MESSAGES/Linux-PAM.mo
/usr/share/locale/si/LC_MESSAGES/Linux-PAM.mo
/usr/share/locale/sk/LC_MESSAGES/Linux-PAM.mo
/usr/share/locale/sl/LC_MESSAGES/Linux-PAM.mo
/usr/share/locale/sq/LC_MESSAGES/Linux-PAM.mo
/usr/share/locale/sr/LC_MESSAGES/Linux-PAM.mo
/usr/share/locale/sr@latin/LC_MESSAGES/Linux-PAM.mo
/usr/share/locale/sv/LC_MESSAGES/Linux-PAM.mo
/usr/share/locale/ta/LC_MESSAGES/Linux-PAM.mo
/usr/share/locale/te/LC_MESSAGES/Linux-PAM.mo
/usr/share/locale/tg/LC_MESSAGES/Linux-PAM.mo
/usr/share/locale/th/LC_MESSAGES/Linux-PAM.mo
/usr/share/locale/tr/LC_MESSAGES/Linux-PAM.mo
/usr/share/locale/uk/LC_MESSAGES/Linux-PAM.mo
/usr/share/locale/ur/LC_MESSAGES/Linux-PAM.mo
/usr/share/locale/vi/LC_MESSAGES/Linux-PAM.mo
/usr/share/locale/yo/LC_MESSAGES/Linux-PAM.mo
/usr/share/locale/zh_CN/LC_MESSAGES/Linux-PAM.mo
/usr/share/locale/zh_HK/LC_MESSAGES/Linux-PAM.mo
/usr/share/locale/zh_TW/LC_MESSAGES/Linux-PAM.mo
/usr/share/locale/zu/LC_MESSAGES/Linux-PAM.mo
/usr/share/man/man3/misc_conv.3.gz
/usr/share/man/man3/pam.3.gz
/usr/share/man/man3/pam_acct_mgmt.3.gz
/usr/share/man/man3/pam_authenticate.3.gz
/usr/share/man/man3/pam_chauthtok.3.gz
/usr/share/man/man3/pam_close_session.3.gz
/usr/share/man/man3/pam_conv.3.gz
/usr/share/man/man3/pam_end.3.gz
/usr/share/man/man3/pam_error.3.gz
/usr/share/man/man3/pam_fail_delay.3.gz
/usr/share/man/man3/pam_get_authtok.3.gz
/usr/share/man/man3/pam_get_authtok_noverify.3.gz
/usr/share/man/man3/pam_get_authtok_verify.3.gz
/usr/share/man/man3/pam_get_data.3.gz
/usr/share/man/man3/pam_get_item.3.gz
/usr/share/man/man3/pam_get_user.3.gz
/usr/share/man/man3/pam_getenv.3.gz
/usr/share/man/man3/pam_getenvlist.3.gz
/usr/share/man/man3/pam_info.3.gz
/usr/share/man/man3/pam_misc_drop_env.3.gz
/usr/share/man/man3/pam_misc_paste_env.3.gz
/usr/share/man/man3/pam_misc_setenv.3.gz
/usr/share/man/man3/pam_open_session.3.gz
/usr/share/man/man3/pam_prompt.3.gz
/usr/share/man/man3/pam_putenv.3.gz
/usr/share/man/man3/pam_set_data.3.gz
/usr/share/man/man3/pam_set_item.3.gz
/usr/share/man/man3/pam_setcred.3.gz
/usr/share/man/man3/pam_sm_acct_mgmt.3.gz
/usr/share/man/man3/pam_sm_authenticate.3.gz
/usr/share/man/man3/pam_sm_chauthtok.3.gz
/usr/share/man/man3/pam_sm_close_session.3.gz
/usr/share/man/man3/pam_sm_open_session.3.gz
/usr/share/man/man3/pam_sm_setcred.3.gz
/usr/share/man/man3/pam_start.3.gz
/usr/share/man/man3/pam_strerror.3.gz
/usr/share/man/man3/pam_syslog.3.gz
/usr/share/man/man3/pam_verror.3.gz
/usr/share/man/man3/pam_vinfo.3.gz
/usr/share/man/man3/pam_vprompt.3.gz
/usr/share/man/man3/pam_vsyslog.3.gz
/usr/share/man/man3/pam_xauth_data.3.gz
/usr/share/man/man5/access.conf.5.gz
/usr/share/man/man5/environment.5.gz
/usr/share/man/man5/faillock.conf.5.gz
/usr/share/man/man5/group.conf.5.gz
/usr/share/man/man5/limits.conf.5.gz
/usr/share/man/man5/namespace.conf.5.gz
/usr/share/man/man5/pam.conf.5.gz
/usr/share/man/man5/pam.d.5.gz
/usr/share/man/man5/pam_env.conf.5.gz
/usr/share/man/man5/time.conf.5.gz
/usr/share/man/man8/PAM.8.gz
/usr/share/man/man8/faillock.8.gz
/usr/share/man/man8/mkhomedir_helper.8.gz
/usr/share/man/man8/pam.8.gz
/usr/share/man/man8/pam_access.8.gz
/usr/share/man/man8/pam_debug.8.gz
/usr/share/man/man8/pam_deny.8.gz
/usr/share/man/man8/pam_echo.8.gz
/usr/share/man/man8/pam_env.8.gz
/usr/share/man/man8/pam_exec.8.gz
/usr/share/man/man8/pam_faildelay.8.gz
/usr/share/man/man8/pam_faillock.8.gz
/usr/share/man/man8/pam_filter.8.gz
/usr/share/man/man8/pam_ftp.8.gz
/usr/share/man/man8/pam_group.8.gz
/usr/share/man/man8/pam_issue.8.gz
/usr/share/man/man8/pam_keyinit.8.gz
/usr/share/man/man8/pam_lastlog.8.gz
/usr/share/man/man8/pam_limits.8.gz
/usr/share/man/man8/pam_listfile.8.gz
/usr/share/man/man8/pam_localuser.8.gz
/usr/share/man/man8/pam_loginuid.8.gz
/usr/share/man/man8/pam_mail.8.gz
/usr/share/man/man8/pam_mkhomedir.8.gz
/usr/share/man/man8/pam_motd.8.gz
/usr/share/man/man8/pam_namespace.8.gz
/usr/share/man/man8/pam_namespace_helper.8.gz
/usr/share/man/man8/pam_nologin.8.gz
/usr/share/man/man8/pam_permit.8.gz
/usr/share/man/man8/pam_pwhistory.8.gz
/usr/share/man/man8/pam_rhosts.8.gz
/usr/share/man/man8/pam_rootok.8.gz
/usr/share/man/man8/pam_securetty.8.gz
/usr/share/man/man8/pam_setquota.8.gz
/usr/share/man/man8/pam_shells.8.gz
/usr/share/man/man8/pam_stress.8.gz
/usr/share/man/man8/pam_succeed_if.8.gz
/usr/share/man/man8/pam_time.8.gz
/usr/share/man/man8/pam_timestamp.8.gz
/usr/share/man/man8/pam_timestamp_check.8.gz
/usr/share/man/man8/pam_umask.8.gz
/usr/share/man/man8/pam_unix.8.gz
/usr/share/man/man8/pam_userdb.8.gz
/usr/share/man/man8/pam_usertype.8.gz
/usr/share/man/man8/pam_warn.8.gz
/usr/share/man/man8/pam_wheel.8.gz
/usr/share/man/man8/pam_xauth.8.gz
/usr/share/man/man8/pwhistory_helper.8.gz
/usr/share/man/man8/unix_chkpwd.8.gz
/usr/share/man/man8/unix_update.8.gz


%doc

%changelog
* Tue May 31 2016 Adam Miller <maxamillion@fedoraproject.org>
-

# see /usr/libexec/rpm/macros for macros
