Summary:	A library for handling encrypted dvds
Summary(pl):	Biblioteka do obs³ugi zakodowanych DVD
Name:		a52dec
Version:	0.7.4
Release:	1
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://liba52.sourceforge.net/files/%{name}-%{version}.tar.gz
URL:		http://liba52.sourceforge.net
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man
%define		_libdir		/usr/lib
%define		_includedir	/usr/include

%description
liba52 is a free library for decoding ATSC A/52 streams. It is
released under the terms of the GPL license. The A/52 standard is used
in a variety of applications, including digital television and DVD. It
is also known as AC-3.

%description -l pl
liba52 jest wolnodostêpn± (na licencji GPL) bibliotek± do dekodowania
strumieni ATSC A/52. Standard A/52 jest u¿ywany w wielu
zastosowaniach, w tym cyfrowej telewizji i DVD. Jest znany tak¿e jako
AC-3.

%package libs
Summary:	Biblioteki a52dec
Summary(pl):	Pakiet z bibliotekami a52dec
Group:		Development/Libraries

%description libs
%{name}-devel includes development files for %{name}.

%description libs -l pl
Pliki dla programistów a52dec.

%package libs-devel
Summary:	%{name} development package
Summary(pl):	Pakiet %{name} dla programistów
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description libs-devel
%{name}-devel includes development files for %{name}.

%description libs-devel -l pl
Pliki dla programistów a52dec.

%package libs-static
Summary:	Biblioteki a52dec
Summary(pl):	Pakiet z bibliotekami a52dec
Group:		Development/Libraries

%description libs-static
%{name}-devel includes development files for %{name}.

%description libs-static -l pl
Pliki dla programistów a52dec.

%prep
%setup -q

%build
rm -f missing
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--enable-shared
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

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
%attr(755,root,root) %{_libdir}/*.so.*

%files libs-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/*.so
%{_includedir}/*

%files libs-static
%defattr(644,root,root,755)
%{_libdir}/*.a
%{_libdir}/*.la
