Name:           libidn2
Version:	2.3.2
Release:        1%{?dist}
Summary:	An implementation of the IDNA2008 specifications (RFCs 5890, 5891, 5892, 5893)

License:	GPL-2+ LGPL-3+
URL:		https://www.gnu.org/software/libidn/#libidn2
Source0:	https://ftpmirror.gnu.org/gnu/libidn/libidn2-%{version}.tar.gz

#BuildRequires:
#Requires:

%description

%prep
%setup -q

%build
%configure --disable-doc \
	   --disable-gcc-warnings \
           --disable-gtk-doc \
	   --libdir=/usr/lib \
	   --with-pkg-config-libdir=/usr/lib/pkgconfig \
	    --disable-nls

make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
%make_install
%{__rm} -f %{buildroot}/usr/share/info/dir
find %{buildroot} -type f -name '*.la' -delete || die

#%post
#/sbin/ldconfig
#/sbin/install-info /usr/share/info/DevIL_manual.info.gz /usr/share/info/dir 2> /dev/null || :

#%postun
#/sbin/ldconfig
#/sbin/install-info --delete /usr/share/info/DevIL_manual.info.gz /usr/share/info/dir 2> /dev/null || :

%files
/usr/bin/idn2
/usr/include/idn2.h
/usr/lib/libidn2.a
/usr/lib/libidn2.so
/usr/lib/libidn2.so.0
/usr/lib/libidn2.so.0.3.7
/usr/lib/pkgconfig/libidn2.pc

%changelog

