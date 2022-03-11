Name:           meson
Version:	0.53.1
Release:        1%{?dist}
Summary:	Open source build system

License:	Apache-2.0
URL:		http://mesonbuild.com
Source0:	https://github.com/mesonbuild/meson/releases/download/0.53.1/meson-0.53.1.tar.gz

#BuildRequires:
#Requires:

%description

%prep
%setup -q

%build
python3 setup.py build

%install
rm -rf $RPM_BUILD_ROOT
python3 setup.py install --root=$RPM_BUILD_ROOT --prefix=/usr --install-lib=/usr/lib/python/site-packages --no-compile


%files
/usr/bin/meson
/usr/lib/python/site-packages/meson-0.53.1-py3.9.egg-info/PKG-INFO
/usr/lib/python/site-packages/meson-0.53.1-py3.9.egg-info/SOURCES.txt
/usr/lib/python/site-packages/meson-0.53.1-py3.9.egg-info/dependency_links.txt
/usr/lib/python/site-packages/meson-0.53.1-py3.9.egg-info/entry_points.txt
/usr/lib/python/site-packages/meson-0.53.1-py3.9.egg-info/requires.txt
/usr/lib/python/site-packages/meson-0.53.1-py3.9.egg-info/top_level.txt
/usr/lib/python/site-packages/mesonbuild/__init__.py
/usr/lib/python/site-packages/mesonbuild/ast/__init__.py
/usr/lib/python/site-packages/mesonbuild/ast/interpreter.py
/usr/lib/python/site-packages/mesonbuild/ast/introspection.py
/usr/lib/python/site-packages/mesonbuild/ast/postprocess.py
/usr/lib/python/site-packages/mesonbuild/ast/printer.py
/usr/lib/python/site-packages/mesonbuild/ast/visitor.py
/usr/lib/python/site-packages/mesonbuild/backend/__init__.py
/usr/lib/python/site-packages/mesonbuild/backend/backends.py
/usr/lib/python/site-packages/mesonbuild/backend/ninjabackend.py
/usr/lib/python/site-packages/mesonbuild/backend/vs2010backend.py
/usr/lib/python/site-packages/mesonbuild/backend/vs2015backend.py
/usr/lib/python/site-packages/mesonbuild/backend/vs2017backend.py
/usr/lib/python/site-packages/mesonbuild/backend/vs2019backend.py
/usr/lib/python/site-packages/mesonbuild/backend/xcodebackend.py
/usr/lib/python/site-packages/mesonbuild/build.py
/usr/lib/python/site-packages/mesonbuild/cmake/__init__.py
/usr/lib/python/site-packages/mesonbuild/cmake/client.py
/usr/lib/python/site-packages/mesonbuild/cmake/common.py
/usr/lib/python/site-packages/mesonbuild/cmake/data/run_ctgt.py
/usr/lib/python/site-packages/mesonbuild/cmake/executor.py
/usr/lib/python/site-packages/mesonbuild/cmake/fileapi.py
/usr/lib/python/site-packages/mesonbuild/cmake/generator.py
/usr/lib/python/site-packages/mesonbuild/cmake/interpreter.py
/usr/lib/python/site-packages/mesonbuild/cmake/traceparser.py
/usr/lib/python/site-packages/mesonbuild/compilers/__init__.py
/usr/lib/python/site-packages/mesonbuild/compilers/c.py
/usr/lib/python/site-packages/mesonbuild/compilers/c_function_attributes.py
/usr/lib/python/site-packages/mesonbuild/compilers/compilers.py
/usr/lib/python/site-packages/mesonbuild/compilers/cpp.py
/usr/lib/python/site-packages/mesonbuild/compilers/cs.py
/usr/lib/python/site-packages/mesonbuild/compilers/cuda.py
/usr/lib/python/site-packages/mesonbuild/compilers/d.py
/usr/lib/python/site-packages/mesonbuild/compilers/fortran.py
/usr/lib/python/site-packages/mesonbuild/compilers/java.py
/usr/lib/python/site-packages/mesonbuild/compilers/mixins/__init__.py
/usr/lib/python/site-packages/mesonbuild/compilers/mixins/arm.py
/usr/lib/python/site-packages/mesonbuild/compilers/mixins/ccrx.py
/usr/lib/python/site-packages/mesonbuild/compilers/mixins/clang.py
/usr/lib/python/site-packages/mesonbuild/compilers/mixins/clike.py
/usr/lib/python/site-packages/mesonbuild/compilers/mixins/elbrus.py
/usr/lib/python/site-packages/mesonbuild/compilers/mixins/emscripten.py
/usr/lib/python/site-packages/mesonbuild/compilers/mixins/gnu.py
/usr/lib/python/site-packages/mesonbuild/compilers/mixins/intel.py
/usr/lib/python/site-packages/mesonbuild/compilers/mixins/islinker.py
/usr/lib/python/site-packages/mesonbuild/compilers/mixins/pgi.py
/usr/lib/python/site-packages/mesonbuild/compilers/mixins/visualstudio.py
/usr/lib/python/site-packages/mesonbuild/compilers/objc.py
/usr/lib/python/site-packages/mesonbuild/compilers/objcpp.py
/usr/lib/python/site-packages/mesonbuild/compilers/rust.py
/usr/lib/python/site-packages/mesonbuild/compilers/swift.py
/usr/lib/python/site-packages/mesonbuild/compilers/vala.py
/usr/lib/python/site-packages/mesonbuild/coredata.py
/usr/lib/python/site-packages/mesonbuild/dependencies/__init__.py
/usr/lib/python/site-packages/mesonbuild/dependencies/base.py
/usr/lib/python/site-packages/mesonbuild/dependencies/boost.py
/usr/lib/python/site-packages/mesonbuild/dependencies/coarrays.py
/usr/lib/python/site-packages/mesonbuild/dependencies/cuda.py
/usr/lib/python/site-packages/mesonbuild/dependencies/data/CMakeLists.txt
/usr/lib/python/site-packages/mesonbuild/dependencies/data/CMakeListsLLVM.txt
/usr/lib/python/site-packages/mesonbuild/dependencies/data/CMakePathInfo.txt
/usr/lib/python/site-packages/mesonbuild/dependencies/dev.py
/usr/lib/python/site-packages/mesonbuild/dependencies/hdf5.py
/usr/lib/python/site-packages/mesonbuild/dependencies/misc.py
/usr/lib/python/site-packages/mesonbuild/dependencies/mpi.py
/usr/lib/python/site-packages/mesonbuild/dependencies/platform.py
/usr/lib/python/site-packages/mesonbuild/dependencies/scalapack.py
/usr/lib/python/site-packages/mesonbuild/dependencies/ui.py
/usr/lib/python/site-packages/mesonbuild/depfile.py
/usr/lib/python/site-packages/mesonbuild/envconfig.py
/usr/lib/python/site-packages/mesonbuild/environment.py
/usr/lib/python/site-packages/mesonbuild/interpreter.py
/usr/lib/python/site-packages/mesonbuild/interpreterbase.py
/usr/lib/python/site-packages/mesonbuild/linkers.py
/usr/lib/python/site-packages/mesonbuild/mconf.py
/usr/lib/python/site-packages/mesonbuild/mdist.py
/usr/lib/python/site-packages/mesonbuild/mesonlib.py
/usr/lib/python/site-packages/mesonbuild/mesonmain.py
/usr/lib/python/site-packages/mesonbuild/minit.py
/usr/lib/python/site-packages/mesonbuild/minstall.py
/usr/lib/python/site-packages/mesonbuild/mintro.py
/usr/lib/python/site-packages/mesonbuild/mlog.py
/usr/lib/python/site-packages/mesonbuild/modules/__init__.py
/usr/lib/python/site-packages/mesonbuild/modules/cmake.py
/usr/lib/python/site-packages/mesonbuild/modules/dlang.py
/usr/lib/python/site-packages/mesonbuild/modules/fs.py
/usr/lib/python/site-packages/mesonbuild/modules/gnome.py
/usr/lib/python/site-packages/mesonbuild/modules/hotdoc.py
/usr/lib/python/site-packages/mesonbuild/modules/i18n.py
/usr/lib/python/site-packages/mesonbuild/modules/modtest.py
/usr/lib/python/site-packages/mesonbuild/modules/pkgconfig.py
/usr/lib/python/site-packages/mesonbuild/modules/python.py
/usr/lib/python/site-packages/mesonbuild/modules/python3.py
/usr/lib/python/site-packages/mesonbuild/modules/qt.py
/usr/lib/python/site-packages/mesonbuild/modules/qt4.py
/usr/lib/python/site-packages/mesonbuild/modules/qt5.py
/usr/lib/python/site-packages/mesonbuild/modules/rpm.py
/usr/lib/python/site-packages/mesonbuild/modules/sourceset.py
/usr/lib/python/site-packages/mesonbuild/modules/unstable_cuda.py
/usr/lib/python/site-packages/mesonbuild/modules/unstable_icestorm.py
/usr/lib/python/site-packages/mesonbuild/modules/unstable_kconfig.py
/usr/lib/python/site-packages/mesonbuild/modules/unstable_simd.py
/usr/lib/python/site-packages/mesonbuild/modules/windows.py
/usr/lib/python/site-packages/mesonbuild/mparser.py
/usr/lib/python/site-packages/mesonbuild/msetup.py
/usr/lib/python/site-packages/mesonbuild/msubprojects.py
/usr/lib/python/site-packages/mesonbuild/mtest.py
/usr/lib/python/site-packages/mesonbuild/munstable_coredata.py
/usr/lib/python/site-packages/mesonbuild/optinterpreter.py
/usr/lib/python/site-packages/mesonbuild/rewriter.py
/usr/lib/python/site-packages/mesonbuild/scripts/__init__.py
/usr/lib/python/site-packages/mesonbuild/scripts/clangformat.py
/usr/lib/python/site-packages/mesonbuild/scripts/clangtidy.py
/usr/lib/python/site-packages/mesonbuild/scripts/cleantrees.py
/usr/lib/python/site-packages/mesonbuild/scripts/commandrunner.py
/usr/lib/python/site-packages/mesonbuild/scripts/coverage.py
/usr/lib/python/site-packages/mesonbuild/scripts/delwithsuffix.py
/usr/lib/python/site-packages/mesonbuild/scripts/depfixer.py
/usr/lib/python/site-packages/mesonbuild/scripts/dirchanger.py
/usr/lib/python/site-packages/mesonbuild/scripts/gettext.py
/usr/lib/python/site-packages/mesonbuild/scripts/gtkdochelper.py
/usr/lib/python/site-packages/mesonbuild/scripts/hotdochelper.py
/usr/lib/python/site-packages/mesonbuild/scripts/meson_exe.py
/usr/lib/python/site-packages/mesonbuild/scripts/msgfmthelper.py
/usr/lib/python/site-packages/mesonbuild/scripts/regen_checker.py
/usr/lib/python/site-packages/mesonbuild/scripts/scanbuild.py
/usr/lib/python/site-packages/mesonbuild/scripts/symbolextractor.py
/usr/lib/python/site-packages/mesonbuild/scripts/tags.py
/usr/lib/python/site-packages/mesonbuild/scripts/uninstall.py
/usr/lib/python/site-packages/mesonbuild/scripts/vcstagger.py
/usr/lib/python/site-packages/mesonbuild/scripts/yelphelper.py
/usr/lib/python/site-packages/mesonbuild/templates/__init__.py
/usr/lib/python/site-packages/mesonbuild/templates/cpptemplates.py
/usr/lib/python/site-packages/mesonbuild/templates/ctemplates.py
/usr/lib/python/site-packages/mesonbuild/templates/dlangtemplates.py
/usr/lib/python/site-packages/mesonbuild/templates/fortrantemplates.py
/usr/lib/python/site-packages/mesonbuild/templates/objctemplates.py
/usr/lib/python/site-packages/mesonbuild/templates/rusttemplates.py
/usr/lib/python/site-packages/mesonbuild/wrap/__init__.py
/usr/lib/python/site-packages/mesonbuild/wrap/wrap.py
/usr/lib/python/site-packages/mesonbuild/wrap/wraptool.py
/usr/share/man/man1/meson.1.gz
/usr/share/polkit-1/actions/com.mesonbuild.install.policy


%changelog
* Tue May 31 2016 Adam Miller <maxamillion@fedoraproject.org>
-

# see /usr/libexec/rpm/macros for macros
