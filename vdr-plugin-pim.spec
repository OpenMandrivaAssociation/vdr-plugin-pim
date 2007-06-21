
%define plugin	pim
%define name	vdr-plugin-%plugin
%define version	0.0.6
%define rel	9

Summary:	VDR plugin: Simple Personal Information Manager
Name:		%name
Version:	%version
Release:	%mkrel %rel
Group:		Video
License:	GPL
URL:		http://pim.vdr-developer.org/
Source:		http://pim.vdr-developer.org/source/vdr-%plugin-%version.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	vdr-devel >= 1.4.1-6
Requires:	vdr-abi = %vdr_abi

%description
This is a plugin for VDR to display a calendar in which you can
store events.

%prep
%setup -q -n %plugin-%version

%build
%vdr_plugin_build

%install
rm -rf %{buildroot}
%vdr_plugin_install

%clean
rm -rf %{buildroot}

%post
%vdr_plugin_post %plugin

%postun
%vdr_plugin_postun %plugin

%files -f %plugin.vdr
%defattr(-,root,root)
%doc README HISTORY


