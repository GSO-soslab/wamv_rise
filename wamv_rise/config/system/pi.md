
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