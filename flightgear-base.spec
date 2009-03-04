%define	name	flightgear-base
%define	oname	FlightGear
%define	version	1.0.0
%define release	%mkrel 4
%define	Summary	The FlightGear Flight Simulator

Summary:	%{Summary}
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Games/Other
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Source0:	ftp://ftp.flightgear.org/pub/fgfs/Shared/fgfs-base-0.9.10.tar.bz2
Source1:	ftp://ftp.planetmirror.com/pub/fgfs/Shared/fgfs-base-0.9.10-to-1.0.0.tar.bz2
BuildArch:	noarch
URL:		http://www.flightgear.org/
Conflicts:	flightgear < 0.9.10-4

%description
The Flight Gear project is working to create a sophisticated flight simulator
framework for the development and pursuit of interesting flight simulator
ideas. We are developing a solid basic sim that can be expanded and improved
upon by anyone interested in contributing.

This package contains the base data files.

%prep
%setup -q -c -T -n %{name}-%{version} 

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_gamesdatadir}/%{oname}
tar xjf %{SOURCE0} -C $RPM_BUILD_ROOT%{_gamesdatadir}/%{oname}
tar xjf %{SOURCE1} -C $RPM_BUILD_ROOT%{_gamesdatadir}/%{oname}
cd $RPM_BUILD_ROOT%{_gamesdatadir}/%{oname}
./finish.sh
cd -

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_gamesdatadir}/%{oname}


