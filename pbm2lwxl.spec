Summary:	A driver for the CoStar Labelwriter XL
Name:		pbm2lwxl
Version:	0
Release:	18
License:	GPL
Group:		System/Printing
Url:		http://www.freelabs.com/~whitis/software/pbm2lwxl
Source0:	http://www.freelabs.com/~whitis/software/pbm2lwxl/pbm2lwxl.tar.gz
Patch0:		pbm2lwxl-20040515-path.patch
Patch1:		pbm2lwxl-LDFLAGS.diff
Requires:	mpage
Requires:	ghostscript

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
install -d %{buildroot}%{_bindir}
install -m0755 pbm2lwxl %{buildroot}%{_bindir}/
install -m0755 ps2lwxl %{buildroot}%{_bindir}/
install -m0755 txt2lwxl %{buildroot}%{_bindir}/
install -m0755 small2lwxl %{buildroot}%{_bindir}/

%files
%doc README index.html license.html
%{_bindir}/pbm2lwxl
%{_bindir}/ps2lwxl
%{_bindir}/small2lwxl
%{_bindir}/txt2lwxl

