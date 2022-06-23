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
	   --with-pkg-config-libdir=/usr/lib/pkgconfig

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
/usr/bin/idn2
/usr/include/idn2.h
/usr/lib/libidn2.a
/usr/lib/libidn2.so
/usr/lib/libidn2.so.0
/usr/lib/libidn2.so.0.3.7
/usr/lib/pkgconfig/libidn2.pc
/usr/share/locale/cs/LC_MESSAGES/libidn2.mo
/usr/share/locale/da/LC_MESSAGES/libidn2.mo
/usr/share/locale/de/LC_MESSAGES/libidn2.mo
/usr/share/locale/eo/LC_MESSAGES/libidn2.mo
/usr/share/locale/es/LC_MESSAGES/libidn2.mo
/usr/share/locale/fi/LC_MESSAGES/libidn2.mo
/usr/share/locale/fr/LC_MESSAGES/libidn2.mo
/usr/share/locale/fur/LC_MESSAGES/libidn2.mo
/usr/share/locale/hr/LC_MESSAGES/libidn2.mo
/usr/share/locale/hu/LC_MESSAGES/libidn2.mo
/usr/share/locale/id/LC_MESSAGES/libidn2.mo
/usr/share/locale/it/LC_MESSAGES/libidn2.mo
/usr/share/locale/ja/LC_MESSAGES/libidn2.mo
/usr/share/locale/nl/LC_MESSAGES/libidn2.mo
/usr/share/locale/pl/LC_MESSAGES/libidn2.mo
/usr/share/locale/pt_BR/LC_MESSAGES/libidn2.mo
/usr/share/locale/ro/LC_MESSAGES/libidn2.mo
/usr/share/locale/ru/LC_MESSAGES/libidn2.mo
/usr/share/locale/sr/LC_MESSAGES/libidn2.mo
/usr/share/locale/sv/LC_MESSAGES/libidn2.mo
/usr/share/locale/uk/LC_MESSAGES/libidn2.mo
/usr/share/locale/vi/LC_MESSAGES/libidn2.mo
/usr/share/locale/zh_CN/LC_MESSAGES/libidn2.mo

%changelog

