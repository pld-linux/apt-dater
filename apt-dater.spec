Summary:	Terminal-based remote package update manager
Name:		apt-dater
Version:	0.9.0
Release:	1
License:	GPL v2
Group:		Applications/System
Source0:	http://downloads.sourceforge.net/apt-dater/%{name}-%{version}.tar.gz
# Source0-md5:	a8ac240ddfb7d4c500505f9d5d821185
URL:		http://www.ibh.de/apt-dater/
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel
BuildRequires:	libxml2-devel
BuildRequires:	ncurses-devel
BuildRequires:	perl-base
BuildRequires:	pkgconfig
BuildRequires:	popt-devel
BuildRequires:	screen
BuildRequires:	sed >= 4.0
BuildRequires:	tcl-devel
Requires:	screen
Requires:	tcl
Suggests:	%{name}-host
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
apt-dater provides an easy to use ncurses frontend for managing
package updates on a large number of remote hosts using SSH. It
supports Debian-based managed hosts as well as OpenSUSE and CentOS
based systems.

%package host
Summary:	host helper application for apt-dater
Group:		Applications/System
Requires:	lsb-release
Requires:	openssh-server
Suggests:	imvirt
Suggests:	perl-imvirt
Suggests:	sudo
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description host
apt-dater provides an easy to use ncurses frontend for managing
package updates on a large number of remote hosts using SSH. It
supports Debian-based managed hosts as well as OpenSUSE and CentOS
based systems.

This package provides the helper application for apt-dater. It has to
be installed on every apt-dater managed host.

%prep
%setup -q

sed -i "s/manhdir = .*$/manhdir = @docdir@/" man/Makefile.in

%build
%configure \
	--libexec=%{_libexecdir}/apt-dater \
	--enable-tclfilter \
	--enable-xmlreport \
	--enable-autoref \
	--enable-history \
	--enable-debug \

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -p clients/rpm/apt-dater-host $RPM_BUILD_ROOT%{_bindir}

%find_lang %{name}

%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README* TODO man/apt-dater.conf.html man/apt-dater.html
%attr(755,root,root) %{_bindir}/apt-dater
%dir %{_libdir}/%{name}
%attr(755,root,root) %{_libdir}/%{name}/cmd
%{_mandir}/man5/apt-dater.conf.5*
%{_mandir}/man8/apt-dater.8*

%files host
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/apt-dater-host
%{_mandir}/man1/apt-dater-host.1*
