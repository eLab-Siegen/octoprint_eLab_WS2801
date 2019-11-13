# coding=utf-8
from __future__ import absolute_import

import octoprint.plugin

from threading import Thread

# Simple demo of of the WS2801/SPI-like addressable RGB LED lights.
import time
import RPi.GPIO as GPIO

# Import the WS2801 module.
import Adafruit_WS2801
import Adafruit_GPIO.SPI as SPI

# Configure the count of pixels:
PIXEL_COUNT = 64
PROGRESSBAR = 15

# Alternatively specify a hardware SPI connection on /dev/spidev0.0:
SPI_PORT   = 0
SPI_DEVICE = 0
pixels = Adafruit_WS2801.WS2801Pixels(PIXEL_COUNT, spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE), gpio=GPIO)


class eLab_WS2801_Plugin(octoprint.plugin.EventHandlerPlugin, octoprint.plugin.ProgressPlugin):

    event_switch = {
	"Startup": [73, 245, 228],
	"Shutdown": [0, 0, 0],
	"ClientOpened": [0, 255, 145],
	"ClientClosed": [73, 245, 228],
	"Connected": [0, 255, 26],
	"Disconnected": [255, 0, 242],
	"Error": [255, 0, 0],
	"PrintStarted": [255, 255, 255],
	"PrintFailed": [199, 4, 49],
	"PrintDone": [0, 255, 0],
	"PrintCancelled": [255, 255, 0]
    }

    def ws2801_all(self, r, g, b):
        pixels.clear()
        for x in range(PIXEL_COUNT):
            pixels.set_pixel(x, Adafruit_WS2801.RGB_to_color( r, g, b ))
        pixels.show()


    def toolchange(self):
        self.ws2801_all(255, 145, 0)
        time.sleep(30)
        self.ws2801_all(255, 255, 255)
        _stop()


    def on_event(self, event, payload):
        if event in self.event_switch:
            rgb = self.event_switch[event]
            self.ws2801_all(rgb[0], rgb[1], rgb[2])

	    if event == "ToolChange":
	        t = Thread(target=self.toolchange, args=())
	        t.start()


    def  on_print_progress(self, storage, path, progress):
        for x in range(PROGRESSBAR):
            pixels.set_pixel(x, Adafruit_WS2801.RGB_to_color( 0, 0, 255 ))
        pixels.set_pixel((PROGRESSBAR - (progress * (100 / PROGRESSBAR))), Adafruit_WS2801.RGB_to_color( 0, 255, 0 ))
        pixels.show()
    
    

__plugin_implementation__ = eLab_WS2801_Plugin()
