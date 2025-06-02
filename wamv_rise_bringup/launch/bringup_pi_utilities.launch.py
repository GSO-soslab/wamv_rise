
from launch import LaunchDescription
from ament_index_python.packages import get_package_share_directory
from launch_ros.actions import Node
import os
import yaml
from launch.substitutions import EnvironmentVariable
import pathlib
import launch.actions
from launch.actions import DeclareLaunchArgument

def generate_launch_description():
    ld = LaunchDescription()

    robot_name = 'wamv_rise'

    gpio_param_file = os.path.join(
        get_package_share_directory('wamv_rise_bringup'),
        'config/gpio_manager.yaml',
        )

    foxglove_launch = os.path.join(
        get_package_share_directory('foxglove_bridge'),
        'launch',
        'foxglove_bridge_launch.xml'
    )

    return LaunchDescription([
    gpio_node(
            package='mvp_gpio_manager',
            executable='gpio_manager_node',
            name='gpio_manager_node',
            namespace=robot_name,
            output='screen',
            prefix=['stdbuf -o L'],
            parameters=[
                gpio_param_file
                ],
           ),

    mvp_monitor_node(
        package = 'computer_monitoring',
        executable = 'computer_monitoring',
        name = 'computer_monitoring_node',
        namespace = robot_name,
        output ='screen'   
        ),

    IncludeLaunchDescription(
            XMLLaunchDescriptionSource(xml_launch_path)
        )
    ])