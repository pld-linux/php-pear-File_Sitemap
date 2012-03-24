%define		status		alpha
%define		pearname	File_Sitemap
%include	/usr/lib/rpm/macros.php
Summary:	%{pearname} - create and manage sitemap files
Summary(pl.UTF-8):	%{pearname} - tworzenie i zarządzanie plikami z "mapą strony"
Name:		php-pear-%{pearname}
Version:	0.1.4
Release:	1
License:	BSD License
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{pearname}-%{version}.tgz
# Source0-md5:	aa8032c0e89bd26a963967f2c814b068
URL:		http://pear.php.net/package/File_Sitemap/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.580
Requires:	php-dom
Requires:	php-pear
Requires:	php-zlib
Suggests:	php-pear-HTTP_Request
Obsoletes:	php-pear-File_Sitemap-tests
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# exclude optional dependencies
%define		_noautoreq	pear(HTTP/Request.*)

%description
This package allow to create sitemap files used to describe your
website to help search engines indexing it. This package contains all
needed functions to create, read, save, add, modify and remove url,
compress to gzip, notify search engine and test url in the sitemap or
sitemap index.

In PEAR status of this package is: %{status}.

%description -l pl.UTF-8
Pakiet ten pozwala na tworzenie plików z mapą strony wykorzystywanych
do opisania serwisu celem ułatwienia wyszukiwarkom internetowym jego
indeksację. Pakiet ten zawiera wszelkie niezbędne funkcje do
tworzenia, odczytu, zapisu, dodawania, modyfikacji oraz usuwania
adresów, kompresji do formatu gzip, informowania wyszukiwark jak
również do testowania adresów.

Ta klasa ma w PEAR status: %{status}.

%prep
%pear_package_setup

mv .%{php_pear_dir}/data/File_Sitemap/README .

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
