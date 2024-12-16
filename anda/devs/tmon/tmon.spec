%global commit e8cae0d88dc8d51cb0e34e3fd3553bcbdaf04ca5
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commit_date 20241215
%global debug_package %{nil}

Name:           tmon
Version:        %{commit_date}.git~%{shortcommit}
Release:        1%{?dist}
Summary:        A tiny system monitor for Linux

License:        GPL-3.0
URL:            https://github.com/pondda/tmon
Source0:        %{url}/archive/%{commit}.tar.gz

Requires:       lm_sensors
Conflicts:      kernel-tools

Suggests:       nerd-fonts

BuildRequires:  make gcc-c++ ncurses-devel

%description
%{summary}

%prep
%autosetup -n %{name}-%{commit}

%build
%make_build

%install
install -m 0755 -vd              %{buildroot}/%{_bindir}
install -m 0755 -vp tmon         %{buildroot}/%{_bindir}/tmon
install -m 0755 -vd              %{buildroot}/%{_sysconfdir}/tmon
install -m 0644 -vp default.conf %{buildroot}/%{_sysconfdir}/tmon/

%files
%license LICENSE
%doc README.md
%{_bindir}/tmon
%{_sysconfdir}/tmon/default.conf

%changelog
* Tue Dec 17 2024 sadlerm <sad_lerm@hotmail.com>
- Initial package

