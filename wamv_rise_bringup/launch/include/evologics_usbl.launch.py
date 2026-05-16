import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration, PythonExpression
from launch.actions import TimerAction, DeclareLaunchArgument


def generate_launch_description():
    # Node argument
    robot_name = LaunchConfiguration('robot_name')
    usbl_driver_delay = LaunchConfiguration('usbl_driver_delay')

    # param path
    param_path = os.path.join(
        get_package_share_directory('wamv_rise_bringup'),
        'config'
        )
    
    # different param
    evologics_param_file = os.path.join(param_path, 'evologics_usbl1.yaml') 

    goby_param_file = os.path.join(param_path, 'goby.yaml') 

    # node
    node = Node(
        package="evologics_ros",
        executable="evologics_ros_node",
        namespace=robot_name,
        name="evologics_ros_node_usbl",
        prefix=['stdbuf -o L'],
        output="screen",
        parameters=[
            evologics_param_file,
            goby_param_file
        ],
        # remappings=[
        #         ('usbl/fix', 'usbl_data'),
        # ],                        
    )

    # launch the node
    return LaunchDescription([
        # Decalre arguments
        DeclareLaunchArgument(
            'robot_name', default_value = 'my_robot'            
        ),

        DeclareLaunchArgument(
            'usbl_driver_delay', default_value = '0.0'            
        ),

        # Delay the node if needed
        TimerAction(
            period=PythonExpression([usbl_driver_delay]),
            actions=[node]
        ),
        
])