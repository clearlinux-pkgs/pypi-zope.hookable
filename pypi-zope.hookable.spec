#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-zope.hookable
Version  : 5.3
Release  : 53
URL      : https://files.pythonhosted.org/packages/03/82/cd8d6c10051478729f23f7f10b6b1eb8897d72669022ce90e7bbfb9ccf6c/zope.hookable-5.3.tar.gz
Source0  : https://files.pythonhosted.org/packages/03/82/cd8d6c10051478729f23f7f10b6b1eb8897d72669022ce90e7bbfb9ccf6c/zope.hookable-5.3.tar.gz
Summary  : Zope hookable
Group    : Development/Tools
License  : ZPL-2.1
Requires: pypi-zope.hookable-filemap = %{version}-%{release}
Requires: pypi-zope.hookable-lib = %{version}-%{release}
Requires: pypi-zope.hookable-license = %{version}-%{release}
Requires: pypi-zope.hookable-python = %{version}-%{release}
Requires: pypi-zope.hookable-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(py)
BuildRequires : pypi(setuptools)
BuildRequires : pypi-pluggy
BuildRequires : pypi-pytest
BuildRequires : pypi-tox
BuildRequires : pypi-virtualenv

%description
===============
zope.hookable
===============
.. image:: https://img.shields.io/pypi/v/zope.hookable.svg
:target: https://pypi.python.org/pypi/zope.hookable/
:alt: Latest release

%package filemap
Summary: filemap components for the pypi-zope.hookable package.
Group: Default

%description filemap
filemap components for the pypi-zope.hookable package.


%package lib
Summary: lib components for the pypi-zope.hookable package.
Group: Libraries
Requires: pypi-zope.hookable-license = %{version}-%{release}
Requires: pypi-zope.hookable-filemap = %{version}-%{release}

%description lib
lib components for the pypi-zope.hookable package.


%package license
Summary: license components for the pypi-zope.hookable package.
Group: Default

%description license
license components for the pypi-zope.hookable package.


%package python
Summary: python components for the pypi-zope.hookable package.
Group: Default
Requires: pypi-zope.hookable-python3 = %{version}-%{release}

%description python
python components for the pypi-zope.hookable package.


%package python3
Summary: python3 components for the pypi-zope.hookable package.
Group: Default
Requires: pypi-zope.hookable-filemap = %{version}-%{release}
Requires: python3-core
Provides: pypi(zope.hookable)
Requires: pypi(setuptools)

%description python3
python3 components for the pypi-zope.hookable package.


%prep
%setup -q -n zope.hookable-5.3
cd %{_builddir}/zope.hookable-5.3
pushd ..
cp -a zope.hookable-5.3 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1667846469
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
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
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}$(python -c "import sys; print(sys.path[-1])") python setup.py test

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-zope.hookable
cp %{_builddir}/zope.hookable-%{version}/LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-zope.hookable/a0b53f43aab58b46bf79ba756c50771c605ab4c5 || :
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

%files filemap
%defattr(-,root,root,-)
/usr/share/clear/filemap/filemap-pypi-zope.hookable

%files lib
%defattr(-,root,root,-)
/usr/share/clear/optimized-elf/other*

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-zope.hookable/a0b53f43aab58b46bf79ba756c50771c605ab4c5

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
