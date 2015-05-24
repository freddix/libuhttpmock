Summary:	HTTP web service mocking project
Name:		libuhttpmock
Version:	0.4.0
Release:	1
License:	LGPL v2.1
Group:		Libraries
Source0:	http://tecnocode.co.uk/downloads/uhttpmock/uhttpmock-%{version}.tar.xz
# Source0-md5:	3eb169b2db6715fcab1a1ac6f1ae7a9c
URL:		https://gitorious.org/uhttpmock/pages/Home
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libsoup-devel
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
HTTP web service mocking project for projects which use libsoup.

%package devel
Summary:	Development files for libuhttpmock
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libstdc++-devel

%description devel
Development files for libuhttpmock.

%package apidocs
Summary:	uhttpmock API documentation
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
uhttpmock API documentation.

%prep
%setup -qn uhttpmock-%{version}

# kill gnome common deps
%{__sed} -i -e '/GNOME_COMPILE_WARNINGS.*/d'		\
    -i -e '/GNOME_MAINTAINER_MODE_DEFINES/d'	\
    -i -e '/GNOME_COMMON_INIT/d'		\
    -i -e '/GNOME_CXX_WARNINGS.*/d'		\
    -i -e '/GNOME_CODE_COVERAGE/d'		\
    -i -e '/GNOME_DEBUG_CHECK/d' configure.ac

%{__sed} -i -e '/@GNOME_CODE_COVERAGE_RULES@/d' Makefile.am

%build
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}
%configure \
	--disable-silent-rules	\
	--disable-static	\
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %ghost %{_libdir}/libuhttpmock-0.0.so.0
%attr(755,root,root) %{_libdir}/libuhttpmock-0.0.so.*.*.*
%{_libdir}/girepository-1.0/Uhm-0.0.typelib

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libuhttpmock-0.0.so
%{_includedir}/libuhttpmock-0.0
%{_pkgconfigdir}/libuhttpmock-0.0.pc
%{_datadir}/gir-1.0/Uhm-0.0.gir
%{_datadir}/vala/vapi/libuhttpmock-0.0.deps
%{_datadir}/vala/vapi/libuhttpmock-0.0.vapi

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/libuhttpmock-*

