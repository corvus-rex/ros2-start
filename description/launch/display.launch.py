from launch import LaunchDescription
from launch.substitutions import LaunchConfiguration
from launch.conditions import IfCondition, UnlessCondition
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    description_pkg = get_package_share_directory('gundam_rx78_description')

    gui_arg = DeclareLaunchArgument(
        name='gui',
        default_value='true',
        description='Use joint_state_publisher_gui if true'
    )

    rvizconfig_arg = DeclareLaunchArgument(
        name='rvizconfig',
        default_value=os.path.join(description_pkg, 'config', 'urdf.rviz'),
        description='Path to the RViz config file'
    )

    upload_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(description_pkg, 'launch', 'upload.launch.py')
        )
    )

    joint_state_publisher_gui = Node(
        package='joint_state_publisher_gui',
        executable='joint_state_publisher_gui',
        name='joint_state_publisher_gui',
        condition=IfCondition(LaunchConfiguration('gui'))
    )

    joint_state_publisher = Node(
        package='joint_state_publisher',
        executable='joint_state_publisher',
        name='joint_state_publisher',
        condition=UnlessCondition(LaunchConfiguration('gui'))
    )

    robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='robot_state_publisher'
    )

    rviz = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz',
        arguments=['-d', LaunchConfiguration('rvizconfig')],
        output='screen'
    )

    return LaunchDescription([
        gui_arg,
        rvizconfig_arg,
        upload_launch,
        joint_state_publisher_gui,
        joint_state_publisher,
        robot_state_publisher,
        rviz
    ])
