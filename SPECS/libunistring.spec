Name:           libunistring
Version:	0.9.10
Release:        1%{?dist}
Summary:	Library for manipulating Unicode and C strings according to Unicode standard

License:	LGPL-3 GPL-3
URL:		https://www.gnu.org/software/libunistring/
Source0:	https://ftp.gnu.org/gnu/libunistring/libunistring-%{version}.tar.gz

#BuildRequires:
#Requires:

%description

%prep
%setup -q

%build
%configure --libdir=/usr/lib
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
/usr/include/unicase.h
/usr/include/uniconv.h
/usr/include/unictype.h
/usr/include/unigbrk.h
/usr/include/unilbrk.h
/usr/include/uniname.h
/usr/include/uninorm.h
/usr/include/unistdio.h
/usr/include/unistr.h
/usr/include/unistring/cdefs.h
/usr/include/unistring/iconveh.h
/usr/include/unistring/inline.h
/usr/include/unistring/localcharset.h
/usr/include/unistring/stdbool.h
/usr/include/unistring/stdint.h
/usr/include/unistring/version.h
/usr/include/unistring/woe32dll.h
/usr/include/unitypes.h
/usr/include/uniwbrk.h
/usr/include/uniwidth.h
/usr/lib/libunistring.a
/usr/lib/libunistring.la
/usr/lib/libunistring.so
/usr/lib/libunistring.so.2
/usr/lib/libunistring.so.2.1.0
/usr/share/doc/libunistring/libunistring_1.html
/usr/share/doc/libunistring/libunistring_10.html
/usr/share/doc/libunistring/libunistring_11.html
/usr/share/doc/libunistring/libunistring_12.html
/usr/share/doc/libunistring/libunistring_13.html
/usr/share/doc/libunistring/libunistring_14.html
/usr/share/doc/libunistring/libunistring_15.html
/usr/share/doc/libunistring/libunistring_16.html
/usr/share/doc/libunistring/libunistring_17.html
/usr/share/doc/libunistring/libunistring_18.html
/usr/share/doc/libunistring/libunistring_19.html
/usr/share/doc/libunistring/libunistring_2.html
/usr/share/doc/libunistring/libunistring_20.html
/usr/share/doc/libunistring/libunistring_21.html
/usr/share/doc/libunistring/libunistring_3.html
/usr/share/doc/libunistring/libunistring_4.html
/usr/share/doc/libunistring/libunistring_5.html
/usr/share/doc/libunistring/libunistring_6.html
/usr/share/doc/libunistring/libunistring_7.html
/usr/share/doc/libunistring/libunistring_8.html
/usr/share/doc/libunistring/libunistring_9.html
/usr/share/doc/libunistring/libunistring_abt.html
/usr/share/doc/libunistring/libunistring_toc.html
/usr/share/info/libunistring.info.gz

