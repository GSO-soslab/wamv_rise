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
    xsens_delay = LaunchConfiguration('xsens_delay')

    # Node param
    parameters_file = Path(
        get_package_share_directory('wamv_rise_bringup'), 
        'config/xsens_ahrs.yaml'
    )

    # Xsens AHRS node
    xsens_node = Node(
        package='xsens_mti_ros2_driver',
        executable='xsens_mti_node',
        name='xsens_ahrs',
        output='screen',
        namespace=robot_name,
        parameters=[parameters_file],
        arguments=[],
        emulate_tty=True,
        respawn=True, 
        respawn_delay=2.0         
    )
    
    return LaunchDescription([

        # Decalre arguments
        DeclareLaunchArgument(
            'robot_name', default_value = 'my_robot'            
        ),

        DeclareLaunchArgument(
            'xsens_delay', default_value = '0.0'            
        ),

        # Env variables
        SetEnvironmentVariable(
            name = 'RCUTILS_LOGGING_USE_STDOU', value = '1'
        ),

        SetEnvironmentVariable(
            name = 'RCUTILS_LOGGING_BUFFERED_STREAM', value = '1'
        ),        

        # Delay the node if needed
        TimerAction(
            period=PythonExpression([xsens_delay]),
            actions=[xsens_node]
        ),
    ])
