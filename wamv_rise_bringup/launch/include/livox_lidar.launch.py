from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch.substitutions import PythonExpression
from launch.actions import SetEnvironmentVariable
from launch.actions import TimerAction
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
from pathlib import Path

def generate_launch_description():

    # Node argument
    robot_name = LaunchConfiguration('robot_name')
    livox_delay = LaunchConfiguration('livox_delay')

    # Node param
    parameters_file = Path(
        get_package_share_directory('wamv_rise_bringup'), 
        'config/livox_lidar.yaml'
    )

    user_config_file = Path(
        get_package_share_directory('wamv_rise_bringup'), 
        'config/livox_MID70.json'
    )

    # Livox Lidar
    node = Node(
        package='livox_ros2_driver',
        executable='livox_ros2_driver_node',
        name='livox_lidar_publisher',
        namespace=robot_name,
        output='screen',
        # prefix=['stdbuf -o L'],
        parameters=[
            parameters_file,
            {'user_config_path': str(user_config_file)},
            {'frame_id': [robot_name, '/livox_frame']},
        ],
        # remappings=[('livox/lidar_3GGDJ3R00100821', 'livox/lidar')],        
        emulate_tty=True        
    )    
    
    return LaunchDescription([

        # Decalre arguments
        DeclareLaunchArgument(
            'robot_name', default_value = 'my_robot'            
        ),

        DeclareLaunchArgument(
            'livox_delay', default_value = '0.0'            
        ),

        # Delay the node if needed
        TimerAction(
            period=PythonExpression([livox_delay]),
            actions=[node]
        ),
    ])
