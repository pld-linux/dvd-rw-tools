Summary:	Toolchain for mastering recordable DVD media
Summary(pl):	Zestaw narzêdzi do nagrywania p³yt DVD
Name:		dvd+rw-tools
Version:	5.16.4.8.5
Release:	0.1
License:	GPL
Group:		Applications/Multimedia
Source0:	http://fy.chalmers.se/~appro/linux/DVD+RW/tools/%{name}-%{version}.tar.gz
# Source0-md5:	3b58b5e48963f7232997b419d6302229
Patch0:		%{name}-makefile.patch
URL:		http://fy.chalmers.se/~appro/linux/DVD+RW/
BuildRequires:	libstdc++-devel
BuildRequires:	glibc-kernel-headers
Requires:	cdrtools-mkisofs >= 1.10
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Collection of tools to master DVD+RW/+R/-R/-RW media.

%description -l pl
Kolekcja narzêdzi do nagrywania p³yt DVD+RW/+R/-R/-RW.

%prep
%setup -q
%patch0 -p1

%build
%{__make}

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
%doc %{_mandir}/man1/*
