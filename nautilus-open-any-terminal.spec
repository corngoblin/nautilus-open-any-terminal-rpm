Name:           nautilus-open-any-terminal
Version:        0.6.0
Release:        1%{?dist}
Summary:        Context-menu entry for opening other terminal in nautilus
License:        GPLv3
URL:            https://github.com/Stunkymonkey/nautilus-open-any-terminal

Source:         %{url}/archive/refs/tags/%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  gettext
BuildRequires:  make

Requires:       nautilus-python
Requires:       glib2

%global _python_dist_allow_version_zero 1

%description
An extension for nautilus, which adds an context-entry for opening other terminal emulators than gnome-terminal.

%prep
%autosetup -n %{name}-%{version}

%build
make 

%install
make install-nautilus schema 

%post
glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :

%files
%license LICENSE
%doc README.md
%{python3_sitelib}/nautilus_open_any_terminal*
%{_datadir}/glib-2.0/schemas/com.github.stunkymonkey.%{name}.gschema.xml
%{_datadir}/locale/*/LC_MESSAGES/%{name}.mo
%{_datadir}/nautilus-python/extensions/nautilus_open_any_terminal.py

