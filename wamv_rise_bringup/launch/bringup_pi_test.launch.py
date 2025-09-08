import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_xml.launch_description_sources import XMLLaunchDescriptionSource

def generate_launch_description():

    robot_name = 'wamv_rise'

    nortek = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            os.path.join(get_package_share_directory('wamv_rise_bringup'), 
            'launch/include/nortek_dvl.launch.py')]),
        launch_arguments={
            'robot_name': robot_name,
            'nortek_delay': '6.0'
        }.items()  
    )


    return LaunchDescription([
        nortek,
    ])    