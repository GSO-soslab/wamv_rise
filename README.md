# WAMV configuration for [RISE project](https://soslab.wordpress.com/rise/)


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