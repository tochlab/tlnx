Name:           setuptools
Version:	57.5.0
Release:        1%{?dist}
Summary:	Collection of extensions to Distutils

License:	MIT
URL:		https://pypi.org/project/setuptools/
Source0:	https://files.pythonhosted.org/packages/20/f7/205a71cc9cc68f23afd9f3083002d0fb0a8c2277baf41a528395552e13c0/setuptools-%{version}.tar.gz

#BuildRequires:
#Requires:

%description
Collection of extensions to Distutils


%prep
%setup -q

%build
python3 setup.py build

%install
rm -rf $RPM_BUILD_ROOT
python3 setup.py install --root=$RPM_BUILD_ROOT --prefix=/usr --install-lib=/usr/lib/python3.8/site-packages --no-compile


#%post
#/sbin/ldconfig
#/sbin/install-info /usr/share/info/DevIL_manual.info.gz /usr/share/info/dir 2> /dev/null || :

#%postun
#/sbin/ldconfig
#/sbin/install-info --delete /usr/share/info/DevIL_manual.info.gz /usr/share/info/dir 2> /dev/null || :

%files
/usr/lib/python3.8/site-packages/_distutils_hack/__init__.py
/usr/lib/python3.8/site-packages/_distutils_hack/override.py
/usr/lib/python3.8/site-packages/distutils-precedence.pth
/usr/lib/python3.8/site-packages/pkg_resources/__init__.py
/usr/lib/python3.8/site-packages/pkg_resources/_vendor/__init__.py
/usr/lib/python3.8/site-packages/pkg_resources/_vendor/appdirs.py
/usr/lib/python3.8/site-packages/pkg_resources/_vendor/packaging/__about__.py
/usr/lib/python3.8/site-packages/pkg_resources/_vendor/packaging/__init__.py
/usr/lib/python3.8/site-packages/pkg_resources/_vendor/packaging/_compat.py
/usr/lib/python3.8/site-packages/pkg_resources/_vendor/packaging/_structures.py
/usr/lib/python3.8/site-packages/pkg_resources/_vendor/packaging/_typing.py
/usr/lib/python3.8/site-packages/pkg_resources/_vendor/packaging/markers.py
/usr/lib/python3.8/site-packages/pkg_resources/_vendor/packaging/requirements.py
/usr/lib/python3.8/site-packages/pkg_resources/_vendor/packaging/specifiers.py
/usr/lib/python3.8/site-packages/pkg_resources/_vendor/packaging/tags.py
/usr/lib/python3.8/site-packages/pkg_resources/_vendor/packaging/utils.py
/usr/lib/python3.8/site-packages/pkg_resources/_vendor/packaging/version.py
/usr/lib/python3.8/site-packages/pkg_resources/_vendor/pyparsing.py
/usr/lib/python3.8/site-packages/pkg_resources/extern/__init__.py
/usr/lib/python3.8/site-packages/pkg_resources/tests/data/my-test-package-source/setup.py
/usr/lib/python3.8/site-packages/setuptools-57.5.0-py3.8.egg-info/PKG-INFO
/usr/lib/python3.8/site-packages/setuptools-57.5.0-py3.8.egg-info/SOURCES.txt
/usr/lib/python3.8/site-packages/setuptools-57.5.0-py3.8.egg-info/dependency_links.txt
/usr/lib/python3.8/site-packages/setuptools-57.5.0-py3.8.egg-info/entry_points.txt
/usr/lib/python3.8/site-packages/setuptools-57.5.0-py3.8.egg-info/requires.txt
/usr/lib/python3.8/site-packages/setuptools-57.5.0-py3.8.egg-info/top_level.txt
/usr/lib/python3.8/site-packages/setuptools/__init__.py
/usr/lib/python3.8/site-packages/setuptools/_deprecation_warning.py
/usr/lib/python3.8/site-packages/setuptools/_distutils/__init__.py
/usr/lib/python3.8/site-packages/setuptools/_distutils/_msvccompiler.py
/usr/lib/python3.8/site-packages/setuptools/_distutils/archive_util.py
/usr/lib/python3.8/site-packages/setuptools/_distutils/bcppcompiler.py
/usr/lib/python3.8/site-packages/setuptools/_distutils/ccompiler.py
/usr/lib/python3.8/site-packages/setuptools/_distutils/cmd.py
/usr/lib/python3.8/site-packages/setuptools/_distutils/command/__init__.py
/usr/lib/python3.8/site-packages/setuptools/_distutils/command/bdist.py
/usr/lib/python3.8/site-packages/setuptools/_distutils/command/bdist_dumb.py
/usr/lib/python3.8/site-packages/setuptools/_distutils/command/bdist_msi.py
/usr/lib/python3.8/site-packages/setuptools/_distutils/command/bdist_rpm.py
/usr/lib/python3.8/site-packages/setuptools/_distutils/command/bdist_wininst.py
/usr/lib/python3.8/site-packages/setuptools/_distutils/command/build.py
/usr/lib/python3.8/site-packages/setuptools/_distutils/command/build_clib.py
/usr/lib/python3.8/site-packages/setuptools/_distutils/command/build_ext.py
/usr/lib/python3.8/site-packages/setuptools/_distutils/command/build_py.py
/usr/lib/python3.8/site-packages/setuptools/_distutils/command/build_scripts.py
/usr/lib/python3.8/site-packages/setuptools/_distutils/command/check.py
/usr/lib/python3.8/site-packages/setuptools/_distutils/command/clean.py
/usr/lib/python3.8/site-packages/setuptools/_distutils/command/config.py
/usr/lib/python3.8/site-packages/setuptools/_distutils/command/install.py
/usr/lib/python3.8/site-packages/setuptools/_distutils/command/install_data.py
/usr/lib/python3.8/site-packages/setuptools/_distutils/command/install_egg_info.py
/usr/lib/python3.8/site-packages/setuptools/_distutils/command/install_headers.py
/usr/lib/python3.8/site-packages/setuptools/_distutils/command/install_lib.py
/usr/lib/python3.8/site-packages/setuptools/_distutils/command/install_scripts.py
/usr/lib/python3.8/site-packages/setuptools/_distutils/command/py37compat.py
/usr/lib/python3.8/site-packages/setuptools/_distutils/command/register.py
/usr/lib/python3.8/site-packages/setuptools/_distutils/command/sdist.py
/usr/lib/python3.8/site-packages/setuptools/_distutils/command/upload.py
/usr/lib/python3.8/site-packages/setuptools/_distutils/config.py
/usr/lib/python3.8/site-packages/setuptools/_distutils/core.py
/usr/lib/python3.8/site-packages/setuptools/_distutils/cygwinccompiler.py
/usr/lib/python3.8/site-packages/setuptools/_distutils/debug.py
/usr/lib/python3.8/site-packages/setuptools/_distutils/dep_util.py
/usr/lib/python3.8/site-packages/setuptools/_distutils/dir_util.py
/usr/lib/python3.8/site-packages/setuptools/_distutils/dist.py
/usr/lib/python3.8/site-packages/setuptools/_distutils/errors.py
/usr/lib/python3.8/site-packages/setuptools/_distutils/extension.py
/usr/lib/python3.8/site-packages/setuptools/_distutils/fancy_getopt.py
/usr/lib/python3.8/site-packages/setuptools/_distutils/file_util.py
/usr/lib/python3.8/site-packages/setuptools/_distutils/filelist.py
/usr/lib/python3.8/site-packages/setuptools/_distutils/log.py
/usr/lib/python3.8/site-packages/setuptools/_distutils/msvc9compiler.py
/usr/lib/python3.8/site-packages/setuptools/_distutils/msvccompiler.py
/usr/lib/python3.8/site-packages/setuptools/_distutils/py35compat.py
/usr/lib/python3.8/site-packages/setuptools/_distutils/py38compat.py
/usr/lib/python3.8/site-packages/setuptools/_distutils/spawn.py
/usr/lib/python3.8/site-packages/setuptools/_distutils/sysconfig.py
/usr/lib/python3.8/site-packages/setuptools/_distutils/text_file.py
/usr/lib/python3.8/site-packages/setuptools/_distutils/unixccompiler.py
/usr/lib/python3.8/site-packages/setuptools/_distutils/util.py
/usr/lib/python3.8/site-packages/setuptools/_distutils/version.py
/usr/lib/python3.8/site-packages/setuptools/_distutils/versionpredicate.py
/usr/lib/python3.8/site-packages/setuptools/_imp.py
/usr/lib/python3.8/site-packages/setuptools/_vendor/__init__.py
/usr/lib/python3.8/site-packages/setuptools/_vendor/more_itertools/__init__.py
/usr/lib/python3.8/site-packages/setuptools/_vendor/more_itertools/more.py
/usr/lib/python3.8/site-packages/setuptools/_vendor/more_itertools/recipes.py
/usr/lib/python3.8/site-packages/setuptools/_vendor/ordered_set.py
/usr/lib/python3.8/site-packages/setuptools/_vendor/packaging/__about__.py
/usr/lib/python3.8/site-packages/setuptools/_vendor/packaging/__init__.py
/usr/lib/python3.8/site-packages/setuptools/_vendor/packaging/_compat.py
/usr/lib/python3.8/site-packages/setuptools/_vendor/packaging/_structures.py
/usr/lib/python3.8/site-packages/setuptools/_vendor/packaging/_typing.py
/usr/lib/python3.8/site-packages/setuptools/_vendor/packaging/markers.py
/usr/lib/python3.8/site-packages/setuptools/_vendor/packaging/requirements.py
/usr/lib/python3.8/site-packages/setuptools/_vendor/packaging/specifiers.py
/usr/lib/python3.8/site-packages/setuptools/_vendor/packaging/tags.py
/usr/lib/python3.8/site-packages/setuptools/_vendor/packaging/utils.py
/usr/lib/python3.8/site-packages/setuptools/_vendor/packaging/version.py
/usr/lib/python3.8/site-packages/setuptools/_vendor/pyparsing.py
/usr/lib/python3.8/site-packages/setuptools/archive_util.py
/usr/lib/python3.8/site-packages/setuptools/build_meta.py
/usr/lib/python3.8/site-packages/setuptools/cli-32.exe
/usr/lib/python3.8/site-packages/setuptools/cli-64.exe
/usr/lib/python3.8/site-packages/setuptools/cli.exe
/usr/lib/python3.8/site-packages/setuptools/command/__init__.py
/usr/lib/python3.8/site-packages/setuptools/command/alias.py
/usr/lib/python3.8/site-packages/setuptools/command/bdist_egg.py
/usr/lib/python3.8/site-packages/setuptools/command/bdist_rpm.py
/usr/lib/python3.8/site-packages/setuptools/command/build_clib.py
/usr/lib/python3.8/site-packages/setuptools/command/build_ext.py
/usr/lib/python3.8/site-packages/setuptools/command/build_py.py
/usr/lib/python3.8/site-packages/setuptools/command/develop.py
/usr/lib/python3.8/site-packages/setuptools/command/dist_info.py
/usr/lib/python3.8/site-packages/setuptools/command/easy_install.py
/usr/lib/python3.8/site-packages/setuptools/command/egg_info.py
/usr/lib/python3.8/site-packages/setuptools/command/install.py
/usr/lib/python3.8/site-packages/setuptools/command/install_egg_info.py
/usr/lib/python3.8/site-packages/setuptools/command/install_lib.py
/usr/lib/python3.8/site-packages/setuptools/command/install_scripts.py
"/usr/lib/python3.8/site-packages/setuptools/command/launcher manifest.xml"
/usr/lib/python3.8/site-packages/setuptools/command/py36compat.py
/usr/lib/python3.8/site-packages/setuptools/command/register.py
/usr/lib/python3.8/site-packages/setuptools/command/rotate.py
/usr/lib/python3.8/site-packages/setuptools/command/saveopts.py
/usr/lib/python3.8/site-packages/setuptools/command/sdist.py
/usr/lib/python3.8/site-packages/setuptools/command/setopt.py
/usr/lib/python3.8/site-packages/setuptools/command/test.py
/usr/lib/python3.8/site-packages/setuptools/command/upload.py
/usr/lib/python3.8/site-packages/setuptools/command/upload_docs.py
/usr/lib/python3.8/site-packages/setuptools/config.py
/usr/lib/python3.8/site-packages/setuptools/dep_util.py
/usr/lib/python3.8/site-packages/setuptools/depends.py
/usr/lib/python3.8/site-packages/setuptools/dist.py
/usr/lib/python3.8/site-packages/setuptools/errors.py
/usr/lib/python3.8/site-packages/setuptools/extension.py
/usr/lib/python3.8/site-packages/setuptools/extern/__init__.py
/usr/lib/python3.8/site-packages/setuptools/glob.py
/usr/lib/python3.8/site-packages/setuptools/gui-32.exe
/usr/lib/python3.8/site-packages/setuptools/gui-64.exe
/usr/lib/python3.8/site-packages/setuptools/gui.exe
/usr/lib/python3.8/site-packages/setuptools/installer.py
/usr/lib/python3.8/site-packages/setuptools/launch.py
/usr/lib/python3.8/site-packages/setuptools/lib2to3_ex.py
/usr/lib/python3.8/site-packages/setuptools/monkey.py
/usr/lib/python3.8/site-packages/setuptools/msvc.py
/usr/lib/python3.8/site-packages/setuptools/namespaces.py
/usr/lib/python3.8/site-packages/setuptools/package_index.py
/usr/lib/python3.8/site-packages/setuptools/py34compat.py
/usr/lib/python3.8/site-packages/setuptools/sandbox.py
"/usr/lib/python3.8/site-packages/setuptools/script (dev).tmpl"
/usr/lib/python3.8/site-packages/setuptools/script.tmpl
/usr/lib/python3.8/site-packages/setuptools/unicode_utils.py
/usr/lib/python3.8/site-packages/setuptools/version.py
/usr/lib/python3.8/site-packages/setuptools/wheel.py
/usr/lib/python3.8/site-packages/setuptools/windows_support.py


%doc

%changelog
* Tue May 31 2016 Adam Miller <maxamillion@fedoraproject.org>
-

# see /usr/libexec/rpm/macros for macros
