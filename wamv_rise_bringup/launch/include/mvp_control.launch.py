from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch.substitutions import PythonExpression
from launch.actions import SetEnvironmentVariable
from launch.actions import TimerAction
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
from pathlib import Path
import os

def generate_launch_description():

    # Node argument
    robot_name = LaunchConfiguration('robot_name')
    contorl_delay = LaunchConfiguration('contorl_delay')

    # Node param
    parameters_file = Path(
        get_package_share_directory('wamv_rise_bringup'), 
        'config/mvp_control.yaml'
    )

    configuration_file = os.path.join(
        get_package_share_directory('wamv_rise_config'), 
        'mvp_control_config', 'config.yaml'
    )    

    # MVP Control node
    node = Node(
        package="mvp_control",
        executable="mvp_control_ros_node",
        namespace=robot_name,
        name="mvp_control",
        prefix=['stdbuf -o L'],
        output="screen",
        parameters=[
            {'config_file': configuration_file},
            {'tf_prefix': robot_name},
            {'odometry_source':  ['/', robot_name, '/odometry/filtered']},
            parameters_file],
        emulate_tty=True
    )
    
    return LaunchDescription([

        # Decalre the arguments
        DeclareLaunchArgument(
            'robot_name', default_value = 'my_robot'            
        ),

        DeclareLaunchArgument(
            'contorl_delay', default_value = '0.0'        
        ),

        # Delay the node if needed
        TimerAction(
            period=PythonExpression([contorl_delay]),
            actions=[node]
        ),
    ])
