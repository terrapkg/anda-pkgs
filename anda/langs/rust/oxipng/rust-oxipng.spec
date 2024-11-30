# Generated by rust2rpm 26
%bcond_without check
# don't mangle shebangs
%global __brp_mangle_shebangs %{nil}

%global crate oxipng

Name:           rust-oxipng
Version:        9.1.3
Release:        %autorelease
Summary:        Lossless PNG compression optimizer

License:        MIT
URL:            https://crates.io/crates/oxipng
Source:         %{crates_source}
# Automatically generated patch to strip dependencies and normalize metadata
Patch:          oxipng-fix-metadata-auto.diff

BuildRequires:  anda-srpm-macros cargo-rpm-macros >= 24

%global _description %{expand:
A lossless PNG compression optimizer.}

%description %{_description}

%package     -n %{crate}
Summary:        %{summary}
# FIXME: paste output of %%cargo_license_summary here
License:        # FIXME
# LICENSE.dependencies contains a full license breakdown

%description -n %{crate} %{_description}

%files       -n %{crate}
%license LICENSE
%license LICENSE.dependencies
%doc CHANGELOG.md
%doc MANUAL.txt
%doc README.md
%{_bindir}/oxipng

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license %{crate_instdir}/LICENSE
%doc %{crate_instdir}/CHANGELOG.md
%doc %{crate_instdir}/MANUAL.txt
%doc %{crate_instdir}/README.md
%{crate_instdir}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+binary-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+binary-devel %{_description}

This package contains library source intended for building other packages which
use the "binary" feature of the "%{crate}" crate.

%files       -n %{name}+binary-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+filetime-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+filetime-devel %{_description}

This package contains library source intended for building other packages which
use the "filetime" feature of the "%{crate}" crate.

%files       -n %{name}+filetime-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+freestanding-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+freestanding-devel %{_description}

This package contains library source intended for building other packages which
use the "freestanding" feature of the "%{crate}" crate.

%files       -n %{name}+freestanding-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+parallel-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+parallel-devel %{_description}

This package contains library source intended for building other packages which
use the "parallel" feature of the "%{crate}" crate.

%files       -n %{name}+parallel-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+sanity-checks-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+sanity-checks-devel %{_description}

This package contains library source intended for building other packages which
use the "sanity-checks" feature of the "%{crate}" crate.

%files       -n %{name}+sanity-checks-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+zopfli-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+zopfli-devel %{_description}

This package contains library source intended for building other packages which
use the "zopfli" feature of the "%{crate}" crate.

%files       -n %{name}+zopfli-devel
%ghost %{crate_instdir}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version} -p1
%cargo_prep_online

%build
%cargo_build
%{cargo_license_summary_online}
%{cargo_license_online} > LICENSE.dependencies

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif

%changelog
%autochangelog
