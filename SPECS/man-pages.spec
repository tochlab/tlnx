Name:           man-pages
Version:	5.09
Release:        1
Summary:	Man page

License:	GPLv2
URL:		https://www.kernel.org/doc/man-pages/
Source0:	https://mirrors.edge.kernel.org/pub/linux/docs/man-pages/man-pages-%{version}.tar.gz
BuildArch:	noarch

%description

%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT
make install PREFIX=/usr DESTDIR=%{buildroot}

%files
/*

%changelog
