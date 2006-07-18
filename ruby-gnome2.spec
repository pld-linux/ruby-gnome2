Summary:	GNOME 2 libraries for Ruby
Summary(pl):	Biblioteki GNOME 2 dla Ruby
Name:		ruby-gnome2
Version:	0.15.0
Release:	1
License:	GPL
Group:		Development/Languages
Source0:	http://dl.sourceforge.net/ruby-gnome2/%{name}-all-%{version}.tar.gz
# Source0-md5:	3e5b89b674a2b60ff9d3a2eeac0468e9
URL:		http://ruby-gnome2.sourceforge.jp/
BuildRequires:	GConf2-devel >= 2.0
BuildRequires:	glib2-devel >= 2.0
BuildRequires:	gnome-panel-devel >= 2.0
BuildRequires:	gnome-vfs2-devel >= 2.0
BuildRequires:	gstreamer-plugins-devel
BuildRequires:	gtk+2-devel >= 2:2.2
BuildRequires:	gtkglext-devel >= 1.0
BuildRequires:	gtksourceview-devel
BuildRequires:	libart_lgpl-devel >= 2.0
BuildRequires:	libgda-devel
BuildRequires:	libglade2-devel >= 2.0
BuildRequires:	libgnomecanvas-devel >= 2.0
BuildRequires:	libgnomeprintui-devel
BuildRequires:	libgnomeui-devel >= 2.0
BuildRequires:	libgtkhtml-devel >= 2.0
BuildRequires:	libpng-devel
BuildRequires:	librsvg-devel
BuildRequires:	pango-devel
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	ruby-devel
BuildRequires:	sed >= 4.0
Requires:	ruby-rcairo
Requires:	ruby-rbogl
%{?ruby_mod_ver_requires_eq}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNOME 2 libraries for Ruby, including GTKHtml2.

%description -l pl
Biblioteki GNOME 2 dla Ruby, w³±cznie z GTKHtml2.

%package devel
Summary:	Header files for Ruby-GNOME2
Summary(pl):	Pliki nag³ówkowe dla Ruby-GNOME2
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for Ruby-GNOME2.

%description devel -l pl
Pliki nag³ówkowe dla Ruby-GNOME2.

%package doc-ri
Summary:	Ruby-GNOME2 ri documentation
Summary(pl):	Dokumentacja dla Ruby-GNOME2 w formacie ri.
Group:		Documentation
Requires:	%{name} = %{version}-%{release}

%description doc-ri
Ruby-GNOME2 ri documentation.

%description doc-ri -l pl
Dokumentacja dla Ruby-GNOME2 w formacie ri.

%package examples
Summary:	Ruby-GNOME2 examples
Summary(pl):	Przyk³ady do Ruby-GNOME2
Group:		Development/Libraries

%description examples
Ruby-GNOME2 examples.

%description examples -l pl
Przyk³ady do Ruby-GNOME2.

%prep
%setup -q -n %{name}-all-%{version}
find . -name '*.rb' | xargs sed -i -e '1s,#.*local/bin/ruby,#!%{_bindir}/ruby,'

%build
ruby extconf.rb --enable-glib-experimental
%{__make}

rdoc -o rdoc
rdoc --ri -o ri

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_archdir},%{ruby_rubylibdir},%{ruby_ridir}} \
	$RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}/{gtkhtml2,gnomecanvas,libart,libglade,gtkglext,gtk/gtk-demo,gtk/misc,gtk/testgtk,gnome/test-gnome,gdkpixbuf,pango}

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

cp -a ri/ri/* $RPM_BUILD_ROOT%{ruby_ridir}
rm -rf $RPM_BUILD_ROOT%{ruby_ridir}/ri/ri/{Array,Object,TC*,Test*}

rm -f $RPM_BUILD_ROOT%{ruby_ridir}/Array/cdesc-Array.yaml

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README ChangeLog rdoc
%attr(755,root,root) %{ruby_archdir}/*.so
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
