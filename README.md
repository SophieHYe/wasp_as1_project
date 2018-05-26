# `wasp_as1_project`

Code from KTH group B for the WASP Autonomous Systems 1 project using Crazyflies.

![cf2](crazyflie-2.png)

In what is described below it is assumed that you have clone this repository and entered the directory.


It is a good idea to run this in a [`virtualenv`](https://pypi.org/project/virtualenv/). It is not a good idea to run this in a virtual machine, since the delays will cause instability.

## Dependencies

Make sure that you have python3 and pip3 installed. On a Ubuntu system you would

```
sudo apt-get install python3 python3-pip python3-pyqt5 python3-pyqt5.qtsvg
```

or on OS X

```
brew install python3 sdl sdl2 sdl_image sdl_mixer sdl_ttf libusb portmidi pyqt5
```

Then install the bitcraze (and other) dependencies
```sh
pip3 install -r requirements.txt
```

## Run

```sh
python3 cf_pc_control.py
```

## Crazyradio PA USB Dongle

If you run on Linux and you system is not recognizing the USB radio dongle you probably want to do

```
sudo groupadd plugdev
sudo usermod -a -G plugdev $USER
echo 'SUBSYSTEM=="usb", ATTRS{idVendor}=="1915", ATTRS{idProduct}=="7777", MODE="0664", GROUP="plugdev"' | sudo tee /etc/udev/rules.d/99-crazyradio.rules
echo 'SUBSYSTEM=="usb", ATTRS{idVendor}=="0483", ATTRS{idProduct}=="5740", MODE="0664", GROUP="plugdev"' | sudo tee /etc/udev/rules.d/99-crazyflie.rules
sudo udevadm control --reload-rules
sudo service udev restart
```

Unplug the radio and plug it in again and it should be recognized

# Flying

PID-controller parameters and coordinates are set in `config.json`. Coordinates can be relative (to starting position) or absolute.

![orientation](https://wiki.bitcraze.io/_media/doc:lps:crazyflie_isometric_drawing_2.png) 

```
{
    "radio": "radio://0/98/2M",
    "pitchroll": {
        "kP": 1.2, "kD": 0.8, "kI": 0
    },
    "thrust": {
        "kP": 1.2, "kD": 0.4, "kI": 0.01, "C": 0.147
    },
    "yaw": {
        "kP": 2, "kD": 0.2, "kI": 0
    },
    "m": 30e-3,
    "g": 9.82,
    "coordinates": {
        "relative": true,
        "x": [0, 0.5, -0.5, 0, 0, 0],
        "y": [0, 0, 0, 0.5, -0.5 ],
        "z": [0.5, 0.5, 0.5, 0.5, 0.5, 0.2],
        "yaw": [0.0, 0, 0.0, 0.0, 0.0, 0.0]
    },
    "waypoint_margin": 0.05
}
```

The configuration is read everytime the log is printed to the screen so that you can adjust the parameters while flying.

This code is tested with [Flowdeck](https://www.bitcraze.io/flow-deck/) and [LPS](https://www.bitcraze.io/loco-pos-system/).

