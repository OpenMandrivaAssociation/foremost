%define Werror_cflags %nil

Summary:        Recover files based on their headers and footers
Name:           foremost
Version:        1.5.7
Release:        %mkrel 2
Epoch:          0
Group:          File tools
License:        Public Domain
URL:            http://foremost.sourceforge.net/
Source0:        http://foremost.sourceforge.net/pkg/foremost-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

%description
Foremost is a Linux program to recover files based on their headers and
footers. Foremost can work on image files, such as those generated by
dd, Safeback, Encase, etc, or directly on a drive. The headers and
footers are specified by a configuration file, so you can pick and
choose which headers you want to look for.

%prep
%setup -q
%{__perl} -pi -e 's/-O2/%{optflags}/g' Makefile
%{__perl} -pi -e 's|/usr/local/etc|%{_sysconfdir}|' config.c

%build
%make

%install
%{__rm} -rf %{buildroot}
%{__mkdir_p} %{buildroot}%{_bindir}
%{__install} -m 755 foremost %{buildroot}%{_bindir}/foremost
%{__mkdir_p} %{buildroot}%{_sysconfdir}
%{__install} -m 644 foremost.conf %{buildroot}%{_sysconfdir}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(0644,root,root,0755)
%doc CHANGES README
%attr(0755,root,root) %{_bindir}/foremost
%config(noreplace) %{_sysconfdir}/%{name}.conf


%changelog
* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 0:1.5.7-2mdv2011.0
+ Revision: 610741
- rebuild

* Thu Apr 22 2010 Sandro Cazzaniga <kharec@mandriva.org> 0:1.5.7-1mdv2010.1
+ Revision: 537781
- update to 1.5.7

* Tue May 26 2009 Frederik Himpe <fhimpe@mandriva.org> 0:1.5.6-1mdv2010.0
+ Revision: 380016
- update to new version 1.5.6

* Tue Feb 17 2009 Jérôme Soyer <saispo@mandriva.org> 0:1.5.5-1mdv2009.1
+ Revision: 341543
- New upstream release

* Sat Jul 26 2008 Erwan Velu <erwan@mandriva.org> 0:1.5.4-1mdv2009.0
+ Revision: 250079
- 1.5.4

* Tue Jul 22 2008 Thierry Vignaud <tv@mandriva.org> 0:1.5-3mdv2009.0
+ Revision: 240720
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Thu Sep 06 2007 Oden Eriksson <oeriksson@mandriva.com> 0:1.5-1mdv2008.0
+ Revision: 80908
- 1.5


* Thu Mar 08 2007 David Walluck <walluck@mandriva.org> 1.4-1mdv2007.1
+ Revision: 134923
- 1.4
- Import foremost

* Wed May 17 2006 Emmanuel Andry <eandry@mandriva.org> 0:1.2-1mdk
- 1.2

* Mon Feb 13 2006 David Walluck <walluck@mandriva.org> 0:1.1-2mdk
- fix config file location

* Mon Feb 13 2006 David Walluck <walluck@mandriva.org> 0:1.1-1mdk
- 1.1

* Fri Mar 18 2005 Oden Eriksson <oeriksson@mandrakesoft.com> 0.69-2mdk
- rebuild

