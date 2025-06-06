import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource

def generate_launch_description():

    robot_name = 'wamv_rise'

    # MVP Control
    control = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            os.path.join(get_package_share_directory('wamv_rise_bringup'), 
            'launch/include/mvp_control.launch.py')]),
        launch_arguments={
            'robot_name': robot_name,
            'control_delay': '0.0'
        }.items()  
    )

    # MVP Mission
    mission = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            os.path.join(get_package_share_directory('wamv_rise_bringup'), 
            'launch/include/mvp_mission.launch.py')]),
        launch_arguments={
            'robot_name': robot_name,
            'mission_delay': '0.0'
        }.items()  
    )

    return LaunchDescription([
        control,
        mission,
    ])