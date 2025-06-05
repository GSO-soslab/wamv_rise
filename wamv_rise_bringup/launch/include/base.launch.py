import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration

def generate_launch_description():

    robot_name = 'wamv_base'

    rf_param_file = os.path.join(
        get_package_share_directory('wamv_rise_bringup'),
        'config/rf_base.yaml'
    )

    joy_param_file = os.path.join(
        get_package_share_directory('wamv_rise_bringup'),
        'config/joy_base.yaml'
    )

    return LaunchDescription([

        # Base RF node
        Node(
            package='wamv_rf_joy',
            executable='rf_joy_base_node',
            name='rf_joy_base_node',
            namespace=robot_name,
            output='screen',
            parameters=[rf_param_file]
        ),        

        Node(
            package='joy',
            executable='joy_node',
            name='joy_node',
            namespace=robot_name,
            output='screen',
            parameters=[joy_param_file]
        ),

    ])



