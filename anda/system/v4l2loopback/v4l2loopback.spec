Name:           v4l2loopback
Summary:        Utils for V4L2 loopback devices
Version:        0.13.2
Release:        1%{?dist}
License:        GPLv2+
URL:            https://github.com/umlaeute/v4l2loopback
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        modprobe-d-98-v4l2loopback.conf
Source2:        modules-load-d-v4l2loopback.conf
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  help2man
BuildRequires:  systemd-rpm-macros
### For Akmods package
Provides:       %{name}-kmod-common = %{version}-%{release}
Requires:       %{name}-kmod >= %{version}
### For compatibility with older names
Provides:       %{name}-utils = %{version}-%{release}
Obsoletes:      %{name}-utils < 0.12.5-2

%description
Allows creation of virtual video devices. Normal (v4l2) applications will read these devices as if they were ordinary video devices.

%prep
%autosetup -p1 -n %{name}-%{version}

%build
%{set_build_flags}
%make_build utils


%install
make V=1 %{?_smp_mflags} install-utils DESTDIR=%{buildroot} PREFIX=%{_prefix}
make V=1 %{?_smp_mflags} install-man DESTDIR=%{buildroot} PREFIX=%{_prefix}
install -D -m 0644 %{SOURCE1} %{buildroot}%{_modprobedir}/98-v4l2loopback.conf
install -D -m 0644 %{SOURCE2} %{buildroot}%{_modulesloaddir}/v4l2loopback.conf

%files
%doc README.md AUTHORS NEWS
%license COPYING
%attr(0755,root,root) %{_bindir}/v4l2loopback-ctl
%attr(0644,root,root) %{_mandir}/man1/v4l2loopback-ctl.1*
%{_modprobedir}/98-v4l2loopback.conf
%{_modulesloaddir}/v4l2loopback.conf

%changelog
%autochangelog
