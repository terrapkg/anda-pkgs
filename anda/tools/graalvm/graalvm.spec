%global mxver 6.27.6
%global jvmci 22.0-b01
%global gsummary Universal virtual machine for running programs in different languages
%global desc %{expand:
GraalVM is a high-performance JDK distribution designed to accelerate the
execution of applications written in Java and other JVM languages along with
support for JavaScript, Ruby, Python, and a number of other popular languages.}

Name:		graalvm
Version:	23.0.0
Release:	1%{?dist}
URL:		https://www.graalvm.org/
Source0:	https://github.com/oracle/graal/archive/refs/tags/vm-ce-%version.tar.gz
Source1:	https://github.com/graalvm/mx/archive/refs/tags/%mxver.tar.gz
Source2:	https://github.com/graalvm/graal-jvmci-8/releases/download/jvmci-%jvmci/openjdk-8u302+06-jvmci-%jvmci-fastdebug-linux-amd64.tar.gz
Summary:	%gsummary
License:	GPL-2.0
Requires:	python3.10
BuildRequires:	fdupes
# https://mail.openjdk.org/pipermail/graal-dev/2015-December/004050.html
BuildRequires:	libstdc++-static hg ant gcc-c++ java-1.8.0-openjdk java-11-openjdk java-17-openjdk java-latest-openjdk make cmake git

%description
%{desc}


%prep
git clone https://github.com/oracle/graal
cd graal
git checkout vm-ce-%version
cd ..
tar xf %SOURCE1
%dnl tar xf %SOURCE2


%build
PATH="$PATH:$PWD/mx-%mxver"
%dnl JAVA_HOME=$PWD/openjdk1.8.0_302-jvmci-%jvmci-fastdebug
cd graal/vm
JAVA_HOME=/usr/lib/jvm/$(alternatives --list | grep jre_1.8.0_openjdk | sed -E 's@.+?/@/@g') mx --env ce build &
JAVA_HOME=/usr/lib/jvm/$(alternatives --list | grep jre_11_openjdk | sed -E 's@.+?/@/@g') mx --env ce build &
JAVA_HOME=/usr/lib/jvm/$(alternatives --list | grep jre_17_openjdk | sed -E 's@.+?/@/@g') mx --env ce build &
JAVA_HOME=/usr/lib/jvm/$(alternatives --list | grep jre_20_openjdk | sed -E 's@.+?/@/@g') mx --env ce build &

wait

%install
ls -alh graal/vm


%files


%changelog
* Sat Jun 17 2023 windowsboy111 <windowsboy111@fyralabs.com> - 22.3.2-2
- Add devel packages.

* Thu May 11 2023 windowsboy111 <windowsboy111@fyralabs.com> - 22.3.2-1
- Remove jdk19
    
* Thu Feb 9 2023 windowsboy111 <windowsboy111@fyralabs.com> - 22.3.1-1
- Initial package
