Summary:	A driver for the CoStar Labelwriter XL
Name:		pbm2lwxl
Version:	0
Release:	%mkrel 1
License:	GPL
Group:		System/Kernel and hardware
URL:		http://www.freelabs.com/~whitis/software/pbm2lwxl
Source0:	http://www.freelabs.com/~whitis/software/pbm2lwxl/pbm2lwxl.tar.gz
Patch0:		pbm2lwxl-20040515-path.patch
Requires:	mpage
Requires:	ghostscript
Conflicts:	printer-utils-2006 printer-utils-2007
Conflicts:	printer-filters-2006 printer-filters-2007
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

%build
make CFLAGS="%{optflags}"

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
