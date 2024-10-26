%define debug_package %nil
%global _build_id_links none

# do not strip binaries
%define __strip /bin/true

# do not perform compression in cpio
# AppImage is already compressed so there's no use
%define _source_payload w0.ufdio
%define _binary_payload w19.zstdio

# Exclude private libraries
%global __provides_exclude_from %{_datadir}/%{name}/.*\\.so

%global vvdeps libffi.so.7 libgcc_s.so.1 liblzma.so.5 libmvec.so.1 libpython3.11.so.1.0 libreadline.so.8 libstdc++.so.6 libtinfo.so.6 libuuid.so.1 libz.so.1
%global libdeps libappindicator.so.1 libgconf-2.so.4 libindicator.so.7 libnotify.so.4 libXss.so.1 libXtst.so.6
%global electrondeps chrome-sandbox chrome_100_percent.pak chrome_200_percent.pak chrome_crashpad_handler chromedriver chromedriver.debug icudtl.dat libEGL.so libGLESv2.so libffmpeg.so libvk_swiftshader.so libvulkan.so.1
Name:			voicevox
Version:		0.21.1
Release:		2%?dist
Summary:		Free Japanese text-to-speech editor
License:		LGPL-3.0
URL:			https://voicevox.hiroshiba.jp
Source0:        https://github.com/VOICEVOX/voicevox/releases/download/%version/VOICEVOX.AppImage.7z.001
Source1:        https://github.com/VOICEVOX/voicevox/releases/download/%version/VOICEVOX.AppImage.7z.002
Source2:        https://github.com/VOICEVOX/voicevox/releases/download/%version/VOICEVOX.AppImage.7z.003
Source3:        https://raw.githubusercontent.com/VOICEVOX/voicevox/refs/tags/%version/LGPL_LICENSE
Packager:       madonuko <mado@fyralabs.com>
Requires:       electron
BuildRequires:  p7zip-plugins
ExclusiveArch:  x86_64
AutoReqProv:    no

%{lua:
for dep in rpm.expand("%vvdeps"):gmatch("[^%s]+") do
    print("Requires: "..dep.."()(64bit)\n")
end

for dep in rpm.expand("%libdeps"):gmatch("[^%s]+") do
    print("Requires: "..dep.."()(64bit)\n")
end
}

%description
VOICEVOX is a free Japanese text-to-speech software with medium output quality.

%package doc
Summary: Documentation files for voicevox (Japanese)

%description doc
%summary.

%prep
7z -y x %SOURCE0
chmod a+x VOICEVOX.AppImage

./VOICEVOX.AppImage --appimage-extract

sed -i "s|Exec=.*|Exec=/usr/share/voicevox/VOICEVOX.AppImage|" squashfs-root/voicevox.desktop

%build
cd squashfs-root
%define dep() rm %1 && echo "%1()(64bit)"
cd vv-engine
rm %vvdeps
cd ..


cd usr/lib
rm %libdeps
cd ../..

# deps provided by electron
rm %electrondeps || true

%install
pushd squashfs-root

mkdir -p %buildroot%_datadir/voicevox %buildroot%_bindir
mv locales resources vv-engine %buildroot%_datadir/voicevox/
install -Dm644 .%_iconsdir/hicolor/0x0/apps/voicevox.png %buildroot%_iconsdir/hicolor/256x256/apps/voicevox.png
install -Dm755 voicevox %buildroot%_bindir/voicevox
install -Dm644 voicevox.desktop %buildroot%_datadir/applications/voicevox.desktop
rm -rf .%_prefix voicevox.png voicevox.desktop voicevox
mv * %buildroot%_datadir/voicevox/

popd

# free up spaces
%dnl rm %SOURCE0 %SOURCE1 %SOURCE2
mv %buildroot%_datadir/voicevox/README.txt .
cp %SOURCE3 ./LICENSE

# HACK: masking /usr/lib/rpm/check-rpaths, no choice
export QA_RPATHS=$(( 0x0002|0x0010 ))


%files
%doc README.txt
%license LICENSE
%_bindir/voicevox
%_datadir/voicevox
%_datadir/applications/voicevox.desktop
%_iconsdir/hicolor/256x256/apps/voicevox.png
