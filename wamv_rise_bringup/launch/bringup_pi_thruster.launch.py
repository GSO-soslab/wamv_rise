import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource

def generate_launch_description():

    robot_name = 'wamv_rise'

    # Torqeedo Thrusters
    torqeedo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            os.path.join(get_package_share_directory('wamv_rise_bringup'), 
            'launch/include/torqeedo_thrusters.launch.py')]),
        launch_arguments={
            'robot_name': robot_name,
            'torqeedo_delay': '0.0'
        }.items()  
    )

    # Vehicle Joy
    # joy = IncludeLaunchDescription(
    #     PythonLaunchDescriptionSource([
    #         os.path.join(get_package_share_directory('wamv_rise_bringup'), 
    #         'launch/include/vehicle_joy.launch.py')]),
    #     launch_arguments={
    #         'robot_name': robot_name,
    #         'joy_delay': '0.0'
    #     }.items()  
    # )

    return LaunchDescription([
        torqeedo,
        # joy,
    ])