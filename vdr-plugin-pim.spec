%define plugin	pim

Summary:	VDR plugin: Simple Personal Information Manager
Name:		vdr-plugin-%plugin
Version:	0.0.8
Release:	6
Group:		Video
License:	GPL
URL:		http://pim.vdr-developer.org/
Source:		http://pim.vdr-developer.org/source/vdr-%plugin-%version.tgz
Patch0:		pim-0.0.8-i18n-1.6.patch
Patch1:		pim-format-string.patch
BuildRequires:	vdr-devel >= 1.6.0
Requires:	vdr-abi = %vdr_abi

%description
This is a plugin for VDR to display a calendar in which you can
store events.

%prep
%setup -q -n %plugin-%version
%patch0 -p1
%patch1 -p1
%vdr_plugin_prep

%build
%vdr_plugin_build

%install
%vdr_plugin_install

%files -f %plugin.vdr
%defattr(-,root,root)
%doc README HISTORY




%changelog
* Tue Jul 28 2009 Anssi Hannula <anssi@mandriva.org> 0.0.8-4mdv2010.0
+ Revision: 401088
- rebuild for new VDR

* Sat Mar 21 2009 Anssi Hannula <anssi@mandriva.org> 0.0.8-3mdv2009.1
+ Revision: 359749
- fix format strings (format-string.patch)
- rebuild for new vdr

* Mon Apr 28 2008 Anssi Hannula <anssi@mandriva.org> 0.0.8-2mdv2009.0
+ Revision: 197961
- rebuild for new vdr

* Sat Apr 26 2008 Anssi Hannula <anssi@mandriva.org> 0.0.8-1mdv2009.0
+ Revision: 197704
- new version
- add vdr_plugin_prep
- bump buildrequires on vdr-devel
- adapt to gettext i18n of VDR 1.6 (semi-automatic patch)

* Fri Jan 04 2008 Anssi Hannula <anssi@mandriva.org> 0.0.6-12mdv2008.1
+ Revision: 145170
- rebuild for new vdr

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Oct 29 2007 Anssi Hannula <anssi@mandriva.org> 0.0.6-11mdv2008.1
+ Revision: 103179
- rebuild for new vdr

* Sun Jul 08 2007 Anssi Hannula <anssi@mandriva.org> 0.0.6-10mdv2008.0
+ Revision: 50029
- rebuild for new vdr

* Thu Jun 21 2007 Anssi Hannula <anssi@mandriva.org> 0.0.6-9mdv2008.0
+ Revision: 42115
- rebuild for new vdr

* Sat May 05 2007 Anssi Hannula <anssi@mandriva.org> 0.0.6-8mdv2008.0
+ Revision: 22767
- rebuild for new vdr


* Tue Dec 05 2006 Anssi Hannula <anssi@mandriva.org> 0.0.6-7mdv2007.0
+ Revision: 90958
- rebuild for new vdr

* Tue Oct 31 2006 Anssi Hannula <anssi@mandriva.org> 0.0.6-6mdv2007.1
+ Revision: 74068
- rebuild for new vdr
- Import vdr-plugin-pim

* Thu Sep 07 2006 Anssi Hannula <anssi@mandriva.org> 0.0.6-5mdv2007.0
- rebuild for new vdr

* Thu Aug 24 2006 Anssi Hannula <anssi@mandriva.org> 0.0.6-4mdv2007.0
- stricter abi requires

* Mon Aug 07 2006 Anssi Hannula <anssi@mandriva.org> 0.0.6-3mdv2007.0
- rebuild for new vdr

* Wed Jul 26 2006 Anssi Hannula <anssi@mandriva.org> 0.0.6-2mdv2007.0
- rebuild for new vdr

* Tue Jul 18 2006 Anssi Hannula <anssi@mandriva.org> 0.0.6-1mdv2007.0
- initial Mandriva release

