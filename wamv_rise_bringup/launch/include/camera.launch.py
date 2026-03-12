import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration
from launch.actions import TimerAction
from launch.substitutions import PythonExpression
from pathlib import Path

def generate_launch_description():
    """
    Launch file to run two instances of the dwe_camera_node for two cameras,
    with remappings to ensure topics are unique.
    """

    # Node argument
    robot_name = LaunchConfiguration('robot_name')
    camera_delay = LaunchConfiguration('camera_delay')
    
    # Camera parameters
    camera_params_path = Path(
        get_package_share_directory('wamv_rise_bringup'), 
        'config/dwe_camera_stellar.yaml')
    
    camera_control_params_path = Path(
        get_package_share_directory('wamv_rise_bringup'), 
        'config/dwe_camera_hardware_controls.yaml')
    
    camera_aux_params_path = Path(
        get_package_share_directory('wamv_rise_bringup'), 
        'config/dwe_camera_auxiliary_processors.yaml')

    camera_node = Node(
        package='dwe_camera_driver',
        executable='camera_node',
        name='camera_node',
        namespace=robot_name,
        output='screen',
        parameters=[
            camera_params_path,
            camera_control_params_path,
            camera_aux_params_path,
        ]
    )

    return LaunchDescription([
        TimerAction(
            period=PythonExpression([camera_delay]),
            actions=[camera_node]
        ),
        
    ])