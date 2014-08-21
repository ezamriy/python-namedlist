%global pkg     namedlist
Name:           python-namedlist
Version:        1.5
Release:        1%{?dist}
Summary:        Similar to namedtuple, but instances are mutable

Group:          Development/Languages
License:        Apache License Version 2.0
URL:            http://bitbucket.org/ericvsmith/%{pkg}/
Source0:        http://pypi.python.org/packages/source/n/%{pkg}/%{pkg}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python-setuptools


%description
namedlist provides 2 factory functions, namedlist.namedlist and
namedlist.namedtuple.

namedlist.namedtuple is similar to collections.namedtuple, with
the following differences:

 - namedlist.namedtuple supports per-field default values.
 - namedlist.namedtuple supports an optional default value, to be used by all
   fields that do not have an explicit default value.

namedlist.namedlist is similar, with this additional difference:

 - namedlist.namedlist instances are mutable.


%prep
%setup -q -n %{pkg}-%{version}


%build
%{__python} setup.py build


%install
rm -fr %{buildroot}
%{__python} setup.py install -O1 --skip-build --root %{buildroot}


%clean
rm -fr %{buildroot}


%files
%defattr(-,root,root,-)
%doc CHANGES.txt README.txt LICENSE.txt
%{python_sitelib}/*


%changelog
* Thu Aug 21 2014 Eugene Zamriy <eugene@zamriy.info> - 1.5-1
- Initial release: 1.5 version
