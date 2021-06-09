# Alesis V Series
![Layout](layout.png)
Source: Screenshot of Alesis V25 Editor

## List of controllers
Since the Alesis V25, the Alesis V49 and the Alesis V61 are basically the same controller only differing in the number of keys only one device script is needed.

__Right now the configuration for the V49 and the V61 are missing. This isn't a problem as it's basically the default configuration with the switches set to momentary mode instead of toggle mode as well as linear velocity curve for the keys.__

## Features
The controllers from the Alesis V Series are a MIDI keyboards with
* 25/49/61 velocity sensitive full size keys
* 8 velocity sensitive drum pads
* 4 switches
* 4 rotary potentiometers
* pitch wheel
* mod wheel

## Instalaltion
Install the script (`device_Alesis_V_Series.py`) to the user data folder as described in the main `README.md`. Next send the configuration file (`configuration.vXX`) to the controller using the manufacturers utility ([Alesis V25 Editor](https://alesis.com/products/view2/v25)/[Alesis V49 Editor](https://alesis.com/products/view2/v49)/[Alesis V61 Editor](https://alesis.com/products/view2/v61)).

## Overall settings
The velocity curves are adjusted to make it feel more responsive.

This script provides three modes. For changing the mode switches 1, 2 and 3 can be used. Switch 4 can be used as usual. To make the LEDs work correctly make sure to set the input and the output device called `V25`/`V49`/`V61` to the same dedicated port. Unfortunately, there is no visual feedback on which mode is currently selected.

### Transport Mode (default) - Switch 1
This mode can be activated with switch 1. It maps the drum pads the following way:
* Pad 1: pattern/song mode
* Pad 2: play/pause
* Pad 3: stop
* Pad 4: record
* Pad 5-8: deactivated to prevent unwanted triggering

Adding functionality to the Pads 5-8 (like loop recording, metronome activation, bpm tapping) is currently on the to do list. 

### FPC Mode - Switch 2
The FPC Mode remaps the drum pads to play the notes with default FPC settings. It maps the drum pads the following way:
* Pad 1: Crash
* Pad 2: Closed Hat
* Pad 3: Pedal HiHat
* Pad 4: Open HiHat
* Pad 5: Kick Drum
* Pad 6: Snare 1
* Pad 7: Snare 2
* Pad 8: SideStick

### Deactivated Mode - Switch 3
The Deactivated Mode deactivates the drum pads to prevent accidentally triggering. The pads kan now be used to rest your left hand on it.