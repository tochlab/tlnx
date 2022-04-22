Name:           rsync
Version:	3.2.4
Release:        1%{?dist}
Summary:	File transfer program to keep remote files into sync

License:	GPL-3
URL:		https://rsync.samba.org/
Source0:	https://download.samba.org/pub/rsync/src/rsync-3.2.4.tar.gz

#BuildRequires:
#Requires:

%description
File transfer program to keep remote files into sync

%prep
%setup -q

%build
%configure --disable-xxhash --disable-lz4
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
/usr/bin/rsync
/usr/bin/rsync-ssl
/usr/share/man/man1/rsync-ssl.1.gz
/usr/share/man/man1/rsync.1.gz
/usr/share/man/man5/rsyncd.conf.5.gz


%doc

%changelog
* Tue May 31 2016 Adam Miller <maxamillion@fedoraproject.org>
-

# see /usr/libexec/rpm/macros for macros
