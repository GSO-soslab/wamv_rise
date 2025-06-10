import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource

def generate_launch_description():

    robot_name = 'wamv_rise'

    # Livox Lidar
    livox = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            os.path.join(get_package_share_directory('wamv_rise_bringup'), 
            'launch/include/livox_lidar.launch.py')]),
        launch_arguments={
            'robot_name': robot_name,
            'livox_delay': '0.0'
        }.items()  
    )

    # Velodyne Lidar
    velodyne = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            os.path.join(get_package_share_directory('wamv_rise_bringup'), 
            'launch/include/velodyne_lidar.launch.py')]),
        launch_arguments={
            'robot_name': robot_name,
            'velodyne_delay': '0.0'
        }.items()  
    )

    # Norbit MBES
    norbit = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            os.path.join(get_package_share_directory('wamv_rise_bringup'), 
            'launch/include/norbit_mbes.launch.py')]),
        launch_arguments={
            'robot_name': robot_name,
            'norbit_delay': '0.0'
        }.items()  
    )

    return LaunchDescription([
        livox,
        velodyne,
        norbit,
    ])