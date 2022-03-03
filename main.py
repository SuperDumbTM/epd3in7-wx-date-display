#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys, getopt
import os
import logging
from lib import epd3in7, weather_info
import time
from PIL import Image,ImageDraw,ImageFont
import traceback

# user input
DIST = ""
RAINFALL_DIST = ""
VERBOSE_FLAG = False
# set font
font24 = ImageFont.truetype("./font/msjh.ttc", 24)
font18 = ImageFont.truetype("./font/msjh.ttc", 18)
font14 = ImageFont.truetype("./font/msjh.ttc", 14)

def drawFrame(epd):
    epd.init(0)
    epd.Clear(0xFF, 0)
    Himage = Image.new('L', (epd.height, epd.width), 0xFF)  # 0xFF: clear the frame, draw white
    draw = ImageDraw.Draw(Himage)
    draw.text((10, 0), 'hello world', font = font24, fill = 0)
    epd.display_4Gray(epd.getbuffer_4Gray(Himage))
    time.sleep(5)
    epd.init(0)
    epd.Clear(0xFF, 0)

def main(argv):

    opts, args = getopt.getopt(argv[1:],'d:r:vh',["district=","rainfaill-district=","verbose","help"])
    for opt,arg in opts:
        if opt in ['-d', '--district']:
            DIST = arg
        elif opt in ['-r', '--rainfaill-district']:
            RAINFALL_DIST = arg
        elif opt in ['-v', '--verbose']:
            VERBOSE_FLAG = True
        elif opt in ['-h', '--help']:
            pass

    try:
        wx = weather_info.WeatherInfo()
        epd = epd3in7.EPD()


        drawFrame()

    except IOError as e:
        logging.info(e)
        
    except KeyboardInterrupt:    
        logging.info("ctrl + c:")
        epd3in7.epdconfig.module_exit()
        exit()


if __name__==__main__:
    main()