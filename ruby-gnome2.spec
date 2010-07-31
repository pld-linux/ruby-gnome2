Summary:	GNOME 2 libraries for Ruby
Summary(pl.UTF-8):	Biblioteki GNOME 2 dla Ruby
Name:		ruby-gnome2
Version:	0.19.4
Release:	0.1
License:	GPL
Group:		Development/Languages
Source0:	http://dl.sourceforge.net/ruby-gnome2/%{name}-all-%{version}.tar.gz
# Source0-md5:	40451e4173e2c8bcd5046aea7e499ef9
Patch0:		%{name}-libxul.patch
Patch1:		%{name}-libgnomeui.patch
Patch2:		%{name}-ruby19.patch
URL:		http://ruby-gnome2.sourceforge.jp/
BuildRequires:	GConf2-devel >= 2.0
BuildRequires:	glib2-devel >= 2.0
BuildRequires:	gnome-panel-devel >= 2.0
BuildRequires:	gnome-vfs2-devel >= 2.0
BuildRequires:	goocanvas-devel >= 0.8
BuildRequires:	gstreamer-plugins-base-devel
BuildRequires:	gtk+2-devel >= 2:2.12.0
BuildRequires:	gtkglext-devel >= 1.0
BuildRequires:	gtksourceview-devel
BuildRequires:	gtksourceview2-devel
BuildRequires:	libart_lgpl-devel >= 2.0
BuildRequires:	libglade2-devel >= 2.0
BuildRequires:	libgnomecanvas-devel >= 2.0
BuildRequires:	libgnomeprintui-devel
BuildRequires:	libgnomeui-devel >= 2.0
BuildRequires:	libgtkhtml-devel >= 2.0
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	librsvg-devel
BuildRequires:	pango-devel
BuildRequires:	pkgconfig
BuildRequires:	poppler-glib-devel >= 0.5.2
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	ruby-devel
BuildRequires:	ruby-rcairo >= 1.8.1-3
BuildRequires:	sed >= 4.0
BuildRequires:	vte-devel >= 0.12.1
BuildRequires:	xulrunner-devel >= 1.9-5
BuildRequires:	zlib-devel
Requires:	ruby-rbogl
Requires:	ruby-rcairo
%{?ruby_mod_ver_requires_eq}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNOME 2 libraries for Ruby, including GTKHtml2.

%description -l pl.UTF-8
Biblioteki GNOME 2 dla Ruby, włącznie z GTKHtml2.

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
Summary(pl.UTF-8):	Dokumentacja dla Ruby-GNOME2 w formacie ri.
Group:		Documentation
Requires:	%{name} = %{version}-%{release}

%description doc-ri
Ruby-GNOME2 ri documentation.

%description doc-ri -l pl.UTF-8
Dokumentacja dla Ruby-GNOME2 w formacie ri.

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
%patch0 -p1
%patch1 -p1
%patch2 -p1
find . -name '*.rb' | xargs sed -i -e '1s,#.*local/bin/ruby,#!%{_bindir}/ruby,'

%build
ruby extconf.rb --enable-glib-experimental
%{__make}

rdoc -o rdoc
rdoc --ri -o ri

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_archdir},%{ruby_rubylibdir},%{ruby_ridir}} \
	$RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}/{gtkhtml2,gnomecanvas,libart,libglade,gtkglext,gtk/{gtk-demo,misc,testgtk},gnome/test-gnome,gdkpixbuf,pango}

%{__make} install \
		RUBYLIBDIR=$RPM_BUILD_ROOT%{ruby_rubylibdir} \
		sitearchdir=$RPM_BUILD_ROOT%{ruby_archdir} \
		RUBYARCHDIR=$RPM_BUILD_ROOT%{ruby_archdir}

install gtkhtml2/sample/*.rb \
	$RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}/gtkhtml2

install gnomecanvas/sample/*.rb \
	$RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}/gnomecanvas

install libart/sample/*.rb \
	$RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}/libart

install libglade/sample/*.rb \
	$RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}/libglade

install gtkglext/sample/*.rb \
	$RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}/gtkglext

install gnome/sample/*.rb \
	$RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}/gnome

install pango/sample/*.rb \
	$RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}/pango

install gdkpixbuf/sample/*.rb \
	$RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}/gdkpixbuf

install gtk/sample/gtk-demo/*.rb \
	$RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}/gtk/gtk-demo

install gtk/sample/misc/*.rb \
	$RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}/gtk/misc

install gtk/sample/testgtk/*.rb \
	$RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}/gtk/testgtk

install gnome/sample/test-gnome/*.rb \
	$RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}/gnome/test-gnome

cp -a ri/* $RPM_BUILD_ROOT%{ruby_ridir}
rm -rf $RPM_BUILD_ROOT%{ruby_ridir}/ri/{Array,Object,TC*,Test*}

rm -f $RPM_BUILD_ROOT%{ruby_ridir}/Array/cdesc-Array.yaml

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README ChangeLog rdoc
%attr(755,root,root) %{ruby_archdir}/atk.so
%attr(755,root,root) %{ruby_archdir}/bonobo2.so
%attr(755,root,root) %{ruby_archdir}/bonoboui2.so
%attr(755,root,root) %{ruby_archdir}/gconf2.so
%attr(755,root,root) %{ruby_archdir}/gdk_pixbuf2.so
%attr(755,root,root) %{ruby_archdir}/glib2.so
%attr(755,root,root) %{ruby_archdir}/gnome2.so
%attr(755,root,root) %{ruby_archdir}/gnomecanvas2.so
%attr(755,root,root) %{ruby_archdir}/gnomeprint2.so
%attr(755,root,root) %{ruby_archdir}/gnomeprintui2.so
%attr(755,root,root) %{ruby_archdir}/gnomevfs.so
%attr(755,root,root) %{ruby_archdir}/goocanvas.so
%attr(755,root,root) %{ruby_archdir}/gst.so
%attr(755,root,root) %{ruby_archdir}/gtk2.so
%attr(755,root,root) %{ruby_archdir}/gtkglext.so
%attr(755,root,root) %{ruby_archdir}/gtkhtml2.so
%attr(755,root,root) %{ruby_archdir}/gtkmozembed.so
%attr(755,root,root) %{ruby_archdir}/gtksourceview.so
%attr(755,root,root) %{ruby_archdir}/gtksourceview2.so
%attr(755,root,root) %{ruby_archdir}/libart2.so
%attr(755,root,root) %{ruby_archdir}/libglade2.so
%attr(755,root,root) %{ruby_archdir}/panelapplet2.so
%attr(755,root,root) %{ruby_archdir}/pango.so
%attr(755,root,root) %{ruby_archdir}/poppler.so
%attr(755,root,root) %{ruby_archdir}/rsvg2.so
%attr(755,root,root) %{ruby_archdir}/vte.so
%{ruby_rubylibdir}/*.rb
%{ruby_rubylibdir}/gtk2

%files devel
%defattr(644,root,root,755)
%{ruby_archdir}/*.h

%files doc-ri
%defattr(644,root,root,755)
%{ruby_ridir}/*

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
