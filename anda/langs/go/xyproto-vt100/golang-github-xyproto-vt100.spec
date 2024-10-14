# Generated by go2rpm 1.8.2
%bcond_without check

# https://github.com/xyproto/vt100
%global goipath         github.com/xyproto/vt100
Version:                1.15.4

%gometa -f

%global common_description %{expand:
:computer: VT100 Terminal Package.}

%global golicenses      LICENSE
%global godocs          README.md cmd/widget/README.md

Name:           golang-%{goname}
Release:        1%?dist
Summary:        VT100 Terminal Package

License:        BSD-3-Clause
URL:            %{gourl}
Source:         %{gosource}

%description %{common_description}

%gopkg

%prep
%goprep

%generate_buildrequires
%go_generate_buildrequires

%build
for cmd in cmd/* ; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
done

%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

%if %{with check}
%check
%gocheck
%endif

%files
%license LICENSE
%doc TODO.md README.md cmd/widget/README.md
%{_bindir}/*

%gopkgfiles

%changelog
%autochangelog
