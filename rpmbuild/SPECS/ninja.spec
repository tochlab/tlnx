Name:           ninja
Version:	1.10.0
Release:        1%{?dist}
Summary:	A small build system similar to make

License:	Apache-2.0
URL:		https://ninja-build.org/
Source0:	https://github.com/ninja-build/ninja/archive/v%{version}.tar.gz	

#BuildRequires:
#Requires:

%description

%prep
%setup -q

%build
python3 configure.py --bootstrap

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/bin
install -vm755 ninja $RPM_BUILD_ROOT/usr/bin/
install -vDm644 misc/bash-completion $RPM_BUILD_ROOT/usr/share/bash-completion/completions/ninja
install -vDm644 misc/zsh-completion  $RPM_BUILD_ROOT/usr/share/zsh/site-functions/_ninja

%files
/usr/bin/ninja
/usr/share/bash-completion/completions/ninja
/usr/share/zsh/site-functions/_ninja


%changelog
* Tue May 31 2016 Adam Miller <maxamillion@fedoraproject.org>
-

# see /usr/libexec/rpm/macros for macros
