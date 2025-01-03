%define debug_package %nil

%global commit 1a3fdb7fa15a4bba7204bef69702b7a10a297828
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commit_date 20241206

Name:           gamescope-session-steam
Version:        %commit_date.%shortcommit
Release:        1%?dist
Summary:        gamescope-session-steam
License:        MIT
URL:            https://github.com/ChimeraOS/gamescope-session-steam
Source0:        %url/archive/%commit.tar.gz

%description
%summary.

%prep
%autosetup -n %name-%commit

%build

%install
mkdir -p %buildroot
cp -r usr %buildroot/

%files
%license LICENSE
%_bindir/steamos-polkit-helpers/
%_bindir/jupiter-biosupdate
%_bindir/steam-http-loader
%_bindir/steamos-select-branch
%_bindir/steamos-session-select
%_bindir/steamos-update
%_datadir/applications/gamescope-mimeapps.list
%_datadir/applications/steam_http_loader.desktop
%_datadir/gamescope-session-plus/sessions.d/steam
%_datadir/polkit-1/actions/org.chimeraos.update.policy
%_datadir/wayland-sessions/gamescope-session-steam.desktop
%_datadir/wayland-sessions/gamescope-session.desktop
