from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, RegisterEventHandler, SetEnvironmentVariable, EmitEvent, TimerAction
from launch.substitutions import LaunchConfiguration
from launch.substitutions import PythonExpression
from launch.events import Shutdown
from launch.event_handlers import OnProcessExit
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
from pathlib import Path
from launch_ros.actions import ComposableNodeContainer
from launch_ros.descriptions import ComposableNode
import launch

def generate_launch_description():

    # Node param
    parameters_file = Path(
        get_package_share_directory('wamv_rise_bringup'), 
        'config/gpsd_usb_gps.yaml'
    )    

    """Generate launch description with multiple components."""
    container = ComposableNodeContainer(
            name='fix_and_odometry_container',
            namespace='wamv_rise',
            package='rclcpp_components',
            executable='component_container',
            composable_node_descriptions=[
                ComposableNode(
                    package='gpsd_client',
                    plugin='gpsd_client::GPSDClientComponent',
                    name='gpsd_client',
                    namespace='wamv_rise',
                    parameters=[parameters_file],
                    remappings=[
                        ('fix', 'usb_gps/fix')
                    ],
                ),
                # ComposableNode(
                #     package='gps_tools',
                #     plugin='gps_tools::UtmOdometryComponent',
                #     name='utm_gpsfix_to_odometry_node')
            ],
            output='screen',
    )    

    return LaunchDescription([

        container,

        RegisterEventHandler(
            event_handler=OnProcessExit(
                target_action=container,
                on_exit=[EmitEvent(event=Shutdown())]
        ))
    ])    