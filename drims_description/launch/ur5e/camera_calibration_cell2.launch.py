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

                "0.75945",

                "--y",

                "0.48809",

                "--z",

                "0.61412",

                "--qx",

                "0.72380",

                "--qy",

                "-0.01736",

                "--qz",

                "-0.68979",

                "--qw",

                "0.00063",

            ],

        ),

    ]

    return LaunchDescription(nodes)