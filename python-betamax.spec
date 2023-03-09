Summary:	A VCR imitation for python-requests
Name:		python-betamax
Version:	0.8.1
Release:	1
License:	Apache-2.0
Group:		Development/Python
URL:		https://pypi.org/project/betamax/
Source0:	https://files.pythonhosted.org/packages/source/b/betamax/betamax-%{version}.tar.gz
BuildRequires:	pkgconfig(python3)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:  python%{pyver}dist(pytest)
BuildRequires:  python%{pyver}dist(requests)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)

BuildArch:	noarch

%description
Betamax is a VCR imitation for requests. This will make mocking out
requests much easier. It is tested on Travis CI.

Put in a more humorous way: "Betamax records your HTTP interactions
so the NSA does not have to."

%files
%doc README.rst
%license LICENSE
%{py_sitedir}/betamax
%{py_sitedir}/betamax-*.*-info

#--------------------------------------------------------------------

%prep
%autosetup -p1 -n betamax-%{version}

%build
%py_build

%install
%py_install

