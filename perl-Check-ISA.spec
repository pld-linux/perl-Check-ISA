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
Version:	0.09
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/M/MA/MANWAR/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	d86bd85a04cdc0976841fdc2c6fa19b5
URL:		http://search.cpan.org/dist/Check-ISA/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Sub-Exporter
BuildRequires:	perl-Test-Simple >= 1.001014
#BuildRequires:	perl-Test-use-ok  # included in Test::Simple >= 1.001014
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides several functions to assist in testing whether a
value is an object, and if so asking about its class.

%description -l pl.UTF-8
Moduł ten dostarcza funkcje wspierające sprawdzanie, czy wartość jest
obiektem, i, jeśli jest, do zapytania o jego klasę.

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
%doc Changes README
%dir %{perl_vendorlib}/Check
%{perl_vendorlib}/Check/ISA.pm
%{_mandir}/man3/Check::ISA.3pm*
