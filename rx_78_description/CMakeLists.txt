cmake_minimum_required(VERSION 3.8)
project(gundam_rx78_description)

# Use ament_cmake as the build system
find_package(ament_cmake REQUIRED)

#############
## Install ##
#############

install(DIRECTORY
  config
  launch
  meshes
  scripts
  urdf
  DESTINATION share/${PROJECT_NAME}
  USE_SOURCE_PERMISSIONS
)

#############
## Package ##
#############

ament_package()
