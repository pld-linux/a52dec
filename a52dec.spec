%define		subver	20040611
%define		rel		4
Summary:	A library for handling encrypted DVDs
Summary(pl.UTF-8):	Biblioteka do obsługi zakodowanych DVD
Name:		a52dec
Version:	0.7.5
Release:	0.%{subver}.%{rel}
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://liba52.sourceforge.net/files/%{name}-snapshot.tar.gz
# Source0-md5:	1729c7507f76b0d4cc04540926c5d0d7
Patch0:		%{name}-opt.patch
Patch1:		%{name}-pic.patch
URL:		http://liba52.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
Requires:	%{name}-libs = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
liba52 is a free library for decoding ATSC A/52 streams. It is
released under the terms of the GPL license. The A/52 standard is used
in a variety of applications, including digital television and DVD. It
is also known as AC-3.

This package contains a52dec utilities.

%description -l pl.UTF-8
liba52 jest wolnodostępną (na licencji GPL) biblioteką do dekodowania
strumieni ATSC A/52. Standard A/52 jest używany w wielu
zastosowaniach, w tym cyfrowej telewizji i DVD. Jest znany także jako
AC-3.

Ten pakiet zawiera narzędzia a52dec.

%package libs
Summary:	a52dec library for handling encrypted DVDs
Summary(pl.UTF-8):	Biblioteka a52dec - do obsługi zakodowanych DVD
Group:		Libraries

%description libs
liba52 is a free library for decoding ATSC A/52 streams. It is
released under the terms of the GPL license. The A/52 standard is used
in a variety of applications, including digital television and DVD. It
is also known as AC-3.

%description libs -l pl.UTF-8
liba52 jest wolnodostępną (na licencji GPL) biblioteką do dekodowania
strumieni ATSC A/52. Standard A/52 jest używany w wielu
zastosowaniach, w tym cyfrowej telewizji i DVD. Jest znany także jako
AC-3.

%package libs-devel
Summary:	Header files for a52dec library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki a52dec
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description libs-devel
Header files for development using a52dec library.

%description libs-devel -l pl.UTF-8
Pliki nagłówkowe do programowania z użyciem biblioteki a52dec.

%package libs-static
Summary:	Static a52dec library
Summary(pl.UTF-8):	Statyczna biblioteka a52dec
Group:		Development/Libraries
Requires:	%{name}-libs-devel = %{version}-%{release}

%description libs-static
Static a52dec library.

%description libs-static -l pl.UTF-8
Statyczna biblioteka a52dec.

%prep
%setup -q -n %{name}-%{version}-cvs
%patch0 -p1
%patch1 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--enable-shared
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README TODO
%attr(755,root,root) %{_bindir}/a52dec
%attr(755,root,root) %{_bindir}/extract_a52
%{_mandir}/man1/a52dec.1*
%{_mandir}/man1/extract_a52.1*

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/liba52.so.*.*.*
%ghost %{_libdir}/liba52.so.0

%files libs-devel
%defattr(644,root,root,755)
%{_libdir}/liba52.so
%{_libdir}/liba52.la
%{_includedir}/a52dec
%{_pkgconfigdir}/liba52.pc

%files libs-static
%defattr(644,root,root,755)
%{_libdir}/liba52.a
