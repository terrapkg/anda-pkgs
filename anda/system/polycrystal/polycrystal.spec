Name:           polycrystal
Version:        0.1.0
Release:        1%?dist
Summary:        Barebones "automatic" Flatpak installer for distribution-default Flatpak packages.
URL:            https://github.com/Ultramarine-Linux/polycrystal
Source0:        %url/archive/refs/tags/v%version.tar.gz
License:        GPL
BuildRequires:  cargo cmake anda-srpm-macros cargo-rpm-macros mold glib2-devel flatpak-devel
Packager:       Owen Zimmerman <owen@fyralabs.com>

%description
%summary

%prep
%autosetup -n polycrystal-%version
%cargo_prep_online

%build
%cargo_build

%install
mkdir -p %{buildroot}%{_datadir}/polycrystal
%cargo_install
mkdir -p %buildroot%{_unitdir}
install -Dm644 polycrystal.service %{buildroot}%{_unitdir}/polycrystal.service

# waiting on preset confirmation
# %post
# %systemd_post 91-ultramarine-surface-default.preset?

# %preun
# %systemd_preun 91-ultramarine-surface-default.preset?

# %postun
# %systemd_postun_with_restart 91-ultramarine-surface-default.preset?

%files
%_bindir/polycrystal
%_datadir/polycrystal/
%{_unitdir}/polycrystal.service
%license LICENSE
%doc README.md

%changelog
* TUe Nov 19 2024 Owen-sz <owen@fyralabs.com>
- Switch from commit based to release based, and add systemd services
%changelog
* Fri Nov 15 2024 Owen-sz <owen@fyralabs.com>
- Package Polycrystal