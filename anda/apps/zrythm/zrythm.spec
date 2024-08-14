# WARN: YOU MUST RUN THIS INSIDE MOCK.
# Running this on a real computer will alter your system, because this
# vendors `rtaudio` (and install it on your system) during build-time.

%global v v1.0.0-rc.1

Name:           zrythm
Version:        %(echo %v | sed 's@-@~@g' | sed 's@^v@@')
Release:        1%?dist
Summary:        Highly automated and intuitive digital audio workstation
License:        AGPL-3.0-or-later
Packager:       madonuko <mado@fyralabs.com>
URL:            https://www.zrythm.org/
Source0:        https://gitlab.zrythm.org/zrythm/zrythm/-/archive/%v/zrythm-%v.tar.gz

# https://github.com/OpenMandrivaAssociation/zrythm/blob/master/zrythm.spec

BuildRequires: automake
BuildRequires: libappstream-glib
BuildRequires: mold
BuildRequires: git
BuildRequires: gettext
BuildRequires: python
BuildRequires: sed
BuildRequires: sassc
BuildRequires: libbacktrace-nightly-devel
BuildRequires: boost-devel
BuildRequires: (ffmpeg-free-devel or ffmpeg-devel)
BuildRequires: ladspa-devel
BuildRequires: graphviz-devel
BuildRequires: pkgconfig(carla-host-plugin)
BuildRequires: pkgconfig(gtk4)
BuildRequires: pkgconfig(gtksourceview-5)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(guile-3.0)
BuildRequires: pkgconfig(audec)
BuildRequires: pkgconfig(libadwaita-1)
BuildRequires: pkgconfig(libchromaprint)
BuildRequires: pkgconfig(libcurl)
#BuildRequires: pkgconfig(libfl)
BuildRequires: libfl-devel
# ^ maybe?
BuildRequires: pkgconfig(libgtop-2.0)
BuildRequires: pkgconfig(libsass)
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: pkgconfig(libcyaml)
BuildRequires: pkgconfig(libpanel-1)
BuildRequires: pkgconfig(libxxhash)
BuildRequires: pkgconfig(lilv-0)
BuildRequires: pkgconfig(lv2)
BuildRequires: pkgconfig(sndfile)
BuildRequires: pkgconfig(sdl2)
BuildRequires: pkgconfig(yaml-0.1)
BuildRequires: pkgconfig(libcyaml)
BuildRequires: pkgconfig(samplerate)
BuildRequires: pkgconfig(alsa)
BuildRequires: pkgconfig(fftw3)
BuildRequires: pkgconfig(portaudio-2.0)
BuildRequires: pkgconfig(reproc)
BuildRequires: pkgconfig(rtmidi)
#BuildRequires: pkgconfig(rtaudio)
BuildRequires: pkgconfig(rubberband)
BuildRequires: pkgconfig(jack)
BuildRequires: pkgconfig(json-glib-1.0)
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Gui)
BuildRequires: pkgconfig(Qt5Widgets)
BuildRequires: pkgconfig(libxdot)
BuildRequires: python3dist(sphinx)
BuildRequires: python3dist(pypandoc)
BuildRequires: pkgconfig(libzstd)
BuildRequires: pkgconfig(lsp-dsp-lib)
BuildRequires: pkgconfig(vamp)
BuildRequires: pkgconfig(soxr)
BuildRequires: pkgconfig(zix-0)
BuildRequires: pkgconfig(yyjson)
BuildRequires: libxml2
BuildRequires: jq-devel
BuildRequires: help2man
BuildRequires: texi2html
BuildRequires: xdg-utils
BuildRequires: meson
BuildRequires: guile
Requires:      carla
Requires:      ladspa
Requires:      lilv
Requires:      lv2
Requires:      fftw
Requires:      jackit
Requires:      %{_lib}lsp-dsp-lib

# for building rtaudio
BuildRequires: pkgconfig(libpulse-simple)

%description
Zrythm is a digital audio workstation designed to be
featureful and easy to use.
It offers streamlined editing workflows with flexible
tools, limitless automation capabilities, powerful
mixing features, chord assistance and support for
various plugin and file formats.

%prep
%autosetup -n %name-%v

# alleviate requirement for carla-host-plugin
# as of 2024-08-12, 2.6.0 doesn't even exist yet
sed -i "/^\s*'carla-host-plugin', version: / s@>=2.6.0@>=2.5.0@" meson.build

mkdir vendor tmproot
cd vendor
git clone https://github.com/thestk/rtaudio --depth 1 -b 6.0.1 -j8

# we need to vendor this here (too new; not even in rawhide)
pushd rtaudio
#? https://src.fedoraproject.org/fork/neil/rpms/rtaudio/blob/rawhide/f/rtaudio.spec
# Fix encoding issues
for file in tests/teststops.cpp; do
   sed 's|\r||' $file > $file.tmp
   iconv -f ISO-8859-1 -t UTF8 $file.tmp > $file.tmp2
   touch -r $file $file.tmp2
   mv -f $file.tmp2 $file
done
export CFLAGS="%optflags -fPIC"
autoreconf -fiv
%configure --with-jack --with-alsa --with-pulse --enable-shared --disable-static --verbose
%make_build
make install
popd


%build
CFLAGS=$(echo "$CFLAGS -fuse-ld=mold -Wno-incompatible-pointer-types -Wno-implicit-function-declaration" | sed -E "s@\b-Werror\b@@")
CXXFLAGS=$(echo "$CFLAGS -fuse-ld=mold" | sed -E "s@\b-Werror\b@@")

%meson \
       -Drtmidi=enabled \
       -Drtaudio=enabled \
       -Dsdl=enabled \
       -Dlsp_dsp=disabled \
       -Dgraphviz=enabled \
       --buildtype=release
%meson_build

%install
%meson_install

%find_lang %name

%files -f %name.lang
%doc README.md
%license COPYING
%_bindir/%name*
%_libdir/zrythm/carla/
%_libdir/zrythm/lv2
%_datadir/applications/org.zrythm.Zrythm.desktop
%_datadir/fonts/%name
%_datadir/glib-2.0/schemas/*.xml
%_iconsdir/hicolor/scalable/apps/%name.svg
%_datadir/%name/
%_datadir/mime/packages/org.zrythm.Zrythm-mime.xml
%bash_completions_dir/zrythm
%fish_completions_dir/zrythm
%_datadir/metainfo/org.zrythm.Zrythm.appdata.xml
%_mandir/man1/zrythm.1.*
