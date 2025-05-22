#
# Conditional build:
%bcond_without	doc	# PDF documentation

# TODO:
# - use system fonts (see files lists) or share fonts for both python versions
# - tools/docco and tools/pythonpoint as subpackages?

Summary:	Python library for generating PDFs and graphics
Summary(pl.UTF-8):	Moduły Pythona do generowania PDF-ów oraz grafik
Name:		python3-reportlab
Version:	4.4.1
Release:	1
License:	BSD-like
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/reportlab/
Source0:	https://files.pythonhosted.org/packages/source/r/reportlab/reportlab-%{version}.tar.gz
# Source0-md5:	d5ac52b0a3fe2c1c8f25680f7d5ea3a2
URL:		https://www.reportlab.com/dev/opensource/
BuildRequires:	freetype-devel >= 2
BuildRequires:	libart_lgpl-devel >= 2
BuildRequires:	python3-devel >= 1:3.7
%{?with_doc:BuildRequires:	python3-pillow >= 9.0.0}
BuildRequires:	python3-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
BuildRequires:	unzip
Requires:	python3-modules >= 1:3.7
Obsoletes:	python3-ReportLab < 3.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A library written in Python that lets you generate platform
independant PDFs and graphics.
- PDF generation: uses Python, a clean OO language, layered
  architecture
- Graphics: provides primitive shapes, reusable widgets, sample
  collections including business chart and diagrams

%description -l pl.UTF-8
Biblioteka napisana w Pythonie pozwalająca na generowanie niezależnych
od platformy PDF-ów oraz grafik.
- Generowanie PDF: używa Pythona, przejrzystego języka obiektowego o
  warstwowej architekturze
- Grafika: podstawowe figury geometryczne, kontrolki, a także
  przykłady, w tym wykresy i diagramy

%package apidocs
Summary:	API documentation for ReportLab module
Summary(pl.UTF_8):	Dokumentacja API modułu ReportLab
Group:		Documentation
BuildArch:	noarch

%description apidocs
API documentation for ReportLab module.

%description apidocs -l pl.UTF-8
Dokumentacja API modułu ReportLab.

%package examples
Summary:	Examples for ReportLab
Summary(pl.UTF-8):	Przykłady do biblioteki ReportLab
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description examples
Examples for ReportLab.

%description examples -l pl.UTF-8
Przykłady do biblioteki ReportLab.

%prep
%setup -q -n reportlab-%{version}

%build
%py3_build

%if %{with doc}
cd docs
PYTHONPATH=$(echo $(pwd)/../build-3/lib.*) \
%{__python3} genAll.py
cd ..
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%{__rm} -r $RPM_BUILD_ROOT%{py3_sitescriptdir}/reportlab/graphics/samples

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a demos $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

# TODO: (whole) pythonpoint as subpackage?
#install -p tools/pythonpoint/pythonpoint.py $RPM_BUILD_ROOT%{_bindir}
#cp -a tools/pythonpoint/demos $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}/pythonpoint-demos

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES.md LICENSE README.txt
%dir %{py3_sitescriptdir}/reportlab
%{py3_sitescriptdir}/reportlab-%{version}-py*.egg-info
%{py3_sitescriptdir}/reportlab/*.py
%{py3_sitescriptdir}/reportlab/__pycache__
%dir %{py3_sitescriptdir}/reportlab/fonts
%{py3_sitescriptdir}/reportlab/fonts/00readme.txt
# Dark Garden font (GPL v2+)
%{py3_sitescriptdir}/reportlab/fonts/DarkGardenMK.afm
%{py3_sitescriptdir}/reportlab/fonts/DarkGardenMK.pfb
%{py3_sitescriptdir}/reportlab/fonts/DarkGarden.sfd
%{py3_sitescriptdir}/reportlab/fonts/DarkGarden-*.txt
# Bitstream Vera font
%{py3_sitescriptdir}/reportlab/fonts/Vera*.ttf
%{py3_sitescriptdir}/reportlab/fonts/bitstream-vera-license.txt
# ?
%{py3_sitescriptdir}/reportlab/fonts/callig15.afm
%{py3_sitescriptdir}/reportlab/fonts/callig15.pfb
# Adobe fonts
%{py3_sitescriptdir}/reportlab/fonts/_a*____.pfb
%{py3_sitescriptdir}/reportlab/fonts/_e*____.pfb
%{py3_sitescriptdir}/reportlab/fonts/co*____.pfb
%{py3_sitescriptdir}/reportlab/fonts/sy______.pfb
%{py3_sitescriptdir}/reportlab/fonts/z?______.pfb
%dir %{py3_sitescriptdir}/reportlab/graphics
%{py3_sitescriptdir}/reportlab/graphics/*.py
%{py3_sitescriptdir}/reportlab/graphics/__pycache__
%dir %{py3_sitescriptdir}/reportlab/graphics/barcode
%{py3_sitescriptdir}/reportlab/graphics/barcode/*.py
%{py3_sitescriptdir}/reportlab/graphics/barcode/__pycache__
%dir %{py3_sitescriptdir}/reportlab/graphics/charts
%{py3_sitescriptdir}/reportlab/graphics/charts/*.py
%{py3_sitescriptdir}/reportlab/graphics/charts/__pycache__
%dir %{py3_sitescriptdir}/reportlab/graphics/widgets
%{py3_sitescriptdir}/reportlab/graphics/widgets/*.py
%{py3_sitescriptdir}/reportlab/graphics/widgets/__pycache__
%dir %{py3_sitescriptdir}/reportlab/lib
%{py3_sitescriptdir}/reportlab/lib/*.py
%{py3_sitescriptdir}/reportlab/lib/__pycache__
%dir %{py3_sitescriptdir}/reportlab/pdfbase
%{py3_sitescriptdir}/reportlab/pdfbase/*.py
%{py3_sitescriptdir}/reportlab/pdfbase/__pycache__
%dir %{py3_sitescriptdir}/reportlab/pdfgen
%{py3_sitescriptdir}/reportlab/pdfgen/*.py
%{py3_sitescriptdir}/reportlab/pdfgen/__pycache__
%dir %{py3_sitescriptdir}/reportlab/platypus
%{py3_sitescriptdir}/reportlab/platypus/*.py
%{py3_sitescriptdir}/reportlab/platypus/__pycache__

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc docs/reportlab-userguide.pdf
%endif

%files examples
%defattr(644,root,root,755)
%dir %{_examplesdir}/%{name}-%{version}
%{_examplesdir}/%{name}-%{version}/demos
