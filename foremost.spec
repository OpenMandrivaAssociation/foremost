Summary:        Recover files based on their headers and footers
Name:           foremost
Version:        1.5
Release:        %mkrel 1
Epoch:          0
Group:          File tools
License:        Public Domain
URL:            http://foremost.sourceforge.net/
Source0:        http://foremost.sourceforge.net/pkg/foremost-%{version}.tar.gz

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
%{__mkdir_p} %{buildroot}%{_mandir}/man1
%{__install} -m 644 foremost.1 %{buildroot}%{_mandir}/man1
%{__mkdir_p} %{buildroot}%{_sysconfdir}
%{__install} -m 644 foremost.conf %{buildroot}%{_sysconfdir}

%clean
%{__rm} -rf %{buildroot}

%files 
%defattr(0644,root,root,0755)
%doc CHANGES README
%attr(0755,root,root) %{_bindir}/foremost
%{_mandir}/man1/%{name}.1*
%config(noreplace) %{_sysconfdir}/%{name}.conf
