
#PiTab
#The RaspberryPi flavour of the Tabularon

This version of the tabulatron is fully autonomous. Once you have the device connected and running it will communicate to the web directly. If using a RaspberryPi 3 you can use the onboard wifi to connect to Eduroam. Specifics are as follows:

##Part List
- 2 LEDS (different color)
- 6 push buttons
- 330 OHM resistor
- AdaFruit RaspiZero Proto shield
- some small gauge wire to connect the buttons
- To encapsulate it all I printed [this](https://thingiverse.com) Raspberry Pi case

##Setup
- Setup your micro SD card with the basic version of raspberry Pi
- Use `sudo raspi-config` to have the device automatically boot and login to CLI
- Download/Clone the software from github (if you are reading this look for the download button up and to the right)
- The bash script `deploy` Does most of the automatic processes
- edit `setttings.py` to set what 6 URLs you want the software to try to grab for each button
- `sudo python3 piTab.py` in the directory where you cloned it will start up the application


##Network Config
- You can connect the pi either using a LAN cable for Wifi
- There is lots of info out there about connected to a WPA2 wifi network using CLI. Heres a good one

##Eduroam
- It is possible to connect to an eduroam network with just the bare amount of fussing as follows:
- stuff for wpa_supplicant

##Make script run on startup
- add the following line to your crontab
`@reboot sudo /home/pi/piTab/boot_script`
- details on cron can be found [here](https://en.wikipedia.org/wiki/Cron)

##Misc
- A log of button presses is kept in `button_log.log`, this is useful for debugging
- Two lights, one stays on to let you know that it is working, both blink on each button press
- If the one light light shuts off, time to reboot/slash troubleshoot
- You do not have to plug in a monitor/keyboard, once you configure it to run on startup you can <ronco>set it and forget it</ronco>

