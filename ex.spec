Summary:	OSSP ex - Exception Handling
Summary(pl):	OSSP ex - biblioteka obs³ugi wyj±tków
Name:		ex
Version:	1.0.4
Release:	0.1
License:	distributable (see README)
Group:		Libraries
Source0:	ftp://ftp.ossp.org/pkg/lib/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	9054e4325e5e182b2105566d9d02732d	
URL:		http://www.ossp.org/pkg/lib/%{name}/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
Requires(post,postun):	/sbin/ldconfig
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

#%%description -l pl

%package devel
Summary:	OSSP sio - Exception Handling - header files and development libraries
Summary(pl):	OSSP sio - biblioteka obs³ugi wyj±tków - pliki nag³ówkowe i biblioteki dla deweloperów
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description devel
OSSP ex - Exception Handling - header files and development
libraries.

%description devel -l pl
OSSP ex - biblioteka obs³ugi wyj±tków - pliki nag³ówkowe i biblioteki
dla deweloperów.

%package static
Summary:	OSSP sio - Exception Handling - static libraries
Summary(pl):	OSSP sio - biblioteka obs³ugi wyj±tków - biblioteki statyczne
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
OSSP ex - Exception Handling - static libraries.

%description static -l pl
OSSP ex - biblioteka obs³ugi wyj±tków - biblioteki statyczne.

%prep
%setup -q
%build
mv -f aclocal.m4 acinclude.m4
%{__libtoolize}
%{__aclocal}
%{__autoconf}

%configure
%{__make}
%{__make} check

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

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

%files static
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.a
