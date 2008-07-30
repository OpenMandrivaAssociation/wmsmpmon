%define Summary System information for Dual CPUs (memory, swap, cpu, IO) in a small dock app
Summary:	%Summary
Name:		wmsmpmon
Version:	3.1
Release:	%mkrel 4
License:	GPLv2+
Group:		Graphical desktop/WindowMaker
Source0:	wmSMPmon-%{version}.tar.gz
Source1:	%{name}-icons.tar.bz2
URL:		http://www.ribbrock.org/binabit/wmSMPmon/
BuildRequires:	libxpm-devel
BuildRequires:	libxext-devel
BuildRequires:	libxau-devel
BuildRequires:	libxdmcp-devel
BuildRoot:	%{_tmppath}/%{name}-buildroot

%description
Monitor your dual processor system, memory, swap, and IOs in a small
dock app. It has been designed to work with wmaker, but nothing prevents
it from being run under another window manager.
 

%prep
rm -rf %buildroot

%setup -q -n wmSMPmon-%{version}

%build
make -C wmSMPmon CFLAGS="$RPM_OPT_FLAGS"

%install
[ -d %buildroot ] && rm -rf %buildroot

install -m 755 -d %buildroot%{_miconsdir}
install -m 755 -d %buildroot%{_iconsdir}
install -m 755 -d %buildroot%{_liconsdir}
tar xOjf %SOURCE1 %{name}.16x16.png > %buildroot%{_miconsdir}/%{name}.png
tar xOjf %SOURCE1 %{name}.32x32.png > %buildroot%{_iconsdir}/%{name}.png
tar xOjf %SOURCE1 %{name}.48x48.png > %buildroot%{_liconsdir}/%{name}.png

mkdir -p %buildroot%{_bindir}/ %buildroot%{_mandir}/man1/
install -m 755 wmSMPmon/wmSMPmon %buildroot%{_bindir}/
install -m 644 wmSMPmon/wmSMPmon.1 %buildroot%{_mandir}/man1/

chmod 644 {GREETINGS,LISEZ-MOI,COPYING}


mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=wmSMPmon
Comment=%{Summary}
Exec=%{_bindir}/wmSMPmon -g 3
Icon=%{name}
Terminal=false
Type=Application
Categories=System;Monitor;
EOF


%clean
rm -rf %buildroot


%if %mdkversion < 200900
%post
%{update_menus}
%endif


%if %mdkversion < 200900
%postun
%{clean_menus}
%endif


%files
%defattr (-,root,root)
%doc GREETINGS  LISEZ-MOI COPYING
%{_bindir}/*
%{_liconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_datadir}/applications/mandriva-%{name}.desktop
%{_mandir}/man1/wmSMPmon.1.*
