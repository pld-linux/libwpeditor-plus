%define snap 20070601
Summary:	In-place editor library for Maemo
Summary(pl.UTF-8):	Biblioteka edytora dla Maemo
Name:		libwpeditor-plus
Version:	0.0.%{snap}
Release:	1
License:	LGPL
Group:		Libraries
Source0:	%{name}-%{snap}.tar.bz2
# Source0-md5:	dd6a1317380f86b9d54581076b0856c8
URL:		http://modest.garage.maemo.org/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
# preferably with hildon patches
BuildRequires:	gtk+2-devel >= 1:2.0.0
BuildRequires:	intltool
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
In-place editor library for the Maemo platform.

%description -l pl.UTF-8
Biblioteka edytora dla platformy Maemo.

%package devel
Summary:	Header files for libwpeditor-plus
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libwpeditor-plus
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gtk+2-devel >= 1:2.0.0

%description devel
Header files for libwpeditor-plus.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libwpeditor-plus.

%prep
%setup -q -n %{name}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libwpeditor-plus.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libwpeditor-plus.so
%{_libdir}/libwpeditor-plus.la
%dir %{_includedir}/libwpeditor-plus
%{_includedir}/libwpeditor-plus/gtksourceiter.h
%{_includedir}/libwpeditor-plus/wptextbuffer.h
%{_includedir}/libwpeditor-plus/wptextview.h
%{_pkgconfigdir}/libwpeditor-plus.pc
