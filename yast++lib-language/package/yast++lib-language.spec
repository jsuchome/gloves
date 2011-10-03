#
# spec file for package yast++lib-language (Version 0.1.0)
#
# Copyright (c) 2011 SUSE LINUX Products GmbH, Nuernberg, Germany.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           yast++lib-language
License:	LGPLv2.1 or LGPLv3
Group:          System/Management
URL:            https://github.com/yast/yast--
Autoreqprov:    on
Version:        0.1.0
Release:        0
Summary:        Library for high level access to language configuration
Source:         %{name}-%{version}.tar.bz2
Requires:	config_agent-country

BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  ruby
BuildRequires:  rubygem-packaging-rake-tasks
BuildRequires:  config_agent-country

# This is for Hudson (build service) to setup the build env correctly
%if 0
BuildRequires:  rubygem-test-unit
BuildRequires:  rubygem-rcov >= 0.9.3.2
%endif

%description
Library for high level access to language configuration. Part of yast++ project.
Authors:
--------
    Jiri Suchomel <jsuchome@suse.cz>
    Josef Reidinger <jreidinger@suse.cz>


%prep
%setup

%build

%check

#---------------------------------------------------------------
%install
rake install[%{buildroot}/,%{rb_vendorlib}]

#---------------------------------------------------------------
%clean
rm -rf $RPM_BUILD_ROOT

#---------------------------------------------------------------
%files 
%defattr(-,root,root)
%{rb_vendorlib}/y_lib

#---------------------------------------------------------------
%changelog