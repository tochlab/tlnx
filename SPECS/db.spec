Name:           db
Version:	5.3.28
Release:        1%{?dist}
Summary:	Oracle Berkeley DB

License:	Sleepycat
URL:		http://www.oracle.com/technetwork/database/database-technologies/berkeleydb/overview/index.html
Source0:	http://distfiles.gentoo.org/distfiles/c5/db-%{version}.tar.gz

#BuildRequires:
#Requires:

%description

%prep
%setup -q

%build
mkdir build
cd build
../dist/configure --program-prefix= \
		  --disable-dependency-tracking \
		  --prefix=/usr --exec-prefix=/usr \
		  --bindir=/usr/bin \
		  --sbindir=/usr/sbin \
		  --sysconfdir=/etc \
		  --datadir=/usr/share \
		  --includedir=/usr/include \
		  --libdir=/usr/lib \
		  --libexecdir=/usr/libexec \
		  --localstatedir=/var/lib \
		  --mandir=/usr/share/man \
		  --infodir=/usr/share/info \
		  --enable-compat185 \
		  --enable-dbm \
		  --enable-o_direct \
		  --without-uniquename \
		  --disable-sql \
		  --disable-sql_codegen \
		  --disable-sql_compat \
		  --disable-java \
		  --disable-tcl


make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
cd build
%make_install
%{__rm} -f %{buildroot}/usr/share/info/dir
%{__rm} -fr %{buildroot}/usr/docs

#%post
#/sbin/ldconfig
#/sbin/install-info /usr/share/info/DevIL_manual.info.gz /usr/share/info/dir 2> /dev/null || :

#%postun
#/sbin/ldconfig
#/sbin/install-info --delete /usr/share/info/DevIL_manual.info.gz /usr/share/info/dir 2> /dev/null || :

%files
/usr/bin/db_archive
/usr/bin/db_checkpoint
/usr/bin/db_deadlock
/usr/bin/db_dump
/usr/bin/db_hotbackup
/usr/bin/db_load
/usr/bin/db_log_verify
/usr/bin/db_printlog
/usr/bin/db_recover
/usr/bin/db_replicate
/usr/bin/db_stat
/usr/bin/db_tuner
/usr/bin/db_upgrade
/usr/bin/db_verify
/usr/include/db.h
/usr/include/db_185.h
/usr/include/db_cxx.h
/usr/lib/libdb-5.3.a
/usr/lib/libdb-5.3.la
/usr/lib/libdb-5.3.so
/usr/lib/libdb-5.so
/usr/lib/libdb.a
/usr/lib/libdb.so

%doc

%changelog
* Tue May 31 2016 Adam Miller <maxamillion@fedoraproject.org>
-

# see /usr/libexec/rpm/macros for macros
