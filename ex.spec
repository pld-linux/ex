#
# Conditional build:
%bcond_without  static_libs # don't build static libraries
%bcond_without	tests # don't perform "make check"
#
Summary:	OSSP ex - Exception Handling
Summary(pl):	OSSP ex - biblioteka obs³ugi wyj±tków
Name:		ex
Version:	1.0.5
Release:	0.1
Epoch:		0
License:	distributable (see README)
Group:		Libraries
Source0:	ftp://ftp.ossp.org/pkg/lib/ex/%{name}-%{version}.tar.gz
# Source0-md5:	419f0915cb578f9eb3bfc483bc49f066
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

%description -l pl
OSSP ex to ma³a biblioteka do obs³ugi wyj±tków w stylu ISO-C++
przeznaczona do u¿ywania w jêzyku ISO-C. Umo¿liwia korzystanie z
paradygmatu rzucania i wy³apywania wyj±tków w celi ograniczenia
ilo¶ci kodu obs³uguj±cego b³êdy bez czynienia programu ubo¿szym.

Zosta³o to osi±gniête poprzez bezpo¶rednie przesy³anie wyj±tkowych
kodów powrotu (i przep³ywu sterowania programu) z miejsca gdzie
wyst±pi³ wyj±tek (miejsca rzucenia) do miejsca jego obs³ugi (miejsca
wy³apania) - zwykle z g³êboko zagnie¿d¿onej podprocedury do procedury
nadrzêdnej. Po¶rednie procedury nie musz± siê ju¿ upewniaæ, ¿e
wyj±tkowe kody powrotu z podprocedur s± poprawnie przekazywane do z
powrotem do rodzica.

U³atwienia OSSP ex daj± tak¿e zaawansowane mo¿liwo¶ci obs³ugi
wyj±tków, takie jak os³aniane i opó¼nione wyj±tki. Ponadto OSSP ex
umo¿liwia wybór udogodnieñ maszyny prze³±czaj±cej kontekst oraz
opcjonaln± obs³ugê ¶rodowisk wielow±tkowych poprzez umo¿liwienie
przechowywania stosu wy³apywania wyj±tków w sposób bezpieczny dla
w±tków.

%package devel
Summary:	OSSP ex - Exception Handling - header files and development libraries
Summary(pl):	OSSP ex - biblioteka obs³ugi wyj±tków - pliki nag³ówkowe i biblioteki dla deweloperów
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description devel
OSSP ex - Exception Handling - header files and development
libraries.

%description devel -l pl
OSSP ex - biblioteka obs³ugi wyj±tków - pliki nag³ówkowe i biblioteki
dla deweloperów.

%package static
Summary:	OSSP ex - Exception Handling - static libraries
Summary(pl):	OSSP ex - biblioteka obs³ugi wyj±tków - biblioteki statyczne
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
OSSP ex - Exception Handling - static libraries.

%description static -l pl
OSSP ex - biblioteka obs³ugi wyj±tków - biblioteki statyczne.

%prep
%setup -q
%patch0 -p1

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
