Name:           gcc
Version:        9.2.0
Release:        1%{?dist}
Summary:        gcc

#Group:          
License:        GPL
URL:            https://gcc.gnu.org/
Source0:        https://ftp.gnu.org/gnu/gcc/gcc-%{version}/gcc-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

#BuildRequires:  
#Requires:       

%description


%prep
%setup -q

%build
mkdir -v build
cd       build
../configure --prefix=/usr            \
             --enable-languages=c,c++ \
             --disable-multilib       \
             --disable-bootstrap      \
             --with-system-zlib

make %{?_smp_mflags}


%install
cd build
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
rm -rf $RPM_BUILD_ROOT/usr/lib/gcc/$(gcc -dumpmachine)/%{version}/include-fixed/bits/
#mkdir -pv $RPM_BUILD_ROOT/usr/share/gdb/auto-load/usr/lib
#mv -v $RPM_BUILD_ROOT/usr/lib/*gdb.py $RPM_BUILD_ROOT/usr/share/gdb/auto-load/usr/lib

%clean
rm -rf $RPM_BUILD_ROOT

%post
chown -v -R root:root \
    /usr/lib/gcc/*linux-gnu/%{version}/include{,-fixed}

ln -sv /usr/bin/cpp /lib
#ln -sv gcc /usr/bin/cc
install -v -dm755 /usr/lib/bfd-plugins
ln -sfv ../../libexec/gcc/$(gcc -dumpmachine)/%{version}/liblto_plugin.so \
        /usr/lib/bfd-plugins/
        
%files
/*


%changelog
