# Linode-DDNS

## Installation:
### Linux:
Move the Linode-DDNS folder into /opt like `mv Linode-DDNS/ /opt`

### **OR:**
Move the folder to a prefered location, and change the directory from WorkingDirectory and ExecStart in linodeddns.service

Copy the linodeddns.service file into /lib/systemd/system like: `cp linodeddns.service /lib/systemd/system`

To reload systemd, run `sudo systemctl daemon-reload`, and to make it start on boot, run `sudo systemctl enable linodeddns.service`