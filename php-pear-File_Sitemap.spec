%include	/usr/lib/rpm/macros.php
%define		_class		File
%define		_subclass	Sitemap
%define		_status		alpha
%define		_pearname	File_Sitemap
Summary:	%{_pearname} - create and manage sitemap files
Summary(pl.UTF-8):	%{_pearname} - tworzenie i zarządzanie plikami z "mapą strony"
Name:		php-pear-%{_pearname}
Version:	0.1.2
Release:	1
License:	BSD License
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	5c8d9b71e7c7f502d309cc2c9f38df1f
URL:		http://pear.php.net/package/File_Sitemap/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# exclude optional dependencies
%define		_noautoreq	'pear(HTTP/Request.*)'

%description
This package allow to create sitemap files used to describe your
website to help search engines indexing it. This package contains all
needed functions to create, read, save, add, modify and remove url,
compress to gzip, notify search engine and test url in the sitemap or
sitemap index.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Pakiet ten pozwala na tworzenie plików z mapą strony wykorzystywanych
do opisania serwisu celem ułatwienia wyszukiwarkom internetowym jego
indeksację. Pakiet ten zawiera wszelkie niezbędne funkcje do
tworzenia, odczytu, zapisu, dodawania, modyfikacji oraz usuwania
adresów, kompresji do formatu gzip, informowania wyszukiwark jak
również do testowania adresów.

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl.UTF-8):	Testy dla PEAR::%{_pearname}
Group:		Development/Languages/PHP
AutoReq:	no
Requires:	%{name} = %{version}-%{release}
AutoProv:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl.UTF-8
Testy dla PEAR::%{_pearname}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ -f %{_docdir}/%{name}-%{version}/optional-packages.txt ]; then
	cat %{_docdir}/%{name}-%{version}/optional-packages.txt
fi

%files
%defattr(644,root,root,755)
%doc install.log optional-packages.txt docs/File_Sitemap/examples
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/File/Sitemap
%{php_pear_dir}/File/Sitemap.php

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/File_Sitemap
