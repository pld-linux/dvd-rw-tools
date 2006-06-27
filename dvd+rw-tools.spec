Summary:	Toolchain for mastering recordable DVD media
Summary(pl):	Zestaw narzêdzi do nagrywania p³yt DVD
Name:		dvd+rw-tools
Version:	6.1
Release:	1.1
License:	GPL
Group:		Applications/Multimedia
Source0:	http://fy.chalmers.se/~appro/linux/DVD+RW/tools/%{name}-%{version}.tar.gz
# Source0-md5:	d6bad594e55a2e0d7cf76ce452fce399
Patch0:		%{name}-makefile.patch
Patch1:		%{name}-bacula.patch
Patch2:		%{name}-printf.patch
URL:		http://fy.chalmers.se/~appro/linux/DVD+RW/
BuildRequires:	libstdc++-devel
BuildRequires:	m4
Requires:	mkisofs >= 5:1.10
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Collection of tools to master DVD+RW/+R/-R/-RW media.

%description -l pl
Kolekcja narzêdzi do nagrywania p³yt DVD+RW/+R/-R/-RW.

%package btcflash
Summary:	BTC CD/DVD reader/writer firmware updater
Summary(pl):	Program do uaktualniania firmware'u czytników/nagrywarek CD/DVD BTC
Group:		Applications/Multimedia

%description btcflash
BTC CD/DVD reader/writer firmware updater.

%description btcflash -l pl
Program do uaktualniania firmware'u czytników/nagrywarek CD/DVD firmy
BTC.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__make} \
	CC="%{__cc}" \
	CXX="%{__cxx}" \
	CFLAGS="%{rpmcflags} -Wall" \
	CXXFLAGS="%{rpmcflags} -fno-exceptions -Wall"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	prefix=%{_prefix} \
	manprefix=%{_mandir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc index.html
%attr(755,root,root) %{_bindir}/*
%exclude %{_bindir}/btcflash
%{_mandir}/man1/*

%files btcflash
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/btcflash
