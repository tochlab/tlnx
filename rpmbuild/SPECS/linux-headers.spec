Name: linux-headers
Version: 4.19.59
Release: 1
Summary: Header files for the Linux kernel for use by glibc
License: GPLv2
URL: https://www.kernel.org
Source0: linux-4.19.59.tar.xz

%description
Kernel-headers includes the C header files that specify the interface
between the Linux kernel and userspace libraries and programs.  The
header files define structures and constants that are needed for
building most standard programs and are also needed for rebuilding the
glibc package.

%prep
%setup -q -n linux-%{version}

%build
make mrproper
make INSTALL_HDR_PATH=dest headers_install
find dest/include \( -name .install -o -name ..install.cmd \) -delete
mkdir -p %{buildroot}/usr/include
cp -rv dest/include/* %{buildroot}/usr/include

%install

%files
/*

%changelog
# Nothing

