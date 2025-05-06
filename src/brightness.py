#!/usr/bin/env python3

from Raspbot_Lib import Raspbot
import time

car = Raspbot()
car.Ctrl_WQ2812_brightness_ALL( 255, 255, 255)
time.sleep(1)
car.Ctrl_WQ2812_brightness_ALL( 0, 0, 0)
