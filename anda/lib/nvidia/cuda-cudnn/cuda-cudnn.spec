%global         debug_package %{nil}
%global         __strip /bin/true
%global         _missing_build_ids_terminate_build 0
%global         _build_id_links none
%global         cuda_version 12

Name:           cuda-cudnn
Version:        9.6.0.74
Release:        1%{?dist}
Epoch:          1
Summary:        NVIDIA CUDA Deep Neural Network library (cuDNN)
License:        NVIDIA Software Development Kit
URL:            https://developer.nvidia.com/cudnn
ExclusiveArch:  x86_64 aarch64

Source0:        https://developer.download.nvidia.com/compute/cudnn/redist/cudnn/linux-x86_64/cudnn-linux-x86_64-%{version}_cuda%{cuda_version}-archive.tar.xz
Source1:        https://developer.download.nvidia.com/compute/cudnn/redist/cudnn/linux-sbsa/cudnn-linux-sbsa-%{version}_cuda%{cuda_version}-archive.tar.xz

%description
The NVIDIA CUDA Deep Neural Network library (cuDNN) is a GPU-accelerated
library of primitives for deep neural networks. cuDNN provides highly tuned
implementations for standard routines such as forward and backward convolution,
pooling, normalization, and activation layers. cuDNN is part of the NVIDIA Deep
Learning SDK.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       cuda%{?_isa} >= %{?epoch:%{epoch}:}%{cuda_version}

%description    devel
The %{name}-devel package contains libraries and header files for developing
applications that use %{name}.

%package        static
Summary:        Static libraries for %{name}
Requires:       %{name}-devel%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description    static
Static library files for %{name}.

%prep
%ifarch x86_64
%setup -q -n cudnn-linux-x86_64-%{version}_cuda%{cuda_version}-archive
%endif

%ifarch aarch64
%setup -q -T -b 1 -n cudnn-linux-sbsa-%{version}_cuda%{cuda_version}-archive
%endif

%install
mkdir -p %{buildroot}%{_libdir}
cp -a lib/*.so* %{buildroot}%{_libdir}/
chmod 755 %{buildroot}%{_libdir}/*.so*
cp -a lib/*.a %{buildroot}%{_libdir}/
chmod 644 %{buildroot}%{_libdir}/*.a

mkdir -p %{buildroot}%{_includedir}
cp -a include/* %{buildroot}%{_includedir}/
chmod 644 %{buildroot}%{_includedir}/*

%{?ldconfig_scriptlets}

%files
%license LICENSE
%{_libdir}/libcudnn*.so.*

%files devel
%{_includedir}/cudnn*
%{_libdir}/libcudnn*.so

%files static
%{_libdir}/libcudnn*.a

%changelog
* Sat Dec 14 2024 Simone Caronni <negativo17@gmail.com> - 1:9.6.0.74-1
- Update to 9.6.0.74.

* Tue Sep 24 2024 Simone Caronni <negativo17@gmail.com> - 1:9.4.0.58-1
- Update to 9.4.0.58.

* Thu Jul 11 2024 Simone Caronni <negativo17@gmail.com> - 1:9.2.1.18-1
- Update to 9.2.1.18.

* Mon Mar 18 2024 Simone Caronni <negativo17@gmail.com> - 1:9.0.0.312-2
- Fix typo.
- Trim changelog.

* Sat Mar 16 2024 Simone Caronni <negativo17@gmail.com> - 1:9.0.0.312-1
- Update to 9.0.0.312.

* Sat Jan 06 2024 Simone Caronni <negativo17@gmail.com> - 1:8.9.7.29-1
- Update to 8.9.7.29.

* Wed Nov 29 2023 Simone Caronni <negativo17@gmail.com> - 1:8.9.6.50-1
- Update to version 8.9.6.50.

* Thu Sep 28 2023 Simone Caronni <negativo17@gmail.com> - 1:8.9.5.29-1
- Update to 8.9.5.29.

* Wed Jul 12 2023 Simone Caronni <negativo17@gmail.com> - 1:8.9.3.28-1
- Update to 8.9.3.28.

* Tue Apr 11 2023 Simone Caronni <negativo17@gmail.com> - 1:8.8.1.3-1
- Update to 8.8.1.3.

* Sat Feb 25 2023 Simone Caronni <negativo17@gmail.com> - 1:8.8.0.121-1
- Update to 8.8.0.121.

* Tue Dec 20 2022 Simone Caronni <negativo17@gmail.com> - 1:8.7.0.84-1
- Update to 8.7.0.84 (still CUDA 11).

* Fri Oct 07 2022 Simone Caronni <negativo17@gmail.com> - 1:8.6.0.163-1
- Update to 8.6.0.163.

* Thu Mar 31 2022 Simone Caronni <negativo17@gmail.com> - 1:8.3.3.40-1
- Update to 8.3.3.40, allow building on ppc64le and aarch64.
- Drop samples subpackage.
- Move headers one level above.

* Tue Nov 02 2021 Simone Caronni <negativo17@gmail.com> - 1:8.2.4.15-1
- Update to 8.2.4.15

* Wed Jul 21 2021 Simone Caronni <negativo17@gmail.com> - 1:8.2.2.26-1
- Update to 8.2.2.26.

* Mon Apr 26 2021 Simone Caronni <negativo17@gmail.com> - 1:8.2.0.53-1
- Update to 8.2.0.53.
- Split static libraries in separate subpackage.

* Thu Feb 18 2021 Simone Caronni <negativo17@gmail.com> - 1:8.1.0.77-1
- Update to 8.1.0.77.

* Mon Nov 16 2020 Simone Caronni <negativo17@gmail.com> - 1:8.0.5.39-1
- Update to 8.0.5.39.

* Tue Mar 03 2020 Simone Caronni <negativo17@gmail.com> - 1:7.6.5.32-1
- Update to 7.6.5.32.
