docker pull osrf/ros:jazzy-desktop-full
docker stop jazzy_ros
docker rm jazzy_ros
docker build -t jazzy_ros .
docker run -t -d --name jazzy_ros -e DISPLAY=host.docker.internal:0.0 jazzy_ros