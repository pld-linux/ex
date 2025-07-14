#
# Conditional build:
%bcond_without	static_libs	# don't build static libraries
%bcond_without	tests		# don't perform "make check"
#
Summary:	OSSP ex - Exception Handling
Summary(pl.UTF-8):	OSSP ex - biblioteka obsługi wyjątków
Name:		ex
Version:	1.0.6
Release:	0.1
Epoch:		0
License:	distributable (see README)
Group:		Libraries
Source0:	ftp://ftp.ossp.org/pkg/lib/ex/%{name}-%{version}.tar.gz
# Source0-md5:	20ff7fb1c49968c51b77e4c669a67e25
Patch0:		%{name}-libs.patch
URL:		http://www.ossp.org/pkg/lib/ex/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
OSSP ex is a small ISO-C++ style exception handling library for use in
the ISO-C language. It allows you to use the paradigm of throwing and
catching exceptions in order to reduce the amount of error handling
code without making your program less robust.

This is achieved by directly transferring exceptional return codes
(and the program control flow) from the location where the exception
is raised (throw point) to the location where it is handled (catch
point) -- usually from a deeply nested sub-routine to a parent
routine. All intermediate routines no longer have to make sure that
the exceptional return codes from sub-routines are correctly passed
back to the parent.

The OSSP ex facility also provides advanced exception handling
features like shielded and deferred exceptions. Additionally, OSSP ex
allows you to choose the used underlying machine context switching
facility and optionally support multi-threading environments by
allowing you to store the exception catching stack in a thread-safe
way.

%description -l pl.UTF-8
OSSP ex to mała biblioteka do obsługi wyjątków w stylu ISO-C++
przeznaczona do używania w języku ISO-C. Umożliwia korzystanie z
paradygmatu rzucania i wyłapywania wyjątków w celi ograniczenia
ilości kodu obsługującego błędy bez czynienia programu uboższym.

Zostało to osiągnięte poprzez bezpośrednie przesyłanie wyjątkowych
kodów powrotu (i przepływu sterowania programu) z miejsca gdzie
wystąpił wyjątek (miejsca rzucenia) do miejsca jego obsługi (miejsca
wyłapania) - zwykle z głęboko zagnieżdżonej podprocedury do procedury
nadrzędnej. Pośrednie procedury nie muszą się już upewniać, że
wyjątkowe kody powrotu z podprocedur są poprawnie przekazywane do z
powrotem do rodzica.

Ułatwienia OSSP ex dają także zaawansowane możliwości obsługi
wyjątków, takie jak osłaniane i opóźnione wyjątki. Ponadto OSSP ex
umożliwia wybór udogodnień maszyny przełączającej kontekst oraz
opcjonalną obsługę środowisk wielowątkowych poprzez umożliwienie
przechowywania stosu wyłapywania wyjątków w sposób bezpieczny dla
wątków.

%package devel
Summary:	OSSP ex - Exception Handling - header files and development libraries
Summary(pl.UTF-8):	OSSP ex - biblioteka obsługi wyjątków - pliki nagłówkowe i biblioteki dla deweloperów
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description devel
OSSP ex - Exception Handling - header files and development
libraries.

%description devel -l pl.UTF-8
OSSP ex - biblioteka obsługi wyjątków - pliki nagłówkowe i biblioteki
dla deweloperów.

%package static
Summary:	OSSP ex - Exception Handling - static libraries
Summary(pl.UTF-8):	OSSP ex - biblioteka obsługi wyjątków - biblioteki statyczne
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
OSSP ex - Exception Handling - static libraries.

%description static -l pl.UTF-8
OSSP ex - biblioteka obsługi wyjątków - biblioteki statyczne.

%prep
%setup -q
%patch -P0 -p1

%build
mv -f aclocal.m4 acinclude.m4
%{__libtoolize}
%{__aclocal}
%{__autoconf}

%configure \
	--enable-static=%{?with_static_libs:yes}%{!?with_static_libs:no}
%{__make}

%{?with_tests:%{__make} check}

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
%doc AUTHORS ChangeLog README THANKS
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*
%{_mandir}/man3/*

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.a
%endif
