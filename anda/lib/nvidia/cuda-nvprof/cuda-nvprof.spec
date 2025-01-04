%global real_name cuda_nvprof

%global debug_package %{nil}
%global __strip /bin/true
%global _missing_build_ids_terminate_build 0
%global _build_id_links none
%global major_package_version 12-6

Name:           %(echo %real_name | tr '_' '-')
Epoch:          1
Version:        12.6.80
Release:        1%{?dist}
Summary:        CUDA command line profiling tool
License:        CUDA Toolkit
URL:            https://developer.nvidia.com/cuda-toolkit
ExclusiveArch:  x86_64

Source0:        https://developer.download.nvidia.com/compute/cuda/redist/%{real_name}/linux-x86_64/%{real_name}-linux-x86_64-%{version}-archive.tar.xz
Source3:        accinj%{__isa_bits}.pc
Source4:        cuinj%{__isa_bits}.pc

Requires(post): ldconfig
Conflicts:      %{name}-%{major_package_version} < %{?epoch:%{epoch}:}%{version}-%{release}

%description
The nvprof profiling tool enables you to collect and view profiling data from
the command-line.

Note that Visual Profiler and nvprof will be deprecated in a future CUDA
release. The NVIDIA Volta platform is the last architecture on which these tools
are fully supported. It is recommended to use next-generation tools NVIDIA
Nsight Systems for GPU and CPU sampling and tracing and NVIDIA Nsight Compute
for GPU kernel profiling.

%package devel
Summary:        Development files for the CUDA command line profiling tool
Requires:       %{name}%{_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Conflicts:      %{name}-devel-%{major_package_version} < %{?epoch:%{epoch}:}%{version}

%description devel
This package provides development files for the CUDA command line profiling tool
libraries.

%prep
%ifarch x86_64
%setup -q -n %{real_name}-linux-x86_64-%{version}-archive
%endif

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_libdir}
mkdir -p %{buildroot}%{_libdir}/pkgconfig/

cp -fr bin/* %{buildroot}%{_bindir}/
cp -fr lib/lib* %{buildroot}%{_libdir}/
cp -fr %{SOURCE3} %{SOURCE4} %{buildroot}/%{_libdir}/pkgconfig/

# Set proper variables
sed -i \
    -e 's|CUDA_VERSION|%{version}|g' \
    -e 's|LIBDIR|%{_libdir}|g' \
    -e 's|INCLUDE_DIR|%{_includedir}|g' \
    %{buildroot}/%{_libdir}/pkgconfig/*.pc

%{?ldconfig_scriptlets}

%files
%license LICENSE
%{_bindir}/nvprof
%{_libdir}/*.so.*

%files devel
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%changelog
* Fri Dec 13 2024 Simone Caronni <negativo17@gmail.com> - 1:12.6.80-1
- Update to 12.6.80.

* Thu Sep 19 2024 Simone Caronni <negativo17@gmail.com> - 1:12.6.68-1
- Update to 12.6.68.

* Thu Jul 11 2024 Simone Caronni <negativo17@gmail.com> - 1:12.5.82-1
- Update to 12.5.82.

* Tue Mar 12 2024 Simone Caronni <negativo17@gmail.com> - 1:12.4.99-1
- Update to 12.4.99.
- Drop ppc64le.

* Tue Nov 28 2023 Simone Caronni <negativo17@gmail.com> - 1:12.3.101-1
- Update to 12.3.101.

* Thu Sep 28 2023 Simone Caronni <negativo17@gmail.com> - 1:12.2.142-1
- Update to 12.2.142.

* Tue Jul 11 2023 Simone Caronni <negativo17@gmail.com> - 1:12.2.60-1
- Update to 12.2.60.

* Thu Jun 08 2023 Simone Caronni <negativo17@gmail.com> - 1:12.1.105-1
- Update to 12.1.105.

* Tue Apr 11 2023 Simone Caronni <negativo17@gmail.com> - 1:12.1.55-1
- Update to 12.1.55.

* Sat Feb 25 2023 Simone Caronni <negativo17@gmail.com> - 1:12.0.146-1
- Update to 12.0.146.

* Tue Dec 13 2022 Simone Caronni <negativo17@gmail.com> - 1:12.0.90-1
- Update to 12.0.90.

* Fri Nov 11 2022 Simone Caronni <negativo17@gmail.com> - 1:11.8.87-1
- Update to 11.8.87.

* Sun Sep 04 2022 Simone Caronni <negativo17@gmail.com> - 1:11.7.101-1
- Update to 11.7.101.

* Thu Jun 23 2022 Simone Caronni <negativo17@gmail.com> - 1:11.7.50-1
- Update to 11.7.50.
- Add aarch64 files.

* Thu Mar 31 2022 Simone Caronni <negativo17@gmail.com> - 1:11.6.124-1
- Update to 11.6.124 (CUDA 11.6.2).

* Tue Mar 08 2022 Simone Caronni <negativo17@gmail.com> - 1:11.6.112-1
- Update to 11.6.112 (CUDA 11.6.1).

* Wed Jan 26 2022 Simone Caronni <negativo17@gmail.com> - 1:11.6.55-1
- First build with the new tarball components.

