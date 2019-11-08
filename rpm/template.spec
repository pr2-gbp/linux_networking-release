Name:           ros-melodic-access-point-control
Version:        1.0.16
Release:        1%{?dist}
Summary:        ROS access_point_control package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/access_point_control
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-melodic-dynamic-reconfigure
Requires:       ros-melodic-rospy
BuildRequires:  ros-melodic-catkin
BuildRequires:  ros-melodic-dynamic-reconfigure
BuildRequires:  ros-melodic-rospy

%description
Defines an API for access point control based on dynamic_reconfigure. Other
packages must implement the API for various access-point models: for example:
hostapd_access_point for hostapd-based control or linksys_access_point for
Linksys router web interface.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/melodic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/melodic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/melodic

%changelog
* Fri Nov 08 2019 Devon Ash <dash@clearpathrobotics.com> - 1.0.16-1
- Autogenerated by Bloom

* Sat Mar 30 2019 Devon Ash <dash@clearpathrobotics.com> - 1.0.15-0
- Autogenerated by Bloom

* Wed Mar 06 2019 Devon Ash <dash@clearpathrobotics.com> - 1.0.13-2
- Autogenerated by Bloom

* Wed Mar 06 2019 Devon Ash <dash@clearpathrobotics.com> - 1.0.13-1
- Autogenerated by Bloom

* Wed Mar 06 2019 Devon Ash <dash@clearpathrobotics.com> - 1.0.13-0
- Autogenerated by Bloom

