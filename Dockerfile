FROM osrf/ros:jazzy-desktop-full

RUN apt-get update
RUN apt-get install -y git && apt-get install -y python3-pip
RUN mkdir -p /home/corvus/Projects/ros2

## Add `ros` to env variable
RUN echo "source /opt/ros/jazzy/setup.bash" >> ~/.bashrc

## Install RQT and Colcon
RUN apt-get install -y '~nros-jazzy-rqt*'
RUN apt-get install -y python3-colcon-common-extensions

## Clone and build Package Underlay (SEQUENTIAL FLAG IS IMPORTANT)
RUN cd /home/corvus/Projects/ros2 && git clone https://github.com/ros2/examples src/examples -b jazzy && colcon build --symlink-install --executor sequential
# RUN git clone https://github.com/corvus-rex/examples src/examples -b jazzy

## Add `colcon_cd` to env variable
RUN echo "source /usr/share/colcon_cd/function/colcon_cd.sh" >> ~/.bashrc && echo "export _colcon_cd_root=/opt/ros/jazzy/" >> ~/.bashrc

RUN echo "All good"