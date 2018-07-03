#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define 	module		langdetect
%define 	egg_name	langdetect
%define		pypi_name	langdetect
Summary:	Language detection library ported from Google's language-detection
Name:		python-%{pypi_name}
Version:	1.0.7
Release:	2
License:	ASL-2.0
Group:		Libraries/Python
Source0:	https://files.pythonhosted.org/packages/source/l/%{pypi_name}/%{pypi_name}-%{version}.zip
# Source0-md5:	6675db2d8abccb97246372767270e912
URL:		https://github.com/Mimino666/langdetect
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-devel
BuildRequires:	python-setuptools
BuildRequires:	python-six
%endif
%if %{with python3}
BuildRequires:	python3-devel
BuildRequires:	python3-setuptools
BuildRequires:	python3-six
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Port of Google's language-detection library to Python.

%package -n python3-%{pypi_name}
Summary:	Language detection library ported from Google's language-detection
Group:		Libraries/Python

%description -n python3-%{pypi_name}
Port of Google's language-detection library to Python.

%prep
%setup -q -n %{pypi_name}-%{version}

# Remove bundled egg-info
%{__rm} -r %{egg_name}.egg-info

%build
%if %{with python2}
%py_build %{?with_tests:test}
%endif

%if %{with python3}
%py3_build %{?with_tests:test}
%endif

%install
rm -rf $RPM_BUILD_ROOT
%if %{with python2}
%py_install
%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc README.md
%{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/%{egg_name}-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-%{pypi_name}
%defattr(644,root,root,755)
%doc README.md
%{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/%{egg_name}-%{version}-py*.egg-info
%endif
