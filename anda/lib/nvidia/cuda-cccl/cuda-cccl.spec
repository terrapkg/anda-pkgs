%global real_name cuda_cccl

%global debug_package %{nil}
%global major_package_version 12-6

Name:           %(echo %real_name | tr '_' '-')
Epoch:          1
Version:        12.6.77
Release:        1%{?dist}
Summary:        CXX Core Compute Libraries
License:        CUDA Toolkit
URL:            https://developer.nvidia.com/cuda-toolkit
ExclusiveArch:  x86_64 aarch64

Source0:        https://developer.download.nvidia.com/compute/cuda/redist/%{real_name}/linux-x86_64/%{real_name}-linux-x86_64-%{version}-archive.tar.xz
Source1:        https://developer.download.nvidia.com/compute/cuda/redist/%{real_name}/linux-sbsa/%{real_name}-linux-sbsa-%{version}-archive.tar.xz

Requires:       cmake-filesystem
Conflicts:      %{name}-%{major_package_version} < %{?epoch:%{epoch}:}%{version}

%description
CXX Core Compute Libraries.

%package devel
Summary:        CXX Core Compute Libraries development files

%description devel
CXX Core Compute Libraries development files.

%prep
%ifarch x86_64
%setup -q -n %{real_name}-linux-x86_64-%{version}-archive
%endif

%ifarch aarch64
%setup -q -T -b 1 -n %{real_name}-linux-sbsa-%{version}-archive
%endif

%install
mkdir -p %{buildroot}%{_includedir}
mkdir -p %{buildroot}%{_libdir}/cmake

cp -fr include/* %{buildroot}%{_includedir}/
# Conflict with rocthrust-devel in main repositories:
mv %{buildroot}%{_includedir}/thrust %{buildroot}%{_includedir}/cuda/

cp -fr lib/cmake/* %{buildroot}%{_libdir}/cmake
rm -f %{buildroot}%{_libdir}/cmake/thrust/README.md

%files devel
%license LICENSE
%doc lib/cmake/thrust/README.md
%{_includedir}/*
%{_libdir}/cmake/*

%changelog
* Fri Dec 13 2024 Simone Caronni <negativo17@gmail.com> - 1:12.6.77-1
- Update to 12.6.77.

* Thu Sep 19 2024 Simone Caronni <negativo17@gmail.com> - 1:12.6.37-1
- Update to 12.6.37.

* Thu Jul 11 2024 Simone Caronni <negativo17@gmail.com> - 1:12.5.39-1
- Update to 12.5.39.

* Tue Mar 12 2024 Simone Caronni <negativo17@gmail.com> - 1:12.4.99-1
- Update to 12.4.99.
- Drop ppc64le.

* Mon Jan 22 2024 Simone Caronni <negativo17@gmail.com> - 1:12.3.101-2
- Move /usr/include/thrust to /usr/include/cuda/thrust to avoid conflict with
  rocthrust-devel (#2).

* Tue Nov 28 2023 Simone Caronni <negativo17@gmail.com> - 1:12.3.101-1
- Update to 12.3.101.

* Thu Sep 28 2023 Simone Caronni <negativo17@gmail.com> - 1:12.2.140-1
- Update to 12.2.140.

* Tue Jul 11 2023 Simone Caronni <negativo17@gmail.com> - 1:12.2.53-1
- Update to 12.2.53.

* Thu Jun 08 2023 Simone Caronni <negativo17@gmail.com> - 1:12.1.109-1
- Update to 12.1.109.

* Tue Apr 11 2023 Simone Caronni <negativo17@gmail.com> - 1:12.1.55-1
- Update to 12.1.55.

* Sat Feb 25 2023 Simone Caronni <negativo17@gmail.com> - 1:12.0.140-1
- Update to 12.0.140.

* Tue Dec 13 2022 Simone Caronni <negativo17@gmail.com> - 1:12.0.90-1
- Update to 12.0.90.

* Fri Nov 11 2022 Simone Caronni <negativo17@gmail.com> - 1:11.8.89-1
- Update to 11.8.89.
- Use aarch64 archive in place of sbsa.

* Sun Sep 04 2022 Simone Caronni <negativo17@gmail.com> - 1:11.7.91-1
- Update to 11.7.91.

* Thu Jun 23 2022 Simone Caronni <negativo17@gmail.com> - 1:11.7.58-1
- Update to 11.7.58.

* Tue Jan 25 2022 Simone Caronni <negativo17@gmail.com> - 11.6.55-1
- First build with the new tarball components.

