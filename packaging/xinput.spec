%bcond_with x

Name:           xinput
Version:        1.6.0
Release:        1
License:        MIT and HPND
Summary:        Utility to configure and test X input devices
Url:            http://xorg.freedesktop.org/
Group:          System/X11
Source0:        http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
Source1001: 	xinput.manifest
BuildRequires:  pkgconfig(inputproto) >= 2.0.99.1
BuildRequires:  pkgconfig(pkg-config)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xi) >= 1.4.99.1
BuildRequires:  pkgconfig(xinerama)
BuildRequires:  pkgconfig(xorg-macros) >= 1.3
BuildRequires:  pkgconfig(xrandr)

%if !%{with x}
ExclusiveArch:
%endif

%description
xinput is a utility to configure and test XInput devices.

%prep
%setup -q
cp %{SOURCE1001} .

%build
%configure --disable-static --libdir=%{_datadir}
make %{?_smp_mflags}

%install
%make_install

%files
%manifest %{name}.manifest
%defattr(-,root,root)
%license COPYING
%{_bindir}/xinput
%{_mandir}/man1/xinput.1%{?ext_man}

%changelog
