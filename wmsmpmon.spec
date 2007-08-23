Summary:  System information for Dual CPUs (memory, swap, cpu, IO) in a small dock app
Name:		wmsmpmon
Version: 2.3
Release: %mkrel 3
License:	GPL
Group:		Graphical desktop/WindowMaker
Source0:	%{name}-%{version}.tar.bz2
Source1:	%{name}-icons.tar.bz2
URL:		http://goupilfr.org/?soft=wmsmpmon
Requires:	XFree86-libs, xpm
BuildRequires:	XFree86-devel, xpm-devel
BuildRoot:	%{_tmppath}/%{name}-buildroot

%description
Monitor your dual processor system, memory, swap, and IOs in a small
dock app. It has been designed to work with wmaker, but nothing prevents
it from being run under another window manager.
 

%prep
rm -rf %buildroot

%setup -n wmSMPmon-2.x

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

mkdir -p %buildroot%{_bindir}/
install -m 755 wmSMPmon/wmSMPmon %buildroot%{_bindir}/

chmod 644 {GREETINGS,LISEZ-MOI,COPYING}

install -m 755 -d %buildroot%{_menudir}
cat << EOF > %buildroot%{_menudir}/%{name}
?package(%{name}):command="%{_bindir}/wmSMPmon -g 3" icon="%{name}.png"\\
                 needs="X11" section="Applications/Monitoring" title="Wmsmpmon"\\
                 longtitle="System information on dual CPU systems in a small icon"
EOF


%clean
rm -rf %buildroot


%post
%{update_menus}


%postun
%{clean_menus}


%files
%defattr (-,root,root)
%doc GREETINGS  LISEZ-MOI COPYING
%{_bindir}/*
%{_liconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_menudir}/%{name}


