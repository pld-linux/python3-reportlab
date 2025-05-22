#
# Conditional build:
%bcond_without	doc	# PDF documentation

# TODO:
# - use system fonts (see files lists) or share fonts for both python versions
# - tools/docco and tools/pythonpoint as subpackages?

Summary:	Python library for generating PDFs and graphics
Summary(pl.UTF-8):	Moduły Pythona do generowania PDF-ów oraz grafik
Name:		python3-reportlab
Version:	3.6.13
Release:	1
License:	BSD-like
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/reportlab/
Source0:	https://files.pythonhosted.org/packages/source/r/reportlab/reportlab-%{version}.tar.gz
# Source0-md5:	8cbb12bb007d2d055d610d05c9869d43
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

install -d $RPM_BUILD_ROOT%{py3_sitescriptdir}/reportlab

%{__rm} -r $RPM_BUILD_ROOT%{py3_sitedir}/reportlab/graphics/samples

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a demos $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

# TODO: (whole) pythonpoint as subpackage?
#install -p tools/pythonpoint/pythonpoint.py $RPM_BUILD_ROOT%{_bindir}
#cp -a tools/pythonpoint/demos $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}/pythonpoint-demos

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES.md LICENSE.txt README.txt
%dir %{py3_sitescriptdir}/reportlab
%dir %{py3_sitedir}/reportlab
%{py3_sitedir}/reportlab-%{version}-py*.egg-info
%{py3_sitedir}/reportlab/*.py
%{py3_sitedir}/reportlab/__pycache__
%dir %{py3_sitedir}/reportlab/fonts
%{py3_sitedir}/reportlab/fonts/00readme.txt
# Dark Garden font (GPL v2+)
%{py3_sitedir}/reportlab/fonts/DarkGardenMK.afm
%{py3_sitedir}/reportlab/fonts/DarkGardenMK.pfb
%{py3_sitedir}/reportlab/fonts/DarkGarden.sfd
%{py3_sitedir}/reportlab/fonts/DarkGarden-*.txt
# Bitstream Vera font
%{py3_sitedir}/reportlab/fonts/Vera*.ttf
%{py3_sitedir}/reportlab/fonts/bitstream-vera-license.txt
# ?
%{py3_sitedir}/reportlab/fonts/callig15.afm
%{py3_sitedir}/reportlab/fonts/callig15.pfb
# Adobe fonts
%{py3_sitedir}/reportlab/fonts/_a*____.pfb
%{py3_sitedir}/reportlab/fonts/_e*____.pfb
%{py3_sitedir}/reportlab/fonts/co*____.pfb
%{py3_sitedir}/reportlab/fonts/sy______.pfb
%{py3_sitedir}/reportlab/fonts/z?______.pfb
%dir %{py3_sitedir}/reportlab/graphics
%attr(755,root,root) %{py3_sitedir}/reportlab/graphics/_renderPM.cpython-*.so
%{py3_sitedir}/reportlab/graphics/*.py
%{py3_sitedir}/reportlab/graphics/__pycache__
%dir %{py3_sitedir}/reportlab/graphics/barcode
%{py3_sitedir}/reportlab/graphics/barcode/*.py
%{py3_sitedir}/reportlab/graphics/barcode/__pycache__
%dir %{py3_sitedir}/reportlab/graphics/charts
%{py3_sitedir}/reportlab/graphics/charts/*.py
%{py3_sitedir}/reportlab/graphics/charts/__pycache__
%dir %{py3_sitedir}/reportlab/graphics/widgets
%{py3_sitedir}/reportlab/graphics/widgets/*.py
%{py3_sitedir}/reportlab/graphics/widgets/__pycache__
%dir %{py3_sitedir}/reportlab/lib
%attr(755,root,root) %{py3_sitedir}/reportlab/lib/_rl_accel.cpython-*.so
%{py3_sitedir}/reportlab/lib/*.py
%{py3_sitedir}/reportlab/lib/__pycache__
%dir %{py3_sitedir}/reportlab/pdfbase
%{py3_sitedir}/reportlab/pdfbase/*.py
%{py3_sitedir}/reportlab/pdfbase/__pycache__
%dir %{py3_sitedir}/reportlab/pdfgen
%{py3_sitedir}/reportlab/pdfgen/*.py
%{py3_sitedir}/reportlab/pdfgen/__pycache__
%dir %{py3_sitedir}/reportlab/platypus
%{py3_sitedir}/reportlab/platypus/*.py
%{py3_sitedir}/reportlab/platypus/__pycache__

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc docs/reportlab-userguide.pdf
%endif

%files examples
%defattr(644,root,root,755)
%dir %{_examplesdir}/%{name}-%{version}
%{_examplesdir}/%{name}-%{version}/demos
