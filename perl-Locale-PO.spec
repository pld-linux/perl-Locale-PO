#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	Locale
%define		pnam	PO
Summary:	Locale::PO - Perl module for manipulating .po entries from GNU gettext
Summary(pl.UTF-8):	Locale::PO - moduł Perla do operacji na wpisach .po z GNU gettexta
Name:		perl-Locale-PO
Version:	0.27
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Locale/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	81545852a510f8e5332ea1e9d6b64a39
URL:		http://search.cpan.org/dist/Locale-PO/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-File-Slurp
BuildRequires:	perl-Test-Simple
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module simplifies management of GNU gettext .po files and is an
alternative to using emacs po-mode. It provides an object-oriented
interface in which each entry in a .po file is a Locale::PO object.

%description -l pl.UTF-8
Ten moduł upraszcza zarządzanie plikami .po GNU gettexta i jest
alternatywą dla trybu po emacsa. Udostępnia zorientowany obiektowo
interfejs, w którym każdy wpis pliku .po jest obiektem Locale::PO.

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
%{perl_vendorlib}/Locale/PO.pm
%{_mandir}/man3/Locale::PO.3pm*
