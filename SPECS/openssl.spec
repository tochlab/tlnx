Name:           openssl
Version:	3.0.12
Release:        1%{?dist}
Summary:	full-strength general purpose cryptography library (including SSL and TLS)

License:	openssl
URL:		https://www.openssl.org/
Source0:	https://www.openssl.org/source/openssl-%{version}.tar.gz

#BuildRequires:
#Requires:

%description

%prep
%setup -q

%build
./config --prefix=/usr         \
         --openssldir=/etc/ssl \
         --libdir=lib          \
         shared                \
         zlib-dynamic

make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
%make_install
%{__rm} -f %{buildroot}/usr/share/man/man1/passwd.1

%files


%changelog
