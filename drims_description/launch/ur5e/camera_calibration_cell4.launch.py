""" Static transform publisher acquired via MoveIt 2 hand-eye calibration """
""" EYE-TO-HAND: table_top -> oak-d-base-frame """
from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description() -> LaunchDescription:
    nodes = [
        Node(
            package="tf2_ros",
            executable="static_transform_publisher",
            output="log",
            arguments=[
                "--frame-id",
                "table_top",
                "--child-frame-id",
                "oak-d-base-frame",
                "--x",
                "0.737091",
                "--y",
                "0.47375",
                "--z",
                "0.619371",
                "--qx",
                "0.708819",
                "--qy",
                "-0.00380556",
                "--qz",
                "-0.705349",
                "--qw",
                "0.00670088",
                # "--roll",
                # "2.43885",
                # "--pitch",
                # "-1.5644",
                # "--yaw",
                # "-0.687888",
            ],
        ),
    ]
    return LaunchDescription(nodes)
