# At this point in time, this package DOES NOT WORK on the main branch due to not being optimized for modern gnome/gnome-shell versions.
# It also does not work on the 'post-gnome45' branch due to an outdated version in the extension's metadata file, which does not update properly once installed through a package.
# This means the best way to get the updated files is from the gnome extensions website's zip archives, but if the GitHub repo gets properly updated, we can switch over to a commit-based package

# We also need to move files to the ~/.local directory instead of the typical gnome extension directory due to this being a User Extension, NOT a System Extension.

%global commit cecb04e68df0d611dc41d1030542bb40c9862d6f
%global commit_date 20240923
%global shortcommit %(c=%{commit}; echo ${c:0:7})

%global extension   tailscale-status
%global uuid        %{extension}@maxgallup.github.com

Name:           gnome-shell-extension-%{extension}
Version:        %commit
Release:        1%{?dist}
Summary:        Extension to manage and check the status of tailscale-cli
License:        GPLv2
URL:            https://github.com/maxgallup/tailscale-status
Source0:        https://extensions.gnome.org/review/download/58475.shell-extension.zip

Packager:       Owen Zimmerman <owen@fyralabs.com>

BuildArch:      noarch

BuildRequires:  wget unzip
Requires:       gnome-shell
Recommends:     gnome-extensions-app
Suggests:       tailscale

%description
An unofficial Gnome Extension to manage and check the status of tailscale-cli.
This extension is in no way affiliated with Tailscale Inc. 

%prep
wget https://extensions.gnome.org/review/download/58475.shell-extension.zip
unzip 58475.shell-extension.zip

%install
mkdir -p %{buildroot}%{_localstatedir}/lib/rpm-state/%{uuid}
mkdir -p %{buildroot}%{_localstatedir}/lib/rpm-state/%{uuid}/schemas

install -Dm644 metadata.json        %{buildroot}%{_localstatedir}/lib/rpm-state/%{uuid}/metadata.json
install -Dm644 extension.js         %{buildroot}%{_localstatedir}/lib/rpm-state/%{uuid}/extension.js
install -Dm644 prefs.js             %{buildroot}%{_localstatedir}/lib/rpm-state/%{uuid}/prefs.js
install -Dm644 icon-down.svg        %{buildroot}%{_localstatedir}/lib/rpm-state/%{uuid}/icon-down.svg
install -Dm644 icon-exit-node.svg   %{buildroot}%{_localstatedir}/lib/rpm-state/%{uuid}/icon-exit-node.svg
install -Dm644 icon-up.svg          %{buildroot}%{_localstatedir}/lib/rpm-state/%{uuid}/icon-up.svg
install -Dm644 schemas/*            %{buildroot}%{_localstatedir}/lib/rpm-state/%{uuid}/schemas/

%files
%dir %{_localstatedir}/lib/rpm-state/%{uuid}
%dir %{_localstatedir}/lib/rpm-state/%{uuid}/schemas
%{_localstatedir}/lib/rpm-state/%{uuid}/metadata.json
%{_localstatedir}/lib/rpm-state/%{uuid}/extension.js
%{_localstatedir}/lib/rpm-state/%{uuid}/prefs.js
%{_localstatedir}/lib/rpm-state/%{uuid}/icon-down.svg
%{_localstatedir}/lib/rpm-state/%{uuid}/icon-exit-node.svg
%{_localstatedir}/lib/rpm-state/%{uuid}/icon-up.svg
%{_localstatedir}/lib/rpm-state/%{uuid}/schemas/*

%post
#Since this is a User Extension, we muct only install for the current user
current_user=$(logname)
echo "Running post-transaction scripts as user ${current_user}..."

# Create the User Extensions directories in the user's home directory
mkdir -p /home/${current_user}/.local/share/gnome-shell/extensions/%{uuid}
mkdir -p /home/${current_user}/.local/share/gnome-shell/extensions/%{uuid}/schemas

# Move the files to the user's User Extensions directory
mv %{_localstatedir}/lib/rpm-state/%{uuid}/metadata.json      /home/${current_user}/.local/share/gnome-shell/extensions/%{uuid}/metadata.json
mv %{_localstatedir}/lib/rpm-state/%{uuid}/extension.js       /home/${current_user}/.local/share/gnome-shell/extensions/%{uuid}/extension.js
mv %{_localstatedir}/lib/rpm-state/%{uuid}/prefs.js           /home/${current_user}/.local/share/gnome-shell/extensions/%{uuid}/prefs.js
mv %{_localstatedir}/lib/rpm-state/%{uuid}/icon-down.svg      /home/${current_user}/.local/share/gnome-shell/extensions/%{uuid}/icon-down.svg
mv %{_localstatedir}/lib/rpm-state/%{uuid}/icon-exit-node.svg /home/${current_user}/.local/share/gnome-shell/extensions/%{uuid}/icon-exit-node.svg
mv %{_localstatedir}/lib/rpm-state/%{uuid}/icon-up.svg        /home/${current_user}/.local/share/gnome-shell/extensions/%{uuid}/icon-up.svg
mv %{_localstatedir}/lib/rpm-state/%{uuid}/schemas/*        /home/${current_user}/.local/share/gnome-shell/extensions/%{uuid}/schemas/

echo "Extension files successfully installed for user ${current_user}"

%postun
# Remove the files from the user's User Extensions directory on package uninstallation
if [ $1 -eq 0 ]; then
    current_user=$(logname)
    echo "Running post-uninstall scripts as user ${current_user}..."

    rm -rf /home/${current_user}/.local/share/gnome-shell/extensions/%{uuid}

    echo "Extension files successfully removed for user ${current_user}"
fi

%changelog
* Tue Jan 14 2025 Owen Zimmerman <owen@fyralabs.com>
- Initial Package