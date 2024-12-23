%global commit e00d8ba9a3fbc074ceb3af145d1055daf8ecc22f
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commit_date 20241223

Name:           fontviewer
Version:        %{commit_date}.git~%{shortcommit}
Release:        1%?dist
Summary:        View and install fonts

License:        GPL-2.0
URL:            https://github.com/chocolateimage/%{name}
Source0:        %{url}/archive/%{commit}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  meson
BuildRequires:  pkgconfig(cairomm-1.0)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gtkmm-3.0)

Requires:       gtk3 fontconfig

Packager:       sadlerm <sad_lerm@hotmail.com>

%description
A platform-agnostic GTK+ 3 alternative to GNOME's Font Viewer

%prep
%autosetup -n %{name}-%{commit} -p1

%build
%meson
%meson_build

%install
%meson_install

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
