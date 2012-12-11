%define upstream_name    Array-Each
%define upstream_version 0.02

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Array-Each module for perl 
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Array/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildArch:	noarch


%description
Array::Each - iterate over one or more arrays, returning one or more
elements from each array followed by the array index.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make
make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/Array/Each
%{perl_vendorlib}/Array/Each.pm
%{_mandir}/*/*


%changelog
* Sat May 28 2011 Funda Wang <fwang@mandriva.org> 0.20.0-2mdv2011.0
+ Revision: 680476
- mass rebuild

* Sat Aug 01 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.20.0-1mdv2011.0
+ Revision: 406835
- rebuild using %%perl_convert_version

* Wed Jul 30 2008 Thierry Vignaud <tv@mandriva.org> 0.02-5mdv2009.0
+ Revision: 255339
- rebuild

* Sat Dec 22 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.02-3mdv2008.1
+ Revision: 136886
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Fri Oct 27 2006 Nicolas LÃ©cureuil <neoclust@mandriva.org> 0.02-2mdv2007.0
+ Revision: 73285
- import perl-Array-Each-0.02-2mdk

* Fri Apr 28 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.02-2mdk
- Fix SPEC according to Perl Policy
	- Source URL
- use mkrel

* Thu Jul 14 2005 Oden Eriksson <oeriksson@mandriva.com> 0.02-1mdk
- initial Mandriva package

