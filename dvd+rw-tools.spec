Summary:	Toolchain for mastering recordable DVD media
Summary(pl):	Zestaw narzêdzi do nagrywania p³yt DVD
Name:		dvd+rw-tools
Version:	6.0
Release:	1
License:	GPL
Group:		Applications/Multimedia
Source0:	http://fy.chalmers.se/~appro/linux/DVD+RW/tools/%{name}-%{version}.tar.gz
# Source0-md5:	0c2b8afa027b93b84005ccd1c06fbd54
Patch0:		%{name}-makefile.patch
Patch1:		%{name}-bacula.patch
Patch2:		%{name}-gcc4.patch
URL:		http://fy.chalmers.se/~appro/linux/DVD+RW/
BuildRequires:	libstdc++-devel
BuildRequires:	m4
Requires:	cdrtools-mkisofs >= 1.10
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Collection of tools to master DVD+RW/+R/-R/-RW media.

%description -l pl
Kolekcja narzêdzi do nagrywania p³yt DVD+RW/+R/-R/-RW.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__make} \
	CC="%{__cc}" \
	CXX="%{__cxx}" \
	CFLAGS="%{rpmcflags}" \
	CXXFLAGS="%{rpmcflags} -fno-exceptions"

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
%{_mandir}/man1/*
