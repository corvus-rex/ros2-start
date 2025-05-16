from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os


def generate_launch_description():
    # Path to the URDF file
    urdf_path = os.path.join(
        get_package_share_directory('rx78_description'),
        'urdf',
        'GGC_TestModel_rx78_20170112.urdf'
    )

    # Read URDF contents into a string
    with open(urdf_path, 'r') as urdf_file:
        robot_description_content = urdf_file.read()

    return LaunchDescription([
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            output='screen',
            parameters=[{'robot_description': robot_description_content}]
        )
    ])
