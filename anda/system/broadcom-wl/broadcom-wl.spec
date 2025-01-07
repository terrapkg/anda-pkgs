%if 0%{?rhel} > 6 || 0%{?fedora}
 %global        _modprobe_d         %{_prefix}/lib/modprobe.d
 %global        _dracut_conf_d      %{_prefix}/lib/dracut/dracut.conf.d
 %global        _nmlibdir_conf_d    %{_prefix}/lib/NetworkManager/conf.d
%else #rhel <= 6
 %global        _modprobe_d         %{_sysconfdir}/modprobe.d
 %global        _dracut_conf_d      %{_sysconfdir}/dracut.conf.d
%endif

%if 0%{?rhel} > 7 || 0%{?fedora}
 %bcond_without python3
%else
 %bcond_with python3
%endif

Name:       broadcom-wl
Version:    6.30.223.271
Release:    1%{?dist}
Summary:    Common files for Broadcom 802.11 STA driver
Group:      System Environment/Kernel
License:    Redistributable, no modification permitted
URL:        https://www.broadcom.com/support/download-search?pg=Legacy+Products&pf=Legacy+Wireless&pn=&pa=&po=&dk=&pl=
Source0:    https://docs.broadcom.com/docs-and-downloads/docs/linux_sta/hybrid-v35-nodebug-pcoem-6_30_223_271.tar.gz
Source1:    https://docs.broadcom.com/docs-and-downloads/docs/linux_sta/hybrid-v35_64-nodebug-pcoem-6_30_223_271.tar.gz
Source2:    https://docs.broadcom.com/docs-and-downloads/docs/linux_sta/README_6.30.223.271.txt
Source3:    broadcom-wl-blacklist.conf
Source4:    20-wl.conf
Source5:    api
Source6:    fedora.readme
Source7:    com.broadcom.wireless.hybrid.driver.metainfo.xml
Source8:    generate-modalias-metadata.py
Source9:    90-broadcom-wl.conf
BuildArch:  noarch
Provides:   wl-kmod-common = %{?epoch}:%{version}
Requires:   wl-kmod >= %{?epoch}:%{version}
ExcludeArch:    ppc ppc64
BuildRequires:    python3
BuildRequires:    libappstream-glib

%description
Packaged Broadcom 802.11 Linux STA Driver for Wi-Fi for BCM4311-, BCM4312-, BCM4313-, BCM4321-, BCM4322-, BCM43142-, BCM43224-, BCM43225-, BCM43227-, BCM43228-, BCM4331-, BCM4360, and -BCM4352-.

%prep
%setup -q -c
iconv -f iso8859-1 -t UTF8 lib/LICENSE.txt -o lib/LICENSE.txt
sed -i 's/\r$//' lib/LICENSE.txt
cp -p %{SOURCE2} .
cp -p %{SOURCE6} .
chmod 644 lib/LICENSE.txt README_6.30.223.271.txt fedora.readme

%build


%install
install    -m 0755 -d         %{buildroot}%{_modprobe_d}
install -p -m 0644 %{SOURCE3} %{buildroot}%{_modprobe_d}/
install    -m 0755 -d         %{buildroot}%{_dracut_conf_d}
install -p -m 0644 %{SOURCE4} %{buildroot}%{_dracut_conf_d}/
install    -m 0755 -d         %{buildroot}%{_sysconfdir}/akmods/akmod-wl/
install -p -m 0644 %{SOURCE5} %{buildroot}%{_sysconfdir}/akmods/akmod-wl/
%if 0%{?rhel} > 6 || 0%{?fedora} >= 25
install    -m 0755 -d         %{buildroot}%{_nmlibdir_conf_d}/
install -p -m 0644 %{SOURCE9} %{buildroot}%{_nmlibdir_conf_d}/
install    -m 0755 -d         %{buildroot}%{_metainfodir}/
install -p -m 0644 %{SOURCE7} %{buildroot}%{_metainfodir}/
fn=%{buildroot}%{_metainfodir}/com.broadcom.wireless.hybrid.driver.metainfo.xml
# appstream-util deletes all comments in the metainfo.xml file, so copyright must be saved and rewritten to the resulting file.
copyright_string=$(grep Copyright ${fn})
%if %{with python3}
python3 %{SOURCE8} README_6.30.223.271.txt "SUPPORTED DEVICES" | xargs appstream-util add-provide ${fn} modalias
%else
python %{SOURCE8} README_6.30.223.271.txt "SUPPORTED DEVICES" | xargs appstream-util add-provide ${fn} modalias
%endif
appstream-util validate-relax --nonet ${fn}
grep -q Copyright ${fn} >/dev/null || sed -i "s%\(^<?xml.*$\)%\1\n${copyright_string}%" ${fn}
%endif

%files
%doc README_6.30.223.271.txt fedora.readme
%doc lib/LICENSE.txt
%{_metainfodir}/com.broadcom.wireless.hybrid.driver.metainfo.xml
%config %{_nmlibdir_conf_d}/90-broadcom-wl.conf
%config(noreplace) %{_modprobe_d}/broadcom-wl-blacklist.conf
%config(noreplace) %{_dracut_conf_d}/20-wl.conf
%config(noreplace) %{_sysconfdir}/akmods/akmod-wl/api

%changelog
%autochangelog
