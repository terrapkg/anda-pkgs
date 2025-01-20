# saves time so we don't have to download the thing manually
#undefine _disable_source_fetch
# We don't have debug symbols, because .NET
%define debug_package %{nil}
# We aren't using Mono but RPM expected Mono
%global __requires_exclude_from ^/usr/lib/opentabletdriver/.*$
%global __os_install_post %{nil}
%global dotnet_sdk_version 8.0
%global dotnet_runtime_version 6.0

Name: opentabletdriver
Version: 0.6.5.0
Release: 2%?dist
Summary: A cross-platform open source tablet driver
License: LGPLv3
URL: https://github.com/OpenTabletDriver/OpenTabletDriver
Packager: Cappy Ishihara <cappy@fyralabs.com>
%define otddir OpenTabletDriver-%{version}


# This package can be built using a newer .NET SDK version, but you
# specifically need .NET 6.0 to run it.
BuildRequires: dotnet-sdk-%{dotnet_sdk_version}
BuildRequires: git jq systemd-rpm-macros
BuildRequires: gtk3-devel

Requires: dotnet-runtime-%{dotnet_runtime_version}
Requires: libevdev.so.2()(64bit)
Requires: gtk3
Requires: udev
Suggests: libX11
Suggests: libXrandr

%description
OpenTabletDriver is an open source, cross platform, user mode tablet driver. The goal of OpenTabletDriver is to be cross platform as possible with the highest compatibility in an easily configurable graphical user interface.

%prep
mkdir -p %{otddir}
cd %{otddir}
git clone -b v%version %url .

%build
cd %{otddir}
./eng/linux/package.sh --output bin

%install
cd %{otddir}
export DONT_STRIP=1
PREFIX="%{_prefix}" ./eng/linux/package.sh --package Generic --build false
mkdir -p "%{buildroot}"
mv ./dist/files/* "%{buildroot}"/
rm -rf ./dist
mkdir -p "%{buildroot}/%{_prefix}/lib/"
cp -r bin "%{buildroot}/%{_prefix}/lib/opentabletdriver"

%post
%systemd_user_post %name.service

%preun
%systemd_user_preun %name.service

%postun
%systemd_user_postun_with_restart %name.service

%files
%defattr(-,root,root)
%dir %{_prefix}/lib/opentabletdriver
%dir %{_prefix}/share/doc/opentabletdriver
%{_bindir}/otd
%{_bindir}/otd-daemon
%{_bindir}/otd-gui
%{_datadir}/libinput/30-vendor-opentabletdriver.quirks
%{_prefix}/lib/modprobe.d/99-opentabletdriver.conf
%{_prefix}/lib/modules-load.d/opentabletdriver.conf
%{_prefix}/lib/opentabletdriver/*
%{_prefix}/lib/systemd/user/opentabletdriver.service
%{_prefix}/lib/udev/rules.d/70-opentabletdriver.rules
%{_prefix}/share/applications/opentabletdriver.desktop
%{_prefix}/share/man/man8/opentabletdriver.8.gz
%{_prefix}/share/doc/opentabletdriver/LICENSE
%{_prefix}/share/pixmaps/otd.ico
%{_prefix}/share/pixmaps/otd.png
