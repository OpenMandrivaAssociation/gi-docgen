Name:		gi-docgen
Version:	2022.2
Release:	2
Summary:	Documentation tool for GObject-based libraries
Group:		Development/Python
License:	GPLv3+ and ASL 2.0 and CC0-1.0
Url:		https://gitlab.gnome.org/GNOME/gi-docgen/
Source0:	https://gitlab.gnome.org/GNOME/gi-docgen/-/archive/%{version}/%{name}-%{version}.tar.xz
BuildArch:	noarch

BuildRequires:	meson
BuildRequires:	python3dist(setuptools)
BuildRequires:	python3dist(jinja2)
BuildRequires:	python3dist(markdown)
BuildRequires:	python3dist(markupsafe)
BuildRequires:	python3dist(pygments)
BuildRequires:	python3dist(toml)
BuildRequires:	python3dist(typogrify)
BuildRequires:	python3dist(wheel)
BuildRequires:	python3dist(pip)

%description
GI-DocGen is a document generator for GObject-based libraries. GObject is
the base type system of the GNOME project. GI-Docgen reuses the
introspection data generated by GObject-based libraries to generate the API
reference of these libraries, as well as other ancillary documentation.

%prep
%autosetup

%build
%py_build

%install
%py_install

%files
%doc README.md
%license LICENSES LICENSES/Apache-2.0.txt LICENSES/GPL-3.0-or-later.txt
%{_bindir}/%{name}
%{_datadir}/pkgconfig/gi-docgen.pc
%{_mandir}/man1/%{name}.1.*
%{python_sitelib}/gidocgen/
%{python_sitelib}/gi_docgen-%{version}.dist-info/
