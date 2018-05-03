%global debug_package %{nil}

Name:           mapbox-variant
Version:        1.1.5
Release:        5%{?dist}
Summary:        A header-only alternative to boost::variant for C++11 and C++14

License:        Boost and BSD
URL:            https://github.com/mapbox/variant
Source0:        https://github.com/mapbox/variant/archive/v%{version}/%{name}-%{version}.tar.gz
# https://github.com/mapbox/variant/pull/143
Patch0:         mapbox-variant-catch.patch

%description
Mapbox variant has the same speedy performance of boost::variant but is
faster to compile, results in smaller binaries, and has no dependencies.


%package        devel
Summary:        Development files for %{name}
Provides:       %{name}-static = %{version}-%{release}

%description    devel
Mapbox variant has the same speedy performance of boost::variant but is
faster to compile, results in smaller binaries, and has no dependencies.


%prep
%setup -n variant-%{version}
%apply_patches
sed -i -e 's/-Werror //' Makefile
sed -i -e 's/-march=native //' Makefile
rm -f test/include/catch.hpp

%build

%install
mkdir -p %{buildroot}%{_includedir}
cp -pr include/mapbox %{buildroot}%{_includedir}

%files devel
%{_includedir}/mapbox
