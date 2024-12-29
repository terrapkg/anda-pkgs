%global commit c8950d376ab3be13fbd9a19317163075f4feddbc
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commit_date 20241228

Name:           ghostty-glfw-nightly
Version:        %{commit_date}.%{shortcommit}
Release:        1%?dist
Summary:        Fast, native, feature-rich terminal emulator pushing modern features. This is the Tip (nightly) build using the GLFW rendering library.
License:        MIT
URL:            https://ghostty.org/
Source0:        https://github.com/ghostty-org/ghostty/archive/%{commit}/ghostty-%{commit}.tar.gz
#Patch0:         use-pkg-config.diff
Patch1:         no-strip.diff
BuildRequires:  fontconfig-devel
BuildRequires:  freetype-devel
BuildRequires:  glfw-devel
BuildRequires:  glib2-devel
BuildRequires:  harfbuzz-devel
BuildRequires:  libpng-devel
BuildRequires:  ncurses
BuildRequires:  ncurses-devel
BuildRequires:  oniguruma-devel
BuildRequires:  pandoc-cli
BuildRequires:  pixman-devel
BuildRequires:  zig
BuildRequires:  zlib-ng-devel
#BuildRequires:  pkg-config
#BuildRequires:  pkgconfig(harfbuzz)
#BuildRequires:  pkgconfig(fontconfig)
#BuildRequires:  pkgconfig(libpng)
#BuildRequires:  pkgconfig(zlib)
#BuildRequires:  pkgconfig(oniguruma)
#BuildRequires:  pkgconfig(glslang)
# Not in Fedora
#BuildRequires:  pkgconfig(spirv-cross)
#BuildRequires:  pkgconfig(simdutf)
#BuildRequires:  pkgconfig(libxml-2.0)
Requires:       ghostty-nightly-terminfo = %{version}-%{release}
Requires:       ghostty-nightly-shell-integration = %{version}-%{release}
Requires:       fontconfig
Requires:       freetype
Requires:       glib2
Requires:       glfw
Requires:       harfbuzz
Requires:       libpng
Requires:       oniguruma
Requires:       pixman
Requires:       zlib-ng
Conflicts:      ghostty
Conflicts:      ghostty-nightly
Conflicts:      ghostty-glfw
Provides:       ghostty-tip-glfw = %{version}-%{release}
Provides:       ghostty-glfw-tip = %{version}-%{release}
Packager:       ShinyGil <rockgrub@protonmail.com>

%description
👻 Ghostty is a fast, feature-rich, and cross-platform terminal emulator that uses platform-native UI and GPU acceleration.

%prep
%autosetup -n ghostty-%{commit} -p1

%build

%install
zig build \
    --summary all \
    -Doptimize=ReleaseFast --release=fast \
    --prefix %{buildroot}%{_prefix} --verbose \
    -Dpie=true \
    -Dapp-runtime=glfw \
    -Demit-docs
rm -rf %{buildroot}%{bash_completions_dir}/ghostty.bash \
       %{buildroot}%{fish_completions_dir}/ghostty.fish \
       %{buildroot}%{zsh_completions_dir}/_ghostty \
       %{buildroot}%{_datadir}/ghostty/shell-integration \
       %{buildroot}%{_datadir}/terminfo/*

%files
%doc README.md
%license LICENSE
%_bindir/ghostty
%_datadir/applications/com.mitchellh.ghostty.desktop
%_datadir/bat/syntaxes/ghostty.sublime-syntax
%_datadir/ghostty/
%_datadir/kio/servicemenus/com.mitchellh.ghostty.desktop
%_datadir/nvim/site/ftdetect/ghostty.vim
%_datadir/nvim/site/ftplugin/ghostty.vim
%_datadir/nvim/site/syntax/ghostty.vim
%_datadir/vim/vimfiles/ftdetect/ghostty.vim
%_datadir/vim/vimfiles/ftplugin/ghostty.vim
%_datadir/vim/vimfiles/syntax/ghostty.vim
%_iconsdir/hicolor/16x16/apps/com.mitchellh.ghostty.png
%_iconsdir/hicolor/16x16@2/apps/com.mitchellh.ghostty.png
%_iconsdir/hicolor/32x32/apps/com.mitchellh.ghostty.png
%_iconsdir/hicolor/32x32@2/apps/com.mitchellh.ghostty.png
%_iconsdir/hicolor/128x128/apps/com.mitchellh.ghostty.png
%_iconsdir/hicolor/128x128@2/apps/com.mitchellh.ghostty.png
%_iconsdir/hicolor/256x256/apps/com.mitchellh.ghostty.png
%_iconsdir/hicolor/256x256@2/apps/com.mitchellh.ghostty.png
%_iconsdir/hicolor/512x512/apps/com.mitchellh.ghostty.png
%_mandir/man1/ghostty.1.gz
%_mandir/man5/ghostty.5.gz

%changelog
* Sun Dec 29 2024 ShinyGil <rockgrub@protonmail.com>
- Initial package
