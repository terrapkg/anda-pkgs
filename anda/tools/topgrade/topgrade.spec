Name:           topgrade
# renovate: datasource=github-releases depName=topgrade-rs/topgrade
Version:        16.0.2
Release:        1%{?dist}
Summary:        Upgrade all the things

SourceLicense:  GPL-3.0-or-later
License:        ((MIT OR Apache-2.0) AND Unicode-DFS-2016) AND (0BSD OR MIT OR Apache-2.0) AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR MIT) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND GPL-3.0 AND MIT AND (MIT OR Apache-2.0) AND (MIT OR Zlib OR Apache-2.0) AND MPL-2.0 AND (Unlicense OR MIT)
URL:            https://github.com/topgrade-rs/%{name}
Source:         https://github.com/topgrade-rs/%{name}/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  cargo
BuildRequires:  rust
BuildRequires:  rpm_macro(cargo_install)
BuildRequires:  anda-srpm-macros

%description
Keeping your system up to date usually involves invoking multiple package managers.
This results in big, non-portable shell one-liners saved in your shell.
To remedy this, Topgrade detects which tools you use and
runs the appropriate commands to update them.

%prep
%autosetup -n %{name}-%{version}
%cargo_prep_online

%build
%cargo_license_summary_online
%{cargo_license_online} > LICENSE.dependencies

%install
%cargo_install

%files
%license LICENSE LICENSE.dependencies
%doc BREAKINGCHANGES.md README.md
%{_bindir}/%{name}

%changelog
* Tue Jul 02 2024 Andrey Brusnik <dev@shdwchn.io> - 15.0.0-1
- chore(topgrade): Bump to 15.0.0

* Tue Jun 18 2024 Andrey Brusnik <dev@shdwchn.io> - 14.0.1-1
- feat: Added topgrade package
