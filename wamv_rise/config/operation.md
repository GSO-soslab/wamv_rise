0) launch base payload: RF
```sh
cd /home/soslab/Develop/ros/wamv_ws
source devel/setup.bash
roslaunch wamv_rise_bringup bringup_base_payload.launch
```

1) launch pi payload:
```sh
roslaunch wamv_rise_bringup bringup_pi_payload.launch
# check gps
cgps -s
# check chrony
watch -n -0.1 chronyc sources -v
```

2) launch thruster:
```sh
roslaunch wamv_rise_bringup bringup_pi_thruster.launch 
```

3) launch untilities:
```sh
roslaunch wamv_rise_bringup bringup_pi_utilities.launch
```

4) open jetson: Jetson, Velodyne, Livox, big router
```sh
# open Jetson side power: 
rosservice call /wamv_rise/gpio_manager/set_power_jetson_board "data: true"
# ping Jetson:
ping 192.168.2.90
# check jetson time:
watch -n -0.1 chronyc sources -v
```

5) open underwater payload: DVL, USBL, Norbit
```sh
# open power
rosservice call /wamv_rise/gpio_manager/set_power_underwater_payload "data: true"
# check norbit DHCP
ping 192.168.3.179
# check DVL
ping 192.168.2.110
# ping USBL
ping 192.168.2.109
# check DVL time sync
rostopic hz /wamv_rise/dvl/bottom_track -c
```

6) open Jetson payload: 
```sh
# launch payload:
roslaunch wamv_rise_bringup bringup_jetson_payload.launch
# check Jetson system time:
watch -n -0.1 date +%s
# check Livox time sync:
rostopic echo /wamv_rise/livox/lidar/header -c
# enable norbit time sync:
rosservice call /wamv_rise/norbit/norbit_node/norbit_cmd "cmd: 'set_ntp_server'
val: '192.168.3.90'"
# check norbit time
rostopic echo /wamv_rise/norbit/cloud/header -c
```

7) WAMV navigation:
```sh
# launch localization
roslaunch wamv_rise_bringup bringup_pi_localization.launch
# reset datum
rosservice call /wamv_rise/world_odom_transform_node/reset_datum "{}"
# launch mvp
roslaunch wamv_rise_bringup bringup_pi_mvp.launch 
```