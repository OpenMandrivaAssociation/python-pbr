%define srcname pbr

%bcond_with docs

Name:           python-%{srcname}
Version:        5.4.5
Release:        %mkrel 1
Summary:        Python Build Reasonableness

Group:          Development/Python
License:        MIT
URL:            https://pypi.python.org/pypi/pbr
Source0:        https://files.pythonhosted.org/packages/source/p/pbr/%{srcname}-%{version}.tar.gz

BuildArch:      noarch
%if %{with docs}
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(sphinx-rtd-theme)
%endif

%description
PBR is a library that injects some useful and sensible default
behaviors into your setuptools run. It started off life as the
chunks of code that were copied between all of the OpenStack
projects. Around the time that OpenStack hit 18 different projects
each with at least 3 active branches, it seems like a good time to
make that code into a proper re-usable library.

%package -n python3-%{srcname}
Summary:        Python Build Reasonableness
Group:          Development/Python
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(setuptools)
%{?python_provide:%python_provide python3-%{srcname}}
Obsoletes:      python2-pbr < 5.4.2

%description -n python3-%{srcname}
Manage dynamic plugins for Python applications.

%prep
%setup -q -n %{srcname}-%{version}

# drop bundled egg-info
rm -rf *.egg-info

%build
%py3_build

%if %{with docs}
PYTHONPATH=$(pwd) sphinx-build doc/source html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}
%endif

%install
%py3_install

%files -n python3-%{srcname}
%license LICENSE
%doc README.rst
%if %{with docs}
%doc html
%endif
%{python3_sitelib}/pbr*
%{_bindir}/pbr
