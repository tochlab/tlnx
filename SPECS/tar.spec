Name:           tar
Version:	1.35
Release:        1%{?dist}
Summary:	GNU Tar provides the ability to create tar archives

License:	GPL-3+
URL:		https://www.gnu.org/software/tar/
Source0:	https://ftpmirror.gnu.org/gnu/tar/tar-%{version}.tar.gz

#BuildRequires:
#Requires:

%description

%prep
%setup -q

%build
export FORCE_UNSAFE_CONFIGURE=1
%configure --prefix=/usr \
            --bindir=/bin \
	    --disable-nls
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
%make_install
rm -f $RPM_BUILD_ROOT/usr/share/info/dir

%files
/bin/tar
/usr/libexec/rmt
/usr/share/info/tar.info-1.gz
/usr/share/info/tar.info-2.gz
/usr/share/info/tar.info-3.gz
/usr/share/info/tar.info.gz
/usr/share/man/man1/tar.1.gz
/usr/share/man/man8/rmt.8.gz


%changelog
