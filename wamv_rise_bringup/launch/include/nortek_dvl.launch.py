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
    nortek_delay = LaunchConfiguration('nortek_delay')

    # Node param
    parameters_file = Path(
        get_package_share_directory('wamv_rise_bringup'), 
        'config/nortek_dvl.yaml'
    )

    # Nortek DVL node
    node = Node(
            package="nortek_dvl",
            executable="nortek_dvl_node",
            name="nortek",
            output="screen",
            namespace=robot_name,
            parameters=[parameters_file],
            emulate_tty=True        
    ),
    
    return LaunchDescription([

        # Decalre arguments
        DeclareLaunchArgument(
            'robot_name', default_value = 'my_robot'            
        ),

        DeclareLaunchArgument(
            'nortek_delay', default_value = '0.0'            
        ),

        # Delay the node if needed
        TimerAction(
            period=PythonExpression([nortek_delay]),
            actions=[node]
        ),
    ])
