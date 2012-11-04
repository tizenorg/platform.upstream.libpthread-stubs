Name:           libpthread-stubs
Version:        0.3
Release:        2.8
License:        MIT
Summary:        PThread Stubs for XCB
Url:            http://xcb.freedesktop.org
Group:          System/X11
Source:         %{name}-%{version}.tar.bz2

%description
PThread Stubs for XCB

%prep
%setup -q

%build
%configure --disable-static
make %{?_smp_mflags}

%install
%make_install

%files
%defattr(-,root,root,-)
%{_libdir}/pkgconfig/pthread-stubs.pc

