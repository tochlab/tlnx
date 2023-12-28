Name:       	acl 
Version:	2.3.1
Release:        1%{?dist}
Summary:	access control list utilities, libraries and headers

License:	LGPL-2.1	
URL:		https://savannah.nongnu.org/projects/acl
Source0:	http://download.savannah.nongnu.org/releases/acl/acl-%{version}.tar.gz

#BuildRequires:
#Requires:

%description
access control list utilities, libraries and headers

%prep
%setup -q

%build
%configure --prefix=/usr         \
            --bindir=/bin         \
	    --libdir=/usr/lib     \
            --disable-static      \
            --libexecdir=/usr/lib \
            --docdir=/usr/share/doc/acl \
            --with-pkg-config-libdir=/usr/lib/pkgconfig \
	    --disable-nls

make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
%make_install
find %{buildroot} -type f -name '*.la' -delete || die

%files
/bin/chacl
/bin/getfacl
/bin/setfacl
/usr/include/acl/libacl.h
/usr/include/sys/acl.h
/usr/lib/libacl.so
/usr/lib/libacl.so.1
/usr/lib/libacl.so.1.1.2301
/usr/lib/pkgconfig/libacl.pc
/usr/share/doc/acl/CHANGES
/usr/share/doc/acl/COPYING
/usr/share/doc/acl/COPYING.LGPL
/usr/share/doc/acl/PORTING
/usr/share/doc/acl/extensions.txt
/usr/share/doc/acl/libacl.txt
/usr/share/man/man1/chacl.1.gz
/usr/share/man/man1/getfacl.1.gz
/usr/share/man/man1/setfacl.1.gz
/usr/share/man/man3/acl_add_perm.3.gz
/usr/share/man/man3/acl_calc_mask.3.gz
/usr/share/man/man3/acl_check.3.gz
/usr/share/man/man3/acl_clear_perms.3.gz
/usr/share/man/man3/acl_cmp.3.gz
/usr/share/man/man3/acl_copy_entry.3.gz
/usr/share/man/man3/acl_copy_ext.3.gz
/usr/share/man/man3/acl_copy_int.3.gz
/usr/share/man/man3/acl_create_entry.3.gz
/usr/share/man/man3/acl_delete_def_file.3.gz
/usr/share/man/man3/acl_delete_entry.3.gz
/usr/share/man/man3/acl_delete_perm.3.gz
/usr/share/man/man3/acl_dup.3.gz
/usr/share/man/man3/acl_entries.3.gz
/usr/share/man/man3/acl_equiv_mode.3.gz
/usr/share/man/man3/acl_error.3.gz
/usr/share/man/man3/acl_extended_fd.3.gz
/usr/share/man/man3/acl_extended_file.3.gz
/usr/share/man/man3/acl_extended_file_nofollow.3.gz
/usr/share/man/man3/acl_free.3.gz
/usr/share/man/man3/acl_from_mode.3.gz
/usr/share/man/man3/acl_from_text.3.gz
/usr/share/man/man3/acl_get_entry.3.gz
/usr/share/man/man3/acl_get_fd.3.gz
/usr/share/man/man3/acl_get_file.3.gz
/usr/share/man/man3/acl_get_perm.3.gz
/usr/share/man/man3/acl_get_permset.3.gz
/usr/share/man/man3/acl_get_qualifier.3.gz
/usr/share/man/man3/acl_get_tag_type.3.gz
/usr/share/man/man3/acl_init.3.gz
/usr/share/man/man3/acl_set_fd.3.gz
/usr/share/man/man3/acl_set_file.3.gz
/usr/share/man/man3/acl_set_permset.3.gz
/usr/share/man/man3/acl_set_qualifier.3.gz
/usr/share/man/man3/acl_set_tag_type.3.gz
/usr/share/man/man3/acl_size.3.gz
/usr/share/man/man3/acl_to_any_text.3.gz
/usr/share/man/man3/acl_to_text.3.gz
/usr/share/man/man3/acl_valid.3.gz
/usr/share/man/man5/acl.5.gz


%changelog
