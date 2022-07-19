Name:           libxml2
Version:	2.9.13
Release:        1%{?dist}
Summary:	XML C parser and toolkit

License:	MIT
URL:		http://www.xmlsoft.org
Source0:	https://gitlab.gnome.org/GNOME/libxml2/-/archive/v%{version}/libxml2-v%{version}.tar.gz

#BuildRequires:
#Requires:

%description
XML C parser and toolkit

%prep
tar xf %{_sourcedir}/libxml2-v%{version}.tar.gz
cd libxml2-v%{version}

%build
cd libxml2-v%{version}
./autogen.sh
%configure --disable-python --disable-static
#make %{?_smp_mflags}
make

%install
rm -rf $RPM_BUILD_ROOT
cd libxml2-v%{version}
%make_install
%{__rm} -f %{buildroot}/usr/share/info/dir
%{__rm} -fr %{buildroot}/usr/share/doc
%{__rm} -fr %{buildroot}/usr/share/gtk-doc
find %{buildroot} -type f -name '*.la' -delete || die

#%post
#/sbin/ldconfig
#/sbin/install-info /usr/share/info/DevIL_manual.info.gz /usr/share/info/dir 2> /dev/null || :

#%postun
#/sbin/ldconfig
#/sbin/install-info --delete /usr/share/info/DevIL_manual.info.gz /usr/share/info/dir 2> /dev/null || :

%files
/usr/bin/xml2-config
/usr/bin/xmlcatalog
/usr/bin/xmllint
/usr/include/libxml2/libxml/DOCBparser.h
/usr/include/libxml2/libxml/HTMLparser.h
/usr/include/libxml2/libxml/HTMLtree.h
/usr/include/libxml2/libxml/SAX.h
/usr/include/libxml2/libxml/SAX2.h
/usr/include/libxml2/libxml/c14n.h
/usr/include/libxml2/libxml/catalog.h
/usr/include/libxml2/libxml/chvalid.h
/usr/include/libxml2/libxml/debugXML.h
/usr/include/libxml2/libxml/dict.h
/usr/include/libxml2/libxml/encoding.h
/usr/include/libxml2/libxml/entities.h
/usr/include/libxml2/libxml/globals.h
/usr/include/libxml2/libxml/hash.h
/usr/include/libxml2/libxml/list.h
/usr/include/libxml2/libxml/nanoftp.h
/usr/include/libxml2/libxml/nanohttp.h
/usr/include/libxml2/libxml/parser.h
/usr/include/libxml2/libxml/parserInternals.h
/usr/include/libxml2/libxml/pattern.h
/usr/include/libxml2/libxml/relaxng.h
/usr/include/libxml2/libxml/schemasInternals.h
/usr/include/libxml2/libxml/schematron.h
/usr/include/libxml2/libxml/threads.h
/usr/include/libxml2/libxml/tree.h
/usr/include/libxml2/libxml/uri.h
/usr/include/libxml2/libxml/valid.h
/usr/include/libxml2/libxml/xinclude.h
/usr/include/libxml2/libxml/xlink.h
/usr/include/libxml2/libxml/xmlIO.h
/usr/include/libxml2/libxml/xmlautomata.h
/usr/include/libxml2/libxml/xmlerror.h
/usr/include/libxml2/libxml/xmlexports.h
/usr/include/libxml2/libxml/xmlmemory.h
/usr/include/libxml2/libxml/xmlmodule.h
/usr/include/libxml2/libxml/xmlreader.h
/usr/include/libxml2/libxml/xmlregexp.h
/usr/include/libxml2/libxml/xmlsave.h
/usr/include/libxml2/libxml/xmlschemas.h
/usr/include/libxml2/libxml/xmlschemastypes.h
/usr/include/libxml2/libxml/xmlstring.h
/usr/include/libxml2/libxml/xmlunicode.h
/usr/include/libxml2/libxml/xmlversion.h
/usr/include/libxml2/libxml/xmlwriter.h
/usr/include/libxml2/libxml/xpath.h
/usr/include/libxml2/libxml/xpathInternals.h
/usr/include/libxml2/libxml/xpointer.h
/usr/lib64/cmake/libxml2/libxml2-config.cmake
#/usr/lib64/libxml2.a
/usr/lib64/libxml2.so
/usr/lib64/libxml2.so.2
/usr/lib64/libxml2.so.2.9.13
/usr/lib64/pkgconfig/libxml-2.0.pc
/usr/lib64/xml2Conf.sh
/usr/share/aclocal/libxml.m4
/usr/share/man/man1/xml2-config.1.gz
/usr/share/man/man1/xmlcatalog.1.gz
/usr/share/man/man1/xmllint.1.gz
/usr/share/man/man3/libxml.3.gz

%doc

%changelog
