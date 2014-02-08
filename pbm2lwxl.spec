Summary:	A driver for the CoStar Labelwriter XL
Name:		pbm2lwxl
Version:	0
Release:	11
License:	GPL
Group:		System/Printing
URL:		http://www.freelabs.com/~whitis/software/pbm2lwxl
Source0:	http://www.freelabs.com/~whitis/software/pbm2lwxl/pbm2lwxl.tar.gz
Patch0:		pbm2lwxl-20040515-path.patch
Patch1:		pbm2lwxl-LDFLAGS.diff
Requires:	mpage
Requires:	ghostscript
Conflicts:	printer-utils = 2007
Conflicts:	printer-filters = 2007
BuildRoot:	%{_tmppath}/%{name}-%{version}-root

%description
A driver for the CoStar printers:
 o LabelWriter II
 o LabelWriter XL+
 o Labelwriter XL
 o EL40
 o EL60
 o Turbo
 o SE250
 o SE250+
 o ASCII
 o ASCII+
 o LW300
 o LW330
 o LW330 Turbo

And Avery Printers:
 o Personal Label Printer and Personal Label Printer+???

%prep

%setup -q -c -T -a0
%patch0 -p1 -b .path
%patch1 -p0 -b .LDFLAGS

%build
make CFLAGS="%{optflags}" LDFLAGS="%{ldflags}"

%install
rm -rf %{buildroot}

install -d %{buildroot}%{_bindir}

install -m0755 pbm2lwxl %{buildroot}%{_bindir}/
install -m0755 ps2lwxl %{buildroot}%{_bindir}/
install -m0755 txt2lwxl %{buildroot}%{_bindir}/
install -m0755 small2lwxl %{buildroot}%{_bindir}/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README index.html license.html
%attr(0755,root,root) %{_bindir}/pbm2lwxl
%attr(0755,root,root) %{_bindir}/ps2lwxl
%attr(0755,root,root) %{_bindir}/small2lwxl
%attr(0755,root,root) %{_bindir}/txt2lwxl


%changelog
* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0-10mdv2011.0
+ Revision: 666997
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 0-9mdv2011.0
+ Revision: 607080
- rebuild

* Sun Mar 14 2010 Oden Eriksson <oeriksson@mandriva.com> 0-8mdv2010.1
+ Revision: 519052
- rebuild

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 0-7mdv2010.0
+ Revision: 426368
- rebuild

* Mon Dec 29 2008 Oden Eriksson <oeriksson@mandriva.com> 0-6mdv2009.1
+ Revision: 321042
- use %%ldflags

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 0-5mdv2009.0
+ Revision: 223444
- rebuild

* Tue Mar 04 2008 Oden Eriksson <oeriksson@mandriva.com> 0-4mdv2008.1
+ Revision: 179150
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Aug 30 2007 Oden Eriksson <oeriksson@mandriva.com> 0-3mdv2008.0
+ Revision: 75351
- fix deps (pixel)

* Thu Aug 16 2007 Oden Eriksson <oeriksson@mandriva.com> 0-2mdv2008.0
+ Revision: 64170
- use the new System/Printing RPM GROUP

* Tue Aug 14 2007 Oden Eriksson <oeriksson@mandriva.com> 0-1mdv2008.0
+ Revision: 63088
- Import pbm2lwxl



* Tue Aug 14 2007 Oden Eriksson <oeriksson@mandriva.com> 0-1mdv2008.0
- initial Mandriva package

* Sun May 16 2004 Marcelo Ricardo Leitner <mrl@conectiva.com.br>
+ 2004-05-16 13:44:58 (60551)
- New upstream, compatible with foomatic.
- Started versioning by date, since this project has no version system.
- Added path patch, fixes some path at /usr/bin scripts.

* Thu Aug 29 2002 Gustavo Niemeyer <niemeyer@conectiva.com>
+ 2002-08-29 18:36:18 (9015)
- Imported package from 8.0.
