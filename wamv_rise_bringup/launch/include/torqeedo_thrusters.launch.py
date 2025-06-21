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
    torqeedo_delay = LaunchConfiguration('torqeedo_delay')

    # Node param
    port_parameters_file = Path(
        get_package_share_directory('wamv_rise_bringup'), 
        'config/torqeedo_port.yaml'
    )

    stbd_parameters_file = Path(
        get_package_share_directory('wamv_rise_bringup'), 
        'config/torqeedo_stbd.yaml'
    )

    # Port Thruster
    node_port = Node(
        package="torqeedo_motor",
        executable="torqeedo_motor_node",
        name="torqeedo_port",
        namespace=robot_name,
        output="screen",
        remappings=[
            # ('control/speed_mode', '/wamv/joy_mode'),
            # ('control/joy_speed', '/wamv/port_thruster'),

            # ('control/speed_mode', '/wamv_rise/rf_joy/joy_mode'),
            # ('control/joy_speed', '/wamv_rise/rf_joy/port_thruster'),
            ('torqeedo_port/control/speed_mode', 'rf_joy/joy_mode'),
            ('torqeedo_port/control/joy_speed', 'rf_joy/port_thruster'),
        ],
        parameters=[port_parameters_file],          
        emulate_tty=True
    )

    # Stbd motor
    node_stbd = Node(
        package="torqeedo_motor",
        executable="torqeedo_motor_node",
        name="torqeedo_stbd",
        namespace=robot_name,
        output="screen",
        remappings=[
            ('torqeedo_stbd/control/speed_mode', 'rf_joy/joy_mode'),
            ('torqeedo_stbd/control/joy_speed', 'rf_joy/starboard_thruster'),
        ],
        parameters=[stbd_parameters_file],
        emulate_tty=True
    )
        

    return LaunchDescription([

        # Decalre the arguments
        DeclareLaunchArgument(
            'robot_name', default_value = 'my_robot'            
        ),

        DeclareLaunchArgument(
            'torqeedo_delay', default_value = '0.0'        
        ),

        # Delay the node if needed
        TimerAction(
            period=PythonExpression([torqeedo_delay]),
            actions=[node_port]
        ),

        TimerAction(
            period=PythonExpression([torqeedo_delay]),
            actions=[node_stbd]
        ),

    ])
