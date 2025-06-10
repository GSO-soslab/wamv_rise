
## Livox
- install ptpd: `sudo apt install ptpd`
- check the Livox subnet belong which netowrk interface using `ifconfig`
- method 1: use the default ptpd config by modifying file `/etc/default/ptpd` as following
  ```sh
  # /etc/default/ptpd

  # Set to "yes" to actually start ptpd automatically
  START_DAEMON="yes"

  # Add command line options for ptpd
  PTPD_OPTS="-M -i eth2 -C"
  ```
- method2: configure a service to auto start the ptpd if something failed (**SELECTED**)
  - setup the config file: `/etc/systemd/system/ptpd.service`
    ```sh
    [Unit]
    Description=ptpd time synchronization
    After=network-online.target
    Wants=network-online.target

    [Service]
    ExecStart=/usr/sbin/ptpd -M -i eth2 -C
    Restart=on-failure
    RestartSec=5

    [Install]
    WantedBy=multi-user.target
    ```
  - restart the service:
    ```sh
    sudo systemctl daemon-reload
    sudo systemctl enable ptpd
    sudo systemctl restart ptpd
    sudo systemctl status ptpd
    # check service issue
    sudo journalctl -u ptpd --no-pager
    ```
- check the timestamp:
```sh
# check ros time
rostopic echo /wamv_rise/livox/lidar/header -c
# check system time
watch -n -0.1 date +%s
```