Summary:	A library for handling encrypted dvds
Summary(pl):	Biblioteka do obsЁugi zakodowanych DVD
Name:		a52dec
Version:	0.7.2
Release:	1
License:	GPL
Group:		X11/Applications/Multimedia
Group(de):	X11/Applikationen/Multimedia
Group(pl):	X11/Aplikacje/Multimedia
Source0:	http://liba52.sourceforge.net/files/%{name}-%{version}.tar.gz
URL:		http://www.dtek.chalmers.se/~dvd/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
liba52 is a free library for decoding ATSC A/52 streams. It is
released under the terms of the GPL license. The A/52 standard is used
in a variety of applications, including digital television and DVD. It
is also known as AC-3.

%description -l pl
liba52 jest wolnodostЙpn╠ (na licencji GPL) bibliotek╠ do dekodowania
strumieni ATSC A/52. Standard A/52 jest u©ywany w wielu
zastosowaniach, w tym cyfrowej telewizji i DVD. Jest znany tak©e jako
AC-3.

%package libs
Summary:	Biblioteki a52dec
Summary(pl):	Pakiet z bibliotekami a52dec
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	Разработка/Библиотеки
Group(uk):	Розробка/Б╕бл╕отеки

%description libs
%{name}-devel includes development files for %{name}.

%description libs -l pl
Pliki dla programistСw a52dec.

%package libs-devel
Summary:	%{name} development package
Summary(pl):	Pakiet %{name} dla programistСw
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	Разработка/Библиотеки
Group(uk):	Розробка/Б╕бл╕отеки
Requires:	%{name}-libs = %{version}-%{release}

%description libs-devel
%{name}-devel includes development files for %{name}.

%description libs-devel -l pl
Pliki dla programistСw a52dec.

%package libs-static
Summary:	Biblioteki a52dec
Summary(pl):	Pakiet z bibliotekami a52dec
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	Разработка/Библиотеки
Group(uk):	Розробка/Б╕бл╕отеки

%description libs-static
%{name}-devel includes development files for %{name}.

%description libs-static -l pl
Pliki dla programistСw a52dec.

%prep
%setup -q

%build
libtoolize --copy --force
aclocal
autoconf
automake -a -c
%configure --enable-shared
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf AUTHORS NEWS README TODO

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc {AUTHORS,NEWS,README,TODO}.gz
%attr(755,root,root) %{_bindir}/*
%{_mandir}/*

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
%attr(755,root,root) %{_libdir}/*.la
