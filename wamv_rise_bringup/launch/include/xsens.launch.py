from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch.actions import SetEnvironmentVariable
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
from pathlib import Path

def generate_launch_description():

    robot_name = LaunchConfiguration('robot_name')

    parameters_file = Path(
        get_package_share_directory('wamv_rise_bringup'), 
        'config/xsens.yaml'
    )

    return LaunchDescription([

        DeclareLaunchArgument(
            'wamv_rise', default_value = 'robot_name'            
        ),

        SetEnvironmentVariable(
            name = 'RCUTILS_LOGGING_USE_STDOU', value = '1'
        ),

        SetEnvironmentVariable(
            name = 'RCUTILS_LOGGING_BUFFERED_STREAM', value = '1'
        ),        

        Node(
            package='xsens_mti_ros2_driver',
            executable='xsens_mti_node',
            name='xsens_mti_node',
            output='screen',
            namespace=robot_name,
            parameters=[parameters_file],
            arguments=[]
        )
    ])
