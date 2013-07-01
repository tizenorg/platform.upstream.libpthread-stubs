Name:           libpthread-stubs
Version:        0.3
Release:        2.8
License:        MIT
Summary:        PThread Stubs for XCB
Url:            http://xcb.freedesktop.org
Group:          System/X11
Source:         %{name}-%{version}.tar.bz2
Source1001: 	libpthread-stubs.manifest

%description
PThread Stubs for XCB

%prep
%setup -q
cp %{SOURCE1001} .

%build
%configure --disable-static
make %{?_smp_mflags}

%install
%make_install

%files
%manifest %{name}.manifest
%license COPYING
%defattr(-,root,root,-)
%{_libdir}/pkgconfig/pthread-stubs.pc

