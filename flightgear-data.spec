%define	name	flightgear-data
%define	oname	FlightGear
%define	version	2.0.0
%define release	%mkrel 1
%define	Summary	The FlightGear Flight Simulator

Summary:	%{Summary}
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Games/Other
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Source0:	ftp://ftp.linux.kiev.ua/pub/mirrors/ftp.flightgear.org/flightgear/Shared/FlightGear-data-%{version}.tar.xz
BuildArch:	noarch
URL:		http://www.flightgear.org/
Conflicts:	flightgear < 0.9.10-4
Obsoletes:	flightgear-base
Provides:	flightgear-base = %{version}-%{release}

%description
The Flight Gear project is working to create a sophisticated flight simulator
framework for the development and pursuit of interesting flight simulator
ideas. We are developing a solid basic sim that can be expanded and improved
upon by anyone interested in contributing.

This package contains the base data files.

%prep

%build

%install
rm -rf %{buildroot}
install -d %{buildroot}%{_gamesdatadir}/FlightGear
tar xf %{SOURCE0} --strip-components 1 \
	-C %{buildroot}/%{_gamesdatadir}/FlightGear

# cleanup temporary files and fix permissions
find %{buildroot}/%{_gamesdatadir}/FlightGear -name '*#*' -exec rm {} \;
find %{buildroot}/%{_gamesdatadir}/FlightGear -type f -exec chmod 644 {} \;

# fix wrong eol encoding on some doc files
for f in Docs/FGShortRef.css Docs/README.kln89.html Docs/FGShortRef.html \
	Docs/README.submodels Docs/README.yasim Docs/README.xmlparticles
do
	sed -i 's/\r//' %{buildroot}/%{_gamesdatadir}/FlightGear/$f
done

# remove hidden dirs
for d in Aircraft/c172/Panels/Textures/.xvpics \
	Textures/Runway/.xvpics
do
	rm -rf %{buildroot}/%{_gamesdatadir}/FlightGear/$d
done

# fix files not in utf-8
for f in Thanks Docs/README.xmlparticles
do
	path=%{buildroot}/%{_gamesdatadir}/FlightGear/$f
	iconv -f iso-8859-1 -t utf-8 -o ${path}.utf8 $path
	mv -f ${path}.utf8 ${path}
done

# put documentation and license in the proper location
mkdir -p %{buildroot}/%{_docdir}/%{name}
for f in COPYING AUTHORS NEWS README Thanks Docs
do
	mv %{buildroot}/%{_gamesdatadir}/FlightGear/$f \
		%{buildroot}/%{_docdir}/%{name}
done

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_gamesdatadir}/%{oname}
%{_docdir}/%{name}/COPYING
%{_docdir}/%{name}/AUTHORS
%{_docdir}/%{name}/NEWS
%{_docdir}/%{name}/README
%{_docdir}/%{name}/Thanks
%{_docdir}/%{name}/Docs

