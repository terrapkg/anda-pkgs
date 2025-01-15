# Generated by rust2rpm 27
%bcond check 0

%global crate sheldon

Name:           rust-sheldon
Version:        0.8.0
Release:        1%?dist
Summary:        Fast, configurable, shell plugin manager

License:        MIT OR Apache-2.0
URL:            https://sheldon.cli.rs
Source:         %{crates_source}

BuildRequires:  cargo-rpm-macros >= 24
BuildRequires:  anda-srpm-macros
BuildRequires:  pkgconfig(openssl)

%global _description %{expand:
Fast, configurable, shell plugin manager.}

%description %{_description}

%package     -n %{crate}
Summary:        %{summary}
License:        (Apache-2.0 OR MIT) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND MIT AND (MIT OR Apache-2.0) AND (MIT OR Apache-2.0 OR Zlib) AND (Unlicense OR MIT) AND (Zlib OR Apache-2.0 OR MIT)

%description -n %{crate} %{_description}

%files       -n %{crate}
%license LICENSE-APACHE
%license LICENSE-MIT
%license LICENSE.dependencies
%doc README.md
%{_bindir}/sheldon

%prep
%autosetup -n %{crate}-%{version} -p1
%cargo_prep_online

%build
%{cargo_license_summary_online}
%{cargo_license_online} > LICENSE.dependencies

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif