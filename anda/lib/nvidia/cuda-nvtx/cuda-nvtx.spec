%global real_name cuda_nvtx

%global debug_package %{nil}
%global __strip /bin/true
%global _missing_build_ids_terminate_build 0
%global _build_id_links none
%global major_package_version 12-6

Name:           %(echo %real_name | tr '_' '-')
Epoch:          1
Version:        12.6.77
Release:        1%{?dist}
Summary:        NVIDIA Tools Extension (NVTX) library
License:        CUDA Toolkit
URL:            https://developer.nvidia.com/cuda-toolkit
ExclusiveArch:  x86_64 aarch64

Source0:        https://developer.download.nvidia.com/compute/cuda/redist/%{real_name}/linux-x86_64/%{real_name}-linux-x86_64-%{version}-archive.tar.xz
Source1:        https://developer.download.nvidia.com/compute/cuda/redist/%{real_name}/linux-sbsa/%{real_name}-linux-sbsa-%{version}-archive.tar.xz
Source3:        nvToolsExt.pc

Requires(post): ldconfig
Conflicts:      %{name}-%{major_package_version} < %{?epoch:%{epoch}:}%{version}-%{release}

%description
A C-based API for annotating events, code ranges, and resources in your
applications. Applications which integrate NVTX can use the Visual Profiler to
capture and visualize these events and ranges.

%package devel
Summary:        Development files for NVIDIA Tools Extension (NVTX) library
Requires:       %{name}%{_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Conflicts:      %{name}-devel-%{major_package_version} < %{?epoch:%{epoch}:}%{version}

%description devel
This package provides development files for the NVIDIA Tools Extension (NVTX)
library.

%prep
%ifarch x86_64
%setup -q -n %{real_name}-linux-x86_64-%{version}-archive
%endif

%ifarch aarch64
%setup -q -T -b 1 -n %{real_name}-linux-sbsa-%{version}-archive
%endif

%install
mkdir -p %{buildroot}%{_includedir}
mkdir -p %{buildroot}%{_libdir}
mkdir -p %{buildroot}%{_libdir}/pkgconfig/

cp -fr include/* %{buildroot}%{_includedir}/
cp -fr lib/* %{buildroot}%{_libdir}/
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
%{_libdir}/libnvToolsExt.so.*

%files devel
%{_includedir}/nvToolsExtCuda.h
%{_includedir}/nvToolsExtCudaRt.h
%{_includedir}/nvToolsExt.h
%{_includedir}/nvToolsExtOpenCL.h
%{_includedir}/nvToolsExtSync.h
%dir %{_includedir}/nvtx3/
%{_includedir}/nvtx3/nvToolsExtCuda.h
%{_includedir}/nvtx3/nvToolsExtCudaRt.h
%{_includedir}/nvtx3/nvToolsExt.h
%{_includedir}/nvtx3/nvToolsExtOpenCL.h
%{_includedir}/nvtx3/nvToolsExtSync.h
%dir %{_includedir}/nvtx3/nvtxDetail/
%{_includedir}/nvtx3/nvtxDetail/nvtxImplCore.h
%{_includedir}/nvtx3/nvtxDetail/nvtxImplCudaRt_v3.h
%{_includedir}/nvtx3/nvtxDetail/nvtxImplCuda_v3.h
%{_includedir}/nvtx3/nvtxDetail/nvtxImpl.h
%{_includedir}/nvtx3/nvtxDetail/nvtxImplOpenCL_v3.h
%{_includedir}/nvtx3/nvtxDetail/nvtxImplSync_v3.h
%{_includedir}/nvtx3/nvtxDetail/nvtxInitDecls.h
%{_includedir}/nvtx3/nvtxDetail/nvtxInitDefs.h
%{_includedir}/nvtx3/nvtxDetail/nvtxInit.h
%{_includedir}/nvtx3/nvtxDetail/nvtxLinkOnce.h
%{_includedir}/nvtx3/nvtxDetail/nvtxTypes.h
%{_libdir}/libnvToolsExt.so
%{_libdir}/pkgconfig/nvToolsExt.pc

%changelog
* Fri Dec 13 2024 Simone Caronni <negativo17@gmail.com> - 1:12.6.77-1
- Update to 12.6.77.

* Thu Sep 19 2024 Simone Caronni <negativo17@gmail.com> - 1:12.6.68-1
- Update to 12.6.68.

* Thu Jul 11 2024 Simone Caronni <negativo17@gmail.com> - 1:12.5.82-1
- Update to 12.5.82.

* Tue Mar 12 2024 Simone Caronni <negativo17@gmail.com> - 1:12.4.99-1
- Update to 12.4.99.
- Drop ppc64le.

* Tue Nov 28 2023 Simone Caronni <negativo17@gmail.com> - 1:12.3.101-1
- Update to 12.3.101.

* Thu Sep 28 2023 Simone Caronni <negativo17@gmail.com> - 1:12.2.140-1
- Update to 12.2.140.

* Tue Jul 11 2023 Simone Caronni <negativo17@gmail.com> - 1:12.2.53-1
- Update to 12.2.53.

* Thu Jun 08 2023 Simone Caronni <negativo17@gmail.com> - 1:12.1.105-1
- Update to 12.1.105.

* Tue Apr 11 2023 Simone Caronni <negativo17@gmail.com> - 1:12.1.66-1
- Update to 12.1.66.

* Sat Feb 25 2023 Simone Caronni <negativo17@gmail.com> - 1:12.0.140-1
- Update to 12.0.140.

* Tue Dec 13 2022 Simone Caronni <negativo17@gmail.com> - 1:12.0.76-1
- Update to 12.0.76.

* Fri Nov 11 2022 Simone Caronni <negativo17@gmail.com> - 1:11.8.86-1
- Update to 11.8.86.
- Use aarch64 archive in place of sbsa.

* Sun Sep 04 2022 Simone Caronni <negativo17@gmail.com> - 1:11.7.91-1
- Update to 11.7.91.

* Thu Jun 23 2022 Simone Caronni <negativo17@gmail.com> - 1:11.7.50-1
- Update to 11.7.50.

* Thu Mar 31 2022 Simone Caronni <negativo17@gmail.com> - 1:11.6.124-1
- Update to 11.6.124 (CUDA 11.6.2).

* Tue Mar 08 2022 Simone Caronni <negativo17@gmail.com> - 1:11.6.112-1
- Update to 11.6.112 (CUDA 11.6.1).

* Tue Jan 25 2022 Simone Caronni <negativo17@gmail.com> - 1:11.6.55-1
- First build with the new tarball components.
