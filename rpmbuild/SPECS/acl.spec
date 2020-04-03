Name:       	acl 
Version:	2.2.53
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
./configure --prefix=/usr         \
            --bindir=/bin         \
            --disable-static      \
            --libexecdir=/usr/lib \
            --docdir=/usr/share/doc/acl-%{version}

make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
%make_install

%files
/bin/chacl
/bin/getfacl
/bin/setfacl
/usr/include/acl/libacl.h
/usr/include/sys/acl.h
/usr/lib/libacl.la
/usr/lib/libacl.so
/usr/lib/libacl.so.1
/usr/lib/libacl.so.1.1.2253
/usr/lib/pkgconfig/libacl.pc
/usr/share/doc/acl-2.2.53/CHANGES
/usr/share/doc/acl-2.2.53/COPYING
/usr/share/doc/acl-2.2.53/COPYING.LGPL
/usr/share/doc/acl-2.2.53/PORTING
/usr/share/doc/acl-2.2.53/extensions.txt
/usr/share/doc/acl-2.2.53/libacl.txt
/usr/share/locale/de/LC_MESSAGES/acl.mo
/usr/share/locale/en@boldquot/LC_MESSAGES/acl.mo
/usr/share/locale/en@quot/LC_MESSAGES/acl.mo
/usr/share/locale/es/LC_MESSAGES/acl.mo
/usr/share/locale/fr/LC_MESSAGES/acl.mo
/usr/share/locale/gl/LC_MESSAGES/acl.mo
/usr/share/locale/pl/LC_MESSAGES/acl.mo
/usr/share/locale/sv/LC_MESSAGES/acl.mo
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
* Tue May 31 2016 Adam Miller <maxamillion@fedoraproject.org>
-
