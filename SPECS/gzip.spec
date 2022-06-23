Name:           gzip
Version:	1.12
Release:        1%{?dist}
Summary:	Standard GNU compressor

License:	GPL-3
URL:		https://www.gnu.org/software/gzip/
Source0:	https://ftpmirror.gnu.org/gnu/gzip/gzip-%{version}.tar.gz

#BuildRequires:
#Requires:

%description

%prep
%setup -q

%build
%configure --prefix=/usr --bindir=/bin
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
%make_install
rm -rf $RPM_BUILD_ROOT/usr/share/info/dir

%files
/bin/gunzip
/bin/gzexe
/bin/gzip
/bin/uncompress
/bin/zcat
/bin/zcmp
/bin/zdiff
/bin/zegrep
/bin/zfgrep
/bin/zforce
/bin/zgrep
/bin/zless
/bin/zmore
/bin/znew
/usr/share/info/gzip.info.gz
/usr/share/man/man1/gunzip.1.gz
/usr/share/man/man1/gzexe.1.gz
/usr/share/man/man1/gzip.1.gz
/usr/share/man/man1/zcat.1.gz
/usr/share/man/man1/zcmp.1.gz
/usr/share/man/man1/zdiff.1.gz
/usr/share/man/man1/zforce.1.gz
/usr/share/man/man1/zgrep.1.gz
/usr/share/man/man1/zless.1.gz
/usr/share/man/man1/zmore.1.gz
/usr/share/man/man1/znew.1.gz


%changelog
