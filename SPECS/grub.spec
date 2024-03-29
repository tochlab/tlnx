Name:           grub
Version:	2.06
Release:        1%{?dist}
Summary:	GNU GRUB boot loader

License:	GPL-3+ BSD MIT
URL:		https://www.gnu.org/software/grub/
Source0:	https://ftpmirror.gnu.org/gnu/grub/grub-%{version}.tar.gz

#BuildRequires:
#Requires:

%description

%prep
%setup -q

%build
%configure --prefix=/usr          \
            --libdir=/usr/lib      \
            --sbindir=/sbin        \
            --sysconfdir=/etc      \
            --disable-efiemu       \
            --disable-werror       \
            --disable-grub-mkfont   \
            --disable-grub-themes   \
            --disable-grub-mount \
	    --disable-nls

make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
%make_install
rm -fr $RPM_BUILD_ROOT/usr/share/info/dir
rm -fr $RPM_BUILD_ROOT/usr/share/man/

%files
/etc/bash_completion.d/grub
/etc/grub.d/00_header
/etc/grub.d/10_linux
/etc/grub.d/20_linux_xen
/etc/grub.d/30_os-prober
/etc/grub.d/40_custom
/etc/grub.d/41_custom
/etc/grub.d/README
/sbin/grub-bios-setup
/sbin/grub-install
/sbin/grub-macbless
/sbin/grub-mkconfig
/sbin/grub-ofpathname
/sbin/grub-probe
/sbin/grub-reboot
/sbin/grub-set-default
/sbin/grub-sparc64-setup
/usr/bin/grub-editenv
/usr/bin/grub-file
/usr/bin/grub-fstest
/usr/bin/grub-glue-efi
/usr/bin/grub-kbdcomp
/usr/bin/grub-menulst2cfg
/usr/bin/grub-mkimage
/usr/bin/grub-mklayout
/usr/bin/grub-mknetdir
/usr/bin/grub-mkpasswd-pbkdf2
/usr/bin/grub-mkrelpath
/usr/bin/grub-mkrescue
/usr/bin/grub-mkstandalone
/usr/bin/grub-render-label
/usr/bin/grub-script-check
/usr/bin/grub-syslinux2cfg
/usr/lib/grub/i386-pc/acpi.mod
/usr/lib/grub/i386-pc/acpi.module
/usr/lib/grub/i386-pc/adler32.mod
/usr/lib/grub/i386-pc/adler32.module
/usr/lib/grub/i386-pc/affs.mod
/usr/lib/grub/i386-pc/affs.module
/usr/lib/grub/i386-pc/afs.mod
/usr/lib/grub/i386-pc/afs.module
/usr/lib/grub/i386-pc/ahci.mod
/usr/lib/grub/i386-pc/ahci.module
/usr/lib/grub/i386-pc/all_video.mod
/usr/lib/grub/i386-pc/all_video.module
/usr/lib/grub/i386-pc/aout.mod
/usr/lib/grub/i386-pc/aout.module
/usr/lib/grub/i386-pc/archelp.mod
/usr/lib/grub/i386-pc/archelp.module
/usr/lib/grub/i386-pc/at_keyboard.mod
/usr/lib/grub/i386-pc/at_keyboard.module
/usr/lib/grub/i386-pc/ata.mod
/usr/lib/grub/i386-pc/ata.module
/usr/lib/grub/i386-pc/backtrace.mod
/usr/lib/grub/i386-pc/backtrace.module
/usr/lib/grub/i386-pc/bfs.mod
/usr/lib/grub/i386-pc/bfs.module
/usr/lib/grub/i386-pc/biosdisk.mod
/usr/lib/grub/i386-pc/biosdisk.module
/usr/lib/grub/i386-pc/bitmap.mod
/usr/lib/grub/i386-pc/bitmap.module
/usr/lib/grub/i386-pc/bitmap_scale.mod
/usr/lib/grub/i386-pc/bitmap_scale.module
/usr/lib/grub/i386-pc/blocklist.mod
/usr/lib/grub/i386-pc/blocklist.module
/usr/lib/grub/i386-pc/boot.image
/usr/lib/grub/i386-pc/boot.img
/usr/lib/grub/i386-pc/boot.mod
/usr/lib/grub/i386-pc/boot.module
/usr/lib/grub/i386-pc/boot_hybrid.image
/usr/lib/grub/i386-pc/boot_hybrid.img
/usr/lib/grub/i386-pc/bsd.mod
/usr/lib/grub/i386-pc/bsd.module
/usr/lib/grub/i386-pc/bswap_test.mod
/usr/lib/grub/i386-pc/bswap_test.module
/usr/lib/grub/i386-pc/btrfs.mod
/usr/lib/grub/i386-pc/btrfs.module
/usr/lib/grub/i386-pc/bufio.mod
/usr/lib/grub/i386-pc/bufio.module
/usr/lib/grub/i386-pc/cat.mod
/usr/lib/grub/i386-pc/cat.module
/usr/lib/grub/i386-pc/cbfs.mod
/usr/lib/grub/i386-pc/cbfs.module
/usr/lib/grub/i386-pc/cbls.mod
/usr/lib/grub/i386-pc/cbls.module
/usr/lib/grub/i386-pc/cbmemc.mod
/usr/lib/grub/i386-pc/cbmemc.module
/usr/lib/grub/i386-pc/cbtable.mod
/usr/lib/grub/i386-pc/cbtable.module
/usr/lib/grub/i386-pc/cbtime.mod
/usr/lib/grub/i386-pc/cbtime.module
/usr/lib/grub/i386-pc/cdboot.image
/usr/lib/grub/i386-pc/cdboot.img
/usr/lib/grub/i386-pc/chain.mod
/usr/lib/grub/i386-pc/chain.module
/usr/lib/grub/i386-pc/cmdline_cat_test.mod
/usr/lib/grub/i386-pc/cmdline_cat_test.module
/usr/lib/grub/i386-pc/cmosdump.mod
/usr/lib/grub/i386-pc/cmosdump.module
/usr/lib/grub/i386-pc/cmostest.mod
/usr/lib/grub/i386-pc/cmostest.module
/usr/lib/grub/i386-pc/cmp.mod
/usr/lib/grub/i386-pc/cmp.module
/usr/lib/grub/i386-pc/cmp_test.mod
/usr/lib/grub/i386-pc/cmp_test.module
/usr/lib/grub/i386-pc/command.lst
/usr/lib/grub/i386-pc/config.h
/usr/lib/grub/i386-pc/configfile.mod
/usr/lib/grub/i386-pc/configfile.module
/usr/lib/grub/i386-pc/cpio.mod
/usr/lib/grub/i386-pc/cpio.module
/usr/lib/grub/i386-pc/cpio_be.mod
/usr/lib/grub/i386-pc/cpio_be.module
/usr/lib/grub/i386-pc/cpuid.mod
/usr/lib/grub/i386-pc/cpuid.module
/usr/lib/grub/i386-pc/crc64.mod
/usr/lib/grub/i386-pc/crc64.module
/usr/lib/grub/i386-pc/crypto.lst
/usr/lib/grub/i386-pc/crypto.mod
/usr/lib/grub/i386-pc/crypto.module
/usr/lib/grub/i386-pc/cryptodisk.mod
/usr/lib/grub/i386-pc/cryptodisk.module
/usr/lib/grub/i386-pc/cs5536.mod
/usr/lib/grub/i386-pc/cs5536.module
/usr/lib/grub/i386-pc/ctz_test.mod
/usr/lib/grub/i386-pc/ctz_test.module
/usr/lib/grub/i386-pc/date.mod
/usr/lib/grub/i386-pc/date.module
/usr/lib/grub/i386-pc/datehook.mod
/usr/lib/grub/i386-pc/datehook.module
/usr/lib/grub/i386-pc/datetime.mod
/usr/lib/grub/i386-pc/datetime.module
/usr/lib/grub/i386-pc/disk.mod
/usr/lib/grub/i386-pc/disk.module
/usr/lib/grub/i386-pc/diskboot.image
/usr/lib/grub/i386-pc/diskboot.img
/usr/lib/grub/i386-pc/diskfilter.mod
/usr/lib/grub/i386-pc/diskfilter.module
/usr/lib/grub/i386-pc/div.mod
/usr/lib/grub/i386-pc/div.module
/usr/lib/grub/i386-pc/div_test.mod
/usr/lib/grub/i386-pc/div_test.module
/usr/lib/grub/i386-pc/dm_nv.mod
/usr/lib/grub/i386-pc/dm_nv.module
/usr/lib/grub/i386-pc/drivemap.mod
/usr/lib/grub/i386-pc/drivemap.module
/usr/lib/grub/i386-pc/echo.mod
/usr/lib/grub/i386-pc/echo.module
/usr/lib/grub/i386-pc/efiemu.mod
/usr/lib/grub/i386-pc/efiemu.module
/usr/lib/grub/i386-pc/ehci.mod
/usr/lib/grub/i386-pc/ehci.module
/usr/lib/grub/i386-pc/elf.mod
/usr/lib/grub/i386-pc/elf.module
/usr/lib/grub/i386-pc/eval.mod
/usr/lib/grub/i386-pc/eval.module
/usr/lib/grub/i386-pc/exfat.mod
/usr/lib/grub/i386-pc/exfat.module
/usr/lib/grub/i386-pc/exfctest.mod
/usr/lib/grub/i386-pc/exfctest.module
/usr/lib/grub/i386-pc/ext2.mod
/usr/lib/grub/i386-pc/ext2.module
/usr/lib/grub/i386-pc/extcmd.mod
/usr/lib/grub/i386-pc/extcmd.module
/usr/lib/grub/i386-pc/f2fs.mod
/usr/lib/grub/i386-pc/f2fs.module
/usr/lib/grub/i386-pc/fat.mod
/usr/lib/grub/i386-pc/fat.module
/usr/lib/grub/i386-pc/fdt.lst
/usr/lib/grub/i386-pc/file.mod
/usr/lib/grub/i386-pc/file.module
/usr/lib/grub/i386-pc/font.mod
/usr/lib/grub/i386-pc/font.module
/usr/lib/grub/i386-pc/freedos.mod
/usr/lib/grub/i386-pc/freedos.module
/usr/lib/grub/i386-pc/fs.lst
/usr/lib/grub/i386-pc/fshelp.mod
/usr/lib/grub/i386-pc/fshelp.module
/usr/lib/grub/i386-pc/functional_test.mod
/usr/lib/grub/i386-pc/functional_test.module
/usr/lib/grub/i386-pc/gcry_arcfour.mod
/usr/lib/grub/i386-pc/gcry_arcfour.module
/usr/lib/grub/i386-pc/gcry_blowfish.mod
/usr/lib/grub/i386-pc/gcry_blowfish.module
/usr/lib/grub/i386-pc/gcry_camellia.mod
/usr/lib/grub/i386-pc/gcry_camellia.module
/usr/lib/grub/i386-pc/gcry_cast5.mod
/usr/lib/grub/i386-pc/gcry_cast5.module
/usr/lib/grub/i386-pc/gcry_crc.mod
/usr/lib/grub/i386-pc/gcry_crc.module
/usr/lib/grub/i386-pc/gcry_des.mod
/usr/lib/grub/i386-pc/gcry_des.module
/usr/lib/grub/i386-pc/gcry_dsa.mod
/usr/lib/grub/i386-pc/gcry_dsa.module
/usr/lib/grub/i386-pc/gcry_idea.mod
/usr/lib/grub/i386-pc/gcry_idea.module
/usr/lib/grub/i386-pc/gcry_md4.mod
/usr/lib/grub/i386-pc/gcry_md4.module
/usr/lib/grub/i386-pc/gcry_md5.mod
/usr/lib/grub/i386-pc/gcry_md5.module
/usr/lib/grub/i386-pc/gcry_rfc2268.mod
/usr/lib/grub/i386-pc/gcry_rfc2268.module
/usr/lib/grub/i386-pc/gcry_rijndael.mod
/usr/lib/grub/i386-pc/gcry_rijndael.module
/usr/lib/grub/i386-pc/gcry_rmd160.mod
/usr/lib/grub/i386-pc/gcry_rmd160.module
/usr/lib/grub/i386-pc/gcry_rsa.mod
/usr/lib/grub/i386-pc/gcry_rsa.module
/usr/lib/grub/i386-pc/gcry_seed.mod
/usr/lib/grub/i386-pc/gcry_seed.module
/usr/lib/grub/i386-pc/gcry_serpent.mod
/usr/lib/grub/i386-pc/gcry_serpent.module
/usr/lib/grub/i386-pc/gcry_sha1.mod
/usr/lib/grub/i386-pc/gcry_sha1.module
/usr/lib/grub/i386-pc/gcry_sha256.mod
/usr/lib/grub/i386-pc/gcry_sha256.module
/usr/lib/grub/i386-pc/gcry_sha512.mod
/usr/lib/grub/i386-pc/gcry_sha512.module
/usr/lib/grub/i386-pc/gcry_tiger.mod
/usr/lib/grub/i386-pc/gcry_tiger.module
/usr/lib/grub/i386-pc/gcry_twofish.mod
/usr/lib/grub/i386-pc/gcry_twofish.module
/usr/lib/grub/i386-pc/gcry_whirlpool.mod
/usr/lib/grub/i386-pc/gcry_whirlpool.module
/usr/lib/grub/i386-pc/gdb.mod
/usr/lib/grub/i386-pc/gdb.module
/usr/lib/grub/i386-pc/gdb_grub
/usr/lib/grub/i386-pc/geli.mod
/usr/lib/grub/i386-pc/geli.module
/usr/lib/grub/i386-pc/gettext.mod
/usr/lib/grub/i386-pc/gettext.module
/usr/lib/grub/i386-pc/gfxmenu.mod
/usr/lib/grub/i386-pc/gfxmenu.module
/usr/lib/grub/i386-pc/gfxterm.mod
/usr/lib/grub/i386-pc/gfxterm.module
/usr/lib/grub/i386-pc/gfxterm_background.mod
/usr/lib/grub/i386-pc/gfxterm_background.module
/usr/lib/grub/i386-pc/gfxterm_menu.mod
/usr/lib/grub/i386-pc/gfxterm_menu.module
/usr/lib/grub/i386-pc/gmodule.pl
/usr/lib/grub/i386-pc/gptsync.mod
/usr/lib/grub/i386-pc/gptsync.module
/usr/lib/grub/i386-pc/gzio.mod
/usr/lib/grub/i386-pc/gzio.module
/usr/lib/grub/i386-pc/halt.mod
/usr/lib/grub/i386-pc/halt.module
/usr/lib/grub/i386-pc/hashsum.mod
/usr/lib/grub/i386-pc/hashsum.module
/usr/lib/grub/i386-pc/hdparm.mod
/usr/lib/grub/i386-pc/hdparm.module
/usr/lib/grub/i386-pc/hello.mod
/usr/lib/grub/i386-pc/hello.module
/usr/lib/grub/i386-pc/help.mod
/usr/lib/grub/i386-pc/help.module
/usr/lib/grub/i386-pc/hexdump.mod
/usr/lib/grub/i386-pc/hexdump.module
/usr/lib/grub/i386-pc/hfs.mod
/usr/lib/grub/i386-pc/hfs.module
/usr/lib/grub/i386-pc/hfsplus.mod
/usr/lib/grub/i386-pc/hfsplus.module
/usr/lib/grub/i386-pc/hfspluscomp.mod
/usr/lib/grub/i386-pc/hfspluscomp.module
/usr/lib/grub/i386-pc/http.mod
/usr/lib/grub/i386-pc/http.module
/usr/lib/grub/i386-pc/iorw.mod
/usr/lib/grub/i386-pc/iorw.module
/usr/lib/grub/i386-pc/iso9660.mod
/usr/lib/grub/i386-pc/iso9660.module
/usr/lib/grub/i386-pc/jfs.mod
/usr/lib/grub/i386-pc/jfs.module
/usr/lib/grub/i386-pc/jpeg.mod
/usr/lib/grub/i386-pc/jpeg.module
/usr/lib/grub/i386-pc/kernel.exec
/usr/lib/grub/i386-pc/kernel.img
/usr/lib/grub/i386-pc/keylayouts.mod
/usr/lib/grub/i386-pc/keylayouts.module
/usr/lib/grub/i386-pc/keystatus.mod
/usr/lib/grub/i386-pc/keystatus.module
/usr/lib/grub/i386-pc/ldm.mod
/usr/lib/grub/i386-pc/ldm.module
/usr/lib/grub/i386-pc/legacy_password_test.mod
/usr/lib/grub/i386-pc/legacy_password_test.module
/usr/lib/grub/i386-pc/legacycfg.mod
/usr/lib/grub/i386-pc/legacycfg.module
/usr/lib/grub/i386-pc/linux.mod
/usr/lib/grub/i386-pc/linux.module
/usr/lib/grub/i386-pc/linux16.mod
/usr/lib/grub/i386-pc/linux16.module
/usr/lib/grub/i386-pc/lnxboot.image
/usr/lib/grub/i386-pc/lnxboot.img
/usr/lib/grub/i386-pc/loadenv.mod
/usr/lib/grub/i386-pc/loadenv.module
/usr/lib/grub/i386-pc/loopback.mod
/usr/lib/grub/i386-pc/loopback.module
/usr/lib/grub/i386-pc/ls.mod
/usr/lib/grub/i386-pc/ls.module
/usr/lib/grub/i386-pc/lsacpi.mod
/usr/lib/grub/i386-pc/lsacpi.module
/usr/lib/grub/i386-pc/lsapm.mod
/usr/lib/grub/i386-pc/lsapm.module
/usr/lib/grub/i386-pc/lsmmap.mod
/usr/lib/grub/i386-pc/lsmmap.module
/usr/lib/grub/i386-pc/lspci.mod
/usr/lib/grub/i386-pc/lspci.module
/usr/lib/grub/i386-pc/luks.mod
/usr/lib/grub/i386-pc/luks.module
/usr/lib/grub/i386-pc/lvm.mod
/usr/lib/grub/i386-pc/lvm.module
/usr/lib/grub/i386-pc/lzma_decompress.image
/usr/lib/grub/i386-pc/lzma_decompress.img
/usr/lib/grub/i386-pc/lzopio.mod
/usr/lib/grub/i386-pc/lzopio.module
/usr/lib/grub/i386-pc/macbless.mod
/usr/lib/grub/i386-pc/macbless.module
/usr/lib/grub/i386-pc/macho.mod
/usr/lib/grub/i386-pc/macho.module
/usr/lib/grub/i386-pc/mda_text.mod
/usr/lib/grub/i386-pc/mda_text.module
/usr/lib/grub/i386-pc/mdraid09.mod
/usr/lib/grub/i386-pc/mdraid09.module
/usr/lib/grub/i386-pc/mdraid09_be.mod
/usr/lib/grub/i386-pc/mdraid09_be.module
/usr/lib/grub/i386-pc/mdraid1x.mod
/usr/lib/grub/i386-pc/mdraid1x.module
/usr/lib/grub/i386-pc/memdisk.mod
/usr/lib/grub/i386-pc/memdisk.module
/usr/lib/grub/i386-pc/memrw.mod
/usr/lib/grub/i386-pc/memrw.module
/usr/lib/grub/i386-pc/minicmd.mod
/usr/lib/grub/i386-pc/minicmd.module
/usr/lib/grub/i386-pc/minix.mod
/usr/lib/grub/i386-pc/minix.module
/usr/lib/grub/i386-pc/minix2.mod
/usr/lib/grub/i386-pc/minix2.module
/usr/lib/grub/i386-pc/minix2_be.mod
/usr/lib/grub/i386-pc/minix2_be.module
/usr/lib/grub/i386-pc/minix3.mod
/usr/lib/grub/i386-pc/minix3.module
/usr/lib/grub/i386-pc/minix3_be.mod
/usr/lib/grub/i386-pc/minix3_be.module
/usr/lib/grub/i386-pc/minix_be.mod
/usr/lib/grub/i386-pc/minix_be.module
/usr/lib/grub/i386-pc/mmap.mod
/usr/lib/grub/i386-pc/mmap.module
/usr/lib/grub/i386-pc/moddep.lst
/usr/lib/grub/i386-pc/modinfo.sh
/usr/lib/grub/i386-pc/morse.mod
/usr/lib/grub/i386-pc/morse.module
/usr/lib/grub/i386-pc/mpi.mod
/usr/lib/grub/i386-pc/mpi.module
/usr/lib/grub/i386-pc/msdospart.mod
/usr/lib/grub/i386-pc/msdospart.module
/usr/lib/grub/i386-pc/mul_test.mod
/usr/lib/grub/i386-pc/mul_test.module
/usr/lib/grub/i386-pc/multiboot.mod
/usr/lib/grub/i386-pc/multiboot.module
/usr/lib/grub/i386-pc/multiboot2.mod
/usr/lib/grub/i386-pc/multiboot2.module
/usr/lib/grub/i386-pc/nativedisk.mod
/usr/lib/grub/i386-pc/nativedisk.module
/usr/lib/grub/i386-pc/net.mod
/usr/lib/grub/i386-pc/net.module
/usr/lib/grub/i386-pc/newc.mod
/usr/lib/grub/i386-pc/newc.module
/usr/lib/grub/i386-pc/nilfs2.mod
/usr/lib/grub/i386-pc/nilfs2.module
/usr/lib/grub/i386-pc/normal.mod
/usr/lib/grub/i386-pc/normal.module
/usr/lib/grub/i386-pc/ntfs.mod
/usr/lib/grub/i386-pc/ntfs.module
/usr/lib/grub/i386-pc/ntfscomp.mod
/usr/lib/grub/i386-pc/ntfscomp.module
/usr/lib/grub/i386-pc/ntldr.mod
/usr/lib/grub/i386-pc/ntldr.module
/usr/lib/grub/i386-pc/odc.mod
/usr/lib/grub/i386-pc/odc.module
/usr/lib/grub/i386-pc/offsetio.mod
/usr/lib/grub/i386-pc/offsetio.module
/usr/lib/grub/i386-pc/ohci.mod
/usr/lib/grub/i386-pc/ohci.module
/usr/lib/grub/i386-pc/part_acorn.mod
/usr/lib/grub/i386-pc/part_acorn.module
/usr/lib/grub/i386-pc/part_amiga.mod
/usr/lib/grub/i386-pc/part_amiga.module
/usr/lib/grub/i386-pc/part_apple.mod
/usr/lib/grub/i386-pc/part_apple.module
/usr/lib/grub/i386-pc/part_bsd.mod
/usr/lib/grub/i386-pc/part_bsd.module
/usr/lib/grub/i386-pc/part_dfly.mod
/usr/lib/grub/i386-pc/part_dfly.module
/usr/lib/grub/i386-pc/part_dvh.mod
/usr/lib/grub/i386-pc/part_dvh.module
/usr/lib/grub/i386-pc/part_gpt.mod
/usr/lib/grub/i386-pc/part_gpt.module
/usr/lib/grub/i386-pc/part_msdos.mod
/usr/lib/grub/i386-pc/part_msdos.module
/usr/lib/grub/i386-pc/part_plan.mod
/usr/lib/grub/i386-pc/part_plan.module
/usr/lib/grub/i386-pc/part_sun.mod
/usr/lib/grub/i386-pc/part_sun.module
/usr/lib/grub/i386-pc/part_sunpc.mod
/usr/lib/grub/i386-pc/part_sunpc.module
/usr/lib/grub/i386-pc/partmap.lst
/usr/lib/grub/i386-pc/parttool.lst
/usr/lib/grub/i386-pc/parttool.mod
/usr/lib/grub/i386-pc/parttool.module
/usr/lib/grub/i386-pc/password.mod
/usr/lib/grub/i386-pc/password.module
/usr/lib/grub/i386-pc/password_pbkdf2.mod
/usr/lib/grub/i386-pc/password_pbkdf2.module
/usr/lib/grub/i386-pc/pata.mod
/usr/lib/grub/i386-pc/pata.module
/usr/lib/grub/i386-pc/pbkdf2.mod
/usr/lib/grub/i386-pc/pbkdf2.module
/usr/lib/grub/i386-pc/pbkdf2_test.mod
/usr/lib/grub/i386-pc/pbkdf2_test.module
/usr/lib/grub/i386-pc/pci.mod
/usr/lib/grub/i386-pc/pci.module
/usr/lib/grub/i386-pc/pcidump.mod
/usr/lib/grub/i386-pc/pcidump.module
/usr/lib/grub/i386-pc/pgp.mod
/usr/lib/grub/i386-pc/pgp.module
/usr/lib/grub/i386-pc/plan9.mod
/usr/lib/grub/i386-pc/plan9.module
/usr/lib/grub/i386-pc/play.mod
/usr/lib/grub/i386-pc/play.module
/usr/lib/grub/i386-pc/png.mod
/usr/lib/grub/i386-pc/png.module
/usr/lib/grub/i386-pc/priority_queue.mod
/usr/lib/grub/i386-pc/priority_queue.module
/usr/lib/grub/i386-pc/probe.mod
/usr/lib/grub/i386-pc/probe.module
/usr/lib/grub/i386-pc/procfs.mod
/usr/lib/grub/i386-pc/procfs.module
/usr/lib/grub/i386-pc/progress.mod
/usr/lib/grub/i386-pc/progress.module
/usr/lib/grub/i386-pc/pxe.mod
/usr/lib/grub/i386-pc/pxe.module
/usr/lib/grub/i386-pc/pxeboot.image
/usr/lib/grub/i386-pc/pxeboot.img
/usr/lib/grub/i386-pc/pxechain.mod
/usr/lib/grub/i386-pc/pxechain.module
/usr/lib/grub/i386-pc/raid5rec.mod
/usr/lib/grub/i386-pc/raid5rec.module
/usr/lib/grub/i386-pc/raid6rec.mod
/usr/lib/grub/i386-pc/raid6rec.module
/usr/lib/grub/i386-pc/random.mod
/usr/lib/grub/i386-pc/random.module
/usr/lib/grub/i386-pc/rdmsr.mod
/usr/lib/grub/i386-pc/rdmsr.module
/usr/lib/grub/i386-pc/read.mod
/usr/lib/grub/i386-pc/read.module
/usr/lib/grub/i386-pc/reboot.mod
/usr/lib/grub/i386-pc/reboot.module
/usr/lib/grub/i386-pc/regexp.mod
/usr/lib/grub/i386-pc/regexp.module
/usr/lib/grub/i386-pc/reiserfs.mod
/usr/lib/grub/i386-pc/reiserfs.module
/usr/lib/grub/i386-pc/relocator.mod
/usr/lib/grub/i386-pc/relocator.module
/usr/lib/grub/i386-pc/romfs.mod
/usr/lib/grub/i386-pc/romfs.module
/usr/lib/grub/i386-pc/scsi.mod
/usr/lib/grub/i386-pc/scsi.module
/usr/lib/grub/i386-pc/search.mod
/usr/lib/grub/i386-pc/search.module
/usr/lib/grub/i386-pc/search_fs_file.mod
/usr/lib/grub/i386-pc/search_fs_file.module
/usr/lib/grub/i386-pc/search_fs_uuid.mod
/usr/lib/grub/i386-pc/search_fs_uuid.module
/usr/lib/grub/i386-pc/search_label.mod
/usr/lib/grub/i386-pc/search_label.module
/usr/lib/grub/i386-pc/sendkey.mod
/usr/lib/grub/i386-pc/sendkey.module
/usr/lib/grub/i386-pc/serial.mod
/usr/lib/grub/i386-pc/serial.module
/usr/lib/grub/i386-pc/setjmp.mod
/usr/lib/grub/i386-pc/setjmp.module
/usr/lib/grub/i386-pc/setjmp_test.mod
/usr/lib/grub/i386-pc/setjmp_test.module
/usr/lib/grub/i386-pc/setpci.mod
/usr/lib/grub/i386-pc/setpci.module
/usr/lib/grub/i386-pc/sfs.mod
/usr/lib/grub/i386-pc/sfs.module
/usr/lib/grub/i386-pc/shift_test.mod
/usr/lib/grub/i386-pc/shift_test.module
/usr/lib/grub/i386-pc/signature_test.mod
/usr/lib/grub/i386-pc/signature_test.module
/usr/lib/grub/i386-pc/sleep.mod
/usr/lib/grub/i386-pc/sleep.module
/usr/lib/grub/i386-pc/sleep_test.mod
/usr/lib/grub/i386-pc/sleep_test.module
/usr/lib/grub/i386-pc/spkmodem.mod
/usr/lib/grub/i386-pc/spkmodem.module
/usr/lib/grub/i386-pc/squash4.mod
/usr/lib/grub/i386-pc/squash4.module
/usr/lib/grub/i386-pc/strtoull_test.mod
/usr/lib/grub/i386-pc/strtoull_test.module
/usr/lib/grub/i386-pc/syslinuxcfg.mod
/usr/lib/grub/i386-pc/syslinuxcfg.module
/usr/lib/grub/i386-pc/tar.mod
/usr/lib/grub/i386-pc/tar.module
/usr/lib/grub/i386-pc/terminal.lst
/usr/lib/grub/i386-pc/terminal.mod
/usr/lib/grub/i386-pc/terminal.module
/usr/lib/grub/i386-pc/terminfo.mod
/usr/lib/grub/i386-pc/terminfo.module
/usr/lib/grub/i386-pc/test.mod
/usr/lib/grub/i386-pc/test.module
/usr/lib/grub/i386-pc/test_blockarg.mod
/usr/lib/grub/i386-pc/test_blockarg.module
/usr/lib/grub/i386-pc/testload.mod
/usr/lib/grub/i386-pc/testload.module
/usr/lib/grub/i386-pc/testspeed.mod
/usr/lib/grub/i386-pc/testspeed.module
/usr/lib/grub/i386-pc/tftp.mod
/usr/lib/grub/i386-pc/tftp.module
/usr/lib/grub/i386-pc/tga.mod
/usr/lib/grub/i386-pc/tga.module
/usr/lib/grub/i386-pc/time.mod
/usr/lib/grub/i386-pc/time.module
/usr/lib/grub/i386-pc/tr.mod
/usr/lib/grub/i386-pc/tr.module
/usr/lib/grub/i386-pc/trig.mod
/usr/lib/grub/i386-pc/trig.module
/usr/lib/grub/i386-pc/true.mod
/usr/lib/grub/i386-pc/true.module
/usr/lib/grub/i386-pc/truecrypt.mod
/usr/lib/grub/i386-pc/truecrypt.module
/usr/lib/grub/i386-pc/udf.mod
/usr/lib/grub/i386-pc/udf.module
/usr/lib/grub/i386-pc/ufs1.mod
/usr/lib/grub/i386-pc/ufs1.module
/usr/lib/grub/i386-pc/ufs1_be.mod
/usr/lib/grub/i386-pc/ufs1_be.module
/usr/lib/grub/i386-pc/ufs2.mod
/usr/lib/grub/i386-pc/ufs2.module
/usr/lib/grub/i386-pc/uhci.mod
/usr/lib/grub/i386-pc/uhci.module
/usr/lib/grub/i386-pc/usb.mod
/usr/lib/grub/i386-pc/usb.module
/usr/lib/grub/i386-pc/usb_keyboard.mod
/usr/lib/grub/i386-pc/usb_keyboard.module
/usr/lib/grub/i386-pc/usbms.mod
/usr/lib/grub/i386-pc/usbms.module
/usr/lib/grub/i386-pc/usbserial_common.mod
/usr/lib/grub/i386-pc/usbserial_common.module
/usr/lib/grub/i386-pc/usbserial_ftdi.mod
/usr/lib/grub/i386-pc/usbserial_ftdi.module
/usr/lib/grub/i386-pc/usbserial_pl2303.mod
/usr/lib/grub/i386-pc/usbserial_pl2303.module
/usr/lib/grub/i386-pc/usbserial_usbdebug.mod
/usr/lib/grub/i386-pc/usbserial_usbdebug.module
/usr/lib/grub/i386-pc/usbtest.mod
/usr/lib/grub/i386-pc/usbtest.module
/usr/lib/grub/i386-pc/vbe.mod
/usr/lib/grub/i386-pc/vbe.module
/usr/lib/grub/i386-pc/vga.mod
/usr/lib/grub/i386-pc/vga.module
/usr/lib/grub/i386-pc/vga_text.mod
/usr/lib/grub/i386-pc/vga_text.module
/usr/lib/grub/i386-pc/video.lst
/usr/lib/grub/i386-pc/video.mod
/usr/lib/grub/i386-pc/video.module
/usr/lib/grub/i386-pc/video_bochs.mod
/usr/lib/grub/i386-pc/video_bochs.module
/usr/lib/grub/i386-pc/video_cirrus.mod
/usr/lib/grub/i386-pc/video_cirrus.module
/usr/lib/grub/i386-pc/video_colors.mod
/usr/lib/grub/i386-pc/video_colors.module
/usr/lib/grub/i386-pc/video_fb.mod
/usr/lib/grub/i386-pc/video_fb.module
/usr/lib/grub/i386-pc/videoinfo.mod
/usr/lib/grub/i386-pc/videoinfo.module
/usr/lib/grub/i386-pc/videotest.mod
/usr/lib/grub/i386-pc/videotest.module
/usr/lib/grub/i386-pc/videotest_checksum.mod
/usr/lib/grub/i386-pc/videotest_checksum.module
/usr/lib/grub/i386-pc/wrmsr.mod
/usr/lib/grub/i386-pc/wrmsr.module
/usr/lib/grub/i386-pc/xfs.mod
/usr/lib/grub/i386-pc/xfs.module
/usr/lib/grub/i386-pc/xnu.mod
/usr/lib/grub/i386-pc/xnu.module
/usr/lib/grub/i386-pc/xnu_uuid.mod
/usr/lib/grub/i386-pc/xnu_uuid.module
/usr/lib/grub/i386-pc/xnu_uuid_test.mod
/usr/lib/grub/i386-pc/xnu_uuid_test.module
/usr/lib/grub/i386-pc/xzio.mod
/usr/lib/grub/i386-pc/xzio.module
/usr/lib/grub/i386-pc/zfs.mod
/usr/lib/grub/i386-pc/zfs.module
/usr/lib/grub/i386-pc/zfscrypt.mod
/usr/lib/grub/i386-pc/zfscrypt.module
/usr/lib/grub/i386-pc/zfsinfo.mod
/usr/lib/grub/i386-pc/zfsinfo.module
/usr/lib/grub/i386-pc/zstd.mod
/usr/lib/grub/i386-pc/zstd.module
/usr/share/grub/grub-mkconfig_lib
/usr/share/info/grub-dev.info.gz
/usr/share/info/grub.info.gz
/etc/grub.d/30_uefi-firmware
/usr/lib/grub/i386-pc/afsplitter.mod
/usr/lib/grub/i386-pc/afsplitter.module
/usr/lib/grub/i386-pc/json.mod
/usr/lib/grub/i386-pc/json.module
/usr/lib/grub/i386-pc/luks2.mod
/usr/lib/grub/i386-pc/luks2.module
/usr/lib/grub/i386-pc/smbios.mod
/usr/lib/grub/i386-pc/smbios.module
/usr/share/info/grub.info-1.gz
/usr/share/info/grub.info-2.gz

%changelog
