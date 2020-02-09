Name:           m4
Version:	1.4.18
Release:        1%{?dist}
Summary:	M4 is an implementation of the traditional Unix macro processor.

License:	GPL
URL:		http://www.gnu.org/software/m4/
Source0:	m4-1.4.18.tar.gz

%description

%prep
%setup -q
sed -i 's/IO_ftrylockfile/IO_EOF_SEEN/' lib/*.c
echo "#define _IO_IN_BACKUP 0x100" >> lib/stdio-impl.h


%build
./configure --prefix=/usr
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
%make_install

%files
/*

%changelog
