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
perl Makefile.PL PREFIX=/usr DESTDIR=%{buildroot} INSTALLPRIVLIB=/usr/lib/perl5/5.34 INSTALLSITELIB=/usr/lib/perl5/5.34 INSTALLVENDORLIB=/usr/lib/perl5/5.34 INSTALLARCHLIB=/usr/lib/perl5/5.34 INSTALLSITEARCH=/usr/lib/perl5/5.34 INSTALLVENDORARCH=/usr/lib/perl5/5.34
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install
rm $RPM_BUILD_ROOT/usr/lib/perl5/5.34/perllocal.pod
chmod +w $RPM_BUILD_ROOT/usr/lib/perl5/5.34/auto/XML/Parser/Expat/Expat.so
rm -fr %{buildroot}/usr/man/
rm -fr %{buildroot}/usr/share/man/

#if [ -e "%{buildroot}/usr/lib64" ]
#then
#mv -f %{buildroot}/usr/lib64 %{buildroot}/usr/lib
#fi


%files
/usr/lib/perl5/5.34/XML/Parser.pm
/usr/lib/perl5/5.34/XML/Parser/Encodings/Japanese_Encodings.msg
/usr/lib/perl5/5.34/XML/Parser/Encodings/README
/usr/lib/perl5/5.34/XML/Parser/Encodings/big5.enc
/usr/lib/perl5/5.34/XML/Parser/Encodings/euc-kr.enc
/usr/lib/perl5/5.34/XML/Parser/Encodings/ibm866.enc
/usr/lib/perl5/5.34/XML/Parser/Encodings/iso-8859-15.enc
/usr/lib/perl5/5.34/XML/Parser/Encodings/iso-8859-2.enc
/usr/lib/perl5/5.34/XML/Parser/Encodings/iso-8859-3.enc
/usr/lib/perl5/5.34/XML/Parser/Encodings/iso-8859-4.enc
/usr/lib/perl5/5.34/XML/Parser/Encodings/iso-8859-5.enc
/usr/lib/perl5/5.34/XML/Parser/Encodings/iso-8859-7.enc
/usr/lib/perl5/5.34/XML/Parser/Encodings/iso-8859-8.enc
/usr/lib/perl5/5.34/XML/Parser/Encodings/iso-8859-9.enc
/usr/lib/perl5/5.34/XML/Parser/Encodings/koi8-r.enc
/usr/lib/perl5/5.34/XML/Parser/Encodings/windows-1250.enc
/usr/lib/perl5/5.34/XML/Parser/Encodings/windows-1251.enc
/usr/lib/perl5/5.34/XML/Parser/Encodings/windows-1252.enc
/usr/lib/perl5/5.34/XML/Parser/Encodings/windows-1255.enc
/usr/lib/perl5/5.34/XML/Parser/Encodings/x-euc-jp-jisx0221.enc
/usr/lib/perl5/5.34/XML/Parser/Encodings/x-euc-jp-unicode.enc
/usr/lib/perl5/5.34/XML/Parser/Encodings/x-sjis-cp932.enc
/usr/lib/perl5/5.34/XML/Parser/Encodings/x-sjis-jdk117.enc
/usr/lib/perl5/5.34/XML/Parser/Encodings/x-sjis-jisx0221.enc
/usr/lib/perl5/5.34/XML/Parser/Encodings/x-sjis-unicode.enc
/usr/lib/perl5/5.34/XML/Parser/Expat.pm
/usr/lib/perl5/5.34/XML/Parser/LWPExternEnt.pl
/usr/lib/perl5/5.34/XML/Parser/Style/Debug.pm
/usr/lib/perl5/5.34/XML/Parser/Style/Objects.pm
/usr/lib/perl5/5.34/XML/Parser/Style/Stream.pm
/usr/lib/perl5/5.34/XML/Parser/Style/Subs.pm
/usr/lib/perl5/5.34/XML/Parser/Style/Tree.pm
/usr/lib/perl5/5.34/auto/XML/Parser/.packlist
/usr/lib/perl5/5.34/auto/XML/Parser/Expat/Expat.so

