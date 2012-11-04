#sbs-git:slp/pkgs/xorg/xcb/libpthread-stubs libpthread-stubs 0.3 ce726f595116dd79d38db013c49c113555b1a15d

Name:           libpthread-stubs
Version:        0.3
Release:        2.8
License:        MIT
Summary:        PThread Stubs for XCB
Url:            http://xcb.freedesktop.org
Group:          System/X11
Source:         %{name}-%{version}.tar.bz2

BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
PThread Stubs for XCB

%prep
%setup -q

%build

%configure --disable-static
# Call make instruction with smp support
make %{?_smp_mflags}

%install
%make_install




%files
%defattr(-,root,root,-)
%{_libdir}/pkgconfig/pthread-stubs.pc

