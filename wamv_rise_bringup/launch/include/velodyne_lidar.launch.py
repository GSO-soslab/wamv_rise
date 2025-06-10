import launch
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, RegisterEventHandler, TimerAction, SetEnvironmentVariable
from launch.substitutions import LaunchConfiguration
from launch.substitutions import PythonExpression
from launch.event_handlers import OnProcessExit
from ament_index_python.packages import get_package_share_directory
from pathlib import Path
from launch_ros.actions import ComposableNodeContainer
from launch_ros.descriptions import ComposableNode
import os
import yaml

def generate_launch_description():

    # ======================================================================= #
    # Node Arguments
    # ======================================================================= #
    robot_name = DeclareLaunchArgument(
        'robot_name', default_value='my_robot'
    )
    velodyne_delay = DeclareLaunchArgument(
        'velodyne_delay', default_value='0.0'
    )

    # ======================================================================= #
    # Param
    # ======================================================================= #
    config_directory = os.path.join(
        get_package_share_directory('wamv_rise_bringup'),
        'config')

    # load driver parametetrs
    driver_file = os.path.join(config_directory, 'velodyne_driver.yaml')
    with open(driver_file, 'r') as f:
        driver_params = yaml.safe_load(f)['/wamv_rise/velodyne_driver_node']['ros__parameters']
    driver_params['frame_id'] = [LaunchConfiguration('robot_name'), '/velodyne']

    # load pointcloud processing parametetrs
    pointcloud_file = os.path.join(config_directory, 'velodyne_pointcloud.yaml')
    with open(pointcloud_file, 'r') as f:
        pointcloud_params = yaml.safe_load(f)['/wamv_rise/velodyne_transform_node']['ros__parameters']

    # set the Lidar calibration parametetr
    share_dir = get_package_share_directory('velodyne_pointcloud')        
    pointcloud_params['calibration'] = os.path.join(share_dir, 'params', 'VLP16db.yaml')

    # ======================================================================= #
    # Composable Node
    # ======================================================================= #        

    container = ComposableNodeContainer(
            name='velodyne_driver_container',
            namespace='velodyne_lidar',
            package='rclcpp_components',
            executable='component_container',
            composable_node_descriptions=[
                ComposableNode(
                    package='velodyne_driver',
                    plugin='velodyne_driver::VelodyneDriver',
                    name='velodyne_driver_node',
                    namespace=LaunchConfiguration('robot_name'),
                    parameters=[driver_params]),
                ComposableNode(
                    package='velodyne_pointcloud',
                    plugin='velodyne_pointcloud::Transform',
                    name='velodyne_transform_node',
                    namespace=LaunchConfiguration('robot_name'),
                    parameters=[pointcloud_params]),
            ],
            output='both',
    )

    # ======================================================================= #
    # Actions
    # ======================================================================= #   

    # Shutdown Handler
    shutdown_on_exit = RegisterEventHandler(
        event_handler=OnProcessExit(
            target_action=container,
            on_exit=[launch.actions.EmitEvent(event=launch.events.Shutdown())]
        )
    )

    # Delay the node
    delayed_container = TimerAction(
        period=LaunchConfiguration('velodyne_delay'),
        actions=[
            container,
            shutdown_on_exit
        ]
    )

    # ======================================================================= #
    # Return
    # ======================================================================= #   

    return LaunchDescription([
        robot_name,
        velodyne_delay, 
        delayed_container
    ])
