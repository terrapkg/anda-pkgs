#? https://src.fedoraproject.org/rpms/libdwarf/blob/epel10/f/libdwarf.spec
Name:          libdwarf
Version:       0.11.1
Release:       %autorelease
Summary:       Library to access the DWARF Debugging file format 

License:       LGPL-2.1-only AND BSD-2-Clause-FreeBSD
URL:           https://www.prevanders.net/dwarf.html
Source0:       https://www.prevanders.net/%{name}-%{version}.tar.xz
# Make default-library=both work on linux
Packager:      madonuko <mado@fyralabs.com>
Patch:         libdwarf-both.patch

BuildRequires: gcc gcc-c++ meson python3

%description
Library to access the DWARF debugging file format which supports
source level debugging of a number of procedural languages, such as C, C++,
and Fortran.  Please see http://www.dwarfstd.org for DWARF specification.

%package devel
Summary:       Library and header files of libdwarf
License:       LGPL-2.1-only AND BSD-2-Clause-FreeBSD
Requires:      %{name} = %{?epoch:%epoch:}%{version}-%{release}

%description devel
Development package containing library and header files of libdwarf.

%package static
Summary:       Static libdwarf library
License:       LGPL-2.1-only AND BSD-2-Clause-FreeBSD
Requires:      %{name}-devel = %{?epoch:%epoch:}%{version}-%{release}

%description static
Static libdwarf library.

%package tools
Summary:       Tools for accessing DWARF debugging information
License:       GPL-2.0-only AND BSD-2-Clause-FreeBSD
Requires:      %{name} = %{?epoch:%epoch:}%{version}-%{release}

%description tools
C++ version of dwarfdump (dwarfdump2) command-line utilities 
to access DWARF debug information.


%prep
%autosetup -p1


%build
%meson --default-library=both
%meson_build


%install
%meson_install


%check
%meson_test


%files
%doc src/lib/libdwarf/ChangeLog src/lib/libdwarf/README
%license src/lib/libdwarf/COPYING src/lib/libdwarf/LIBDWARFCOPYRIGHT src/lib/libdwarf/LGPL.txt
%{_libdir}/libdwarf.so.0
%{_libdir}/libdwarf.so.0.*


%files static
%{_libdir}/libdwarf.a


%files devel
%doc doc/*.pdf
%{_includedir}/libdwarf-0
%{_libdir}/libdwarf.so
%{_libdir}/pkgconfig/libdwarf.pc


%files tools
%license src/bin/dwarfdump/COPYING src/bin/dwarfdump/DWARFDUMPCOPYRIGHT src/bin/dwarfdump/GPL.txt
%{_bindir}/dwarfdump
%{_datadir}/dwarfdump/dwarfdump.conf
%{_mandir}/man1/dwarfdump.1.gz


%changelog
* Fri Dec 20 2024 madonuko <mado@fyralabs.com> - 0.11.1-1
- Repackaged for Terra el10 from Fedora el10
