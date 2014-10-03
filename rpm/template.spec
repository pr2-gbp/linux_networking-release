Name:           ros-hydro-asmach
Version:        1.0.4
Release:        0%{?dist}
Summary:        ROS asmach package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/smach
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  ros-hydro-catkin

%description
SMACH, which stands for 'state machine', is a task-level architecture for
rapidly creating complex robot behavior. At its core, SMACH is a ROS-independent
Python library to build hierarchical state machines. SMACH is a new library that
takes advantage of very old concepts in order to quickly create robust robot
behavior with maintainable and modular code.

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
* Fri Oct 03 2014 Dash <dash@clearpathrobotics.com> - 1.0.4-0
- Autogenerated by Bloom

