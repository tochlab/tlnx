Name:           gawk
Version:	5.1.1
Release:        1%{?dist}
Summary:	GNU awk pattern-matching language

License:	GPL-2
URL:		https://www.gnu.org/software/gawk/gawk.html
Source0:	https://ftpmirror.gnu.org/gnu/gawk/gawk-%{version}.tar.gz

#BuildRequires:
#Requires:

%description

%prep
%setup -q

%build
%configure --prefix=/usr --libdir=/usr/lib --disable-nls
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
%make_install
rm -rf $RPM_BUILD_ROOT/usr/share/info/dir

%files
/usr/bin/awk
/usr/bin/gawk
/usr/bin/gawk-%{version}
/etc/profile.d/gawk.csh
/etc/profile.d/gawk.sh
/usr/include/gawkapi.h
/usr/lib/gawk/filefuncs.so
/usr/lib/gawk/fnmatch.so
/usr/lib/gawk/fork.so
/usr/lib/gawk/inplace.so
/usr/lib/gawk/intdiv.so
/usr/lib/gawk/ordchr.so
/usr/lib/gawk/readdir.so
/usr/lib/gawk/readfile.so
/usr/lib/gawk/revoutput.so
/usr/lib/gawk/revtwoway.so
/usr/lib/gawk/rwarray.so
/usr/lib/gawk/time.so
/usr/libexec/awk/grcat
/usr/libexec/awk/pwcat
/usr/share/awk/assert.awk
/usr/share/awk/bits2str.awk
/usr/share/awk/cliff_rand.awk
/usr/share/awk/ctime.awk
/usr/share/awk/ftrans.awk
/usr/share/awk/getopt.awk
/usr/share/awk/gettime.awk
/usr/share/awk/group.awk
/usr/share/awk/have_mpfr.awk
/usr/share/awk/inplace.awk
/usr/share/awk/intdiv0.awk
/usr/share/awk/join.awk
/usr/share/awk/libintl.awk
/usr/share/awk/noassign.awk
/usr/share/awk/ns_passwd.awk
/usr/share/awk/ord.awk
/usr/share/awk/passwd.awk
/usr/share/awk/processarray.awk
/usr/share/awk/quicksort.awk
/usr/share/awk/readable.awk
/usr/share/awk/readfile.awk
/usr/share/awk/rewind.awk
/usr/share/awk/round.awk
/usr/share/awk/shellquote.awk
/usr/share/awk/strtonum.awk
/usr/share/awk/walkarray.awk
/usr/share/awk/zerofile.awk
/usr/share/info/gawk.info.gz
/usr/share/info/gawkinet.info.gz
/usr/share/info/gawkworkflow.info.gz
/usr/share/man/man1/gawk.1.gz
/usr/share/man/man3/filefuncs.3am.gz
/usr/share/man/man3/fnmatch.3am.gz
/usr/share/man/man3/fork.3am.gz
/usr/share/man/man3/inplace.3am.gz
/usr/share/man/man3/ordchr.3am.gz
/usr/share/man/man3/readdir.3am.gz
/usr/share/man/man3/readfile.3am.gz
/usr/share/man/man3/revoutput.3am.gz
/usr/share/man/man3/revtwoway.3am.gz
/usr/share/man/man3/rwarray.3am.gz
/usr/share/man/man3/time.3am.gz
/usr/share/awk/isnumeric.awk

%changelog
