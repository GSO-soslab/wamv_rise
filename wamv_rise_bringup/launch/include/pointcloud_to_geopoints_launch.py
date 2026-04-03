import os
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from ament_index_python.packages import get_package_share_directory, get_package_prefix
from launch.actions import TimerAction
from launch.substitutions import PythonExpression


def generate_launch_description():
    package_name = 'pointcloud_to_geopoints'

    # Node argument
    robot_name = LaunchConfiguration('robot_name')
    pc2gp_delay = LaunchConfiguration('pc2gp_delay')

    param_config = os.path.join(
        get_package_share_directory('wamv_rise_bringup'),
        'config',
        'pointcloud_to_geopoints.yaml'
    )

    node = Node(
        package=package_name,
        executable='pointcloud_to_geopoints',
        name=package_name,
        namespace=robot_name,
        parameters=[param_config],
        output='screen'
    )

    return LaunchDescription([

        # Decalre arguments
        DeclareLaunchArgument(
            'robot_name', default_value = 'my_robot'            
        ),

        DeclareLaunchArgument(
            'pc2gp_delay', default_value = '0.0'            
        ),

        # Delay the node if needed
        TimerAction(
            period=PythonExpression([pc2gp_delay]),
            actions=[node]
        ),
    ])