Name: korora-videos
Version: 0.1
Release: 1%{?dist}
Summary: Package to provide Korora videos

Group: Documentation
License: Creative Commons SA
URL: http://kororaproject.org
Source0: korora-install-howto.webm
BuildArch: noarch

%description
Package to provide video on how to use Korora.

%prep

%build

%install
mkdir -p  %{buildroot}/%{_datadir}/%{name}/
install -m 644 %{SOURCE0} %{buildroot}/%{_datadir}/%{name}/

%files
%doc
%{_datadir}/%{name}/korora-install-howto.webm


%changelog
* Mon Feb 11 2013 Chris Smart <csmart@kororaproject.org> - 0.1-1
- Initial spec.

