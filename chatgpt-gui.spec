Name:           chatgpt-gui
Version:        0.4.1
Release:        1%{?dist}
Summary:        An unofficial GUI app for ChatGPT.
License:        MIT
URL:            https://pypi.org/project/chatgpt-gui/
Source:         %{pypi_source chatgpt-gui}

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
This is package 'chatgpt-gui' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-chatgpt-gui
Summary:        %{summary}

%description -n python3-chatgpt-gui %_description

%prep
%autosetup -p1 -n chatgpt-gui-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files '*' +auto

%check
%pyproject_check_import

%files -n python3-chatgpt-gui -f %{pyproject_files}

%changelog
* Thu Mar 23 2023 Kalvin McCallum <kalvin_mccallum@student.uml.edu> - 0.4.1-1
- Initial package
