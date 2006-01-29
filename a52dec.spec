%define		_snap	20040611
Summary:	A library for handling encrypted DVDs
Summary(pl):	Biblioteka do obs³ugi zakodowanych DVD
Name:		a52dec
Version:	0.7.5
Release:	0.%{_snap}.1
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

%description -l pl
liba52 jest wolnodostêpn± (na licencji GPL) bibliotek± do dekodowania
strumieni ATSC A/52. Standard A/52 jest u¿ywany w wielu
zastosowaniach, w tym cyfrowej telewizji i DVD. Jest znany tak¿e jako
AC-3.

Ten pakiet zawiera narzêdzia a52dec.

%package libs
Summary:	a52dec library for handling encrypted DVDs
Summary(pl):	Biblioteka a52dec - do obs³ugi zakodowanych DVD
Group:		Development/Libraries

%description libs
liba52 is a free library for decoding ATSC A/52 streams. It is
released under the terms of the GPL license. The A/52 standard is used
in a variety of applications, including digital television and DVD. It
is also known as AC-3.

%description libs -l pl
liba52 jest wolnodostêpn± (na licencji GPL) bibliotek± do dekodowania
strumieni ATSC A/52. Standard A/52 jest u¿ywany w wielu
zastosowaniach, w tym cyfrowej telewizji i DVD. Jest znany tak¿e jako
AC-3.

%package libs-devel
Summary:	Header files for a52dec library
Summary(pl):	Pliki nag³ówkowe biblioteki a52dec
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description libs-devel
Header files for development using a52dec library.

%description libs-devel -l pl
Pliki nag³ówkowe do programowania z u¿yciem biblioteki a52dec.

%package libs-static
Summary:	Static a52dec library
Summary(pl):	Statyczna biblioteka a52dec
Group:		Development/Libraries
Requires:	%{name}-libs-devel = %{version}-%{release}

%description libs-static
Static a52dec library.

%description libs-static -l pl
Statyczna biblioteka a52dec.

%prep
%setup -q -n %{name}-%{version}-cvs
%patch -p1
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

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man?/*

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/*.so.*.*

%files libs-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/*.so
%{_libdir}/*.la
%{_includedir}/*
%{_pkgconfigdir}/*.pc

%files libs-static
%defattr(644,root,root,755)
%{_libdir}/*.a
