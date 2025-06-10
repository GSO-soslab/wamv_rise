
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