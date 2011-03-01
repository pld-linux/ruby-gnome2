Summary:	GNOME 2 libraries for Ruby
Summary(pl.UTF-8):	Biblioteki GNOME 2 dla Ruby
Name:		ruby-gnome2
Version:	0.90.6
Release:	2
License:	GPL
Group:		Development/Languages
Source0:	http://downloads.sourceforge.net/ruby-gnome2/%{name}-all-%{version}.tar.gz
# Source0-md5:	089986860203f87c5fcfa0c375637d60
URL:		http://ruby-gnome2.sourceforge.jp/
BuildRequires:	glib2-devel >= 1:2.16.0
BuildRequires:	goocanvas-devel >= 0.8
BuildRequires:	gstreamer-plugins-base-devel
BuildRequires:	gtk+2-devel >= 2:2.12.0
BuildRequires:	gtksourceview2-devel
BuildRequires:	librsvg-devel
BuildRequires:	pango-devel
BuildRequires:	pkgconfig
BuildRequires:	poppler-glib-devel >= 0.5.2
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	ruby-devel
BuildRequires:	ruby-pkg-config
BuildRequires:	ruby-rubygems
BuildRequires:	sed >= 4.0
BuildRequires:	vte-devel >= 0.12.1
BuildRequires:	xulrunner-devel >= 1.9-5
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
find . -name '*.rb' | xargs sed -i -e '1s,#.*local/bin/ruby,#!%{_bindir}/ruby,'

%build
ruby extconf.rb --enable-glib-experimental
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

cp -a poppler/sample \
	$RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}/poppler

cp -a gtkmozembed/sample \
	$RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}/gtkmozembed

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
rm -rf $RPM_BUILD_ROOT%{ruby_ridir}/ri/{Array,Object,TC*,Test*}

rm -f $RPM_BUILD_ROOT%{ruby_ridir}/Array/cdesc-Array.yaml

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README ChangeLog rdoc
%attr(755,root,root) %{ruby_archdir}/atk.so
%attr(755,root,root) %{ruby_archdir}/gdk_pixbuf2.so
%attr(755,root,root) %{ruby_archdir}/gio2.so
%attr(755,root,root) %{ruby_archdir}/glib2.so
%attr(755,root,root) %{ruby_archdir}/gst.so
%attr(755,root,root) %{ruby_archdir}/gtk2.so
%attr(755,root,root) %{ruby_archdir}/gtkmozembed.so
%attr(755,root,root) %{ruby_archdir}/gtksourceview2.so
%attr(755,root,root) %{ruby_archdir}/pango.so
%attr(755,root,root) %{ruby_archdir}/poppler.so
%attr(755,root,root) %{ruby_archdir}/rsvg2.so
%attr(755,root,root) %{ruby_archdir}/vte.so
%{ruby_rubylibdir}/*.rb
%{ruby_rubylibdir}/gtk2

%files devel
%defattr(644,root,root,755)
%{ruby_archdir}/*.h
%{_pkgconfigdir}/*.pc

%files doc-ri
%defattr(644,root,root,755)
%{ruby_ridir}/*

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
