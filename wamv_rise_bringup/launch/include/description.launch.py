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
    description_delay = LaunchConfiguration('description_delay')

    # Node param
    urdf = Path(
        get_package_share_directory('wamv_rise_description'), 
        'urdf/base.urdf'
    )
    with open(urdf, 'r') as infp:
        robot_desc = infp.read()

    # State Publisher node
    tf_states = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='robot_state_publisher',
        namespace=robot_name,
        # output='screen',
        parameters=[{'robot_description' : robot_desc},
                    {'frame_prefix': [robot_name, '/']}],
    )
    
    # Static Publisher node
    tf_enu_ned = Node(
        package='tf2_ros',
        executable='static_transform_publisher',
        name='world2ned',
        arguments = ["0.0", "0.0", "0.0", "1.570796327", "0.0", "3.141592653589793", 
                    #  robot_name+'/world', 
                    [robot_name, '/world'],
                    [robot_name, '/world_ned']
                    #  robot_name+'/world_ned'
                    ]    
    )
        
    return LaunchDescription([

        # Decalre arguments
        DeclareLaunchArgument(
            'robot_name', default_value = 'my_robot'            
        ),

        DeclareLaunchArgument(
            'description_delay', default_value = '0.0'            
        ),

        # Delay the node if needed
        TimerAction(
            period=PythonExpression([description_delay]),
            actions=[tf_states]
        ),

        TimerAction(
            period=PythonExpression([description_delay]),
            actions=[tf_enu_ned]
        ),

    ])
