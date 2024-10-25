Name:                   msm-cros-efs-loader
Version:                1.0.2
Release:                1%?dist
Summary:                EFS loader for Qualcomm-based Chrome OS devices
License:                GPL-3.0-or-later
URL:                    https://gitlab.postmarketos.org/postmarketOS/msm-cros-efs-loader
Source0:                %{url}/-/archive/v%{version}/msm-cros-efs-loader-v%{version}.tar.gz
Source1:                msm-cros-efs-loader.service
Requires:               rmtfs crossystem
BuildArch:              noarch
 
%{?systemd_requires}
BuildRequires:  systemd-rpm-macros
 
%description
EFS loader for Qualcomm-based Chrome OS devices
 
%prep
%autosetup -n msm-cros-efs-loader-v%{version}
 
%install
install -Dm755 %{name}.sh %{buildroot}/usr/bin/%{name}
install -Dm644 %SOURCE1 %{buildroot}/%{_unitdir}/msm-cros-efs-loader.service
 
%post
systemctl mask rmtfs.service
%systemd_post msm-cros-efs-loader.service
 
%files
%_bindir/%name
%{_unitdir}/msm-cros-efs-loader.service
 
%changelog
* Fri Oct 25 2024 WeirdTreeThing <bradyn127@protonmail.com>
- initial release
