%define	oname	flightgear

Name:		flightgear-data
Version:	2.12.1
Release:	1
Summary:	The data for FlightGear Flight Simulator
License:	GPLv2
Group:		Games/Other
URL:		http://www.flightgear.org/
Source0:	ftp://ftp.linux.kiev.ua/pub/mirrors/ftp.flightgear.org/flightgear/Shared/FlightGear-data-%{version}.tar.bz2

BuildArch:	noarch

Conflicts:	flightgear < 0.9.10-4
Provides:	flightgear-base = %{version}-%{release}

%description
The Flight Gear project is working to create a sophisticated flight simulator
framework for the development and pursuit of interesting flight simulator
ideas. We are developing a solid basic sim that can be expanded and improved
upon by anyone interested in contributing.

This package contains the base data files.

%prep
%setup -q -n data

%build
# Nothing

%install
install -d -m 0755 %{buildroot}%{_datadir}/%{oname}/
cp -a * %{buildroot}%{_datadir}/%{oname}/

# cleanup temporary files and fix permissions
find %{buildroot}%{_datadir}/%{oname} -name '*#*' -exec rm {} \;
find %{buildroot}%{_datadir}/%{oname} -type f -exec chmod 644 {} \;

# fix wrong eol encoding on some doc files
for f in Docs/FGShortRef.css Docs/README.kln89.html Docs/FGShortRef.html \
	Docs/README.submodels Docs/README.yasim Docs/README.xmlparticles
do
	sed -i 's/\r//' %{buildroot}%{_datadir}/%{oname}/$f
done

# fix files not in utf-8
for f in Thanks Docs/README.xmlparticles
do
	path=%{buildroot}%{_datadir}/%{oname}/$f
	iconv -f iso-8859-1 -t utf-8 -o ${path}.utf8 $path
	mv -f ${path}.utf8 ${path}
done

%files
%doc AUTHORS COPYING NEWS README Thanks Docs
%{_datadir}/%{oname}

