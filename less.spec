Summary:	Text file browser
Name:		less
Version:	444
Release:	2
License:	GPL v2
Group:		Applications/Text
Source0:	http://www.greenwoodsoftware.com/less/%{name}-%{version}.tar.gz
# Source0-md5:	56f9f76ffe13f70155f47f6b3c87d421
Source1:	lesspipe.sh
Patch0:		%{name}-shell.patch
Patch1:		%{name}-libtinfo.patch
URL:		http://www.greenwoodsoftware.com/less/
BuildRequires:	autoconf
BuildRequires:	ncurses-devel
Requires:	file
Requires:	setup
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The less utility is a text file browser that resembles more.

%prep
%setup  -q
%patch0 -p1
%patch1 -p1

%build
chmod -R u+w .
%{__autoconf}
%configure
%{__make} \
	CPPFLAGS="-D_GNU_SOURCE -D_LARGEFILE_SOURCE -D_LARGEFILE64_SOURCE -D_FILE_OFFSET_BITS=64"

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

