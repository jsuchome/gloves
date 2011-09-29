#
# spec file for package configagents (Version 0.1.0)
#
# Copyright (c) 2011 SUSE LINUX Products GmbH, Nuernberg, Germany.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           config_agent-country
License:	      LGPLv2.1 or LGPLv3
Group:          System/Management
URL:            https://github.com/yast/yast--
Autoreqprov:    on
Version:        0.1.0
Release:        0
Summary:        Set of dbus services for basic access to country config
Source:         %{name}-%{version}.tar.bz2
Source1:        %{name}-rpmlintrc
Requires:       libconfigagent
Requires:       rubygem-ruby-augeas
Requires:       augeas
Requires:       rubygem-ruby-dbus

BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  ruby
BuildRequires:  rubygem-packaging-rake-tasks
BuildRequires:  libconfigagent

# This is for Hudson (build service) to setup the build env correctly
%if 0
BuildRequires:  rubygem-test-unit
BuildRequires:  rubygem-rcov >= 0.9.3.2
%endif

%description
config_agent-country - Set of config agents for for easier access to country (locale) configuration files and scripts.
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
%dir /etc/dbus-1
%dir /etc/dbus-1/system.d
%dir /usr/share/dbus-1
%dir /usr/share/dbus-1/system-services
%dir /usr/share/polkit-1
%dir /usr/share/polkit-1/actions
%doc COPYING COPYING.LESSER
%config /etc/dbus-1/system.d/org.opensuse.config_agent*
%{rb_vendorlib}/config_agent
/usr/share/config_agents
/usr/share/dbus-1/system-services/org.opensuse.config_agent*
/usr/share/polkit-1/actions/org.opensuse.config_agent*


#---------------------------------------------------------------
%changelog
