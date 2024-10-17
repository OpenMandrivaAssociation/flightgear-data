%define	oname	flightgear
# The usual payload causes timeouts in some builders
%define _binary_payload w1.zstdio

Name:		flightgear-data
Version:	2020.3.19
Release:	1
Summary:	The data for FlightGear Flight Simulator
License:	GPLv2
Group:		Games/Other
URL:		https://www.flightgear.org/
Source0:	https://sourceforge.net/projects/flightgear/files/release-2020.3/FlightGear-%{version}-data.txz
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
%setup -q -n fgdata

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
#for f in Thanks Docs/README.xmlparticles
#do
#	path=%{buildroot}%{_datadir}/%{oname}/$f
#	iconv -f iso-8859-1 -t utf-8 -o ${path}.utf8 $path
#	mv -f ${path}.utf8 ${path}
#done

%files
%{_datadir}/%{oname}
