#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Check
%define	pnam	ISA
Summary:	Check::ISA - DWIM, correct checking of an object's class
Summary(pl.UTF-8):	Check::ISA - DWIM, poprawne sprawdzanie klas obiektów
Name:		perl-Check-ISA
Version:	0.04
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://search.cpan.org/CPAN/authors/id/N/NU/NUFFIN/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	7d118aadd4069b4287f309482776a2bd
URL:		http://search.cpan.org/dist/Check-ISA/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Sub-Exporter
BuildRequires:	perl-Test-use-ok
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides several functions to assist in testing whether a
value is an object, and if so asking about its class.

%description -l pl.UTF-8
Moduł ten dostarcza funkcje do wparcia sprawdzania czy wartość jest
obiektem, i jeśli jest, do odpytania o jego klasę.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%dir %{perl_vendorlib}/Check
%{perl_vendorlib}/Check/*.pm
%{_mandir}/man3/*
