Name:           coreutils
Version:	8.31
Release:        1%{?dist}
Summary:	Standard GNU utilities (chmod, cp, dd, ls, sort, tr, head, wc, who,...

License:	GPL-3
URL:		https://www.gnu.org/software/coreutils/
Source0:	https://ftp.gnu.org/gnu/coreutils/coreutils-%{version}.tar.xz

#BuildRequires:
#Requires:

%description

%prep
%setup -q

%build
# autoreconf
#    This command updates generated configuration files consistent with the latest version of automake.
# FORCE_UNSAFE_CONFIGURE=1
#    This environment variable allows the package to be built as the root user.

autoreconf -fiv
FORCE_UNSAFE_CONFIGURE=1 ./configure \
            --prefix=/usr            \
            --enable-no-install-program=kill,uptime \
	    --bindir=/bin
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
%make_install

%files
/bin/[
/bin/b2sum
/bin/base32
/bin/base64
/bin/basename
/bin/basenc
/bin/cat
/bin/chcon
/bin/chgrp
/bin/chmod
/bin/chown
/bin/chroot
/bin/cksum
/bin/comm
/bin/cp
/bin/csplit
/bin/cut
/bin/date
/bin/dd
/bin/df
/bin/dir
/bin/dircolors
/bin/dirname
/bin/du
/bin/echo
/bin/env
/bin/expand
/bin/expr
/bin/factor
/bin/false
/bin/fmt
/bin/fold
/bin/groups
/bin/head
/bin/hostid
/bin/id
/bin/install
/bin/join
/bin/link
/bin/ln
/bin/logname
/bin/ls
/bin/md5sum
/bin/mkdir
/bin/mkfifo
/bin/mknod
/bin/mktemp
/bin/mv
/bin/nice
/bin/nl
/bin/nohup
/bin/nproc
/bin/numfmt
/bin/od
/bin/paste
/bin/pathchk
/bin/pinky
/bin/pr
/bin/printenv
/bin/printf
/bin/ptx
/bin/pwd
/bin/readlink
/bin/realpath
/bin/rm
/bin/rmdir
/bin/runcon
/bin/seq
/bin/sha1sum
/bin/sha224sum
/bin/sha256sum
/bin/sha384sum
/bin/sha512sum
/bin/shred
/bin/shuf
/bin/sleep
/bin/sort
/bin/split
/bin/stat
/bin/stdbuf
/bin/stty
/bin/sum
/bin/sync
/bin/tac
/bin/tail
/bin/tee
/bin/test
/bin/timeout
/bin/touch
/bin/tr
/bin/true
/bin/truncate
/bin/tsort
/bin/tty
/bin/uname
/bin/unexpand
/bin/uniq
/bin/unlink
/bin/users
/bin/vdir
/bin/wc
/bin/who
/bin/whoami
/bin/yes
/usr/libexec/coreutils/libstdbuf.so
/usr/share/info/coreutils.info.gz
/usr/share/locale/af/LC_MESSAGES/coreutils.mo
/usr/share/locale/af/LC_TIME/coreutils.mo
/usr/share/locale/be/LC_MESSAGES/coreutils.mo
/usr/share/locale/be/LC_TIME/coreutils.mo
/usr/share/locale/bg/LC_MESSAGES/coreutils.mo
/usr/share/locale/bg/LC_TIME/coreutils.mo
/usr/share/locale/ca/LC_MESSAGES/coreutils.mo
/usr/share/locale/ca/LC_TIME/coreutils.mo
/usr/share/locale/cs/LC_MESSAGES/coreutils.mo
/usr/share/locale/cs/LC_TIME/coreutils.mo
/usr/share/locale/da/LC_MESSAGES/coreutils.mo
/usr/share/locale/da/LC_TIME/coreutils.mo
/usr/share/locale/de/LC_MESSAGES/coreutils.mo
/usr/share/locale/de/LC_TIME/coreutils.mo
/usr/share/locale/el/LC_MESSAGES/coreutils.mo
/usr/share/locale/el/LC_TIME/coreutils.mo
/usr/share/locale/eo/LC_MESSAGES/coreutils.mo
/usr/share/locale/eo/LC_TIME/coreutils.mo
/usr/share/locale/es/LC_MESSAGES/coreutils.mo
/usr/share/locale/es/LC_TIME/coreutils.mo
/usr/share/locale/et/LC_MESSAGES/coreutils.mo
/usr/share/locale/et/LC_TIME/coreutils.mo
/usr/share/locale/eu/LC_MESSAGES/coreutils.mo
/usr/share/locale/eu/LC_TIME/coreutils.mo
/usr/share/locale/fi/LC_MESSAGES/coreutils.mo
/usr/share/locale/fi/LC_TIME/coreutils.mo
/usr/share/locale/fr/LC_MESSAGES/coreutils.mo
/usr/share/locale/fr/LC_TIME/coreutils.mo
/usr/share/locale/ga/LC_MESSAGES/coreutils.mo
/usr/share/locale/ga/LC_TIME/coreutils.mo
/usr/share/locale/gl/LC_MESSAGES/coreutils.mo
/usr/share/locale/gl/LC_TIME/coreutils.mo
/usr/share/locale/hr/LC_MESSAGES/coreutils.mo
/usr/share/locale/hr/LC_TIME/coreutils.mo
/usr/share/locale/hu/LC_MESSAGES/coreutils.mo
/usr/share/locale/hu/LC_TIME/coreutils.mo
/usr/share/locale/ia/LC_MESSAGES/coreutils.mo
/usr/share/locale/ia/LC_TIME/coreutils.mo
/usr/share/locale/id/LC_MESSAGES/coreutils.mo
/usr/share/locale/id/LC_TIME/coreutils.mo
/usr/share/locale/it/LC_MESSAGES/coreutils.mo
/usr/share/locale/it/LC_TIME/coreutils.mo
/usr/share/locale/ja/LC_MESSAGES/coreutils.mo
/usr/share/locale/ja/LC_TIME/coreutils.mo
/usr/share/locale/kk/LC_MESSAGES/coreutils.mo
/usr/share/locale/kk/LC_TIME/coreutils.mo
/usr/share/locale/ko/LC_MESSAGES/coreutils.mo
/usr/share/locale/ko/LC_TIME/coreutils.mo
/usr/share/locale/lg/LC_MESSAGES/coreutils.mo
/usr/share/locale/lg/LC_TIME/coreutils.mo
/usr/share/locale/lt/LC_MESSAGES/coreutils.mo
/usr/share/locale/lt/LC_TIME/coreutils.mo
/usr/share/locale/ms/LC_MESSAGES/coreutils.mo
/usr/share/locale/ms/LC_TIME/coreutils.mo
/usr/share/locale/nb/LC_MESSAGES/coreutils.mo
/usr/share/locale/nb/LC_TIME/coreutils.mo
/usr/share/locale/nl/LC_MESSAGES/coreutils.mo
/usr/share/locale/nl/LC_TIME/coreutils.mo
/usr/share/locale/pl/LC_MESSAGES/coreutils.mo
/usr/share/locale/pl/LC_TIME/coreutils.mo
/usr/share/locale/pt/LC_MESSAGES/coreutils.mo
/usr/share/locale/pt/LC_TIME/coreutils.mo
/usr/share/locale/pt_BR/LC_MESSAGES/coreutils.mo
/usr/share/locale/pt_BR/LC_TIME/coreutils.mo
/usr/share/locale/ro/LC_MESSAGES/coreutils.mo
/usr/share/locale/ro/LC_TIME/coreutils.mo
/usr/share/locale/ru/LC_MESSAGES/coreutils.mo
/usr/share/locale/ru/LC_TIME/coreutils.mo
/usr/share/locale/sk/LC_MESSAGES/coreutils.mo
/usr/share/locale/sk/LC_TIME/coreutils.mo
/usr/share/locale/sl/LC_MESSAGES/coreutils.mo
/usr/share/locale/sl/LC_TIME/coreutils.mo
/usr/share/locale/sr/LC_MESSAGES/coreutils.mo
/usr/share/locale/sr/LC_TIME/coreutils.mo
/usr/share/locale/sv/LC_MESSAGES/coreutils.mo
/usr/share/locale/sv/LC_TIME/coreutils.mo
/usr/share/locale/tr/LC_MESSAGES/coreutils.mo
/usr/share/locale/tr/LC_TIME/coreutils.mo
/usr/share/locale/uk/LC_MESSAGES/coreutils.mo
/usr/share/locale/uk/LC_TIME/coreutils.mo
/usr/share/locale/vi/LC_MESSAGES/coreutils.mo
/usr/share/locale/vi/LC_TIME/coreutils.mo
/usr/share/locale/zh_CN/LC_MESSAGES/coreutils.mo
/usr/share/locale/zh_CN/LC_TIME/coreutils.mo
/usr/share/locale/zh_TW/LC_MESSAGES/coreutils.mo
/usr/share/locale/zh_TW/LC_TIME/coreutils.mo
/usr/share/man/man1/b2sum.1.gz
/usr/share/man/man1/base32.1.gz
/usr/share/man/man1/base64.1.gz
/usr/share/man/man1/basename.1.gz
/usr/share/man/man1/basenc.1.gz
/usr/share/man/man1/cat.1.gz
/usr/share/man/man1/chcon.1.gz
/usr/share/man/man1/chgrp.1.gz
/usr/share/man/man1/chmod.1.gz
/usr/share/man/man1/chown.1.gz
/usr/share/man/man1/chroot.1.gz
/usr/share/man/man1/cksum.1.gz
/usr/share/man/man1/comm.1.gz
/usr/share/man/man1/cp.1.gz
/usr/share/man/man1/csplit.1.gz
/usr/share/man/man1/cut.1.gz
/usr/share/man/man1/date.1.gz
/usr/share/man/man1/dd.1.gz
/usr/share/man/man1/df.1.gz
/usr/share/man/man1/dir.1.gz
/usr/share/man/man1/dircolors.1.gz
/usr/share/man/man1/dirname.1.gz
/usr/share/man/man1/du.1.gz
/usr/share/man/man1/echo.1.gz
/usr/share/man/man1/env.1.gz
/usr/share/man/man1/expand.1.gz
/usr/share/man/man1/expr.1.gz
/usr/share/man/man1/factor.1.gz
/usr/share/man/man1/false.1.gz
/usr/share/man/man1/fmt.1.gz
/usr/share/man/man1/fold.1.gz
/usr/share/man/man1/groups.1.gz
/usr/share/man/man1/head.1.gz
/usr/share/man/man1/hostid.1.gz
/usr/share/man/man1/id.1.gz
/usr/share/man/man1/install.1.gz
/usr/share/man/man1/join.1.gz
/usr/share/man/man1/link.1.gz
/usr/share/man/man1/ln.1.gz
/usr/share/man/man1/logname.1.gz
/usr/share/man/man1/ls.1.gz
/usr/share/man/man1/md5sum.1.gz
/usr/share/man/man1/mkdir.1.gz
/usr/share/man/man1/mkfifo.1.gz
/usr/share/man/man1/mknod.1.gz
/usr/share/man/man1/mktemp.1.gz
/usr/share/man/man1/mv.1.gz
/usr/share/man/man1/nice.1.gz
/usr/share/man/man1/nl.1.gz
/usr/share/man/man1/nohup.1.gz
/usr/share/man/man1/nproc.1.gz
/usr/share/man/man1/numfmt.1.gz
/usr/share/man/man1/od.1.gz
/usr/share/man/man1/paste.1.gz
/usr/share/man/man1/pathchk.1.gz
/usr/share/man/man1/pinky.1.gz
/usr/share/man/man1/pr.1.gz
/usr/share/man/man1/printenv.1.gz
/usr/share/man/man1/printf.1.gz
/usr/share/man/man1/ptx.1.gz
/usr/share/man/man1/pwd.1.gz
/usr/share/man/man1/readlink.1.gz
/usr/share/man/man1/realpath.1.gz
/usr/share/man/man1/rm.1.gz
/usr/share/man/man1/rmdir.1.gz
/usr/share/man/man1/runcon.1.gz
/usr/share/man/man1/seq.1.gz
/usr/share/man/man1/sha1sum.1.gz
/usr/share/man/man1/sha224sum.1.gz
/usr/share/man/man1/sha256sum.1.gz
/usr/share/man/man1/sha384sum.1.gz
/usr/share/man/man1/sha512sum.1.gz
/usr/share/man/man1/shred.1.gz
/usr/share/man/man1/shuf.1.gz
/usr/share/man/man1/sleep.1.gz
/usr/share/man/man1/sort.1.gz
/usr/share/man/man1/split.1.gz
/usr/share/man/man1/stat.1.gz
/usr/share/man/man1/stdbuf.1.gz
/usr/share/man/man1/stty.1.gz
/usr/share/man/man1/sum.1.gz
/usr/share/man/man1/sync.1.gz
/usr/share/man/man1/tac.1.gz
/usr/share/man/man1/tail.1.gz
/usr/share/man/man1/tee.1.gz
/usr/share/man/man1/test.1.gz
/usr/share/man/man1/timeout.1.gz
/usr/share/man/man1/touch.1.gz
/usr/share/man/man1/tr.1.gz
/usr/share/man/man1/true.1.gz
/usr/share/man/man1/truncate.1.gz
/usr/share/man/man1/tsort.1.gz
/usr/share/man/man1/tty.1.gz
/usr/share/man/man1/uname.1.gz
/usr/share/man/man1/unexpand.1.gz
/usr/share/man/man1/uniq.1.gz
/usr/share/man/man1/unlink.1.gz
/usr/share/man/man1/users.1.gz
/usr/share/man/man1/vdir.1.gz
/usr/share/man/man1/wc.1.gz
/usr/share/man/man1/who.1.gz
/usr/share/man/man1/whoami.1.gz
/usr/share/man/man1/yes.1.gz


%changelog
* Tue May 31 2016 Adam Miller <maxamillion@fedoraproject.org>
-

# kill/uptime - procps
# groups/su   - shadow
# hostname    - net-tools
# see /usr/libexec/rpm/macros for macros
