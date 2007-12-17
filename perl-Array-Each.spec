%define real_name Array-Each

Summary:	Array-Each module for perl 
Name:		perl-%{real_name}
Version:	0.02
Release: %mkrel 2
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{real_name}/
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Array/%{real_name}-%{version}.tar.bz2
BuildRequires:	perl-devel
BuildArch:	noarch

%description
Array::Each - iterate over one or more arrays, returning one or more
elements from each array followed by the array index.

%prep
%setup -q -n %{real_name}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make
make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/Array/Each
%{perl_vendorlib}/Array/Each.pm
%{_mandir}/*/*




