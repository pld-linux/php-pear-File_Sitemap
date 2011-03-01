%include	/usr/lib/rpm/macros.php
%define		_class		File
%define		_subclass	Sitemap
%define		_status		alpha
%define		_pearname	File_Sitemap
Summary:	%{_pearname} - create and manage sitemap files
Summary(pl.UTF-8):	%{_pearname} - tworzenie i zarządzanie plikami z "mapą strony"
Name:		php-pear-%{_pearname}
Version:	0.1.3
Release:	3
License:	BSD License
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	3bed2666446710966cda547d5140aad0
URL:		http://pear.php.net/package/File_Sitemap/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-dom
Requires:	php-pear
Requires:	php-zlib
Suggests:	php-pear-HTTP_Request
Obsoletes:	php-pear-File_Sitemap-tests
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
