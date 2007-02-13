Summary:	Implementation of Conway's Life, a cellular automation
Summary(pl.UTF-8):	Implementacja gry Conwaya Life - automat komórkowy
Name:		gtklife
Version:	4.2
Release:	1
Group:		X11/Applications/Games
License:	GPL v2
Source0:	http://ironphoenix.org/tril/gtklife/%{name}-%{version}.tar.gz
# Source0-md5:	d0c0ad4d989e865a7eec6f941b0142d2
Source1:	%{name}.desktop
URL:		http://www.igs.net/~tril/gtklife/
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

%description -l pl.UTF-8
GtkLife jest implementacją grupy Conwaya - Life, automatu
komórkowego (opartego na komórkach sztucznego życia), tworzonego przez
matematyka Johna Conwaya. Charakteryzuje się wysoko zoptymalizowanym
algorytmem obliczeń generacji, wielkim universum (1 milion x 1 milion
komórek), oraz nowoczesnym, przyjaznym dla użytkowników interfejsem.
Przykładowe wzory dostępne są z opcjonalnego paska w głównym oknie.
Użytkownik może także rysować własne wzory oraz wczytywać i zachowywać
pliki w różnych popularnych formatach Life.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
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
%doc README NEWS doc/*
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/%{name}
%{_desktopdir}/%{name}.desktop
