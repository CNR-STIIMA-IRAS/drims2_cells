cmake_minimum_required(VERSION 3.8)
project(smart_gripper_action_control)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(rclcpp_action REQUIRED)
find_package(control_msgs REQUIRED)
find_package(std_srvs REQUIRED)

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  set(ament_cmake_copyright_FOUND TRUE)
  set(ament_cmake_cpplint_FOUND TRUE)
  ament_lint_auto_find_test_dependencies()
endif()

# ✅ Nodo standalone
add_executable(smart_gripper_action_control
  src/smart_gripper_action_control.cpp
)

ament_target_dependencies(smart_gripper_action_control
  rclcpp
  rclcpp_action
  control_msgs
  std_srvs
)

install(TARGETS
  smart_gripper_action_control
  DESTINATION lib/${PROJECT_NAME}
)

ament_package()
