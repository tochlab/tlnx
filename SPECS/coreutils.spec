Name:           coreutils
Version:	8.32
Release:        1%{?dist}
Summary:	Standard GNU utilities (chmod, cp, dd, ls, sort, tr, head, wc, who,...

License:	GPL-3
URL:		https://www.gnu.org/software/coreutils/
Source0:	https://ftpmirror.gnu.org/gnu/coreutils/coreutils-%{version}.tar.xz

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
	    --disable-nls
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
%make_install
# Move critical binaries into /bin (required by FHS)
mkdir $RPM_BUILD_ROOT/bin/
cd $RPM_BUILD_ROOT/usr/bin
fhs="cat chgrp chmod chown cp date dd df echo false ln ls mkdir mknod mv pwd rm rmdir stty sync true uname"
mv ${fhs} $RPM_BUILD_ROOT/bin/

rm -f $RPM_BUILD_ROOT/usr/share/info/dir

%files
/usr/bin/[
/usr/bin/b2sum
/usr/bin/base32
/usr/bin/base64
/usr/bin/basename
/usr/bin/basenc
/bin/cat
/usr/bin/chcon
/bin/chgrp
/bin/chmod
/bin/chown
/usr/bin/chroot
/usr/bin/cksum
/usr/bin/comm
/bin/cp
/usr/bin/csplit
/usr/bin/cut
/bin/date
/bin/dd
/bin/df
/usr/bin/dir
/usr/bin/dircolors
/usr/bin/dirname
/usr/bin/du
/bin/echo
/usr/bin/env
/usr/bin/expand
/usr/bin/expr
/usr/bin/factor
/bin/false
/usr/bin/fmt
/usr/bin/fold
/usr/bin/groups
/usr/bin/head
/usr/bin/hostid
/usr/bin/id
/usr/bin/install
/usr/bin/join
/usr/bin/link
/bin/ln
/usr/bin/logname
/bin/ls
/usr/bin/md5sum
/bin/mkdir
/usr/bin/mkfifo
/bin/mknod
/usr/bin/mktemp
/bin/mv
/usr/bin/nice
/usr/bin/nl
/usr/bin/nohup
/usr/bin/nproc
/usr/bin/numfmt
/usr/bin/od
/usr/bin/paste
/usr/bin/pathchk
/usr/bin/pinky
/usr/bin/pr
/usr/bin/printenv
/usr/bin/printf
/usr/bin/ptx
/bin/pwd
/usr/bin/readlink
/usr/bin/realpath
/bin/rm
/bin/rmdir
/usr/bin/runcon
/usr/bin/seq
/usr/bin/sha1sum
/usr/bin/sha224sum
/usr/bin/sha256sum
/usr/bin/sha384sum
/usr/bin/sha512sum
/usr/bin/shred
/usr/bin/shuf
/usr/bin/sleep
/usr/bin/sort
/usr/bin/split
/usr/bin/stat
/usr/bin/stdbuf
/bin/stty
/usr/bin/sum
/bin/sync
/usr/bin/tac
/usr/bin/tail
/usr/bin/tee
/usr/bin/test
/usr/bin/timeout
/usr/bin/touch
/usr/bin/tr
/bin/true
/usr/bin/truncate
/usr/bin/tsort
/usr/bin/tty
/bin/uname
/usr/bin/unexpand
/usr/bin/uniq
/usr/bin/unlink
/usr/bin/users
/usr/bin/vdir
/usr/bin/wc
/usr/bin/who
/usr/bin/whoami
/usr/bin/yes
/usr/libexec/coreutils/libstdbuf.so
/usr/share/info/coreutils.info.gz
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
