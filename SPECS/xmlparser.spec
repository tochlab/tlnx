Name:           XML-Parser
Version:	2.46
Release:        1%{?dist}
Summary:	A Perl extension interface to James Clark's XML parser, expat

License:	PERL
URL:		https://metacpan.org/pod/XML::Parser
Source0:	https://cpan.metacpan.org/authors/id/T/TO/TODDR/XML-Parser-%{version}.tar.gz

#BuildRequires:
#Requires:

%description

%prep
%setup -q

%build
perl Makefile.PL
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
%make_install

%files
/usr/local/lib64/perl5/5.30.1/perllocal.pod
/usr/local/lib64/perl5/5.30.1/x86_64-linux/XML/Parser.pm
/usr/local/lib64/perl5/5.30.1/x86_64-linux/XML/Parser/Encodings/Japanese_Encodings.msg
/usr/local/lib64/perl5/5.30.1/x86_64-linux/XML/Parser/Encodings/README
/usr/local/lib64/perl5/5.30.1/x86_64-linux/XML/Parser/Encodings/big5.enc
/usr/local/lib64/perl5/5.30.1/x86_64-linux/XML/Parser/Encodings/euc-kr.enc
/usr/local/lib64/perl5/5.30.1/x86_64-linux/XML/Parser/Encodings/ibm866.enc
/usr/local/lib64/perl5/5.30.1/x86_64-linux/XML/Parser/Encodings/iso-8859-15.enc
/usr/local/lib64/perl5/5.30.1/x86_64-linux/XML/Parser/Encodings/iso-8859-2.enc
/usr/local/lib64/perl5/5.30.1/x86_64-linux/XML/Parser/Encodings/iso-8859-3.enc
/usr/local/lib64/perl5/5.30.1/x86_64-linux/XML/Parser/Encodings/iso-8859-4.enc
/usr/local/lib64/perl5/5.30.1/x86_64-linux/XML/Parser/Encodings/iso-8859-5.enc
/usr/local/lib64/perl5/5.30.1/x86_64-linux/XML/Parser/Encodings/iso-8859-7.enc
/usr/local/lib64/perl5/5.30.1/x86_64-linux/XML/Parser/Encodings/iso-8859-8.enc
/usr/local/lib64/perl5/5.30.1/x86_64-linux/XML/Parser/Encodings/iso-8859-9.enc
/usr/local/lib64/perl5/5.30.1/x86_64-linux/XML/Parser/Encodings/koi8-r.enc
/usr/local/lib64/perl5/5.30.1/x86_64-linux/XML/Parser/Encodings/windows-1250.enc
/usr/local/lib64/perl5/5.30.1/x86_64-linux/XML/Parser/Encodings/windows-1251.enc
/usr/local/lib64/perl5/5.30.1/x86_64-linux/XML/Parser/Encodings/windows-1252.enc
/usr/local/lib64/perl5/5.30.1/x86_64-linux/XML/Parser/Encodings/windows-1255.enc
/usr/local/lib64/perl5/5.30.1/x86_64-linux/XML/Parser/Encodings/x-euc-jp-jisx0221.enc
/usr/local/lib64/perl5/5.30.1/x86_64-linux/XML/Parser/Encodings/x-euc-jp-unicode.enc
/usr/local/lib64/perl5/5.30.1/x86_64-linux/XML/Parser/Encodings/x-sjis-cp932.enc
/usr/local/lib64/perl5/5.30.1/x86_64-linux/XML/Parser/Encodings/x-sjis-jdk117.enc
/usr/local/lib64/perl5/5.30.1/x86_64-linux/XML/Parser/Encodings/x-sjis-jisx0221.enc
/usr/local/lib64/perl5/5.30.1/x86_64-linux/XML/Parser/Encodings/x-sjis-unicode.enc
/usr/local/lib64/perl5/5.30.1/x86_64-linux/XML/Parser/Expat.pm
/usr/local/lib64/perl5/5.30.1/x86_64-linux/XML/Parser/LWPExternEnt.pl
/usr/local/lib64/perl5/5.30.1/x86_64-linux/XML/Parser/Style/Debug.pm
/usr/local/lib64/perl5/5.30.1/x86_64-linux/XML/Parser/Style/Objects.pm
/usr/local/lib64/perl5/5.30.1/x86_64-linux/XML/Parser/Style/Stream.pm
/usr/local/lib64/perl5/5.30.1/x86_64-linux/XML/Parser/Style/Subs.pm
/usr/local/lib64/perl5/5.30.1/x86_64-linux/XML/Parser/Style/Tree.pm
/usr/local/lib64/perl5/5.30.1/x86_64-linux/auto/XML/Parser/.packlist
/usr/local/lib64/perl5/5.30.1/x86_64-linux/auto/XML/Parser/Expat/Expat.so
/usr/local/man/man3/XML::Parser.3pm
/usr/local/man/man3/XML::Parser::Expat.3pm
/usr/local/man/man3/XML::Parser::Style::Debug.3pm
/usr/local/man/man3/XML::Parser::Style::Objects.3pm
/usr/local/man/man3/XML::Parser::Style::Stream.3pm
/usr/local/man/man3/XML::Parser::Style::Subs.3pm
/usr/local/man/man3/XML::Parser::Style::Tree.3pm

%changelog
* Tue May 31 2016 Adam Miller <maxamillion@fedoraproject.org>
-

# see /usr/libexec/rpm/macros for macros
