#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys, getopt
import os
import logging
from lib import epd3in7, weather_info
import time
from PIL import Image,ImageDraw,ImageFont
import traceback

# path
picdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'pic')
libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)
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

    frame = Image.new('L', (epd.height, epd.width), 0xFF)  # 0xFF: clear the frame, draw white
    draw = ImageDraw.Draw(frame)
    draw.text((10, 0), 'hello world', font = font24, fill = 0)
    epd.display_4Gray(epd.getbuffer_4Gray(frame))
    time.sleep(5)

    print(os.path.join(picdir, "3in7_Scale.bmp"))
    Himage=Image.open(os.path.join(picdir, "3in7_Scale.bmp"))
    print("after Himage")
    epd.display_4Gray(epd.getbuffer_4Gray(Himage))
    time.sleep(5)

    Limage = Image.new('L', (epd.width, epd.height), 0xFF)  # 0xFF: clear the frame
    draw = ImageDraw.Draw(Limage)
    draw.text((2, 0), 'hello world', font = font18, fill = 0)
    draw.text((2, 20), '3.7inch epd', font = font18, fill = 0)
    draw.rectangle((130, 20, 274, 56), 'black', 'black')
    epd.display_4Gray(epd.getbuffer_4Gray(Limage))
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


        drawFrame(epd)

    except IOError as e:
        logging.info(e)
        
    except KeyboardInterrupt:    
        logging.info("ctrl + c:")
        epd3in7.epdconfig.module_exit()
        exit()


if __name__=="__main__":
    main(sys.argv)