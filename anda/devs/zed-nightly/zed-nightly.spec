%global commit 64bb79b71dc2b70b627a264c9b63ea1a8c8dc524
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commit_date 20240613
%global ver v0.56.0

%bcond_without check
%global debug_package %{nil}

%global crate zed
%global app_id dev.zed.Zed-Nightly

Name:           zed-nightly
Version:        %ver^%commit_date.%shortcommit
Release:        1%?dist
Summary:        Zed is a high-performance, multiplayer code editor

License:        MIT
URL:            https://zed.dev/
Source0:        https://github.com/zed-industries/zed/archive/%{commit}.zip
# Source1:        zed-nightly.desktop

Conflicts:      zed
Provides:       zed

BuildRequires:  cargo-rpm-macros >= 24
BuildRequires:  anda-srpm-macros
BuildRequires:  gcc
BuildRequires:  g++
BuildRequires:  clang
BuildRequires:  mold
BuildRequires:  alsa-lib-devel
BuildRequires:  fontconfig-devel
BuildRequires:  wayland-devel
BuildRequires:  libxkbcommon-x11-devel
BuildRequires:  openssl-devel
BuildRequires:  libzstd-devel
BuildRequires:  perl-FindBin
BuildRequires:  perl-IPC-Cmd
BuildRequires:  perl-File-Compare
BuildRequires:  perl-File-Copy
BuildRequires:  perl-lib
BuildRequires:  vulkan-loader

%description
Code at the speed of thought - Zed is a high-performance, multiplayer code editor from the creators of Atom and Tree-sitter.

%prep
%autosetup -n %{crate}-%{commit} -p1
%cargo_prep_online

export DO_STARTUP_NOTIFY="true"
export APP_ID="%app_id"
export APP_ICON="%app_id"
export APP_NAME="Zed Nightly"
export APP_CLI="zed"
export ZED_UPDATE_EXPLANATION="Run dnf up to update Zed Nightly from Terra."
export ZED_RELEASE_CHANNEL=nightly
export BRANDING_LIGHT="#e9aa6a"
export BRANDING_DARK="#1a5fb4"

echo "StartupWMClass=$APP_ID" >> crates/zed/resources/zed.desktop.in
envsubst < "crates/zed/resources/zed.desktop.in" > $APP_ID.desktop # from https://aur.archlinux.org/cgit/aur.git/tree/PKGBUILD?h=zed-git#n52

envsubst < "crates/zed/resources/flatpak/zed.metainfo.xml.in" > $APP_ID.metainfo.xml

%build
export ZED_UPDATE_EXPLANATION="Run dnf up to update Zed Nightly from Terra."

echo "nightly" > crates/zed/RELEASE_CHANNEL

cargo build --release --package zed --package cli
script/generate-licenses

%install
install -Dm755 target/release/zed %{buildroot}%{_libexecdir}/zed-editor
install -Dm755 target/release/cli %{buildroot}%{_bindir}/zed

install -Dm644 %app_id.desktop %{buildroot}%{_datadir}/applications/%app_id.desktop
install -Dm644 crates/zed/resources/app-icon-nightly.png %{buildroot}%{_datadir}/pixmaps/%app_id.png

install -Dm644 %app_id.metainfo.xml %{buildroot}%{_metainfodir}/%app_id.metainfo.xml

%if %{with check}
%check
%cargo_test
%endif

%files
%{_libexecdir}/zed-editor
%{_bindir}/zed
%{_datadir}/applications/%app_id.desktop
%{_datadir}/pixmaps/%app_id.png
%{_metainfodir}/%app_id.metainfo.xml
%license assets/licenses.md

%changelog
%autochangelog
