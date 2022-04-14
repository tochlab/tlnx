Name:           m4
Version:	1.4.19
Release:        1%{?dist}
Summary:	M4 is an implementation of the traditional Unix macro processor.

License:	GPL
URL:		http://www.gnu.org/software/m4/
Source0:	https://ftpmirror.gnu.org/gnu/m4/m4-%{version}.tar.gz

%description

%prep
%setup -q
#sed -i 's/IO_ftrylockfile/IO_EOF_SEEN/' lib/*.c
#echo "#define _IO_IN_BACKUP 0x100" >> lib/stdio-impl.h


%build
%configure --prefix=/usr
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
%{__rm} -f %{buildroot}/usr/share/info/dir

%files
/usr/bin/m4
/usr/share/info/m4.info-1.gz
/usr/share/info/m4.info-2.gz
/usr/share/info/m4.info.gz
/usr/share/man/man1/m4.1.gz
/usr/share/locale/bg/LC_MESSAGES/m4.mo
/usr/share/locale/cs/LC_MESSAGES/m4.mo
/usr/share/locale/da/LC_MESSAGES/m4.mo
/usr/share/locale/de/LC_MESSAGES/m4.mo
/usr/share/locale/el/LC_MESSAGES/m4.mo
/usr/share/locale/eo/LC_MESSAGES/m4.mo
/usr/share/locale/es/LC_MESSAGES/m4.mo
/usr/share/locale/fi/LC_MESSAGES/m4.mo
/usr/share/locale/fr/LC_MESSAGES/m4.mo
/usr/share/locale/ga/LC_MESSAGES/m4.mo
/usr/share/locale/gl/LC_MESSAGES/m4.mo
/usr/share/locale/hr/LC_MESSAGES/m4.mo
/usr/share/locale/id/LC_MESSAGES/m4.mo
/usr/share/locale/ja/LC_MESSAGES/m4.mo
/usr/share/locale/ko/LC_MESSAGES/m4.mo
/usr/share/locale/nl/LC_MESSAGES/m4.mo
/usr/share/locale/pl/LC_MESSAGES/m4.mo
/usr/share/locale/pt_BR/LC_MESSAGES/m4.mo
/usr/share/locale/ro/LC_MESSAGES/m4.mo
/usr/share/locale/ru/LC_MESSAGES/m4.mo
/usr/share/locale/sr/LC_MESSAGES/m4.mo
/usr/share/locale/sv/LC_MESSAGES/m4.mo
/usr/share/locale/uk/LC_MESSAGES/m4.mo
/usr/share/locale/vi/LC_MESSAGES/m4.mo
/usr/share/locale/zh_CN/LC_MESSAGES/m4.mo
/usr/share/locale/zh_TW/LC_MESSAGES/m4.mo
%changelog
