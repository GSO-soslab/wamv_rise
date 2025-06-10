## install livox
```sh
## install other dependences:
sudo apt install ros-jazzy-pcl-ros
## install ros2 driver
git clone https://github.com/GSO-soslab/livox_ros2_driver
## build (it will auto install the SDK)
colcon build --parallel-worker $(nproc)
```
