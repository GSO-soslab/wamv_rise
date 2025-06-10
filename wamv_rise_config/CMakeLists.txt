cmake_minimum_required(VERSION 3.8)
project(wamv_rise_config)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)

##config files
install(DIRECTORY
  mvp_control_config
  DESTINATION share/${PROJECT_NAME}
)

install(DIRECTORY
  mvp_mission_config
  DESTINATION share/${PROJECT_NAME}
)


ament_package()