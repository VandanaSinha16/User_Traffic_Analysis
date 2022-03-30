%define name        user_traffic_analysis
%{!?_release: %define _release 1 }
%define release     %{_release}
%define version     0.0.1
%define _url        https://github.com/anuj942/User_Traffic_Analysis.git
%define _srcdir     .
%define PACKAGE_OS_SPECIFIC no
%define OWNER root
%define GROUP root
%define PERM 755


Summary: RPM package consist of tools for user web traffic analysis
Name:           %{name}
Version:        %{version}
Release:        %{release}
URL:            %{_url}
Source0:        %{name}-%{version}.tar.gz
License:        Yahoo
BuildRoot:      %{buildroot}/BUILDROOT
ExclusiveArch:  x86_64

Requires: bash

%description
RPM package consist of tools for user web traffic analysis

%prep
/usr/bin/gzip -d < /root/rpmbuild/SOURCES/%{name}-%{version}.tar.gz |  tar xvf -
tree ~/rpmbuild/

%build

%install
mkdir -p %{buildroot}/opt/user_traffic_analysis/
mkdir -p %{buildroot}/opt/user_traffic_analysis/data
mkdir -p %{buildroot}/opt/user_traffic_analysis/log
mkdir -p %{buildroot}/opt/user_traffic_analysis/conf
mkdir -p %{buildroot}/opt/user_traffic_analysis/results
mkdir -p %{buildroot}/opt/user_traffic_analysis/scripts
install -T ~/rpmbuild/BUILD${SD_SOURCE_DIR}/scripts/Controller.py %{buildroot}/opt/user_traffic_analysis/scripts/Controller.py
install -T ~/rpmbuild/BUILD${SD_SOURCE_DIR}/scripts/HttpMethodsManager.py %{buildroot}/opt/user_traffic_analysis/scripts/HttpMethodsManager.py
install -T ~/rpmbuild/BUILD${SD_SOURCE_DIR}/scripts/UserRequestsManager.py %{buildroot}/opt/user_traffic_analysis/scripts/UserRequestsManager.py
install -T ~/rpmbuild/BUILD${SD_SOURCE_DIR}/scripts/UserAgentsManager.py %{buildroot}/opt/user_traffic_analysis/scripts/UserAgentsManager.py
install -T ~/rpmbuild/BUILD${SD_SOURCE_DIR}/scripts/Usage.py %{buildroot}/opt/user_traffic_analysis/scripts/Usage.py
install -T ~/rpmbuild/BUILD${SD_SOURCE_DIR}/scripts/Utils.py %{buildroot}/opt/user_traffic_analysis/scripts/Utils.py

install -T ~/rpmbuild/BUILD${SD_SOURCE_DIR}/log/sample.log %{buildroot}/opt/user_traffic_analysis/log/sample.log

%files
%defattr(755,root,root,755)
%attr(755,-,-) %dir /opt/user_traffic_analysis/
%attr(755,-,-) %dir /opt/user_traffic_analysis/data
%attr(755,-,-) %dir /opt/user_traffic_analysis/log
%attr(755,-,-) %dir /opt/user_traffic_analysis/conf
%attr(755,-,-) %dir /opt/user_traffic_analysis/results
%attr(755,-,-) %dir /opt/user_traffic_analysis/scripts

%attr(0755,root,root)  /opt/user_traffic_analysis/scripts/Controller.py
%attr(0755,root,root)  /opt/user_traffic_analysis/scripts/Usage.py
%attr(0755,root,root)  /opt/user_traffic_analysis/scripts/UserAgentsManager.py
%attr(0755,root,root)  /opt/user_traffic_analysis/scripts/UserRequestsManager.py
%attr(0755,root,root)  /opt/user_traffic_analysis/scripts/HttpMethodsManager.py
%attr(0755,root,root)  /opt/user_traffic_analysis/scripts/Utils.py

%attr(0755,root,root)  /opt/user_traffic_analysis/log/sample.log

%pre
# equivalent of pre-activate

%post
# equivalent of post-activate

%preun
# equivalent of pre-deactivate

%postun
# equivalent of post-deactivate

%changelog
* Wed Mar 30 2022 Anuj Singh <anu942singh@gmail.com>
- Initial build from source files