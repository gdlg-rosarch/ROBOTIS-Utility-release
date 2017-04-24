Name:           ros-kinetic-ros-mpg321-player
Version:        0.1.2
Release:        0%{?dist}
Summary:        ROS ros_mpg321_player package

Group:          Development/Libraries
License:        BSD
URL:            http://wiki.ros.org/ros_mpg321_player
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-kinetic-roscpp
Requires:       ros-kinetic-std-msgs
BuildRequires:  ros-kinetic-catkin
BuildRequires:  ros-kinetic-roscpp
BuildRequires:  ros-kinetic-std-msgs

%description
This package is a node that can playing mp3 file. This package is using mpg321
which is command-line mp3 player.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Mon Apr 24 2017 Pyo <pyo@robotis.com> - 0.1.2-0
- Autogenerated by Bloom

* Fri Sep 23 2016 Pyo <pyo@robotis.com> - 0.1.1-2
- Autogenerated by Bloom

* Fri Sep 23 2016 Pyo <pyo@robotis.com> - 0.1.1-1
- Autogenerated by Bloom

* Fri Sep 23 2016 Pyo <pyo@robotis.com> - 0.1.1-0
- Autogenerated by Bloom

* Wed Aug 17 2016 pyo <pyo@robotis.com> - 0.1.0-0
- Autogenerated by Bloom

