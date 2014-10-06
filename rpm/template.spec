Name:           ros-hydro-ieee80211-channels
Version:        1.0.5
Release:        0%{?dist}
Summary:        ROS ieee80211_channels package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/ieee80211_channels
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  ros-hydro-catkin

%description
This package provides mapping from frequencies to IEEE802.11 channels and vice-
versa.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
mkdir -p build && cd build
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/hydro" \
        -DCMAKE_PREFIX_PATH="/opt/ros/hydro" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
cd build
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/hydro

%changelog
* Mon Oct 06 2014 Dash <dash@clearpathrobotics.com> - 1.0.5-0
- Autogenerated by Bloom

* Fri Oct 03 2014 Dash <dash@clearpathrobotics.com> - 1.0.4-0
- Autogenerated by Bloom

