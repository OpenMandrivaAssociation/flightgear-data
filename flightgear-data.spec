%define	oname	flightgear

Name:		flightgear-data
Version:	2.8.0
Release:	%mkrel 1
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

%install
rm -rf %{buildroot}
install -d -m 0755 %{buildroot}%{_datadir}/%{oname}/
cp -a * %{buildroot}%{_datadir}/%{oname}/

# cleanup temporary files and fix permissions
find %{buildroot}%{_datadir}/%{oname} -name '*#*' -exec %__rm {} \;
find %{buildroot}%{_datadir}/%{oname} -type f -exec %__chmod 644 {} \;

# fix wrong eol encoding on some doc files
for f in Docs/FGShortRef.css Docs/README.kln89.html Docs/FGShortRef.html \
	Docs/README.submodels Docs/README.yasim Docs/README.xmlparticles
do
	%__sed -i 's/\r//' %{buildroot}%{_datadir}/%{oname}/$f
done

# fix files not in utf-8
for f in Thanks Docs/README.xmlparticles
do
	path=%{buildroot}%{_datadir}/%{oname}/$f
	iconv -f iso-8859-1 -t utf-8 -o ${path}.utf8 $path
	%__mv -f ${path}.utf8 ${path}
done

%clean
rm -rf %{buildroot}

%files
%doc AUTHORS COPYING NEWS README Thanks Docs
%{_datadir}/%{oname}

%changelog
* Mon Aug 20 2012 Anton Chernyshov <ach@rosalab.ru> 2.8.0-1
- New upstream release - 2.8.0

* Fri Feb 24 2012 Andrey Bondrov <abondrov@mandriva.org> 2.6.0-1
+ Revision: 780078
- New version 2.6.0, place game data in /usr/share/flightgear

* Sun Sep 18 2011 Andrey Bondrov <abondrov@mandriva.org> 2.4.0-1
+ Revision: 700213
- New version: 2.4.0

* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 2.0.0-2mdv2011.0
+ Revision: 610712
- rebuild

* Sun Mar 07 2010 Frederik Himpe <fhimpe@mandriva.org> 2.0.0-1mdv2010.1
+ Revision: 515584
- Update to new version 2.0.0

* Thu Sep 10 2009 Thierry Vignaud <tv@mandriva.org> 1.9.0-2mdv2010.0
+ Revision: 437557
- rebuild

* Wed Mar 04 2009 Frederik Himpe <fhimpe@mandriva.org> 1.9.0-1mdv2009.1
+ Revision: 348704
- Update to new version 1.9.0
- Rename to flightgear-data
- compress upstream tarball with xz
- Use similar %%install section as Fedora

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 1.0.0-4mdv2009.0
+ Revision: 267915
+ rebuild (emptylog)

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 1.0.0-3mdv2009.0
+ Revision: 245200
- rebuild
- fix no-buildroot-tag

* Sat Dec 22 2007 Andreas Hasenack <andreas@mandriva.com> 1.0.0-1mdv2008.1
+ Revision: 136836
- updated base scenery to version 1.0.0 via patch file

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

