%global debug_package %{nil}
%global __strip /bin/true
%global _missing_build_ids_terminate_build 0
%global _build_id_links none
%global major_package_version 12-6

Name:           libcurand
Epoch:          2
Version:        10.3.7.77
Release:        1%{?dist}
Summary:        NVIDIA CUDA Random Number Generation library (cuRAND)
License:        CUDA Toolkit
URL:            https://developer.nvidia.com/cuda-toolkit
ExclusiveArch:  x86_64 aarch64

Source0:        https://developer.download.nvidia.com/compute/cuda/redist/%{name}/linux-x86_64/%{name}-linux-x86_64-%{version}-archive.tar.xz
Source1:        https://developer.download.nvidia.com/compute/cuda/redist/%{name}/linux-sbsa/%{name}-linux-sbsa-%{version}-archive.tar.xz
Source3:        curand.pc

Requires(post): ldconfig
Conflicts:      %{name}-%{major_package_version} < %{?epoch:%{epoch}:}%{version}-%{release}

%description
The NVIDIA CUDA Random Number Generation library (cuRAND) delivers high
performance GPU-accelerated random number generation (RNG). The cuRAND library
delivers high quality random numbers 8x faster using hundreds of processor
cores available in NVIDIA GPUs.

%package devel
Summary:        Development files for NVIDIA CUDA Random Number Generation library (cuRAND)
Requires:       %{name}%{_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Conflicts:      %{name}-devel-%{major_package_version} < %{?epoch:%{epoch}:}%{version}

%description devel
This package provides development files for the NVIDIA CUDA Random Number
Generation library (cuRAND).

%package static
Summary:        Static libraries for NVIDIA CUDA Random Number Generation (cuRAND)
Requires:       %{name}-devel%{_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description static
This package contains static libraries for NVIDIA CUDA Random Number Generation
(cuRAND).

%prep
%ifarch x86_64
%setup -q -n %{name}-linux-x86_64-%{version}-archive
%endif

%ifarch aarch64
%setup -q -T -b 1 -n %{name}-linux-sbsa-%{version}-archive
%endif

%install
mkdir -p %{buildroot}%{_includedir}
mkdir -p %{buildroot}%{_libdir}
mkdir -p %{buildroot}%{_libdir}/pkgconfig/

cp -fr include/* %{buildroot}%{_includedir}/
cp -fr lib/lib* %{buildroot}%{_libdir}/
cp -fr %{SOURCE3} %{buildroot}/%{_libdir}/pkgconfig/

# Set proper variables
sed -i \
    -e 's|CUDA_VERSION|%{version}|g' \
    -e 's|LIBDIR|%{_libdir}|g' \
    -e 's|INCLUDE_DIR|%{_includedir}|g' \
    %{buildroot}/%{_libdir}/pkgconfig/*.pc

%{?ldconfig_scriptlets}

%files
%license LICENSE
%{_libdir}/libcurand.so.*

%files devel
%{_includedir}/curand_discrete2.h
%{_includedir}/curand_discrete.h
%{_includedir}/curand_globals.h
%{_includedir}/curand.h
%{_includedir}/curand_kernel.h
%{_includedir}/curand_lognormal.h
%{_includedir}/curand_mrg32k3a.h
%{_includedir}/curand_mtgp32dc_p_11213.h
%{_includedir}/curand_mtgp32.h
%{_includedir}/curand_mtgp32_host.h
%{_includedir}/curand_mtgp32_kernel.h
%{_includedir}/curand_normal.h
%{_includedir}/curand_normal_static.h
%{_includedir}/curand_philox4x32_x.h
%{_includedir}/curand_poisson.h
%{_includedir}/curand_precalc.h
%{_includedir}/curand_uniform.h
%{_libdir}/libcurand.so
%{_libdir}/pkgconfig/curand.pc

%files static
%{_libdir}/libcurand_static.a

%changelog
* Fri Dec 13 2024 Simone Caronni <negativo17@gmail.com> - 2:10.3.7.77-1
- Update to 10.3.7.77.

* Thu Sep 19 2024 Simone Caronni <negativo17@gmail.com> - 2:10.3.7.68-1
- Update to 10.3.7.68.

* Thu Jul 11 2024 Simone Caronni <negativo17@gmail.com> - 2:10.3.6.82-1
- Update to 10.3.6.82.

* Tue Mar 12 2024 Simone Caronni <negativo17@gmail.com> - 2:10.3.5.119-1
- Update to 10.3.5.119.
- Drop ppc64le.

* Sat Jan 06 2024 Simone Caronni <negativo17@gmail.com> - 2:10.3.4.107-1
- Update to 10.3.4.107.

* Tue Nov 28 2023 Simone Caronni <negativo17@gmail.com> - 2:10.3.4.101-1
- Update to 10.3.4.101.

* Thu Sep 28 2023 Simone Caronni <negativo17@gmail.com> - 2:10.3.3.141-1
- Update to 10.3.3.141.

* Tue Jul 11 2023 Simone Caronni <negativo17@gmail.com> - 2:10.3.3.53-1
- Update to 10.3.3.53.

* Thu Jun 08 2023 Simone Caronni <negativo17@gmail.com> - 2:10.3.2.106-1
- Update to 10.3.2.106.

* Tue Apr 11 2023 Simone Caronni <negativo17@gmail.com> - 2:10.3.2.56-1
- Update to 10.3.2.56.

* Sat Feb 25 2023 Simone Caronni <negativo17@gmail.com> - 2:10.3.1.124-1
- Update to 10.3.1.124.

* Tue Dec 13 2022 Simone Caronni <negativo17@gmail.com> - 2:10.3.1.50-1
- Update to 10.3.1.50.

* Fri Nov 11 2022 Simone Caronni <negativo17@gmail.com> - 2:10.3.0.86-1
- Update to 10.3.0.86.
- Use aarch64 archive in place of sbsa.

* Sun Sep 04 2022 Simone Caronni <negativo17@gmail.com> - 2:10.2.10.91-1
- Update to 10.2.10.91.

* Thu Jun 23 2022 Simone Caronni <negativo17@gmail.com> - 2:10.2.10.50-1
- Update to 10.2.10.50.

* Thu Mar 31 2022 Simone Caronni <negativo17@gmail.com> - 2:10.2.9.124-1
- Update to 10.2.9.124 (CUDA 11.6.2).

* Wed Jan 26 2022 Simone Caronni <negativo17@gmail.com> - 2:10.2.9.55-1
- First build with the new tarball components.

