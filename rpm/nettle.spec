Name:           nettle
Version:        3.7.3
Release:        1%{?dist}
Summary:        A low-level cryptographic library

License:        GPLv2+ and LGPLv3+
URL:            https://www.lysator.liu.se/~nisse/nettle/
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  m4
BuildRequires:  make
BuildRequires:  gmp-devel
BuildRequires:  libtool
BuildRequires:  autoconf
BuildRequires:  automake
Requires(post): coreutils
Requires(postun): coreutils

%package devel
Summary:        Development headers for a low-level cryptographic library
Requires:       %{name} = %{version}-%{release}
Requires:       gmp-devel%{?_isa}

%description
Nettle is a cryptographic library that is designed to fit easily in more
or less any context: In crypto toolkits for object-oriented languages
(C++, Python, Pike, ...), in applications like LSH or GNUPG, or even in
kernel space.

Categories:
  - Library
Custom:
  Repo: https://github.com/sailfishos-chum/nettle

%description devel
Nettle is a cryptographic library that is designed to fit easily in more
or less any context: In crypto toolkits for object-oriented languages
(C++, Python, Pike, ...), in applications like LSH or GNUPG, or even in
kernel space.  This package contains the files needed for developing
applications with nettle.

Custom:
  Repo: https://github.com/sailfishos-chum/nettle

%prep
%setup -q -n %{name}-%{version}/nettle

%build
%reconfigure --enable-shared --enable-fat
%make_build

%install
%make_install
make install-shared DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
rm -f $RPM_BUILD_ROOT%{_bindir}/nettle-lfib-stream
rm -f $RPM_BUILD_ROOT%{_bindir}/pkcs1-conv
rm -f $RPM_BUILD_ROOT%{_bindir}/sexp-conv
rm -f $RPM_BUILD_ROOT%{_bindir}/nettle-hash
rm -f $RPM_BUILD_ROOT%{_bindir}/nettle-pbkdf2

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%files
%doc AUTHORS NEWS README
%license COPYINGv2 COPYING.LESSERv3
%{_libdir}/libnettle.so.8
%{_libdir}/libnettle.so.8.*
%{_libdir}/libhogweed.so.6
%{_libdir}/libhogweed.so.6.*

%files devel
%doc descore.README
%{_includedir}/nettle
%{_libdir}/libnettle.so
%{_libdir}/libhogweed.so
%{_libdir}/pkgconfig/hogweed.pc
%{_libdir}/pkgconfig/nettle.pc

%changelog
* Mon Sep 20 2021 Renaud Casenave-Péré <renaud@casenave-pere.fr> - 3.7.3-1
- Initial version
