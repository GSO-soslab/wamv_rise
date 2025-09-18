from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch.substitutions import PythonExpression
from launch.actions import SetEnvironmentVariable
from launch.actions import TimerAction
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
from pathlib import Path
import os

def generate_launch_description():

    # Node argument
    robot_name = LaunchConfiguration('robot_name')
    localization_delay = LaunchConfiguration('localization_delay')

    # Node param
    localization_param_file = Path(
        get_package_share_directory('wamv_rise_bringup'), 
        'config/localization.yaml'
    )
     
    mag_model_path = os.path.join(
        get_package_share_directory('mvp_localization_utilities'), 
        'config/magnetic/'
    )

    init_file = Path(
        get_package_share_directory('wamv_rise_bringup'), 
        'config/initialization.yaml'
    )    

    # Robot_Localization node
    localization = Node(
            package='robot_localization',
            executable='ekf_node',
            name='ekf_filter_node',
            namespace=robot_name,
            # output='screen',
            parameters=[localization_param_file],
            emulate_tty=True        
    )

    # Initialization node
    initialization = Node(
            package='mvp_localization_utilities',
            executable='world_odom_transform_node',
            name='world_odom_transform_node',
            namespace=robot_name,
            output='screen',
            prefix=['stdbuf -o L'],
            parameters=[
                {'tf_prefix': robot_name},
                {'mag_model_path': mag_model_path},
                 init_file
            ],
            remappings=[
                        ('gps/fix', 'unicore_rtk/fix'),
                        ('gps/odometry', 'unicore_rtk/gps_odometry'),
                        ('odometry', 'odometry/filtered'),
                        ('depth', 'nortek_dvl/depth_odometry') ],
            emulate_tty=True        
    )

    # Other GPS odometry 

    # xsens_gps_node = Node(
    #     package='mvp_localization_utilities',
    #     executable='gps_world_odom_publisher',
    #     name='xsens_gps_world_odom_publisher',
    #     namespace=robot_name,
    #     output='screen',
    #     prefix=['stdbuf -o L'],
    #     parameters=[
    #         {'tf_prefix': robot_name},
    #         {'gps_frame': 'xsens_gps'},
    #         {'acceptable_var': 10.0}, 
    #         {'manual_position_covariance': 10.0}    
    #         ],
    #     remappings=[
    #             ('gps/fix', 'xsens_ahrs/gnss'),
    #             ('gps/world_odometry', 'xsens_ahrs/gps_odometry'),
    #         ],
    #     emulate_tty=True
    # ) 

    # airmar_gps_node = Node(
    #     package='mvp_localization_utilities',
    #     executable='gps_world_odom_publisher',
    #     name='airmar_gps_world_odom_publisher',
    #     namespace=robot_name,
    #     output='screen',
    #     prefix=['stdbuf -o L'],
    #     parameters=[
    #         {'tf_prefix': robot_name},
    #         {'gps_frame': 'airmar_gps'},
    #         {'acceptable_var': 10.0}, 
    #         {'manual_position_covariance': 6.5}    
    #         ],
    #     remappings=[
    #             ('gps/fix', 'airmar/gps_fix'),
    #             ('gps/world_odometry', 'airmar/gps_odometry'),
    #         ],
    #     emulate_tty=True
    # ) 

    return LaunchDescription([

        # Decalre arguments
        DeclareLaunchArgument(
            'robot_name', default_value = 'my_robot'            
        ),

        DeclareLaunchArgument(
            'localization_delay', default_value = '0.0'            
        ),

        # Delay the node if needed
        TimerAction(
            period=PythonExpression([localization_delay]),
            actions=[localization]
        ),

        TimerAction(
            period=PythonExpression([localization_delay]),
            actions=[initialization]
        ),   

        # TimerAction(
        #     period=PythonExpression([localization_delay]),
        #     actions=[xsens_gps_node]
        # ),  

        # TimerAction(
        #     period=PythonExpression([localization_delay]),
        #     actions=[airmar_gps_node]
        # ),                     
    ])
