Summary:	Implementation of Conway's Life, a cellular automation
Summary(pl):	Implementacja gry Conway-a Life, automat komórkowy
Name:		gtklife
Version:	4.1
Release:	1
Group:		X11/Applications/Games
License:	GPL
Url:		http://www.igs.net/~tril/gtklife/
Source0:	http://www.igs.net/~tril/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	e5fc1290429aa58ff9ba1a6da502f142
Source1:	%{name}.desktop
BuildRequires:	glib-devel
BuildRequires:	gtk+-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GtkLife is an implementation of Conway's Life, a cellular automaton
(grid-based artificial life) developed by the mathematician John
Conway. It features a highly optimized algorithm for computing
generations, a giant universe (1 million x 1 million cells), and a
modern, user-friendly interface. Example patterns are available from
an optional sidebar on the main window. The user can also draw their
own patterns, and load and save files in a number of popular Life
formats.

%description
GtkLife jest implementacj± grupy Conwaya - Life, automatu
komórkowego(opartego na gridach sztucznego ¿ycia), tworzonego przez
matematyka Johna Conwaya. Charakteryzuje siê wysoko zoptymalizowanym
algorytmem obliczeñ generacji, wielkim universum(1 milion x 1 milion
komórek), oraz nowoczesnym, przyjaznym dla u¿ytkowników interfejsem.
Przyk³adowe wzory dostêpne s± z opcjonalnego paska w g³ównym oknie.
U¿ytkownik mo¿e tak¿e rysowaæ w³asne wzory oraz wczytywaæ i zachowywaæ
pliki w ró¿nych popularnych formatach Life.

%prep
%setup -q

%build
%{__make} \
	CFLAGS="%{rpmcflags}" \
	PREFIX=%{_prefix} \
	BINDIR=%{_bindir} \
	DOCDIR=%{_docdir}/%{name}-%{version} \
	DATADIR=%{_datadir}/%{name}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	PREFIX=$RPM_BUILD_ROOT%{_prefix} \
	BINDIR=$RPM_BUILD_ROOT%{_bindir} \
	DOCDIR=$RPM_BUILD_ROOT%{_docdir}/%{name}-%{version} \
	DATADIR=$RPM_BUILD_ROOT%{_datadir}/%{name}

install -D %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}/%{name}.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/%{name}
%{_desktopdir}/%{name}.desktop
%doc README NEWS ChangeLog doc/*
