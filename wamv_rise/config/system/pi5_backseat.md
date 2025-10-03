## PI5 using systemd-networkd

```sh
network:
  version: 2
  wifis:
      # hidden wifi
      wlan0:
        optional: true
        dhcp4: true
        access-points:
            "SSID_NAME":
                hidden: true
                password: "WIFI_PASSWORD"

  ethernets:
    eth0:
      match:
        macaddress: d8:3a:dd:e4:a2:16
      dhcp4: false
      addresses: [192.168.2.91/24]

```

## PI5 SSD setup
```sh
# change the ownership
sudo chown -R mvp_admin:mvp_admin /home/mvp_admin/ssd/
# check
touch /home/mvp_admin/ssd/test.txt
```