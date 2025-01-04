%global gcc_major 13

Name:           cuda-gcc
Version:        13.3.1
Release:        2%{?dist}
Summary:        GNU Compiler Collection CUDA compatibility package
License:        BSD
URL:            http://gcc.gnu.org

BuildArch:      noarch

Requires:       gcc%{gcc_major}-c++

Provides:       cuda-gcc = %{version}-%{release}
Obsoletes:      cuda-gcc < %{version}-%{release}
Provides:       cuda-gcc-c++ = %{version}-%{release}
Obsoletes:      cuda-gcc-c++ < %{version}-%{release}
Provides:       cuda-gcc-gfortran = %{version}-%{release}
Obsoletes:      cuda-gcc-gfortran < %{version}-%{release}

%description
The %{name} package contains scripts that are sourced in the environment to use
the GCC compatibility packages when invoking NVCC.

%install
mkdir -p %{buildroot}%{_sysconfdir}/profile.d/

cat > %{buildroot}%{_sysconfdir}/profile.d/%{name}.sh <<EOF
export NVCC_CCBIN='g++-%{gcc_major}'

# Alternatively you can use the following:
export NVCC_PREPEND_FLAGS='-ccbin %{_bindir}/g++-%{gcc_major}'
EOF

cat > %{buildroot}%{_sysconfdir}/profile.d/%{name}.csh <<EOF
setenv NVCC_CCBIN 'g++-%{gcc_major}'

# Alternatively you can use the following:
setenv NVCC_PREPEND_FLAGS '-ccbin %{_bindir}/g++-%{gcc_major}'
EOF

%files
%config(noreplace) %{_sysconfdir}/profile.d/%{name}.csh
%config(noreplace) %{_sysconfdir}/profile.d/%{name}.sh

%changelog
* Mon Dec 16 2024 Simone Caronni <negativo17@gmail.com> - 13.3.1-2
- Trim changelog.

* Fri Dec 13 2024 Simone Caronni <negativo17@gmail.com> - 13.3.1-1
- There is no need anymore for a custom GCC package, as Fedora ships gcc13 as a
  compatibility package. Adjust accordingly. This package is just now a profile.

* Wed Jul 10 2024 Simone Caronni <negativo17@gmail.com> - 13.3.0-1
- Update to 13.3.0.

* Mon Mar 25 2024 Simone Caronni <negativo17@gmail.com> - 12.3.0-2
- Fix library exclusions.

* Sat Jun 03 2023 Simone Caronni <negativo17@gmail.com> - 12.3.0-1
- Update to 12.3.0.
- Adjust binary move.

* Fri Mar 31 2023 Simone Caronni <negativo17@gmail.com> - 12.2.1-2
- Re-enable libquadmath support.
- Fix rpm perl macro invocation during build and double bin path.

* Mon Mar 13 2023 Simone Caronni <negativo17@gmail.com> - 12.2.1-1
- Update to latest 12 snapshot.
- Simplify installation. If the package is installed, nvcc is always executed
  with -ccbin.

* Mon Aug 08 2022 Peter Kovář <peter.kovar@reflexion.tv> - 11.3.0-2
- Remove info files.

* Tue May 17 2022 Simone Caronni <negativo17@gmail.com> - 11.3.0-1
- Update to 11.3.0
- Simplify SPEC file.
