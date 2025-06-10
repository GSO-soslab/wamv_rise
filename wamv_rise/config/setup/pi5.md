## install livox
```sh
## install SDK, from:  
cd 
mkdir 3rd
cd 3rd
git clone https://github.com/Livox-SDK/Livox-SDK2.git
# modify the code from: https://github.com/Livox-SDK/Livox-SDK2/issues/90
cd Livox-SDK2
mkdir build
cd build
cmake .. && make -j2
sudo make install

## install other dependences:
sudo apt install ros-jazzy-pcl-ros

## install ros2 driver
git clone https://github.com/GSO-soslab/livox_ros_driver2
git checkout jazzy-devel
cd livox_ros_driver2
./build.sh jazzy
```
