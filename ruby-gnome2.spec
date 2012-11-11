Summary:	GNOME 2 libraries for Ruby
Summary(pl.UTF-8):	Biblioteki GNOME 2 dla języka Ruby
Name:		ruby-gnome2
Version:	1.1.5
Release:	0.1
License:	LGPL v2.1
Group:		Development/Languages
Source0:	http://downloads.sourceforge.net/ruby-gnome2/%{name}-all-%{version}.tar.gz
# Source0-md5:	6158ad49d59a1faa9f1f67356124a3c7
URL:		http://ruby-gnome2.sourceforge.jp/
BuildRequires:	atk-devel >= 1.0
BuildRequires:	cairo-devel >= 1.10.0
BuildRequires:	gdk-pixbuf2-devel >= 2
BuildRequires:	glib2-devel >= 1:2.16.0
BuildRequires:	goocanvas-devel >= 0.8
BuildRequires:	gstreamer0.10-devel >= 0.10.35
BuildRequires:	gstreamer0.10-plugins-base-devel >= 0.10.35
BuildRequires:	gtk+2-devel >= 2:2.12.0
BuildRequires:	gtksourceview2-devel
BuildRequires:	librsvg-devel >= 2.8
BuildRequires:	pango-devel >= 1:1.0
BuildRequires:	pkgconfig
BuildRequires:	poppler-glib-devel >= 0.8.0
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	ruby-devel >= 1.8.5
BuildRequires:	ruby-pkg-config
BuildRequires:	ruby-rubygems
BuildRequires:	sed >= 4.0
BuildRequires:	vte-devel >= 0.12.1
# for pango and gtk2
Requires:	ruby-rcairo
%{?ruby_mod_ver_requires_eq}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNOME 2 libraries for Ruby.

%description -l pl.UTF-8
Biblioteki GNOME 2 dla języka Ruby.

%package devel
Summary:	Header files for Ruby-GNOME2
Summary(pl.UTF-8):	Pliki nagłówkowe dla Ruby-GNOME2
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for Ruby-GNOME2.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla Ruby-GNOME2.

%package doc-ri
Summary:	Ruby-GNOME2 ri documentation
Summary(pl.UTF-8):	Dokumentacja dla Ruby-GNOME2 w formacie ri
Group:		Documentation
Requires:	%{name} = %{version}-%{release}

%description doc-ri
Ruby-GNOME2 ri documentation.

%description doc-ri -l pl.UTF-8
Dokumentacja dla Ruby-GNOME2 w formacie ri.

%package doc-html
Summary:	Ruby-GNOME2 HTML documentation
Summary(pl.UTF-8):	Dokumentacja dla Ruby-GNOME2 w formacie HTML
Group:		Documentation
Requires:	%{name} = %{version}-%{release}

%description doc-html
Ruby-GNOME2 HTML documentation.

%description doc-html -l pl.UTF-8
Dokumentacja dla Ruby-GNOME2 w formacie HTML.

%package examples
Summary:	Ruby-GNOME2 examples
Summary(pl.UTF-8):	Przykłady do Ruby-GNOME2
Group:		Development/Libraries

%description examples
Ruby-GNOME2 examples.

%description examples -l pl.UTF-8
Przykłady do Ruby-GNOME2.

%prep
%setup -q -n %{name}-all-%{version}
find . -name '*.rb' | xargs sed -i -e '1s,#.*local/bin/ruby,#!%{_bindir}/ruby,'

%build
ruby extconf.rb \
	--enable-glib-experimental
%{__make}

rdoc -o rdoc
rdoc --ri -o ri

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_archdir},%{ruby_rubylibdir},%{ruby_ridir}} \
	$RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	RUBYLIBDIR=$RPM_BUILD_ROOT%{ruby_rubylibdir} \
	sitearchdir=$RPM_BUILD_ROOT%{ruby_archdir} \
	pkgconfigdir=$RPM_BUILD_ROOT%{_pkgconfigdir} \
	RUBYARCHDIR=$RPM_BUILD_ROOT%{ruby_archdir}

cp -a gdk_pixbuf2/sample \
	$RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}/gdk_pixbuf2

cp -a glib2/sample \
	$RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}/glib2

cp -a goocanvas/sample \
	$RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}/goocanvas

cp -a gstreamer/sample \
	$RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}/gstreamer

cp -a gtk2/sample \
	$RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}/gtk2

cp -a gtksourceview2/sample \
	$RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}/gtksourceview2

cp -a pango/sample \
	$RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}/pango

cp -a poppler/sample \
	$RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}/poppler

cp -a rsvg2/sample \
	$RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}/rsvg2

cp -a vte/sample \
	$RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}/vte

cp -a ri/* $RPM_BUILD_ROOT%{ruby_ridir}
%{__rm} -r $RPM_BUILD_ROOT%{ruby_ridir}/{Object,TC_*,Test*}
%{__rm} $RPM_BUILD_ROOT%{ruby_ridir}/{cache.ri,created.rid}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%attr(755,root,root) %{ruby_archdir}/atk.so
%attr(755,root,root) %{ruby_archdir}/gdk_pixbuf2.so
%attr(755,root,root) %{ruby_archdir}/gio2.so
%attr(755,root,root) %{ruby_archdir}/glib2.so
%attr(755,root,root) %{ruby_archdir}/gstreamer.so
%attr(755,root,root) %{ruby_archdir}/gtk2.so
%attr(755,root,root) %{ruby_archdir}/gtksourceview2.so
%attr(755,root,root) %{ruby_archdir}/pango.so
%attr(755,root,root) %{ruby_archdir}/poppler.so
%attr(755,root,root) %{ruby_archdir}/rsvg2.so
%attr(755,root,root) %{ruby_archdir}/vte.so
%{ruby_rubylibdir}/atk.rb
%{ruby_rubylibdir}/gdk_pixbuf2.rb
%{ruby_rubylibdir}/gio2.rb
%{ruby_rubylibdir}/glib-mkenums.rb
%{ruby_rubylibdir}/glib2.rb
%{ruby_rubylibdir}/gnome2-raketask.rb
%{ruby_rubylibdir}/gnome2-win32-binary-build-task.rb
%{ruby_rubylibdir}/gnome2-win32-binary-download-task.rb
%{ruby_rubylibdir}/gst.rb
%{ruby_rubylibdir}/gtk2.rb
%{ruby_rubylibdir}/gtksourceview2.rb
%{ruby_rubylibdir}/mkmf-gnome2.rb
%{ruby_rubylibdir}/pango.rb
%{ruby_rubylibdir}/poppler.rb
%{ruby_rubylibdir}/rsvg2.rb
%{ruby_rubylibdir}/vte.rb
%{ruby_rubylibdir}/gio2
%{ruby_rubylibdir}/glib2
%{ruby_rubylibdir}/gtk2
%{ruby_rubylibdir}/vte

%files devel
%defattr(644,root,root,755)
%{ruby_archdir}/glib-enum-types.h
%{ruby_archdir}/rbatk.h
%{ruby_archdir}/rbatkversion.h
%{ruby_archdir}/rbgcompat.h
%{ruby_archdir}/rbgdk-pixbuf.h
%{ruby_archdir}/rbgdk-pixbuf2conversions.h
%{ruby_archdir}/rbgdk.h
%{ruby_archdir}/rbgdkconversions.h
%{ruby_archdir}/rbglib.h
%{ruby_archdir}/rbglib2conversions.h
%{ruby_archdir}/rbglibdeprecated.h
%{ruby_archdir}/rbgobject.h
%{ruby_archdir}/rbgtk.h
%{ruby_archdir}/rbgtkconversions.h
%{ruby_archdir}/rbgtkmacros.h
%{ruby_archdir}/rbgutil.h
%{ruby_archdir}/rbgutil_list.h
%{ruby_archdir}/rbgutildeprecated.h
%{ruby_archdir}/rbpango.h
%{ruby_archdir}/rbpangoconversions.h
%{ruby_archdir}/rbpangoversion.h
%{_pkgconfigdir}/ruby-atk.pc
%{_pkgconfigdir}/ruby-gdk-pixbuf2.pc
%{_pkgconfigdir}/ruby-gio2.pc
%{_pkgconfigdir}/ruby-glib2.pc
%{_pkgconfigdir}/ruby-gstreamer.pc
%{_pkgconfigdir}/ruby-gtk2.pc
%{_pkgconfigdir}/ruby-gtksourceview2.pc
%{_pkgconfigdir}/ruby-pango.pc
%{_pkgconfigdir}/ruby-poppler.pc
%{_pkgconfigdir}/ruby-rsvg2.pc
%{_pkgconfigdir}/ruby-vte.pc

%files doc-html
%defattr(644,root,root,755)
%doc rdoc/*

%files doc-ri
%defattr(644,root,root,755)
%{ruby_ridir}/A
%{ruby_ridir}/AlphaDemo
%{ruby_ridir}/AssistantRunner
%{ruby_ridir}/Atk
%{ruby_ridir}/ButtonBoxSample
%{ruby_ridir}/ButtonSample
%{ruby_ridir}/Cairo
%{ruby_ridir}/Canvas
%{ruby_ridir}/CanvasSampleArrowhead
%{ruby_ridir}/CanvasSampleFifteen
%{ruby_ridir}/CheckButtonSample
%{ruby_ridir}/ColorSelectionSample
%{ruby_ridir}/Demo
%{ruby_ridir}/DestWindow
%{ruby_ridir}/DialogSample
%{ruby_ridir}/DraggableWidget
%{ruby_ridir}/EntrySample
%{ruby_ridir}/FileSelectionSample
%{ruby_ridir}/FontSelectionSample
%{ruby_ridir}/GLib
%{ruby_ridir}/GLibTestUtils
%{ruby_ridir}/GNOME2Package
%{ruby_ridir}/GNOME2Win32BinaryBuildTask
%{ruby_ridir}/GNOME2Win32BinaryDownloadTask
%{ruby_ridir}/GammaCurveSample
%{ruby_ridir}/Gdk
%{ruby_ridir}/Gesture
%{ruby_ridir}/GestureProcessor
%{ruby_ridir}/GesturedWidget
%{ruby_ridir}/Gio
%{ruby_ridir}/Goo
%{ruby_ridir}/GooCanvasSample
%{ruby_ridir}/Gst
%{ruby_ridir}/GstTestUtils
%{ruby_ridir}/Gtk
%{ruby_ridir}/GtkTestUtils
%{ruby_ridir}/Inspector
%{ruby_ridir}/Layout
%{ruby_ridir}/LayoutSample
%{ruby_ridir}/MediaInfo
%{ruby_ridir}/MediaInfoStream
%{ruby_ridir}/MediaInfoTrack
%{ruby_ridir}/MenuSample
%{ruby_ridir}/MultiTerm
%{ruby_ridir}/MyButton
%{ruby_ridir}/MyButton2
%{ruby_ridir}/MyGtkPlug
%{ruby_ridir}/MyGtkSocket
%{ruby_ridir}/NotebookSample
%{ruby_ridir}/Pager
%{ruby_ridir}/Pango
%{ruby_ridir}/PangoTestUtils
%{ruby_ridir}/PixmapSample
%{ruby_ridir}/Pong
%{ruby_ridir}/Poppler
%{ruby_ridir}/PopplerTestUtils
%{ruby_ridir}/Print
%{ruby_ridir}/ProgressBarSample
%{ruby_ridir}/RSVG
%{ruby_ridir}/RadioButtonSample
%{ruby_ridir}/RangeSample
%{ruby_ridir}/ReparentSample
%{ruby_ridir}/RulerSample
%{ruby_ridir}/Sample
%{ruby_ridir}/SampleClass
%{ruby_ridir}/SampleDialog
%{ruby_ridir}/SampleWindow
%{ruby_ridir}/SavedPositionSample
%{ruby_ridir}/ScrolledWindowSample
%{ruby_ridir}/ShapeSampleBasic
%{ruby_ridir}/ShapeSampleModeller
%{ruby_ridir}/ShapeSampleRings
%{ruby_ridir}/ShapeSampleSheets
%{ruby_ridir}/ShapesSample
%{ruby_ridir}/SpinButtonSample
%{ruby_ridir}/SrcWindow
%{ruby_ridir}/StatusIconSample
%{ruby_ridir}/StatusbarSample
%{ruby_ridir}/ToggleButtonSample
%{ruby_ridir}/ToolbarSample
%{ruby_ridir}/TooltipsSample
%{ruby_ridir}/Vte
%{ruby_ridir}/WMHintsSample
%{ruby_ridir}/Window

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
