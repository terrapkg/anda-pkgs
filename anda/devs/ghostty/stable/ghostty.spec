%global debug_package %{nil}

Name:           ghostty
Version:        1.0.0
Release:        1%?dist
Summary:        A fast, native terminal emulator written in Zig
License:        MIT
URL:            https://ghostty.org/
Source0:        https://release.files.ghostty.org/%version/ghostty-source.tar.gz
BuildRequires:  zig
BuildRequires:  gtk4-devel libadwaita-devel
Conflicts:      ghostty-nightly
Packager:       ShinyGil <rockgrub@protonmail.com>

%description
👻 Ghostty is a fast, feature-rich, and cross-platform terminal emulator that uses platform-native UI and GPU acceleration.

%package        fish-completion
Summary:        Ghostty Fish completion
Requires:       %{name}
Requires:       fish

%description    fish-completion
%summary.

%package        zsh-completion
Summary:        Ghostty Zsh completion
Requires:       %{name}
Requires:       zsh

%description    zsh-completion
%summary.

%prep
%autosetup -n ghostty-source

%build
zig build -Doptimize=ReleaseFast --release=fast

%install
install -Dpm755 zig-out/bin/ghostty %buildroot%_bindir/ghostty
install -Dpm644 zig-out/share/applications/com.mitchellh.ghostty.desktop %buildroot%_datadir/applications/com.mitchellh.ghostty.desktop
install -Dpm644 zig-out/share/bat/syntaxes/ghostty.sublime-syntax %buildroot%_datadir/bat/syntaxes/ghostty.sublime-syntax
install -Dpm644 zig-out/share/ghostty/shell-integration/bash/bash-preexec.sh %buildroot%_datadir/ghostty/shell-integration/bash/bash-preexec.sh
install -Dpm644 zig-out/share/ghostty/shell-integration/bash/ghostty.bash %buildroot%_datadir/ghostty/shell-integration/bash/ghostty.bash
install -Dpm644 zig-out/share/ghostty/shell-integration/elvish/lib/ghostty-integration.elv %buildroot%_datadir/ghostty/shell-integration/elvish/lib/ghostty-integration.elv
install -Dpm644 zig-out/share/ghostty/shell-integration/fish/vendor_conf.d/ghostty-shell-integration.fish %buildroot%_datadir/ghostty/shell-integration/fish/vendor_conf.d/ghostty-shell-integration.fish
install -Dpm644 zig-out/share/ghostty/shell-integration/zsh/.zshenv %buildroot%_datadir/ghostty/shell-integration/zsh/.zshenv
install -Dpm644 zig-out/share/ghostty/shell-integration/zsh/ghostty-integration %buildroot%_datadir/ghostty/shell-integration/zsh/ghostty-integration
install -Dpm644 zig-out/share/kio/servicemenus/com.mitchellh.ghostty.desktop %buildroot%_datadir/kio/servicemenus/com.mitchellh.ghostty.desktop
install -Dpm644 zig-out/share/nvim/site/ftdetect/ghostty.vim %buildroot%_datadir/nvim/site/ftdetect/ghostty.vim
install -Dpm644 zig-out/share/nvim/site/ftplugin/ghostty.vim %buildroot%_datadir/nvim/site/ftplugin/ghostty.vim
install -Dpm644 zig-out/share/nvim/site/syntax/ghostty.vim %buildroot%_datadir/nvim/site/syntax/ghostty.vim
install -Dpm644 zig-out/share/vim/vimfiles/ftdetect/ghostty.vim %buildroot%_datadir/vim/vimfiles/ftdetect/ghostty.vim
install -Dpm644 zig-out/share/vim/vimfiles/ftplugin/ghostty.vim %buildroot%_datadir/vim/vimfiles/ftplugin/ghostty.vim
install -Dpm644 zig-out/share/vim/vimfiles/syntax/ghostty.vim %buildroot%_datadir/vim/vimfiles/syntax/ghostty.vim
install -Dpm644 zig-out/share/terminfo/ghostty.termcap %buildroot%_datadir/terminfo/ghostty.termcap
install -Dpm644 zig-out/share/terminfo/ghostty.terminfo %buildroot%_datadir/terminfo/ghostty.terminfo
install -Dpm644 zig-out/share/terminfo/g/ghostty %buildroot%_datadir/terminfo/g/ghostty
install -Dpm644 zig-out/share/terminfo/x/xterm-ghostty %buildroot%_datadir/terminfo/x/xterm-ghostty
install -Dpm644 zig-out/share/icons/hicolor/16x16/apps/com.mitchellh.ghostty.png %buildroot%_iconsdir/hicolor/16x16/apps/com.mitchellh.ghostty.png
install -Dpm644 zig-out/share/icons/hicolor/16x16@2/apps/com.mitchellh.ghostty.png %buildroot%_iconsdir/hicolor/16x16@2/apps/com.mitchellh.ghostty.png
install -Dpm644 zig-out/share/icons/hicolor/32x32/apps/com.mitchellh.ghostty.png %buildroot%_iconsdir/hicolor/32x32/apps/com.mitchellh.ghostty.png
install -Dpm644 zig-out/share/icons/hicolor/32x32@2/apps/com.mitchellh.ghostty.png %buildroot%_iconsdir/hicolor/32x32@2/apps/com.mitchellh.ghostty.png
install -Dpm644 zig-out/share/icons/hicolor/128x128/apps/com.mitchellh.ghostty.png %buildroot%_iconsdir/hicolor/128x128/apps/com.mitchellh.ghostty.png
install -Dpm644 zig-out/share/icons/hicolor/128x128@2/apps/com.mitchellh.ghostty.png %buildroot%_iconsdir/hicolor/128x128@2/apps/com.mitchellh.ghostty.png
install -Dpm644 zig-out/share/icons/hicolor/256x256/apps/com.mitchellh.ghostty.png %buildroot%_iconsdir/hicolor/256x256/apps/com.mitchellh.ghostty.png
install -Dpm644 zig-out/share/icons/hicolor/256x256@2/apps/com.mitchellh.ghostty.png %buildroot%_iconsdir/hicolor/256x256@2/apps/com.mitchellh.ghostty.png
install -Dpm644 zig-out/share/icons/hicolor/512x512/apps/com.mitchellh.ghostty.png %buildroot%_iconsdir/hicolor/512x512/apps/com.mitchellh.ghostty.png
install -Dpm644 zig-out/share/fish/vendor_completions.d/ghostty.fish %buildroot%fish_completions_dir/ghostty.fish
install -Dpm644 zig-out/share/zsh/site-functions/_ghostty %buildroot%zsh_completions_dir/_ghostty

%files
%doc README.md
%license LICENSE
%_bindir/ghostty
%_datadir/applications/com.mitchellh.ghostty.desktop
%_datadir/bat/syntaxes/ghostty.sublime-syntax
%_datadir/ghostty/shell-integration/bash/bash-preexec.sh
%_datadir/ghostty/shell-integration/bash/ghostty.bash
%_datadir/ghostty/shell-integration/elvish/lib/ghostty-integration.elv
%_datadir/ghostty/shell-integration/fish/vendor_conf.d/ghostty-shell-integration.fish
%_datadir/ghostty/shell-integration/zsh/.zshenv
%_datadir/ghostty/shell-integration/zsh/ghostty-integration
%_datadir/kio/servicemenus/com.mitchellh.ghostty.desktop
%_datadir/nvim/site/ftdetect/ghostty.vim
%_datadir/nvim/site/ftplugin/ghostty.vim
%_datadir/nvim/site/syntax/ghostty.vim
%_datadir/vim/vimfiles/ftdetect/ghostty.vim
%_datadir/vim/vimfiles/ftplugin/ghostty.vim
%_datadir/vim/vimfiles/syntax/ghostty.vim
%_datadir/terminfo/ghostty.termcap
%_datadir/terminfo/ghostty.terminfo
%_datadir/terminfo/g/ghostty
%_datadir/terminfo/x/xterm-ghostty
%_iconsdir/hicolor/16x16/apps/com.mitchellh.ghostty.png
%_iconsdir/hicolor/16x16@2/apps/com.mitchellh.ghostty.png
%_iconsdir/hicolor/32x32/apps/com.mitchellh.ghostty.png
%_iconsdir/hicolor/32x32@2/apps/com.mitchellh.ghostty.png
%_iconsdir/hicolor/128x128/apps/com.mitchellh.ghostty.png
%_iconsdir/hicolor/128x128@2/apps/com.mitchellh.ghostty.png
%_iconsdir/hicolor/256x256/apps/com.mitchellh.ghostty.png
%_iconsdir/hicolor/256x256@2/apps/com.mitchellh.ghostty.png
%_iconsdir/hicolor/512x512/apps/com.mitchellh.ghostty.png

%files fish-completion
%fish_completions_dir/ghostty.fish

%files zsh-completion
%zsh_completions_dir/_ghostty

%changelog
* Thu Dec 26 2024 ShinyGil <rockgrub@protonmail.com>
- Initial package
