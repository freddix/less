Summary:	Text file browser
Name:		less
Version:	458
Release:	1
License:	GPL v2
Group:		Applications/Text
Source0:	http://www.greenwoodsoftware.com/less/%{name}-%{version}.tar.gz
# Source0-md5:	935b38aa2e73c888c210dedf8fd94f49
Source1:	lesspipe.sh
URL:		http://www.greenwoodsoftware.com/less/
BuildRequires:	autoconf
BuildRequires:	ncurses-devel
BuildRequires:	pcre-devel
Requires:	file
Requires:	setup
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The less utility is a text file browser that resembles more.

%prep
%setup  -q

%build
chmod -R u+w .
%{__autoconf}
%configure \
	--with-regex=pcre
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_mandir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -p %{SOURCE1} $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README NEWS
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*

