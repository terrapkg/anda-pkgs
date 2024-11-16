%global commit 76190e5b6f1e5d9fa0cd1800ec260a868df9e5e8
%global commit_date 20241115
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           polycrystal
Version:        %commit_date.%shortcommit
Release:        1%?dist
Summary:        Barebones "automatic" Flatpak installer for distribution-default Flatpak packages.
URL:            https://github.com/Ultramarine-Linux/polycrystal
Source0:        %url/archive/%commit/polycrystal-%commit.tar.gz
License:        GPL
BuildRequires:  cargo cmake anda-srpm-macros cargo-rpm-macros mold glib2-devel flatpak-devel
Packager:       Owen Zimmerman <owen@fyralabs.com>

%description
%summary

%prep
%autosetup -n polycrystal-%commit
%cargo_prep_online

%build
%cargo_build

%install
mkdir -p %{buildroot}%{_datadir}/polycrystal
%cargo_install

%files
%_bindir/polycrystal
%_datadir/polycrystal/
%license LICENSE
%doc README.md

%changelog
* Fri Nov 15 2024 Owen-sz <owen@fyralabs.com>
- Package Polycrystal