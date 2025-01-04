%global debug_package %{nil}
%global __strip /bin/true
%global _missing_build_ids_terminate_build 0
%global _build_id_links none
%global major_package_version 12-6

Name:           libnvjpeg
Epoch:          1
Version:        12.3.3.54
Release:        1%{?dist}
Summary:        CUDA NVIDIA JPEG decoder (nvJPEG)
License:        CUDA Toolkit
URL:            https://developer.nvidia.com/cuda-toolkit
ExclusiveArch:  x86_64 aarch64

Source0:        https://developer.download.nvidia.com/compute/cuda/redist/%{name}/linux-x86_64/%{name}-linux-x86_64-%{version}-archive.tar.xz
Source1:        https://developer.download.nvidia.com/compute/cuda/redist/%{name}/linux-sbsa/%{name}-linux-sbsa-%{version}-archive.tar.xz
Source3:        nvjpeg.pc

Requires(post): ldconfig
Conflicts:      %{name}-%{major_package_version} < %{?epoch:%{epoch}:}%{version}-%{release}

%description
nvJPEG is a high-performance GPU-accelerated library for JPEG decoding. nvJPEG
supports decoding of single and batched images, color space conversion, multiple
phase decoding, and hybrid decoding using both CPU and GPU. Applications that
rely on nvJPEG for decoding deliver higher throughput and lower latency JPEG
decode compared CPU-only decoding.

%package devel
Summary:        Development files for CUDA NVIDIA JPEG decoder (nvJPEG)
Requires:       %{name}%{_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Conflicts:      %{name}-devel-%{major_package_version} < %{?epoch:%{epoch}:}%{version}

%description devel
This package provides development files for the CUDA NVIDIA JPEG decoder
(nvJPEG).

%package static
Summary:        Static libraries for CUDA NVIDIA JPEG decoder (nvJPEG)
Requires:       %{name}-devel%{_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description static
This package contains static libraries for CUDA NVIDIA JPEG decoder (nvJPEG).

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
%{_libdir}/libnvjpeg.so.*

%files devel
%{_includedir}/nvjpeg.h
%{_libdir}/libnvjpeg.so
%{_libdir}/pkgconfig/nvjpeg.pc

%files static
%{_libdir}/libnvjpeg_static.a

%changelog
* Thu Sep 19 2024 Simone Caronni <negativo17@gmail.com> - 1:12.3.3.54-1
- Update to 12.3.3.54.

* Thu Jul 11 2024 Simone Caronni <negativo17@gmail.com> - 1:12.3.2.81-1
- Update to 12.3.2.81.

* Tue Mar 12 2024 Simone Caronni <negativo17@gmail.com> - 1:12.3.1.89-1
- Update to 12.3.1.89.
- Drop ppc64le.

* Tue Nov 28 2023 Simone Caronni <negativo17@gmail.com> - 1:12.3.0.81-1
- Update to 12.3.0.81.

* Thu Sep 28 2023 Simone Caronni <negativo17@gmail.com> - 1:12.2.2.4-1
- Update to 12.2.2.4.

* Tue Jul 11 2023 Simone Caronni <negativo17@gmail.com> - 1:12.1.1.14-1
- Update to 12.1.1.14.

* Thu Jun 08 2023 Simone Caronni <negativo17@gmail.com> - 1:12.2.0.2-1
- Update to 12.2.0.2.

* Tue Apr 11 2023 Simone Caronni <negativo17@gmail.com> - 1:12.1.0.39-1
- Update to 12.1.0.39.

* Sat Feb 25 2023 Simone Caronni <negativo17@gmail.com> - 1:12.0.1.102-1
- Update to 12.0.1.102.

* Tue Dec 13 2022 Simone Caronni <negativo17@gmail.com> - 1:12.0.0.28-1
- Update to 12.0.0.28.

* Fri Nov 11 2022 Simone Caronni <negativo17@gmail.com> - 1:11.9.0.86-1
- Update to 11.9.0.86.

* Sun Sep 04 2022 Simone Caronni <negativo17@gmail.com> - 1:11.8.0.2-1
- Update to 11.8.0.2.

* Thu Jun 23 2022 Simone Caronni <negativo17@gmail.com> - 1:11.7.2.34-1
- Update to 11.7.2.34.

* Thu Mar 31 2022 Simone Caronni <negativo17@gmail.com> - 1:11.6.2.124-1
- Update to 11.6.2.124 (CUDA 11.6.2).

* Tue Mar 08 2022 Simone Caronni <negativo17@gmail.com> - 1:11.6.1.112-1
- Update to 11.6.1.112 (CUDA 11.6.1).

* Wed Jan 26 2022 Simone Caronni <negativo17@gmail.com> - 1:11.6.0.55-1
- First build with the new tarball components.

