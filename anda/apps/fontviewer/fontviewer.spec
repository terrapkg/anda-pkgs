%global commit f215a218d8145cb86d50fc7a8dd81563fff83955
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commit_date 20241217

Name:           fontviewer
Version:        %{commit_date}.git~%{shortcommit}
Release:        1%?dist
Summary:        View and install fonts

License:        GPL-2.0
URL:            https://github.com/chocolateimage/%{name}
Source0:        %{url}/archive/%{commit}.tar.gz 
Patch0:         fontviewer-meson.patch

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

install -m 0755 -vd %{buildroot}%{_datadir}/applications
install -m 0644 -vp data/%{name}.desktop %{buildroot}%{_datadir}/applications/

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
