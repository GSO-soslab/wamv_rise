# check USB device
```sh
# give you detail info for the USB device
lsusb -v | grep -A 10 "U-Blox"

# make a rules
cd /etc/udev/rules.d
sudo vim 99-{DEVICE}.rules
# with folloing examples:
# SUBSYSTEM=="tty", ATTRS{idVendor}=="0403", ATTRS{idProduct}=="d9a9", ATTRS{serial}=="28EA9", SYMLINK+="airmar"

# enable the new rules
sudo udevadm control --reload-rules  
sudo service udev restart 
sudo udevadm trigger
```