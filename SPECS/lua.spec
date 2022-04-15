Name:           lua
Version:	5.4.4
Release:        1%{?dist}
Summary:	A powerful light-weight programming language designed for extending applications

License:	MIT
URL:		https://www.lua.org/
Source0:	https://www.lua.org/ftp/lua-%{version}.tar.gz
Patch0:         lua-makefile.patch

#BuildRequires:
#Requires:

%description

%prep
%setup -q
%patch0 -p1

%build
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
%make_install INSTALL_TOP=%{buildroot}/usr
%{__rm} -f %{buildroot}/usr/share/info/dir

#%post
#/sbin/ldconfig
#/sbin/install-info /usr/share/info/DevIL_manual.info.gz /usr/share/info/dir 2> /dev/null || :

#%postun
#/sbin/ldconfig
#/sbin/install-info --delete /usr/share/info/DevIL_manual.info.gz /usr/share/info/dir 2> /dev/null || :

%files
/usr/bin/lua
/usr/bin/luac
/usr/include/lauxlib.h
/usr/include/lua.h
/usr/include/lua.hpp
/usr/include/luaconf.h
/usr/include/lualib.h
/usr/lib/liblua.a
/usr/lib/liblua.so
/usr/man/man1/lua.1.gz
/usr/man/man1/luac.1.gz

%changelog
* Tue May 31 2016 Adam Miller <maxamillion@fedoraproject.org>
-

# see /usr/libexec/rpm/macros for macros
