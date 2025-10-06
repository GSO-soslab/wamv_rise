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

    # Nortek1000 DVL
    nortek = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            os.path.join(get_package_share_directory('wamv_rise_bringup'), 
            'launch/include/nortek_dvl.launch.py')]),
        launch_arguments={
            'robot_name': robot_name,
            'nortek_delay': '6.0'
        }.items()  
    )

    # Airmar weatherstation
    airmar = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            os.path.join(get_package_share_directory('wamv_rise_bringup'), 
            'launch/include/airmar_ws.launch.py')]),
        launch_arguments={
            'robot_name': robot_name,
            'airmar_delay': '9.0'
        }.items()  
    ) 

    # USB GPS
    usb_gps = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            os.path.join(get_package_share_directory('wamv_rise_bringup'), 
            'launch/include/gpsd_usb_gps.launch.py')]),
        # launch_arguments={
        #     'robot_name': robot_name,
        #     'gps_delay': '9.0'
        # }.items()  
    )     

    # Evologics USBL
    usbl = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            os.path.join(get_package_share_directory('wamv_rise_bringup'),
            'launch/include/evologics_usbl.launch.py')]),
    )

    return LaunchDescription([
        xsens,
        unicore,
        nortek,
        airmar,
        usb_gps,
        usbl
    ])