%define srcname pbr

%bcond_with docs

Name:           python-%{srcname}
Version:	5.5.1
Release:	1
Summary:        Python Build Reasonableness

Group:          Development/Python
License:        MIT
URL:            https://pypi.python.org/pypi/pbr
Source0:	https://files.pythonhosted.org/packages/65/e2/8cb5e718a3a63e8c22677fde5e3d8d18d12a551a1bbd4557217e38a97ad0/pbr-5.5.1.tar.gz

BuildArch:      noarch
%if %{with docs}
BuildRequires:  python3dist(sphinx)
#BuildRequires:  python3dist(sphinx-rtd-theme)
%endif
BuildRequires:  pkgconfig(python)
BuildRequires:  python3dist(setuptools)
%{?python_provide:%python_provide python3-%{srcname}}

%description
PBR is a library that injects some useful and sensible default
behaviors into your setuptools run. It started off life as the
chunks of code that were copied between all of the OpenStack
projects. Around the time that OpenStack hit 18 different projects
each with at least 3 active branches, it seems like a good time to
make that code into a proper re-usable library.

%prep
%setup -q -n %{srcname}-%{version}

# drop bundled egg-info
rm -rf *.egg-info

%build
%py_build

%if %{with docs}
PYTHONPATH=$(pwd) sphinx-build doc/source html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}
%endif

%install
%py_install

%files
%license LICENSE
%doc README.rst
%if %{with docs}
%doc html
%endif
%{python_sitelib}/pbr*
%{_bindir}/pbr
