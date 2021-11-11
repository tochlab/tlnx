Name:           libtirpc
Version:	1.3.2
Release:        2%{?dist}
Summary:	Transport Independent RPC library (SunRPC replacement)

License:	GPL-2
URL:		https://sourceforge.net/projects/libtirpc/
Source0:	https://deac-riga.dl.sourceforge.net/project/libtirpc/libtirpc/%{version}/libtirpc-%{version}.tar.bz2

#BuildRequires:
#Requires:

%description
Transport Independent RPC library (SunRPC replacement)

%prep
%setup -q

%build
%configure --libdir=/lib --disable-gssapi
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
/etc/bindresvport.blacklist
/etc/netconfig
/lib/libtirpc.a
/lib/libtirpc.la
/lib/libtirpc.so
/lib/libtirpc.so.3
/lib/libtirpc.so.3.0.0
/lib/pkgconfig/libtirpc.pc
/usr/include/tirpc/netconfig.h
/usr/include/tirpc/rpc/auth.h
/usr/include/tirpc/rpc/auth_des.h
/usr/include/tirpc/rpc/auth_unix.h
/usr/include/tirpc/rpc/clnt.h
/usr/include/tirpc/rpc/clnt_soc.h
/usr/include/tirpc/rpc/clnt_stat.h
/usr/include/tirpc/rpc/des.h
/usr/include/tirpc/rpc/des_crypt.h
/usr/include/tirpc/rpc/key_prot.h
/usr/include/tirpc/rpc/nettype.h
/usr/include/tirpc/rpc/pmap_clnt.h
/usr/include/tirpc/rpc/pmap_prot.h
/usr/include/tirpc/rpc/pmap_rmt.h
/usr/include/tirpc/rpc/raw.h
/usr/include/tirpc/rpc/rpc.h
/usr/include/tirpc/rpc/rpc_com.h
/usr/include/tirpc/rpc/rpc_msg.h
/usr/include/tirpc/rpc/rpcb_clnt.h
/usr/include/tirpc/rpc/rpcb_prot.h
/usr/include/tirpc/rpc/rpcb_prot.x
/usr/include/tirpc/rpc/rpcent.h
/usr/include/tirpc/rpc/svc.h
/usr/include/tirpc/rpc/svc_auth.h
/usr/include/tirpc/rpc/svc_dg.h
/usr/include/tirpc/rpc/svc_mt.h
/usr/include/tirpc/rpc/svc_soc.h
/usr/include/tirpc/rpc/types.h
/usr/include/tirpc/rpc/xdr.h
/usr/include/tirpc/rpcsvc/crypt.h
/usr/include/tirpc/rpcsvc/crypt.x
/usr/share/man/man3/bindresvport.3t.gz
/usr/share/man/man3/des_crypt.3t.gz
/usr/share/man/man3/getnetconfig.3t.gz
/usr/share/man/man3/getnetpath.3t.gz
/usr/share/man/man3/getrpcent.3t.gz
/usr/share/man/man3/getrpcport.3t.gz
/usr/share/man/man3/rpc.3t.gz
/usr/share/man/man3/rpc_clnt_auth.3t.gz
/usr/share/man/man3/rpc_clnt_calls.3t.gz
/usr/share/man/man3/rpc_clnt_create.3t.gz
/usr/share/man/man3/rpc_secure.3t.gz
/usr/share/man/man3/rpc_soc.3t.gz
/usr/share/man/man3/rpc_svc_calls.3t.gz
/usr/share/man/man3/rpc_svc_create.3t.gz
/usr/share/man/man3/rpc_svc_err.3t.gz
/usr/share/man/man3/rpc_svc_reg.3t.gz
/usr/share/man/man3/rpc_xdr.3t.gz
/usr/share/man/man3/rpcbind.3t.gz
/usr/share/man/man3/rtime.3t.gz
/usr/share/man/man5/netconfig.5.gz


%doc

%changelog
* Tue May 31 2016 Adam Miller <maxamillion@fedoraproject.org>
-

# see /usr/libexec/rpm/macros for macros
