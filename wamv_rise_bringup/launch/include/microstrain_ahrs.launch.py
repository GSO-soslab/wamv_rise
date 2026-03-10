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
    microstrain_delay = LaunchConfiguration('microstrain_delay')

    # Node param
    parameters_file = Path(
        get_package_share_directory('wamv_rise_bringup'), 
        'config/microstrain_ahrs.yaml'
    )

    # microstrain AHRS node
    microstrain_node = Node(
        package='microstrain_inertial_driver',
        executable='microstrain_inertial_driver_node',
        name='microstrain_ahrs',
        output='screen',
        namespace=robot_name,
        parameters=[parameters_file], 
        arguments=[],
        emulate_tty=True,
        # remappings=[('ext/heading_enu', 'unicore_rtk_driver/heading_enu_pose')],        
        # remappings=[('ext/heading_enu', 'unicore_rtk/heading_enu_pose')],        
        # respawn=True, 
        # respawn_delay=2.0                 
    )
    
    return LaunchDescription([

        # Decalre arguments
        DeclareLaunchArgument(
            'robot_name', default_value = 'my_robot'            
        ),

        DeclareLaunchArgument(
            'microstrain_delay', default_value = '0.0'            
        ),

        # Delay the node if needed
        TimerAction(
            period=PythonExpression([microstrain_delay]),
            actions=[microstrain_node]
        ),
    ])
