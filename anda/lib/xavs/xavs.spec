Name:           xavs
Version:        0.1.55
Release:        1%{?dist}
Summary:        AVS1 (First-generation AVS Standards) library
License:        GPLv2
URL:            http://xavs.sourceforge.net/

Source0:        https://sourceforge.net/code-snapshots/svn/x/xa/xavs/code/xavs-code-r55-trunk.zip
Patch0:         %{name}-cflags.patch

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  libtool
#BuildRequires:  yasm

%description
AVS is a complete standard system including system, video, audio, and digital
rights management, providing a more comprehensive solution for the digital audio
and video industry.

%package -n lib%{name}
Summary:        AVS1 (First-generation AVS Standards) library

%description -n lib%{name}
AVS is a complete standard system including system, video, audio, and digital
rights management, providing a more comprehensive solution for the digital audio
and video industry.

%package -n lib%{name}-devel
Summary:        Development files for %{name}
Requires:       lib%{name}%{?_isa} = %{version}-%{release}
Requires:       pkg-config

%description -n lib%{name}-devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -p1 -n xavs-code-r55-trunk

%build
%configure \
    --disable-asm \
    --enable-pic \
    --enable-shared \
    --extra-cflags="-Wno-int-conversion -Wno-declaration-missing-parameter-type"
%make_build

%install
%make_install
rm -f %{buildroot}%{_libdir}/*.a

%files
%{_bindir}/%{name}

%files -n lib%{name}
%{_libdir}/*.so.*

%files -n lib%{name}-devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
* Tue Aug 13 2024 Simone Caronni <negativo17@gmail.com> - 0.1.55-1
- First build.
