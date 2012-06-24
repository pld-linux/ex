#
# Conditional build:
%bcond_without  static_libs # don't build static libraries
%bcond_without	tests # don't perform "make check"
#
Summary:	OSSP ex - Exception Handling
Summary(pl):	OSSP ex - biblioteka obs�ugi wyj�tk�w
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
OSSP ex to ma�a biblioteka do obs�ugi wyj�tk�w w stylu ISO-C++
przeznaczona do u�ywania w j�zyku ISO-C. Umo�liwia korzystanie z
paradygmatu rzucania i wy�apywania wyj�tk�w w celi ograniczenia
ilo�ci kodu obs�uguj�cego b��dy bez czynienia programu ubo�szym.

Zosta�o to osi�gni�te poprzez bezpo�rednie przesy�anie wyj�tkowych
kod�w powrotu (i przep�ywu sterowania programu) z miejsca gdzie
wyst�pi� wyj�tek (miejsca rzucenia) do miejsca jego obs�ugi (miejsca
wy�apania) - zwykle z g��boko zagnie�d�onej podprocedury do procedury
nadrz�dnej. Po�rednie procedury nie musz� si� ju� upewnia�, �e
wyj�tkowe kody powrotu z podprocedur s� poprawnie przekazywane do z
powrotem do rodzica.

U�atwienia OSSP ex daj� tak�e zaawansowane mo�liwo�ci obs�ugi
wyj�tk�w, takie jak os�aniane i op�nione wyj�tki. Ponadto OSSP ex
umo�liwia wyb�r udogodnie� maszyny prze��czaj�cej kontekst oraz
opcjonaln� obs�ug� �rodowisk wielow�tkowych poprzez umo�liwienie
przechowywania stosu wy�apywania wyj�tk�w w spos�b bezpieczny dla
w�tk�w.

%package devel
Summary:	OSSP ex - Exception Handling - header files and development libraries
Summary(pl):	OSSP ex - biblioteka obs�ugi wyj�tk�w - pliki nag��wkowe i biblioteki dla deweloper�w
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description devel
OSSP ex - Exception Handling - header files and development
libraries.

%description devel -l pl
OSSP ex - biblioteka obs�ugi wyj�tk�w - pliki nag��wkowe i biblioteki
dla deweloper�w.

%package static
Summary:	OSSP ex - Exception Handling - static libraries
Summary(pl):	OSSP ex - biblioteka obs�ugi wyj�tk�w - biblioteki statyczne
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
OSSP ex - Exception Handling - static libraries.

%description static -l pl
OSSP ex - biblioteka obs�ugi wyj�tk�w - biblioteki statyczne.

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
