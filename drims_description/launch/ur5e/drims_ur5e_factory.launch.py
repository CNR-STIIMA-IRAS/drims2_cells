from launch.launch_description import LaunchDescription
from launch.actions import OpaqueFunction, IncludeLaunchDescription, DeclareLaunchArgument, TimerAction
from launch.substitutions import PathJoinSubstitution, LaunchConfiguration
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.substitutions import FindPackageShare
from launch_ros.actions import Node
from launch.conditions import UnlessCondition

def generate_launch_description():
  launch_args = [
    DeclareLaunchArgument(name="fake", default_value="true", description="use fake hardware"),
    DeclareLaunchArgument(name="robot_ip", default_value="192.168.125.121", description="Robot ip"),
    DeclareLaunchArgument(name="cell_configuration_file",
                          default_value=PathJoinSubstitution(
                            [FindPackageShare("drims_description"), "config", "ur5e", "cell_1_configuration.yaml"]),
                          description="yaml file to configure the cell geometry"),
  ]
  return LaunchDescription(launch_args + [OpaqueFunction(function=launch_setup)])

def launch_setup(context):
  launch_moveit_path = PathJoinSubstitution([FindPackageShare('drims_description'), 'launch', 'ur5e', 'ur5e_moveit.launch.py'])
  launch_moveit = IncludeLaunchDescription(
    launch_description_source = PythonLaunchDescriptionSource(launch_moveit_path),
    launch_arguments = [('fake', LaunchConfiguration("fake"))]
  )

  launch_controllers_path = PathJoinSubstitution([FindPackageShare('drims_description'), 'launch', 'ur5e', 'ur5e_control.launch.py'])
  launch_controllers_launch  = IncludeLaunchDescription(
    launch_description_source = PythonLaunchDescriptionSource(launch_controllers_path),
    launch_arguments = [('fake', LaunchConfiguration("fake")),
                        ('robot_ip', LaunchConfiguration("robot_ip")),
                        ('cell_configuration_file', LaunchConfiguration("cell_configuration_file")),]
  )

  motion_server_path = PathJoinSubstitution([FindPackageShare("drims_description"), "launch", "ur5e", "ur5e_motion_server.launch.py"])
  motion_server_launch = IncludeLaunchDescription(
      launch_description_source = PythonLaunchDescriptionSource(motion_server_path),
      launch_arguments = [('fake', LaunchConfiguration("fake"))]
  )

  delayed_control_server = TimerAction(
      period=2.0,
      actions=[motion_server_launch]
  )

  ur_startup_node = Node (
      package = "ur_utils_ros2_py",
      executable = "restart_ros_control",
      name = "restart_ros_control",
      condition = UnlessCondition(LaunchConfiguration('fake')),
  )

  delayed_ur_startup = TimerAction(
      period=3.0,
      actions=[ur_startup_node]
  )

  return [
    launch_moveit,
    launch_controllers_launch,
    delayed_control_server,
    delayed_ur_startup
  ]