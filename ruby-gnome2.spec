# TODO
# - update to 2.2.0
# - gtk3 packages (or create separate ruby-gtk2, ruby-gtk3 packages besides ruby-gnome2?)
# - cairo-gobject
# - gobject-introspection
#        /usr/lib/ruby/2.0/cairo_gobject.so
#        /usr/lib/ruby/2.0/gobject_introspection.so
#        /usr/lib/ruby/2.0/rbgio2.h
#        /usr/lib/ruby/2.0/rbgio2conversions.h
#        /usr/share/ruby/2.0/cairo-gobject.rb
#        /usr/share/ruby/2.0/gobject-introspection
#        /usr/share/ruby/2.0/gobject-introspection.rb
#
# Conditional build:
%bcond_with	gtk3		# build GTK+3

Summary:	GNOME 2 libraries for Ruby
Summary(pl.UTF-8):	Biblioteki GNOME 2 dla języka Ruby
Name:		ruby-gnome2
Version:	1.1.9
Release:	1
License:	LGPL v2.1
Group:		Development/Languages
Source0:	http://downloads.sourceforge.net/ruby-gnome2/%{name}-all-%{version}.tar.gz
# Source0-md5:	852a528f8e58ca2729dada994c938be0
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
BuildRequires:	ruby-rcairo-devel
BuildRequires:	ruby-rubygems
BuildRequires:	sed >= 4.0
BuildRequires:	vte0-devel >= 0.12.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNOME 2 libraries for Ruby.

%description -l pl.UTF-8
Biblioteki GNOME 2 dla języka Ruby.

%package -n ruby-glib2
Summary:	Ruby/Glib2, Ruby/GIO2 - Ruby bindings of GLib 2.x
Summary(pl.UTF-8):	Ruby/Glib2, Ruby/GIO2 - wiązania języka Ruby do bibliotek GLib 2.x
Group:		Development/Languages
Requires:	glib2 >= 1:2.16.0
Requires:	ruby >= 1.8.5
Obsoletes:	ruby-gnome2

%description -n ruby-glib2
Ruby/Glib2 is a Ruby binding of GLib 2.x. Ruby/GIO2 is a Ruby binding
of gio 2.x.

%description -n ruby-glib2 -l pl.UTF-8
Ruby/Glib2 to wiązanie języka Ruby do biblioteki GLib 2.x. Ruby/GIO2
to wiązanie języka Ruby do biblioteki gio 2.x.

%package -n ruby-glib2-devel
Summary:	Header files for Ruby/GLib2 and Ruby/GIO2 libraries
Summary(pl.UTF-8):	Pliki nagłówkowe bibliotek Ruby/GLib2 i Ruby/GIO2
Group:		Development/Libraries
Requires:	glib2-devel >= 1:2.16.0
Requires:	ruby-devel >= 1.8.5
Requires:	ruby-glib2 = %{version}-%{release}
Obsoletes:	ruby-gnome2-devel

%description -n ruby-glib2-devel
Header files for Ruby/GLib2 and Ruby/GIO2 libraries.

%description -n ruby-glib2-devel -l pl.UTF-8
Pliki nagłówkowe bibliotek Ruby/GLib2 i Ruby/GIO2.

%package -n ruby-atk
Summary:	Ruby/ATK - Ruby binding of ATK
Summary(pl.UTF-8):	Ruby/ATK - wiązanie języka Ruby do biblioteki ATK
Group:		Development/Languages
Requires:	atk >= 1.0
Requires:	ruby-glib2 = %{version}-%{release}

%description -n ruby-atk
Ruby/ATK is a Ruby binding of ATK.

%description -n ruby-atk -l pl.UTF-8
Ruby/ATK to wiązanie języka Ruby do biblioteki ATK.

%package -n ruby-atk-devel
Summary:	Header files for Ruby/ATK library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki Ruby/ATK
Group:		Development/Libraries
Requires:	atk-devel >= 1.0
Requires:	ruby-atk = %{version}-%{release}
Requires:	ruby-glib2-devel = %{version}-%{release}

%description -n ruby-atk-devel
Header files for Ruby/ATK library.

%description -n ruby-atk-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki Ruby/ATK.

%package -n ruby-pango
Summary:	Ruby/Pango - Ruby binding of pango 1.x
Summary(pl.UTF-8):	Ruby/Pango - wiązanie języka Ruby do biblioteki pango 1.x
Group:		Development/Languages
Requires:	cairo >= 1.10.0
Requires:	pango >= 1:1.0
Requires:	ruby-glib2 = %{version}-%{release}
Requires:	ruby-rcairo

%description -n ruby-pango
Ruby/Pango is a Ruby binding of pango 1.x.

%description -n ruby-pango -l pl.UTF-8
Ruby/Pango to wiązanie języka Ruby do biblioteki pango 1.x.

%package -n ruby-pango-devel
Summary:	Header files for Ruby/Pango library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki Ruby/Pango
Group:		Development/Libraries
Requires:	cairo-devel >= 1.10.0
Requires:	pango-devel >= 1.0
Requires:	ruby-glib2-devel = %{version}-%{release}
Requires:	ruby-pango = %{version}-%{release}

%description -n ruby-pango-devel
Header files for Ruby/Pango library.

%description -n ruby-pango-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki Ruby/Pango.

%package -n ruby-gdk_pixbuf2
Summary:	Ruby/GdkPixbuf2 - Ruby binding of GdkPixbuf 2.x
Summary(pl.UTF-8):	Ruby/GdkPixbuf2 - wiązanie języka Ruby do biblioteki GdkPixbuf 2.x
Group:		Development/Languages
Requires:	gdk-pixbuf2 >= 2
Requires:	ruby-glib2 = %{version}-%{release}

%description -n ruby-gdk_pixbuf2
Ruby/GdkPixbuf2 is a Ruby binding of GdkPixbuf 2.x.

%description -n ruby-gdk_pixbuf2 -l pl.UTF-8
Ruby/GdkPixbuf2 to wiązanie języka Ruby do biblioteki GdkPixbuf 2.x.

%package -n ruby-gdk_pixbuf2-devel
Summary:	Header files for Ruby/GdkPixbuf2 library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki Ruby/GdkPixbuf2
Group:		Development/Libraries
Requires:	gdk-pixbuf2-devel >= 2
Requires:	ruby-gdk_pixbuf2 = %{version}-%{release}
Requires:	ruby-glib2-devel = %{version}-%{release}

%description -n ruby-gdk_pixbuf2-devel
Header files for Ruby/GdkPixbuf2 library.

%description -n ruby-gdk_pixbuf2-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki Ruby/GdkPixbuf2.

%package -n ruby-gtk2
Summary:	Ruby/GTK2 - Ruby binding of GTK+ 2.x
Summary(pl.UTF-8):	Ruby/GTK2 - wiązanie języka Ruby do biblioteki GTK+ 2.x
Group:		Development/Languages
Requires:	gtk+2 >= 2:2.12.0
Requires:	ruby-atk = %{version}-%{release}
Requires:	ruby-gdk_pixbuf2 = %{version}-%{release}
Requires:	ruby-glib2 = %{version}-%{release}
Requires:	ruby-pango = %{version}-%{release}

%description -n ruby-gtk2
Ruby/GTK2 is a Ruby binding of GTK+ 2.x.

%description -n ruby-gtk2 -l pl.UTF-8
Ruby/GTK2 to wiązanie języka Ruby do biblioteki GTK+ 2.x.

%package -n ruby-gtk2-devel
Summary:	Header files for Ruby/GTK2 library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki Ruby/GTK2
Group:		Development/Libraries
Requires:	gtk+2-devel >= 2:2.12.0
Requires:	ruby-atk-devel = %{version}-%{release}
Requires:	ruby-gdk_pixbuf2-devel = %{version}-%{release}
Requires:	ruby-glib2-devel = %{version}-%{release}
Requires:	ruby-gtk2 = %{version}-%{release}
Requires:	ruby-pango-devel = %{version}-%{release}

%description -n ruby-gtk2-devel
Header files for Ruby/GTK2 library.

%description -n ruby-gtk2-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki Ruby/GTK2.

%package -n ruby-goocanvas
Summary:	Ruby/GooCanvas - Ruby binding of GooCanvas
Summary(pl.UTF-8):	Ruby/GooCanvas - wiązanie języka Ruby do biblioteki GooCanvas
Group:		Development/Languages
Requires:	goocanvas >= 0.8
Requires:	ruby-gtk2 = %{version}-%{release}
Requires:	ruby-rcairo

%description -n ruby-goocanvas
Ruby/GooCanvas is a Ruby binding of GooCanvas.

%description -n ruby-goocanvas -l pl.UTF-8
Ruby/GooCanvas to wiązanie języka Ruby do biblioteki GooCanvas.

%package -n ruby-goocanvas-devel
Summary:	Header files for Ruby/GooCanvas library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki Ruby/GooCanvas
Group:		Development/Libraries
Requires:	goocanvas-devel >= 0.8
Requires:	ruby-gtk2-devel = %{version}-%{release}
Requires:	ruby-rcairo-devel

%description -n ruby-goocanvas-devel
Header files for Ruby/GooCanvas library.

%description -n ruby-goocanvas-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki Ruby/GooCanvas.

%package -n ruby-gstreamer
Summary:	Ruby/GStreamer - Ruby binding of GStreamer
Summary(pl.UTF-8):	Ruby/GStreamer - wiązanie języka Ruby do biblioteki GStreamer
Group:		Development/Languages
Requires:	gstreamer0.10 >= 0.10.35
Requires:	gstreamer0.10-plugins-base >= 0.10.35
Requires:	ruby-gdk_pixbuf2 = %{version}-%{release}
Requires:	ruby-glib2 = %{version}-%{release}
Requires:	ruby-pango = %{version}-%{release}

%description -n ruby-gstreamer
Ruby/GStreamer is a Ruby binding of GStreamer.

%description -n ruby-gstreamer -l pl.UTF-8
Ruby/GStreamer to wiązanie języka Ruby do biblioteki GStreamer.

%package -n ruby-gstreamer-devel
Summary:	Header files for Ruby/GStreamer library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki Ruby/GStreamer
Group:		Development/Libraries
Requires:	gstreamer0.10-devel >= 0.10.35
Requires:	gstreamer0.10-plugins-base-devel >= 0.10.35
Requires:	ruby-gdk_pixbuf2-devel = %{version}-%{release}
Requires:	ruby-glib2-devel = %{version}-%{release}
Requires:	ruby-pango-devel = %{version}-%{release}

%description -n ruby-gstreamer-devel
Header files for Ruby/GStreamer library.

%description -n ruby-gstreamer-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki Ruby/GStreamer.

%package -n ruby-gtksourceview2
Summary:	Ruby/GtkSourceView2 - Ruby binding of gtksourceview 2.x
Summary(pl.UTF-8):	Ruby/GtkSourceView2 - wiązanie języka Ruby do biblioteki gtksourceview 2.x
Group:		Development/Languages
Requires:	gtksourceview2 >= 2.0.0
Requires:	ruby-gtk2 = %{version}-%{release}

%description -n ruby-gtksourceview2
Ruby/GtkSourceView2 is a Ruby binding of gtksourceview 2.x.

%description -n ruby-gtksourceview2 -l pl.UTF-8
Ruby/GtkSourceView2 to wiązanie języka Ruby do biblioteki
gtksourceview 2.x.

%package -n ruby-gtksourceview2-devel
Summary:	Header files for Ruby/GtkSourceView2 library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki Ruby/GtkSourceView2
Group:		Development/Libraries
Requires:	gtksourceview2-devel >= 2.0.0
Requires:	ruby-gtk2-devel = %{version}-%{release}

%description -n ruby-gtksourceview2-devel
Header files for Ruby/GtkSourceView2 library.

%description -n ruby-gtksourceview2-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki Ruby/GtkSourceView2.

%package -n ruby-poppler
Summary:	Ruby/Poppler - Ruby binding of poppler-glib
Summary(pl.UTF-8):	Ruby/Poppler - wiązanie języka Ruby do biblioteki poppler-glib
Group:		Development/Languages
Requires:	poppler-glib >= 0.8.0
Requires:	ruby-gdk_pixbuf2 = %{version}-%{release}
Requires:	ruby-glib2 = %{version}-%{release}
Requires:	ruby-gtk2 = %{version}-%{release}

%description -n ruby-poppler
Ruby/Poppler is a Ruby binding of poppler-glib.

%description -n ruby-poppler -l pl.UTF-8
Ruby/Poppler to wiązanie języka Ruby do biblioteki poppler-glib.

%package -n ruby-poppler-devel
Summary:	Header files for Ruby/Poppler library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki Ruby/Poppler
Group:		Development/Libraries
Requires:	poppler-glib-devel >= 0.8.0
Requires:	ruby-gdk_pixbuf2-devel = %{version}-%{release}
Requires:	ruby-glib2-devel = %{version}-%{release}
Requires:	ruby-gtk2-devel = %{version}-%{release}

%description -n ruby-poppler-devel
Header files for Ruby/Poppler library.

%description -n ruby-poppler-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki Ruby/Poppler.

%package -n ruby-rsvg2
Summary:	Ruby/RSVG - Ruby binding of librsvg
Summary(pl.UTF-8):	Ruby/RSVG - wiązanie języka Ruby do biblioteki librsvg
Group:		Development/Languages
Requires:	librsvg >= 2.8
Requires:	ruby-gdk_pixbuf2 = %{version}-%{release}
Requires:	ruby-glib2 = %{version}-%{release}
Requires:	ruby-rcairo

%description -n ruby-rsvg2
Ruby/RSVG is a Ruby binding of librsvg.

%description -n ruby-rsvg2 -l pl.UTF-8
Ruby/RSVG to wiązanie języka Ruby do biblioteki librsvg.

%package -n ruby-rsvg2-devel
Summary:	Header files for Ruby/RSVG library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki Ruby/RSVG
Group:		Development/Libraries
Requires:	librsvg-devel >= 2.8
Requires:	ruby-gdk_pixbuf2-devel = %{version}-%{release}
Requires:	ruby-glib2-devel = %{version}-%{release}

%description -n ruby-rsvg2-devel
Header files for Ruby/RSVG library.

%description -n ruby-rsvg2-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki Ruby/RSVG.

%package -n ruby-vte
Summary:	Ruby/VTE - Ruby binding of VTE
Summary(pl.UTF-8):	Ruby/VTE - wiązanie języka Ruby do biblioteki VTE
Group:		Development/Languages
Requires:	ruby-gtk2 = %{version}-%{release}
Requires:	vte0 >= 0.12.1

%description -n ruby-vte
Ruby/VTE is a Ruby binding of VTE.

%description -n ruby-vte -l pl.UTF-8
Ruby/VTE to wiązanie języka Ruby do biblioteki VTE.

%package -n ruby-vte-devel
Summary:	Header files for Ruby/VTE library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki Ruby/VTE
Group:		Development/Libraries
Requires:	ruby-gtk2-devel = %{version}-%{release}
Requires:	vte0-devel >= 0.12.1

%description -n ruby-vte-devel
Header files for Ruby/VTE library.

%description -n ruby-vte-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki Ruby/VTE.

%package doc-ri
Summary:	Ruby-GNOME2 ri documentation
Summary(pl.UTF-8):	Dokumentacja dla Ruby-GNOME2 w formacie ri
Group:		Documentation
Requires:	ruby

%description doc-ri
Ruby-GNOME2 ri documentation.

%description doc-ri -l pl.UTF-8
Dokumentacja dla Ruby-GNOME2 w formacie ri.

%package doc-html
Summary:	Ruby-GNOME2 HTML documentation
Summary(pl.UTF-8):	Dokumentacja dla Ruby-GNOME2 w formacie HTML
Group:		Documentation

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

cp -p glib2/README README.glib2
cp -p glib2/TODO TODO.glib2
cp -p gio2/README README.gio2
cp -p gio2/TODO TODO.gio2

%build
# echo */extconf.rb | xargs -l1 dirname

comps="
	atk
	cairo-gobject
	gdk_pixbuf2
	gio2
	glib2
	gobject-introspection
	goocanvas
	gstreamer
	gtk2
	gtksourceview2
	pango
	poppler
	rsvg2
	vte
%if %{with gtk3}
	gdk3
	gtk3
	gtksourceview3
	vte3
%endif
"

ruby extconf.rb \
	--vendor \
	--enable-glib-experimental \
	$comps
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

%files -n ruby-glib2
%defattr(644,root,root,755)
%doc AUTHORS NEWS README README.glib2 TODO.glib2 README.gio2 TODO.gio2
%attr(755,root,root) %{ruby_archdir}/gio2.so
%attr(755,root,root) %{ruby_archdir}/glib2.so
%{ruby_rubylibdir}/gio2.rb
%{ruby_rubylibdir}/glib-mkenums.rb
%{ruby_rubylibdir}/glib2.rb
%{ruby_rubylibdir}/gnome2-raketask.rb
# these files are expected to exist not only on Win32
%{ruby_rubylibdir}/gnome2-win32-binary-build-task.rb
%{ruby_rubylibdir}/gnome2-win32-binary-download-task.rb
%{ruby_rubylibdir}/mkmf-gnome2.rb
%{ruby_rubylibdir}/gio2
%{ruby_rubylibdir}/glib2

%files -n ruby-glib2-devel
%defattr(644,root,root,755)
%{ruby_archdir}/glib-enum-types.h
%{ruby_archdir}/rbgcompat.h
%{ruby_archdir}/rbglib.h
%{ruby_archdir}/rbglib2conversions.h
%{ruby_archdir}/rbglibdeprecated.h
%{ruby_archdir}/rbgobject.h
%{ruby_archdir}/rbgutil.h
%{ruby_archdir}/rbgutil_list.h
%{ruby_archdir}/rbgutildeprecated.h
%{_pkgconfigdir}/ruby-gio2.pc
%{_pkgconfigdir}/ruby-glib2.pc

%files -n ruby-atk
%defattr(644,root,root,755)
%doc atk/README
%attr(755,root,root) %{ruby_archdir}/atk.so
%{ruby_rubylibdir}/atk.rb

%files -n ruby-atk-devel
%defattr(644,root,root,755)
%{ruby_archdir}/rbatk.h
%{ruby_archdir}/rbatkversion.h
%{_pkgconfigdir}/ruby-atk.pc

%files -n ruby-pango
%defattr(644,root,root,755)
%doc pango/README
%attr(755,root,root) %{ruby_archdir}/pango.so
%{ruby_rubylibdir}/pango.rb

%files -n ruby-pango-devel
%defattr(644,root,root,755)
%{ruby_archdir}/rbpango.h
%{ruby_archdir}/rbpangoconversions.h
%{ruby_archdir}/rbpangoversion.h
%{_pkgconfigdir}/ruby-pango.pc

%files -n ruby-gdk_pixbuf2
%defattr(644,root,root,755)
%doc gdk_pixbuf2/README
%attr(755,root,root) %{ruby_archdir}/gdk_pixbuf2.so
%{ruby_rubylibdir}/gdk_pixbuf2.rb

%files -n ruby-gdk_pixbuf2-devel
%defattr(644,root,root,755)
%{ruby_archdir}/rbgdk-pixbuf.h
%{ruby_archdir}/rbgdk-pixbuf2conversions.h
%{_pkgconfigdir}/ruby-gdk-pixbuf2.pc

%files -n ruby-gtk2
%defattr(644,root,root,755)
%doc gtk2/README
%attr(755,root,root) %{ruby_archdir}/gtk2.so
%{ruby_rubylibdir}/gtk2.rb
%{ruby_rubylibdir}/gtk2

%files -n ruby-gtk2-devel
%defattr(644,root,root,755)
%{ruby_archdir}/rbgdk.h
%{ruby_archdir}/rbgdkconversions.h
%{ruby_archdir}/rbgtk.h
%{ruby_archdir}/rbgtkconversions.h
%{ruby_archdir}/rbgtkmacros.h
%{_pkgconfigdir}/ruby-gtk2.pc

%files -n ruby-goocanvas
%defattr(644,root,root,755)
%doc goocanvas/README
%attr(755,root,root) %{ruby_archdir}/goocanvas.so
%{ruby_rubylibdir}/goocanvas.rb

%files -n ruby-goocanvas-devel
%defattr(644,root,root,755)
%{_pkgconfigdir}/ruby-goocanvas.pc

%files -n ruby-gstreamer
%defattr(644,root,root,755)
%doc gstreamer/README
%attr(755,root,root) %{ruby_archdir}/gstreamer.so
%{ruby_rubylibdir}/gst.rb

%files -n ruby-gstreamer-devel
%defattr(644,root,root,755)
%{_pkgconfigdir}/ruby-gstreamer.pc

%files -n ruby-gtksourceview2
%defattr(644,root,root,755)
%doc gtksourceview2/README
%attr(755,root,root) %{ruby_archdir}/gtksourceview2.so
%{ruby_rubylibdir}/gtksourceview2.rb

%files -n ruby-gtksourceview2-devel
%defattr(644,root,root,755)
%{_pkgconfigdir}/ruby-gtksourceview2.pc

%files -n ruby-poppler
%defattr(644,root,root,755)
%doc poppler/README
%attr(755,root,root) %{ruby_archdir}/poppler.so
%{ruby_rubylibdir}/poppler.rb

%files -n ruby-poppler-devel
%defattr(644,root,root,755)
%{_pkgconfigdir}/ruby-poppler.pc

%files -n ruby-rsvg2
%defattr(644,root,root,755)
%doc rsvg2/README
%attr(755,root,root) %{ruby_archdir}/rsvg2.so
%{ruby_rubylibdir}/rsvg2.rb

%files -n ruby-rsvg2-devel
%defattr(644,root,root,755)
%{_pkgconfigdir}/ruby-rsvg2.pc

%files -n ruby-vte
%defattr(644,root,root,755)
%attr(755,root,root) %{ruby_archdir}/vte.so
%{ruby_rubylibdir}/vte.rb
%{ruby_rubylibdir}/vte

%files -n ruby-vte-devel
%defattr(644,root,root,755)
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
