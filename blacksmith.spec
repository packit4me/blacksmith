%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

Name:           blacksmith
Version:        0.1
Release:        1
Summary:        cli ssh public key deployment utility

Group:          Applications/Internet
License:        GPLv3
URL:            https://github.com/gregswift/blacksmith
Source0:        %{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch

BuildRequires:  python-setuptools
Requires:       python-requests
Requires:       python-jinja2
Requires:       python-simplejson

%description
blacksmith is a python application that allows you to deploy your ssh
public key to remote systems without having to remember all the
little things, like file permissions.


%prep
%setup -q


%build
%{__python} setup.py build


%install
rm -rf %{buildroot}
%{__python} setup.py install --root=%{buildroot} --record=INSTALLED_FILES


%clean
rm -rf %{buildroot}


%files -f INSTALLED_FILES
%defattr(755,root,root,-)



%changelog
* Tue May 21 2013 Greg Swift <gregswift@gmail.com> 0.1-1
- initial rpm build - when?
