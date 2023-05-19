#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: distutils3
#
# Source0 file verified with key 0x78D7DEFB9AD59AF1 (scott@kitterman.com)
#
Name     : pypi-py3dns
Version  : 3.2.1
Release  : 1
URL      : https://files.pythonhosted.org/packages/8a/b7/bd0fca1b330527ccf5f47a586900797dd1e054909f7d4c5e287de8b3fe59/py3dns-3.2.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/8a/b7/bd0fca1b330527ccf5f47a586900797dd1e054909f7d4c5e287de8b3fe59/py3dns-3.2.1.tar.gz
Source1  : https://files.pythonhosted.org/packages/8a/b7/bd0fca1b330527ccf5f47a586900797dd1e054909f7d4c5e287de8b3fe59/py3dns-3.2.1.tar.gz.asc
Summary  : Python 3 DNS library
Group    : Development/Tools
License  : Python-2.0
Requires: pypi-py3dns-python = %{version}-%{release}
Requires: pypi-py3dns-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
Release 3.2.0 Mon Jul 23 2018
Switched from distutils to setuptools because "it's the future".  It is
unlikely to have end user impact.  For python3.3+ no additional dependencies
are required.

%package python
Summary: python components for the pypi-py3dns package.
Group: Default
Requires: pypi-py3dns-python3 = %{version}-%{release}

%description python
python components for the pypi-py3dns package.


%package python3
Summary: python3 components for the pypi-py3dns package.
Group: Default
Requires: python3-core
Provides: pypi(py3dns)

%description python3
python3 components for the pypi-py3dns package.


%prep
%setup -q -n py3dns-3.2.1
cd %{_builddir}/py3dns-3.2.1
pushd ..
cp -a py3dns-3.2.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1684517326
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*