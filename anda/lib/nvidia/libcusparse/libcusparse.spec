%global debug_package %{nil}
%global __strip /bin/true
%global _missing_build_ids_terminate_build 0
%global _build_id_links none
%global major_package_version 12-6

Name:           libcusparse
Epoch:          1
Version:        12.5.4.2
Release:        1%{?dist}
Summary:        NVIDIA CUDA Sparse Matrix library (cuSPARSE) library
License:        CUDA Toolkit
URL:            https://developer.nvidia.com/cuda-toolkit
ExclusiveArch:  x86_64 aarch64

Source0:        https://developer.download.nvidia.com/compute/cuda/redist/%{name}/linux-x86_64/%{name}-linux-x86_64-%{version}-archive.tar.xz
Source1:        https://developer.download.nvidia.com/compute/cuda/redist/%{name}/linux-sbsa/%{name}-linux-sbsa-%{version}-archive.tar.xz
Source3:        cusparse.pc

Requires(post): ldconfig
Conflicts:      %{name}-%{major_package_version} < %{?epoch:%{epoch}:}%{version}-%{release}

%description
The NVIDIA CUDA Sparse Matrix library (cuSPARSE) provides a collection of basic
linear algebra subroutines used for sparse matrices that delivers up to 8x
faster performance than the latest MKL. The cuSPARSE library is designed to be
called from C or C++, and the latest release includes a sparse triangular
solver.

%package devel
Summary:        Development files for NVIDIA CUDA Sparse Matrix (cuSPARSE) library
Requires:       %{name}%{_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Conflicts:      %{name}-devel-%{major_package_version} < %{?epoch:%{epoch}:}%{version}

%description devel
This package provides development files for the NVIDIA CUDA Sparse Matrix
library (cuSPARSE) library.

%package static
Summary:        Static libraries for NVIDIA CUDA Sparse Matrix (cuSPARSE)
Requires:       %{name}-devel%{_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description static
This package contains static libraries for NVIDIA CUDA Sparse Matrix (cuSPARSE).

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
%{_libdir}/libcusparse.so.*

%files devel
%ifarch x86_64
%doc src
%endif
%{_includedir}/cusparse.h
%{_includedir}/cusparse_v2.h
%{_libdir}/libcusparse.so
%{_libdir}/pkgconfig/cusparse.pc

%files static
%{_libdir}/libcusparse_static.a

%changelog
* Fri Dec 13 2024 Simone Caronni <negativo17@gmail.com> - 1:12.5.4.2-1
- Update to 12.5.4.2.

* Thu Sep 19 2024 Simone Caronni <negativo17@gmail.com> - 1:12.5.3.3-1
- Update to 12.5.3.3.

* Thu Jul 11 2024 Simone Caronni <negativo17@gmail.com> - 1:12.5.1.3-1
- Update to 12.5.1.3.

* Mon Mar 18 2024 Simone Caronni <negativo17@gmail.com> - 1:12.3.0.142-2
- Fix build on aarch64.

* Tue Mar 12 2024 Simone Caronni <negativo17@gmail.com> - 1:12.3.0.142-1
- Update to 12.3.0.142.
- Drop ppc64le.

* Tue Nov 28 2023 Simone Caronni <negativo17@gmail.com> - 1:12.2.0.103-1
- Update to 12.2.0.103.

* Thu Sep 28 2023 Simone Caronni <negativo17@gmail.com> - 1:12.1.2.141-1
- Update to 12.1.2.141.

* Tue Jul 11 2023 Simone Caronni <negativo17@gmail.com> - 1:12.1.1.53-1
- Update to 12.1.1.53.

* Thu Jun 08 2023 Simone Caronni <negativo17@gmail.com> - 1:12.1.0.106-1
- Update to 12.1.0.106.

* Tue Apr 11 2023 Simone Caronni <negativo17@gmail.com> - 1:12.0.2.55-1
- Update to 12.0.2.55.

* Sat Feb 25 2023 Simone Caronni <negativo17@gmail.com> - 1:12.0.1.140-1
- Update to 12.0.1.140.

* Tue Dec 13 2022 Simone Caronni <negativo17@gmail.com> - 1:12.0.0.76-1
- Update to 12.0.0.76.

* Fri Nov 11 2022 Simone Caronni <negativo17@gmail.com> - 1:11.7.5.86-1
- Update to 11.7.5.86.
- Use aarch64 archive in place of sbsa.

* Sun Sep 04 2022 Simone Caronni <negativo17@gmail.com> - 1:11.7.4.91-1
- Update to 11.7.4.91.

* Thu Jun 23 2022 Simone Caronni <negativo17@gmail.com> - 1:11.7.3.50-1
- Update to 11.7.3.50.

* Thu Mar 31 2022 Simone Caronni <negativo17@gmail.com> - 1:11.7.2.124-1
- Update to 11.7.2.124 (CUDA 11.6.2).

* Tue Mar 08 2022 Simone Caronni <negativo17@gmail.com> - 1:11.7.2.112-1
- Update to 11.7.2.112 (CUDA 11.6.1).

* Wed Jan 26 2022 Simone Caronni <negativo17@gmail.com> - 1:11.7.1.55-1
- First build with the new tarball components.

