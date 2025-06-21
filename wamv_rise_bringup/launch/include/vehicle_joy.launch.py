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
    joy_delay = LaunchConfiguration('joy_delay')

    # Node param
    parameters_file = Path(
        get_package_share_directory('wamv_rise_bringup'), 
        'config/vehicle_joy.yaml'
    )

    # Vehicle joy
    node = Node(
        package='wamv_rf_joy',
        executable='rf_joy_vehicle_node',
        name='rf_joy',
        namespace=robot_name,
        output='screen',
        parameters=[parameters_file],          
        emulate_tty=True
    )

    return LaunchDescription([

        # Decalre the arguments
        DeclareLaunchArgument(
            'robot_name', default_value = 'my_robot'            
        ),

        DeclareLaunchArgument(
            'joy_delay', default_value = '0.0'        
        ),

        # Delay the node if needed
        TimerAction(
            period=PythonExpression([joy_delay]),
            actions=[node]
        ),
    ])
