Name:           chatgpt-gui
Version:        0.4.1
Release:        1%{?dist}
Summary:        A GUI application for ChatGPT.

License:        MIT
URL:            https://github.com/Cubicpath/ChatGPT-GUI
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-wheel
BuildRequires:  python3-numpy
BuildArch: noarch

Requires:       python3-tkinter

%description
ChatGPT GUI is an interactive GUI application for ChatGPT.

%prep
%autosetup -n %{name}-%{version}

%build

%install
%py3_build
%py3_install

%files
%license LICENSE
%doc README.md
%{_bindir}/chatgpt-gui
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
* Fri Mar 17 2023 Kalvin McCallum <kalvin_mccallum@student.uml.edu> - 0.4.1-1
- Updated package version and release number
- Removed the -p1 option in %prep section
- No other changes made.
