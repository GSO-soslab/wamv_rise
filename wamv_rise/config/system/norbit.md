
## Norbit:

### Basic configuration for static IP when norbit is configured in DHCP:
1) The DHCP config configured the norbit as static IP here: `/etc/dhcp/dhcpd.conf`
```conf
subnet 192.168.3.0 netmask 255.255.255.0{
  range 192.168.3.100 192.168.3.200; # DCHP range 
  option routers 192.168.3.1; # Default gateway
  option subnet-mask 255.255.255.0;
  option broadcast-address 192.168.3.255;
  option domain-name-servers 8.8.8.8; # google's DNS
}

host norbit{
  hardware ethernet 70:B3:D5:F4:5A:13;  # MAC address
  fixed-address 192.168.3.179; # sensor IP address
}
```
2) Ethernet port setup in here: `/etc/default/isc-dhcp-server`. Please check the actual port used for norbit use `ifconfig`
```conf
INTERFACESv4="eth0"
```
3) Restart the service
```sh
# check status
sudo systemctl status isc-dhcp-server
# restart service
sudo systemctl restart isc-dhcp-server 
# check the failed reason
sudo journalctl -u isc-dhcp-server --no-pager | tail -30
``` 

### Auto set if the norbit powered at unknown time:

1) configure a service to auto start the isc-dhcp-server if something failed (**SELECTED**)
  - setup the config file: `/etc/systemd/system/isc-dhcp-server.service`
    ```sh
    [Unit]
    Description=ISC DHCP Ipv4 server
    After=network-online.target
    Wants=network-online.target

    [Service]
    ExecStart=/usr/sbin/dhcpd -4 -f -cf /etc/dhcp/dhcpd.conf eth0
    Restart=on-failure
    RestartSec=5

    [Install]
    WantedBy=multi-user.target
    ```
  - restart the service: 
    ```sh
    sudo systemctl daemon-reload
    sudo systemctl enable isc-dhcp-server
    sudo systemctl restart isc-dhcp-server
    sudo systemctl status isc-dhcp-server
    # check service issue
    sudo journalctl -u isc-dhcp-server --no-pager
    ```
  - if still something wrong, remove this service file and run `sudo systemctl restart isc-dhcp-server` right after norbit is power on. 

### NTP time sync
```sh
# rosservice method after roslaunch driver
rosservice call /wamv_rise/norbit/norbit_node/norbit_cmd "cmd: 'set_ntp_server'
val: '192.168.3.90'"
# telnet method
telnet 192.168.3.179 2209
# set 
set_ntp_server 192.168.3.90
# check
ntp_log
# exit
ctrl + ] quit
```

```sh
# ros2
ros2 service call /wamv_rise/norbit_mbes/norbit_cmd norbit_msgs/srv/NorbitCmd "{cmd: 'set_ntp_server', val: '192.168.2.55'}"
# telnet method
telnet 192.168.2.130 2209
# set 
set_ntp_server 192.168.2.55
# check
ntp_log
# exit
ctrl + ] quit
```