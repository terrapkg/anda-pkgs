%global debug_package %{nil}

Name:           topgrade
# renovate: datasource=github-releases depName=topgrade-rs/topgrade
Version:        16.0.2
Release:        1%{?dist}
Summary:        Upgrade all the things

License:        GPL-3.0-or-later
URL:            https://github.com/topgrade-rs/%{name}
Source:         https://github.com/topgrade-rs/%{name}/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  cargo
BuildRequires:  rust

%description
Keeping your system up to date usually involves invoking multiple package managers.
This results in big, non-portable shell one-liners saved in your shell.
To remedy this, Topgrade detects which tools you use and
runs the appropriate commands to update them.

%prep
%autosetup -n %{name}-%{version}

%build
cargo build --release --locked

%install
install -Dpm 0755 target/release/%{name} -t %{buildroot}%{_bindir}/

%files
%license LICENSE
%doc BREAKINGCHANGES.md README.md
%{_bindir}/%{name}

%changelog
* Thu Jan 2 2025 Owen Zimmerman <owen@fyralabs.com>
- Package topgrade, port from Bazzite

* Tue Jul 02 2024 Andrey Brusnik <dev@shdwchn.io> - 15.0.0-1
- chore(topgrade): Bump to 15.0.0

* Tue Jun 18 2024 Andrey Brusnik <dev@shdwchn.io> - 14.0.1-1
- feat: Added topgrade package