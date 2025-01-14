%global debug_package %{nil}
%global commit 3c1cdd3e634bb4668a900d75efd4d6292b8c7d1d
%global commitdate 20240507
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           ipu6-camera-bins
Summary:        Binary libraries for Intel IPU6
Version:        %{commitdate}.%{shortcommit}
Release:        1%?dist
License:        Proprietary
URL:            https://github.com/intel/ipu6-camera-bins
Source0:        https://github.com/intel/%{name}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
BuildRequires:  systemd-rpm-macros
BuildRequires:  chrpath
BuildRequires:  patchelf
ExclusiveArch:  x86_64
#Requires:       gstreamer1-plugin-icamerasrc
Requires:       v4l2-relayd
Requires:       intel-ipu6-kmod
Requires:       intel-vsc-firmware >= 20240513
Obsoletes:      ipu6-camera-bins-firmware < 0.0-11
### For Akmods package
Provides:       intel-ipu6-kmod-common = %{version}

%description
Provides binaries for Intel IPU6, including libraries and firmware.


%package devel
Summary:        IPU6 development files
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
This provides the header files for IPU6 development.

%prep
%setup -q -n %{name}-%{commit}
for i in ipu_tgl ipu_adl ipu_mtl; do
  chrpath --delete lib/$i/*.so
done

%build

%install
mkdir -p %{buildroot}%{_includedir}
for i in ipu_tgl ipu_adl ipu_mtl; do
  mkdir -p %{buildroot}%{_libdir}/$i
  cp -pr include/$i %{buildroot}%{_includedir}
  cp -pr lib/$i/lib* lib/$i/pkgconfig %{buildroot}%{_libdir}/$i
  patchelf --set-rpath %{_libdir}/$i %{buildroot}%{_libdir}/$i/*.so
  sed -i \
    -e "s|libdir=\${prefix}/lib/$i|libdir=%{_libdir}/$i|g" \
    %{buildroot}%{_libdir}/$i/pkgconfig/*.pc
done


%files
%license LICENSE
%dir %{_libdir}/ipu_tgl
%dir %{_libdir}/ipu_adl
%dir %{_libdir}/ipu_mtl
%{_libdir}/ipu_tgl/*.so*
%{_libdir}/ipu_adl/*.so*
%{_libdir}/ipu_mtl/*.so*

%files devel
%dir %{_includedir}/ipu_tgl
%dir %{_includedir}/ipu_adl
%dir %{_includedir}/ipu_mtl
%dir %{_libdir}/ipu_tgl/pkgconfig
%dir %{_libdir}/ipu_adl/pkgconfig
%dir %{_libdir}/ipu_mtl/pkgconfig
%{_includedir}/ipu_tgl/*
%{_includedir}/ipu_adl/*
%{_includedir}/ipu_mtl/*
%{_libdir}/ipu_tgl/pkgconfig/*
%{_libdir}/ipu_adl/pkgconfig/*
%{_libdir}/ipu_mtl/pkgconfig/*
%{_libdir}/ipu_tgl/*.a
%{_libdir}/ipu_adl/*.a
%{_libdir}/ipu_mtl/*.a


%changelog
%autochangelog
