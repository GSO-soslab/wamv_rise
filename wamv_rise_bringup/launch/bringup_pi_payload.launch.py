import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource

def generate_launch_description():

    robot_name = 'wamv_rise'

    # Xsens AHRS
    xsens = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            os.path.join(get_package_share_directory('wamv_rise_bringup'), 
            'launch/include/xsens_ahrs.launch.py')]),
        launch_arguments={
            'robot_name': robot_name,
            'xsens_delay': '0.0'
        }.items()  
    )

    # Unicore RTK GPS
    unicore = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            os.path.join(get_package_share_directory('wamv_rise_bringup'), 
            'launch/include/unicore_rtk.launch.py')]),
        launch_arguments={
            'robot_name': robot_name,
            'unicore_delay': '3.0'
        }.items()  
    )

    return LaunchDescription([
        xsens,
        unicore,
    ])