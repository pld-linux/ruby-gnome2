#
# TODO:
#   - subpackages
#
%define	ruby_archdir	%(ruby -r rbconfig -e 'print Config::CONFIG["archdir"]')
%define	ruby_rubylibdir	%(ruby -r rbconfig -e 'print Config::CONFIG["rubylibdir"]')
%define	ruby_ridir	%(ruby -r rbconfig -e 'include Config; print File.join(CONFIG["datadir"], "ri", CONFIG["ruby_version"], "system")')
Summary:	GNOME 2 libraries for Ruby
Summary(pl):	Biblioteki GNOME 2 dla Ruby
Name:		ruby-gnome2
Version:	0.11.0
Release:	1
License:	GPL
Group:		Development/Languages
Source0:	http://unc.dl.sourceforge.net/%{name}/%{name}-all-%{version}.tar.gz
# Source0-md5:	a4fe0c52f971bf01e2382479f4c56470
URL:		http://ruby-gnome2.sourceforge.jp/
BuildRequires:	GConf2-devel >= 2.0
BuildRequires:	glib2-devel >= 2.0
BuildRequires:	gtk+2-devel >= 2:2.2
BuildRequires:	gnome-panel-devel >= 2.0
BuildRequires:	gnome-vfs2-devel >= 2.0
BuildRequires:	gstreamer-plugins-devel
BuildRequires:	gtkglext-devel >= 1.0
BuildRequires:	gtksourceview-devel
BuildRequires:	libart_lgpl-devel >= 2.0
BuildRequires:	libgda-devel
BuildRequires:	libglade2-devel >= 2.0
BuildRequires:	libgnomecanvas-devel >= 2.0
BuildRequires:	libgnomeui-devel >= 2.0
BuildRequires:	libgtkhtml-devel >= 2.0
BuildRequires:	libpng-devel
BuildRequires:	pango-devel
BuildRequires:	pkgconfig
BuildRequires:	ruby
Requires:	ruby-rbogl
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNOME 2 libraries for Ruby, including GTKHtml2.

%description -l pl
Biblioteki GNOME 2 dla Ruby, w³±cznie z GTKHtml2.

%prep
%setup -q -n %{name}-all-%{version}

%build
find . -name '*.rb' | xargs perl -pi -e "s#local/bin/ruby#bin/ruby#"
ruby extconf.rb --enable-glib-experimental
%{__make}

rdoc -o rdoc
rdoc --ri -o ri

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_archdir},%{ruby_rubylibdir},%{ruby_ridir}} \
	$RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}/{gtkhtml2,gnomecanvas,libart,libglade,gtkglext,gtk/gtk-demo,gtk/misc,gtk/testgtk,gnome/test-gnome,gdkpixbuf,pango}

install atk/src/atk.so \
	gconf/src/gconf2.so \
	gdkpixbuf/gdk_pixbuf2.so \
	glib/src/glib2.so \
	gnomecanvas/src/gnomecanvas2.so \
	gnomeprint/src/gnomeprint2.so \
	gnomeprintui/src/gnomeprintui2.so \
	gnome/src/gnome2.so \
	gnomevfs/src/gnomevfs.so \
	gstreamer/src/gst.so \
	gtkglext/src/gtkglext.so \
	gtkhtml2/src/gtkhtml2.so \
	gtksourceview/src/gtksourceview.so \
	gtk/src20/gtk20.so \
	gtk/src22/gtk22.so \
	gtk/src/gtk2.so \
	libart/src/libart2.so \
	libgda/src/libgda.so \
	libglade/libglade2.so \
	panel-applet/panelapplet2.so \
	pango/src/pango.so \
	rsvg/src/rsvg2.so \
	$RPM_BUILD_ROOT%{ruby_archdir}



install atk/src/lib/atk.rb \
	gconf/src/lib/gconf2.rb \
	glib/src/lib/glib2.rb \
	glib/src/lib/mkmf-gnome2.rb \
	gnomecanvas/src/lib/gnomecanvas2.rb \
	gnomeprint/src/lib/gnomeprint2.rb \
	gnomeprintui/src/lib/gnomeprintui2.rb \
	gnome/src/lib/gnome2.rb \
	gnomevfs/src/lib/gnomevfs.rb \
	gstreamer/src/lib/gst.rb \
	gtkglext/src/lib/gtkglext.rb \
	gtkhtml2/src/lib/gtkhtml2.rb \
	gtksourceview/src/lib/gtksourceview.rb \
	gtk/src/lib/gtk2.rb \
	libgda/src/lib/libgda.rb \
	pango/src/lib/pango.rb \
	rsvg/src/lib/rsvg2.rb \
	$RPM_BUILD_ROOT%{ruby_rubylibdir}

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

rm ri/ri/TC* ri/ri/Test* ri/ri/Array ri/ri/Object -r
cp -a ri/ri/* $RPM_BUILD_ROOT%{ruby_ridir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README ChangeLog rdoc
%attr(755,root,root) %{ruby_archdir}/*.so
%{ruby_rubylibdir}/*.rb
%{ruby_ridir}/*
%{_examplesdir}/%{name}-%{version}
