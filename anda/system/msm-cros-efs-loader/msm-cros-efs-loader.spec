Name:                   terra-msm-cros-efs-loader
Version:                1.0.2
Release:                2%?dist
Summary:                EFS loader for Qualcomm-based Chrome OS devices
License:                GPL-3.0-or-later
URL:                    https://gitlab.postmarketos.org/postmarketOS/msm-cros-efs-loader
Source0:                %{url}/-/archive/v%{version}/msm-cros-efs-loader-v%{version}.tar.gz
Source1:                msm-cros-efs-loader.service
Requires:               rmtfs crossystem
BuildArch:              noarch
Packager:               WeirdTreeThing <bradyn127@protonmail.com>
Conflicts:              msm-cros-efs-loader
Provides:               msm-cros-efs-loader
 
%{?systemd_requires}
BuildRequires:  systemd-rpm-macros
 
%description
EFS loader for Qualcomm-based Chrome OS devices
 
%prep
%autosetup -n msm-cros-efs-loader-v%{version}
 
%install
install -Dm755 msm-cros-efs-loader.sh %{buildroot}/usr/bin/msm-cros-efs-loader
install -Dm644 %SOURCE1 %{buildroot}/%{_unitdir}/msm-cros-efs-loader.service

# These systemd services should be included in the preset file for Ultramarine Linux sc7180 (ARM) Chromebook images
%post
%systemd_post msm-cros-efs-loader.service

%preun
%systemd_preun msm-cros-efs-loader.service

%postun
%systemd_postun_with_restart msm-cros-efs-loader.service
 
%files
%_bindir/msm-cros-efs-loader
%{_unitdir}/msm-cros-efs-loader.service
 
%changelog
* Fri Oct 25 2024 WeirdTreeThing <bradyn127@protonmail.com>
- initial release
