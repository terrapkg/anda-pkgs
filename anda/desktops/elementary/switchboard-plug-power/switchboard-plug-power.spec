%global __provides_exclude_from ^%{_libdir}/switchboard/.*\\.so$

%global srcname switchboard-plug-power

%global plug_type hardware
%global plug_name power
%global plug_rdnn io.elementary.switchboard.power

Name:           switchboard-plug-power
Summary:        Switchboard Power Plug
Version:        2.7.0
Release:        1%?dist
License:        GPL-2.0-or-later

URL:            https://github.com/elementary/%name
Source0:        %url/archive/%version/%srcname-%version.tar.gz

BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  vala

BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(granite-7)
BuildRequires:  pkgconfig(polkit-gobject-1)
BuildRequires:  polkit-devel
BuildRequires:  switchboard-devel

Requires:       switchboard%?_isa
Supplements:    switchboard%?_isa

%description
%summary.

%prep
%autosetup -n %srcname-%version -p1


%build
%meson
%meson_build


%install
%meson_install

%find_lang %plug_name-plug


%check
appstream-util validate-relax --nonet \
    %buildroot/%_datadir/metainfo/%plug_rdnn.appdata.xml


%files -f %plug_name-plug.lang
%doc README.md
%license COPYING

%_libdir/switchboard/%plug_type/lib%plug_name.so

%_datadir/metainfo/%plug_rdnn.appdata.xml

%changelog
* Tue Jun 13 2023 windowsboy111 <windowsboy111@fyralabs.com> - 2.7.0-1
- Initial package.
