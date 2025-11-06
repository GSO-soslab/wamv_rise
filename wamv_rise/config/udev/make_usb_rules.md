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


# Setup new USB device
```sh
# find new device (not has udev symbolic link: A -> /dev/ttyUSB*), for example: /dev/ttyUSB0
ls -l /dev/ | grep ttyUSB* 
ls -l /dev/ | grep ttyACM*

# get the Vendor ID
udevadm info -q property -n /dev/ttyUSB4 | grep ID_VENDOR_ID

# get the idProduct
udevadm info -q property -n /dev/ttyUSB4 | grep ID_USB_MODEL_ID

# get serial number
udevadm info -q property -n /dev/ttyUSB4 | grep ID_USB_SERIAL_SHORT

# cpoy the rules
```