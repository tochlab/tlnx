Name:           bzip2
Version:        1.0.8
Release:        1%{?dist}
Summary:        bzip2 archiver

License:        BSD
URL:            https://sourceware.org/pub/bzip2/bzip2-1.0.8.tar.gz
Source0:        https://sourceware.org/pub/bzip2/bzip2-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

#BuildRequires:  
#Requires:       

%description


%prep
%setup -q
sed -i 's@\(ln -s -f \)$(PREFIX)/bin/@\1@' Makefile
sed -i "s@(PREFIX)/man@(PREFIX)/share/man@g" Makefile
make -f Makefile-libbz2_so


%build
make -f Makefile-libbz2_so
make



%install
rm -rf $RPM_BUILD_ROOT
#make install PREFIX=%{buildroot}
mkdir -p %{buildroot}/lib
mkdir -p %{buildroot}/usr/include
cp -av bzlib.h %{buildroot}/usr/include
mkdir -p %{buildroot}/bin
cp libbz2.so.* %{buildroot}/lib
cp -av bzdiff bzgrep bzmore bzip2 bzip2recover %{buildroot}/bin
cd %{buildroot}/bin
ln -sf bzip2 bunzip2
ln -sf bzip2 bzcat
ln -sf bzdiff bzcmp
ln -sf bzgrep bzegrep
ln -sf bzgrep bzfgrep
ln -sf bzmore bzless
cd %{buildroot}/lib
ln -sf libbz2.so.1.0 libbz2.so.1
ln -sf libbz2.so.1.0 libbz2.so

%clean
rm -rf $RPM_BUILD_ROOT


%files
%{!?_licensedir:%global license %%doc}
#%license add-license-file-here
#%doc add-docs-here
/bin/bunzip2
/bin/bzcat
/bin/bzip2
/lib/libbz2.so
/lib/libbz2.so.1
/lib/libbz2.so.1.0
/lib/libbz2.so.%{version}
/bin/bzcmp
/bin/bzdiff
/bin/bzegrep
/bin/bzfgrep
/bin/bzgrep
/bin/bzip2recover
/bin/bzless
/bin/bzmore
/usr/include/bzlib.h

%changelog
