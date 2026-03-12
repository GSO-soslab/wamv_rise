import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration
from launch.actions import TimerAction
from launch.substitutions import PythonExpression

def generate_launch_description():
    """
    Launch file to run two instances of the dwe_camera_node for two cameras,
    with remappings to ensure topics are unique.
    """

    # Node argument
    robot_name = LaunchConfiguration('robot_name')
    camera_delay = LaunchConfiguration('camera_delay')
    
    # The package name is 'dwe_camera' as defined in setup.py
    robot_param_path = get_package_share_directory(robot_bringup)

    dual_camera_params_path = os.path.join(robot_param_path, 'config', 'dwe_stellar_camera.yaml')

    camera_node = Node(
        package='dwe_camera_driver',
        executable='camera_node',
        name='camera_node',
        namespace=robot_name,
        output='screen',
        parameters=[dual_camera_params_path],
    )

    return LaunchDescription([
        TimerAction(
            period=PythonExpression([camera_delay]),
            actions=[camera_node]
        ),
        
    ])