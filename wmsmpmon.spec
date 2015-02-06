%define Summary System information for Dual CPUs (memory, swap, cpu, IO) in a small dock app
Summary:	%Summary
Name:		wmsmpmon
Version:	3.1
Release:	7
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


%changelog
* Wed Sep 09 2009 Thierry Vignaud <tvignaud@mandriva.com> 3.1-6mdv2010.0
+ Revision: 434896
- rebuild

* Sun Aug 03 2008 Thierry Vignaud <tvignaud@mandriva.com> 3.1-5mdv2009.0
+ Revision: 262089
- rebuild

* Wed Jul 30 2008 Thierry Vignaud <tvignaud@mandriva.com> 3.1-4mdv2009.0
+ Revision: 256261
- rebuild
- drop old menu
- kill re-definition of %%buildroot on Pixel's request

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Tue Nov 06 2007 Funda Wang <fundawang@mandriva.org> 3.1-2mdv2008.1
+ Revision: 106462
- rebuild for new lzma

* Fri Sep 14 2007 Gustavo De Nardin <gustavodn@mandriva.com> 3.1-1mdv2008.1
+ Revision: 85711
- new version 3.1
- new URL
- fine grained BuildRequires
- xdg menu
- manpage

  + Thierry Vignaud <tvignaud@mandriva.com>
    - use %%mkrel


* Thu Jun 02 2005 Nicolas Lécureuil <neoclust@mandriva.org> 2.3-2mdk
- Rebuild

* Thu Apr 10 2003 HA Quôc-Viêt <viet@mandrakesoft.com> 2.3-1mdk
- new release

* Mon Feb 11 2002 HA Quôc-Viêt <viet@mandrakesoft.com> 2.2-2mdk
- new URL
- xpm converted to png
- prefix changed from /usr/X11R6 to /usr
- compile flags now works

* Thu Jul 12 2001 HA Quôc-Viêt <viet@mandrakesoft.com> 2.2-1mdk
- Source update

* Wed Mar 28 2001 HA Quôc-Viêt <viet@mandrakesoft.com> 2.1-1mdk
- Initial release.

