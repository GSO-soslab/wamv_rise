
## Pi time sync: gpsd + chrony
- install dependency
```sh
sudo apt install gpsd gpsd-clients pps-tools chrony
```
- copy the following to the file: `/etc/default/gpsd`
```sh
# Devices gpsd should collect to at boot time.
# They need to be read/writeable, either by user gpsd or the group dialout.

# Start at boot time
START_DAEMON="true"
# Get the data from UDP, which from airmar ros driver
DEVICES="udp://127.0.0.1:5005"
# Other options you want to pass to gpsd
GPSD_OPTIONS="-n"
```
- check:
```sh
# restart
sudo systemctl restart gpsd
# check data
cgps -s
```
- copy following to the file `/etc/chrony/chrony.conf`:
```sh
### /etc/chrony/chrony.conf ###

#### This conf used for time sync from GPS 

## Internet server
pool ntp.ubuntu.com iburst maxsources 4

driftfile /var/lib/chrony/drift

# make it serve time even if it is not synced (as it can't reach out)
local stratum 10

## Used for NTP time sync for other system (e.g. DVL, Topside)
allow 192.168.2.0/24
local stratum 8

## Used for time sync from gpsd daemon (NMEA string) 
makestep 1.0 3
maxupdateskew 100.0
refclock SHM 0 poll 2 refid GPS precision 1e-1 offset 0.128 trust
initstepslew 30
```
- check:
```sh
# restart
sudo systemctl restart chrony
# checl data
watch -n -0.1 chronyc sources -v
```

## Pi4 using NetworkManager

```sh
network:
    version: 2
    renderer: NetworkManager
    wifis:
      #wlan0:
      #    access-points:
      #        soslab:
      #             password: d4735688c0f567c5f535a78dd633065e2af25d2f35c3bc88151f5889c390033f
      #    dhcp4: no
      #    addresses: [192.168.1.100/24]
      #    nameservers:
      #        addresses: [192.168.1.1, 8.8.8.8]
      #    gateway4: 192.168.1.1

      # hidden wifi
      wlan0:
            optional: true
            access-points:
                "SSID_NAME":
                    password: "WIFI_PASSWORD"
            dhcp4: true

    ethernets:
        eth0:
           dhcp4: no
           addresses: [192.168.2.55/24]
```