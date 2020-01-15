# eLab_WS2801

Printer Status Messages via WS2081 RGB-LEDs for Octoprint on Raspberry-Pi.

## Setup

Important: SPI Interface must be activated. Use "sudo raspi-config" to activate.

Install via the bundled [Plugin Manager](https://github.com/foosel/OctoPrint/wiki/Plugin:-Plugin-Manager)
or manually using this URL:

    https://github.com/eLab-Siegen/octoprint_eLab_WS2801/archive/master.zip

## Wiring
| WS2801          | Rasperry Pi   |
| -------------   |---------------|
| Clock (CK / CL) | Pin 23        |
| Data (SI / DI)  | Pin 19        |
| Ground (GND)    | Pin 6         |
      

## Configuration

Currently no configuration.
