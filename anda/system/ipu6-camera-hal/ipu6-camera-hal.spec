%global commit 289e645dffbd0ea633f10bb4f93855f1e4429e9a
%global commitdate 20240509
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global __cmake_in_source_build 1

Name:           ipu6-camera-hal
Summary:        Hardware abstraction layer for Intel IPU6
URL:            https://github.com/intel/ipu6-camera-hal
Version:        %{commitdate}.%{shortcommit}
Release:        1%{?dist}
License:        Apache-2.0
Source0:        https://github.com/intel/%{name}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
Source1:        60-intel-ipu6.rules
Source2:        v4l2-relayd-adl
Source3:        v4l2-relayd-tgl
Source4:        icamera_ipu6_isys.conf
Source5:        ipu6-driver-select.sh
### RPM Fusion | [ipu6-camera-hal] Update to the latest commit
## https://lists.rpmfusion.org/archives/list/rpmfusion-commits@lists.rpmfusion.org/thread/O6IPZMHMP7A3LQBDY4AEORTDEX4P6ESY
Patch00:        0000-lib-path.patch
### intel/ipu6-camera-hal | PR #113 | CMakeLists fixes
## https://github.com/intel/ipu6-camera-hal/pull/113
Patch01:        0001-CMakeLists-fixes.patch
### intel/ipu6-camera-hal | PR #114 | MediaControl: Dymically set mainline IVSC media-entity src-pad index
## https://github.com/intel/ipu6-camera-hal/pull/114
Patch02:        0002-set-mainline.patch
BuildRequires:  systemd-rpm-macros
BuildRequires:  ipu6-camera-bins-devel >= 0.0-11
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  g++
BuildRequires:  expat-devel
BuildRequires:  libdrm-devel
ExclusiveArch:  x86_64
Requires:       ipu6-camera-bins >= 0.0-11

%description
This package provides the basic Hardware Avstraction Layer (HAL) access APIs for IPU6.

%package devel
Summary:        IPU6 header files for HAL
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ipu6-camera-bins-devel

%description devel
This provides the necessary header files for IPU6 HAL development.

%prep
%autosetup -p1 -n %{name}-%{commit}
sed -i "s|/etc/camera/|/usr/share/defaults/etc/camera/|g" \
  src/platformdata/PlatformData.h


%build
for i in ipu_tgl ipu_adl ipu_mtl; do
  export PKG_CONFIG_PATH=%{_libdir}/$i/pkgconfig/
  export LDFLAGS="$RPM_LD_FLAGS -Wl,-rpath=%{_libdir}/$i"
  mkdir $i && pushd $i
  if [ $i = "ipu_tgl" ]; then
    IPU_VERSION=ipu6
  elif [ $i = "ipu_adl" ]; then
    IPU_VERSION=ipu6ep
  elif [ $i = "ipu_mtl" ]; then
    IPU_VERSION=ipu6epmtl
  else
    IPU_VERSION=ipu
  fi
  %cmake -DCMAKE_BUILD_TYPE=Release -DIPU_VER=$IPU_VERSION \
         -DCMAKE_INSTALL_SUB_PATH:PATH="$i" \
         -DCMAKE_INSTALL_SYSCONFDIR:PATH="share/defaults/etc" \
         -DBUILD_CAMHAL_TESTS=OFF -DUSE_PG_LITE_PIPE=ON ..
  %make_build
  popd
done

### hal_adaptor.so dispatches between different libcamhal.so builds so only build it once!
mkdir hal_adaptor && pushd hal_adaptor
%cmake ../src/hal/hal_adaptor
%make_build
popd


%install
for i in ipu_tgl ipu_adl ipu_mtl; do
  pushd $i
  %make_install
  rm %{buildroot}%{_libdir}/$i/libcamhal.a
  ### New icamerasrc must use hal_adaptor so drop libcamhal.pc!
  rm -r %{buildroot}%{_libdir}/$i/pkgconfig
  popd
done

pushd hal_adaptor
%make_install
popd

### udev-rules set the ipu_xxx /run/v4l2-relayd cfg link + /dev/ipu-psys0 uaccess
install -p -m 0644 -D %{SOURCE1} %{buildroot}%{_udevrulesdir}/60-intel-ipu6.rules

### v4l2-relayd configuration examples (mtl uses same config as adl)
install -p -m 0644 %{SOURCE2} %{buildroot}%{_datadir}/defaults/etc/camera/ipu_adl/v4l2-relayd
install -p -m 0644 %{SOURCE2} %{buildroot}%{_datadir}/defaults/etc/camera/ipu_mtl/v4l2-relayd
install -p -m 0644 %{SOURCE3} %{buildroot}%{_datadir}/defaults/etc/camera/ipu_tgl/v4l2-relayd

### Make kmod-intel-ipu6 use /dev/video7 leaving /dev/video0 for loopback
install -p -D -m 0644 %{SOURCE4} %{buildroot}%{_modprobedir}/icamera_ipu6_isys.conf

### Script to switch between proprietary and foss ipu6 stacks
install -p -D -m 0755 %{SOURCE5} %{buildroot}%{_bindir}/ipu6-driver-select


%posttrans
### Ensure that v4l2-relayd service enabled if ipu6-driver-select is installed
if [ ! -f /etc/modprobe.d/ipu6-driver-select.conf ]; then
    /usr/bin/ipu6-driver-select proprietary
fi
### Skip triggering if udevd isn't accessible
if [ -S /run/udev/control ]; then
    /usr/bin/udevadm control --reload
    /usr/bin/udevadm trigger /sys/devices/pci0000:00/0000:00:05.0
fi


%files
%license LICENSE
%ghost %{_sysconfdir}/modprobe.d/ipu6-driver-select.conf
%{_bindir}/ipu6-driver-select
%{_libdir}/*/libcamhal.so*
%{_libdir}/libhal_adaptor.so.*
%{_datadir}/defaults
%{_modprobedir}/icamera_ipu6_isys.conf
%{_udevrulesdir}/60-intel-ipu6.rules

%files devel
%{_includedir}/hal_adaptor
%{_libdir}/libhal_adaptor.so
%{_libdir}/pkgconfig/hal_adaptor.pc


%changelog
%autochangelog
