
from launch import LaunchDescription
from ament_index_python.packages import get_package_share_directory
from launch_ros.actions import Node
import os
import yaml
from launch.substitutions import EnvironmentVariable, PythonExpression, LaunchConfiguration
import pathlib
import launch.actions
from launch.actions import DeclareLaunchArgument, TimerAction

def generate_launch_description():
    # Node argument
    robot_name = LaunchConfiguration('robot_name')
    usbl_acomm_delay = LaunchConfiguration('usbl_acomm_delay')

    # Node
    node = Node(
        package='mvp_acomm_utilities',
        executable='acomm_geopoint_node',
        name='acomm_geopoint_node',
        namespace=robot_name,
        output='screen',
        prefix=['stdbuf -o L'],
        parameters=[
            {'tf_prefix': robot_name},
            # {'use_reference_geopose_orientation': True},
            {'usbl_frame_id': 'usbl'},
            {'world_frame_id': 'world'},
            ],
        # remappings=[
        #         ('reference_geopose', robot_name + '/geopose'),
        #     ],
        )

    return LaunchDescription([
        # Decalre arguments
        DeclareLaunchArgument(
            'robot_name', default_value = 'my_robot'            
        ),

        DeclareLaunchArgument(
            'usbl_acomm_delay', default_value = '0.0'            
        ),

        # Delay the node if needed
        TimerAction(
            period=PythonExpression([usbl_acomm_delay]),
            actions=[node]
        ),

        #    #USBL to ship TF setup
        #    Node(
        #     package='tf2_ros',
        #     executable='static_transform_publisher',
        #     name='ship2usbl',
        #     arguments = ["2.0", "0.0", "0.0", "0.0", "0.0", "3.1415926", robot_name+'/ship_link', robot_name+'/usbl']    
        #     #              x, y,z,yaw,pitch,roll
        # ),
])
