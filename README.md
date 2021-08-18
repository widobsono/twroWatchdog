# twroWatchdog
Simple watchdog to reboot and shutdown a Raspberry system

## Running
Copy the `watchdog.service` file into the `Systemd` unit file location: `sudo cp watchdog.service /etc/systemd/system/watchdog.service`

Reload the Systemd daemon (`sudo systemctl daemon-reload`) to load in the new unit file. To Run on Boot `sudo systemctl enable watchdog.service`
