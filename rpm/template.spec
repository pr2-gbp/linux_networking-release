Name:           ros-indigo-linux-networking
Version:        1.0.10
Release:        0%{?dist}
Summary:        ROS linux_networking package

Group:          Development/Libraries
License:        TODO
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-indigo-access-point-control
Requires:       ros-indigo-asmach
Requires:       ros-indigo-asmach-tutorials
Requires:       ros-indigo-ddwrt-access-point
Requires:       ros-indigo-hostapd-access-point
Requires:       ros-indigo-ieee80211-channels
Requires:       ros-indigo-linksys-access-point
Requires:       ros-indigo-multi-interface-roam
Requires:       ros-indigo-network-control-tests
Requires:       ros-indigo-network-detector
Requires:       ros-indigo-network-monitor-udp
Requires:       ros-indigo-network-traffic-control
BuildRequires:  ros-indigo-catkin

%description
The linux_networking package

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Wed Sep 16 2015 Devon Ash <dash@clearpathrobotics.com> - 1.0.10-0
- Autogenerated by Bloom

