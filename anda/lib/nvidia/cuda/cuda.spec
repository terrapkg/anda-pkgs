%global debug_package %{nil}
%global major_package_version 12-6

Name:           cuda
Version:        12.6.77
Release:        1%{?dist}
Summary:        NVIDIA Compute Unified Device Architecture Toolkit
Epoch:          1
License:        CUDA Toolkit
URL:            https://developer.nvidia.com/cuda-zone
ExclusiveArch:  x86_64 aarch64

# Nvidia really provides the same package for ppc64le, aarch64 and x86_64 but
# it's really the same package.
Source0:        https://developer.download.nvidia.com/compute/cuda/redist/cuda_documentation/linux-x86_64/cuda_documentation-linux-x86_64-%{version}-archive.tar.xz

Source3:        %{name}.sh
Source4:        %{name}.csh
Source21:       cuda.pc

Requires:       %{name}-libs%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Conflicts:      %{name}-%{major_package_version} < %{?epoch:%{epoch}:}%{version}-%{release}
Conflicts:      %{name}-minimal-build-%{major_package_version} < %{?epoch:%{epoch}:}%{version}-%{release}

%description
CUDA is a parallel computing platform and programming model that enables
dramatic increases in computing performance by harnessing the power of the
graphics processing unit (GPU).

%package cli-tools
Summary:        Compute Unified Device Architecture command-line tools
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}-cupti%{?_isa}
Requires:       %{name}-devel%{?_isa}
Requires:       %{name}-gdb%{?_isa}
Requires:       %{name}-memcheck%{?_isa}
Requires:       %{name}-nvdisasm%{?_isa}
%ifnarch aarch64
Requires:       %{name}-nvprof%{?_isa}
%endif
Requires:       %{name}-nvtx%{?_isa}
Requires:       %{name}-sanitizer%{?_isa}
Requires:       expat >= 1.95
Conflicts:      %{name}-command-line-tools-%{major_package_version} < %{?epoch:%{epoch}:}%{version}-%{release}

%description cli-tools
Contains the command line tools to debug and profile CUDA applications.

%package libs
Summary:        Compute Unified Device Architecture native run-time library
Requires(post): ldconfig
Requires:       %{name}-cudart%{?_isa}
Requires:       %{name}-nvrtc%{?_isa}
Requires:       libcublas%{?_isa}
Requires:       libcufft%{?_isa}
Requires:       libcufile%{?_isa}
Requires:       libcurand%{?_isa}
Requires:       libcusolver%{?_isa}
Requires:       libcusparse%{?_isa}
Requires:       libnpp%{?_isa}
Requires:       libnvjpeg%{?_isa}
Conflicts:      %{name}-driver-devel-%{major_package_version} < %{?epoch:%{epoch}:}%{version}-%{release}
Conflicts:      %{name}-libraries-%{major_package_version} < %{?epoch:%{epoch}:}%{version}-%{release}
# Explicitly declare the dependency or libcuda.so.1()(64bit) will pull in xorg-x11-drv-cuda-libs
Requires:       nvidia-driver-cuda-libs%{_isa}

%description libs
Contains the CUDA run-time library required to run CUDA application natively.

%package extra-libs
Summary:        All runtime NVIDIA CUDA libraries
Requires(post): ldconfig
Requires:       %{name}-cupti%{?_isa}
Conflicts:      %{name}-runtime-%{major_package_version} < %{?epoch:%{epoch}:}%{version}-%{release}

%description extra-libs
Metapackage that installs all runtime NVIDIA CUDA libraries.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}-libs%{_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}-cccl-devel%{?_isa}
Requires:       %{name}-cudart-devel%{?_isa}
Requires:       %{name}-cupti-devel%{?_isa}
Requires:       %{name}-nvcc%{?_isa}
Requires:       %{name}-nvprof-devel%{?_isa}
Requires:       %{name}-nvprune%{?_isa}
Requires:       %{name}-nvml-devel%{?_isa}
Requires:       %{name}-nvrtc-devel%{?_isa}
Requires:       %{name}-nvtx-devel%{?_isa}
Requires:       %{name}-cuobjdump%{?_isa}
Requires:       %{name}-cuxxfilt-devel%{?_isa}
Requires:       libcublas-devel%{?_isa}
Requires:       libcufft-devel%{?_isa}
Requires:       libcufile-devel%{?_isa}
Requires:       libcurand-devel%{?_isa}
Requires:       libcusolver-devel%{?_isa}
Requires:       libcusparse-devel%{?_isa}
Requires:       libnpp-devel%{?_isa}
Requires:       libnvjpeg-devel%{?_isa}
Conflicts:      %{name}-headers-%{major_package_version} < %{?epoch:%{epoch}:}%{version}
Conflicts:      %{name}-libraries-dev-%{major_package_version} < %{?epoch:%{epoch}:}%{version}
Conflicts:      %{name}-misc-headers-%{major_package_version} < %{?epoch:%{epoch}:}%{version}
Conflicts:      %{name}-toolkit-%{major_package_version} < %{?epoch:%{epoch}:}%{version}
Provides:       %{name}-toolkit-%{major_package_version} = %{?epoch:%{epoch}:}%{version}

%description devel
This package provides the development files of the %{name} package.

%prep
%setup -q -n cuda_documentation-linux-x86_64-%{version}-archive

%build
# Nothing to build

%install
mkdir -p %{buildroot}%{_libdir}/pkgconfig/
mkdir -p %{buildroot}%{_sysconfdir}/profile.d/

# Environment settings
install -pm 644 %{SOURCE3} %{SOURCE4} %{buildroot}%{_sysconfdir}/profile.d

# pkg-config files
install -pm 644 %{SOURCE21} %{buildroot}/%{_libdir}/pkgconfig

# Set proper variables
sed -i \
    -e 's|CUDA_VERSION|%{version}|g' \
    -e 's|LIBDIR|%{_libdir}|g' \
    -e 's|INCLUDE_DIR|%{_includedir}/cuda|g' \
    %{buildroot}/%{_libdir}/pkgconfig/*.pc

%files
%license LICENSE
%doc CUDA_Toolkit_Release_Notes.txt DOCS EULA.txt README tools
%config(noreplace) %{_sysconfdir}/profile.d/%{name}.*sh

%files cli-tools
# Empty metapackage

%files libs
# Empty metapackage

%files extra-libs
# Empty metapackage

%files devel
%{_libdir}/pkgconfig/cuda.pc

%changelog
* Fri Dec 13 2024 Simone Caronni <negativo17@gmail.com> - 1:12.6.77-1
- Update to 12.6.77.

* Thu Sep 19 2024 Simone Caronni <negativo17@gmail.com> - 1:12.6.68-1
- Update to 12.6.68.

* Thu Jul 11 2024 Simone Caronni <negativo17@gmail.com> - 1:12.5.82-1
- Update to 12.5.82.

* Thu Jul 11 2024 Simone Caronni <negativo17@gmail.com> - 1:12.4.99-1
- Update to 12.4.99.

* Thu Mar 14 2024 Simone Caronni <negativo17@gmail.com> - 1:12.4.99-2
- Require cuda-cccl-devel in cuda-devel (#31).

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

* Tue Apr 11 2023 Simone Caronni <negativo17@gmail.com> - 1:12.1.55-1
- Update to 12.1.55.

* Sat Feb 25 2023 Simone Caronni <negativo17@gmail.com> - 1:12.0.140-1
- Update to 12.0.140.

* Tue Dec 13 2022 Simone Caronni <negativo17@gmail.com> - 1:12.0.76-1
- Update to 12.0.76.

* Fri Nov 11 2022 Simone Caronni <negativo17@gmail.com> - 1:11.8.86-1
- Update to 11.8.86.

* Sun Sep 04 2022 Simone Caronni <negativo17@gmail.com> - 1:11.7.91-1
- Update to 11.7.91.

* Thu Jun 23 2022 Simone Caronni <negativo17@gmail.com> - 1:11.7.50-1
- Update to 11.7.50.

* Thu Mar 31 2022 Simone Caronni <negativo17@gmail.com> - 1:11.6.124-1
- Update to 11.6.124 (CUDA 11.6.2).

* Tue Mar 08 2022 Simone Caronni <negativo17@gmail.com> - 1:11.6.112-1
- Update to 11.6.112 (CUDA 11.6.1).

* Wed Feb 02 2022 Simone Caronni <negativo17@gmail.com> - 1:11.6.55-1
- Update to 11.6.
- Use new tarball distribution method.
- Add new cufile/GDS dependencies.
- Trim changelog.

* Wed Sep 22 2021 Simone Caronni <negativo17@gmail.com> - 1:11.4.2-1
- Update to 11.4.2.

* Tue Jul 20 2021 Simone Caronni <negativo17@gmail.com> - 1:11.4.0-1
- Update to 11.4.0.
- Update package names used in conflict statements to match upstream changes.
- Add missing CCCL (C++ Core Compute libraries )headers to devel subpackage.

* Sun Apr 25 2021 Simone Caronni <negativo17@gmail.com> - 1:11.3.0-1
- Update to 11.3.0.
- Split static libraries in subpackages.

* Thu Feb 18 2021 Simone Caronni <negativo17@gmail.com> - 1:11.2.1-1
- Update to 11.2.1.

* Sun Dec 20 2020 Simone Caronni <negativo17@gmail.com> - 1:11.2.0-1
- Update to CUDA 11.2.0.

* Sat Nov 28 2020 Simone Caronni <negativo17@gmail.com> - 1:11.1.1-3
- GCC 10 works fine.
- rpmlint fixes.

* Mon Nov 16 2020 Simone Caronni <negativo17@gmail.com> - 1:11.1.1-2
- Nsight Compute & Systems are available separately.

* Sat Nov 14 2020 Simone Caronni <negativo17@gmail.com> - 1:11.1.1-1
- Update to 11.1.1.

* Sat Sep 05 2020 Simone Caronni <negativo17@gmail.com> - 1:11.0.3-1
- Update to 11.0.3.

* Mon Mar 16 2020 Simone Caronni <negativo17@gmail.com> - 1:10.2.89-2
- Do not merge the CUDA C++ standard library headers with the rest.

* Sun Feb 02 2020 Simone Caronni <negativo17@gmail.com> - 1:10.2.89-1
- Update to 10.2.89.

* Wed Oct 02 2019 Simone Caronni <negativo17@gmail.com> - 1:10.1.243-1
- Update to CUDA 10.1 update 2.

* Mon Jun 10 2019 Simone Caronni <negativo17@gmail.com> - 1:10.1.168-1
- Update to 10.1.168.
- Remove post* scriptlets.

* Sat Apr 06 2019 Simone Caronni <negativo17@gmail.com> - 1:10.1.105-1
- Update to 10.1.105.
- Trim changelog.
- Require cuda-gcc only on Fedora 30+ (GCC 9).

* Sat Jan 12 2019 Simone Caronni <negativo17@gmail.com> - 1:10.0.130-2
- Update SPEC file.

* Thu Jan 03 2019 Simone Caronni <negativo17@gmail.com> - 1:10.0.130-1
- Update to 10.0.130.
