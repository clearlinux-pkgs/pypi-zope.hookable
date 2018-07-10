#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : zope.hookable
Version  : 4.2.0
Release  : 17
URL      : https://pypi.debian.net/zope.hookable/zope.hookable-4.2.0.tar.gz
Source0  : https://pypi.debian.net/zope.hookable/zope.hookable-4.2.0.tar.gz
Summary  : Zope hookable
Group    : Development/Tools
License  : ZPL-2.1
Requires: zope.hookable-python3
Requires: zope.hookable-license
Requires: zope.hookable-python
Requires: Sphinx
Requires: coverage
Requires: setuptools
Requires: zope.testing
BuildRequires : pbr
BuildRequires : pip
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : tox
BuildRequires : virtualenv

%description
zope.hookable
        ===============

%package license
Summary: license components for the zope.hookable package.
Group: Default

%description license
license components for the zope.hookable package.


%package python
Summary: python components for the zope.hookable package.
Group: Default
Requires: zope.hookable-python3

%description python
python components for the zope.hookable package.


%package python3
Summary: python3 components for the zope.hookable package.
Group: Default
Requires: python3-core

%description python3
python3 components for the zope.hookable package.


%prep
%setup -q -n zope.hookable-4.2.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1530331917
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python3.7/site-packages python3 setup.py test
%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/zope.hookable
cp LICENSE.txt %{buildroot}/usr/share/doc/zope.hookable/LICENSE.txt
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(-,root,root,-)
/usr/share/doc/zope.hookable/LICENSE.txt

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
