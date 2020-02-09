Name:           man-pages
Version:	5.01
Release:        1
Summary:	Man page

License:	GPLv2
URL:		https://www.kernel.org/doc/man-pages/
Source0:	man-pages-5.01.tar.xz
BuildArch:	noarch

%description

%prep
%setup -q

%build

%install
make install PREFIX=/usr DESTDIR=%{buildroot}

%files
/*

%changelog
