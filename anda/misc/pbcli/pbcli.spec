%global ver v2.6.0
%global goodver %(echo %ver | sed 's/v//g')
%global __brp_mangle_shebangs %{nil}
%bcond_without mold

%global _description %{expand:
pbcli is a command line client which allows to upload and download pastes from privatebin directly from the command line.}

Name:           pbcli
Version:        2.6.0
Release:        1%?dist
Summary:        A PrivateBin commandline upload and download utility
License:        MIT
URL:            https://github.com/Mydayyy/pbcli
Source0:        https://github.com/Mydayyy/pbcli/archive/refs/tags/%ver.tar.gz
BuildRequires:  cargo-rpm-macros >= 24
BuildRequires:  anda-srpm-macros mold
BuildRequires:  perl-IPC-Cmd perl-ExtUtils-MM-Utils perl-FindBin perl-lib perl-File-Compare perl-File-Copy
BuildRequires:  openssl-libs openssl-devel
Packager:       ShinyGil <rockgrub@protonmail.com>

%description %_description

%files
%doc README.md
%license LICENSE-MIT
%license LICENSE-UNLICENSE
%license LICENSE.dependencies
%_bindir/pbcli
%_libdir/libpbcli.so

%prep
%autosetup -n pbcli-%goodver
%cargo_prep_online

%build
%cargo_build
%{cargo_license_online} > LICENSE.dependencies

%install
install -Dm755 target/rpm/pbcli %{buildroot}%{_bindir}/pbcli
install -Dm755 target/rpm/libpbcli.so %{buildroot}%{_libdir}/libpbcli.so

%changelog
* Sat Dec 21 2024 ShinyGil <rockgrub@protonmail.com>
- Initial package
