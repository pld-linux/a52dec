Summary:	A library for handling encrypted dvds.
Name:		a52dec
Version:	0.7.1b
Release:	3
License:	GPL
Group:		X11/Applications/Multimedia
Group(de):	X11/Applikationen/Multimedia
Group(pl):	X11/Aplikacje/Multimedia
Source0:	http://liba52.sourceforge.net/files/%{name}-%{version}.tar.gz
URL:		http://www.dtek.chalmers.se/~dvd/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
liba52 is a free library for decoding ATSC A/52 streams. It is
released under the terms of the GPL license. The A/52 standard is used
in a variety of applications, including digital television and DVD. It
is also known as AC-3.

%package devel
Summary:	%{name} development package
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	Разработка/Библиотеки
Group(uk):	Розробка/Б╕бл╕отеки
Requires:	%{name} = %{version}-%{release}

%description devel
%{name}-devel includes development files for %{name}

%prep
%setup -q

%build
libtoolize --copy --force
aclocal
autoconf
automake -a -c
%configure
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

%files devel
%defattr(644,root,root,755)
%{_includedir}/*
%{_libdir}/*.a
%attr(755,root,root) %{_libdir}/*.la
