#
# TODO:
#   - subpackages
#
%define	ruby_archdir	%(ruby -r rbconfig -e 'print Config::CONFIG["archdir"]')
%define	ruby_rubylibdir	%(ruby -r rbconfig -e 'print Config::CONFIG["rubylibdir"]')
Summary:	Gnome2 libraries for Ruby
Summary(pl):	Biblioteki Gnome2 dla Ruby
Name:		ruby-gnome2
Version:	0.7.0
Release:	1
License:	GPL
Group:		Development/Languages
Source0:	http://dl.sourceforge.net/%{name}/%{name}-all-%{version}.tar.gz
# Source0-md5:	412292423f145ef756edf918f0892d7e
Source1:	http://www.intersect-uk.co.uk/~iugeoff/glibinterface.tar.gz
# Source1-md5:	4b33c9c638dd3861e8da7fa43cfe9a1f
Patch0:		%{name}-extconf.patch
Patch1:		%{name}-glibinterface.patch
URL:		http://ruby-gnome2.sourceforge.jp/
BuildRequires:	gnome-vfs2-devel
BuildRequires:	gtkglext-devel
BuildRequires:	gtkhtml-devel
BuildRequires:	ruby
Requires:	ruby-rbogl
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gnome2 libraries for Ruby, including gstreamer and GTKHtml2.

%description -l pl
Biblioteki Gnome2 dla Ruby, w³±cznie z gstreamer i GTKHtml2.

%prep
%setup -q -n %{name}-all-%{version} -a1
%patch0 -p1
%patch1 -p0

%build
cp glibinterface/treemodel.iface.h gtk/src
ruby extconf.rb --enable-glib-experimental
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_archdir},%{ruby_rubylibdir}} \
	$RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}/{gtkhtml2,gnomecanvas,libart,libglade,gtkglext,gstreamer,gtk/gtk-demo,gtk/misc,gtk/testgtk,gnome/test-gnome,gdkpixbuf,pango}

install gtkglext/src/gtkglext.so gnomevfs/src/gnomevfs.so \
	gnomecanvas/src/gnomecanvas2.so gnome/src/gnome2.so \
	gconf/src/gconf2.so gdkpixbuf/gdk_pixbuf2.so \
	glib/src/glib2.so gstreamer/src/gst.so gtk/src/gtk2.so \
	gtk/src20/gtk20.so gtk/src22/gtk22.so gtkhtml2/src/gtkhtml2.so \
	libart/src/libart2.so libglade/libglade2.so pango/src/pango.so \
	$RPM_BUILD_ROOT%{ruby_archdir}

install gconf/src/lib/gconf2.rb gdkpixbuf/lib/gdk_pixbuf2.rb \
	glib/src/lib/mkmf-gnome2.rb glib/src/lib/glib2.rb \
	gnome/src/lib/gnome2.rb gnomecanvas/src/lib/gnomecanvas2.rb \
	gnomevfs/src/lib/gnomevfs.rb gstreamer/src/lib/gst.rb \
	gtk/src/lib/gtk2.rb gtkhtml2/src/lib/gtkhtml2.rb \
	libglade/lib/libglade2.rb pango/src/lib/pango.rb \
	gtkglext/src/lib/gtkglext.rb \
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

install gstreamer/sample/*.rb \
	$RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}/gstreamer

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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README ChangeLog
%attr(755,root,root) %{ruby_archdir}/*.so
%{ruby_rubylibdir}/*.rb
%{_examplesdir}/%{name}-%{version}
