#!/usr/bin/python
# -*- coding:utf-8 -*-

import epd2in7
import time
from PIL import Image,ImageDraw,ImageFont
import traceback
import FetchWeather

WeatherCodes = (FetchWeather.GetWeather().Codes())
WeatherToday = WeatherCodes[0]
WeatherTomorrow = WeatherCodes[1]

try:
    epd = epd2in7.EPD()
    epd.init()
    epd.Clear(0xFF)
    
    # Drawing on the Horizontal image
    Himage = Image.new('1', (epd2in7.EPD_HEIGHT, epd2in7.EPD_WIDTH), 255)  # 255: clear the frame
    # Drawing on the Vertical image
    Limage = Image.new('1', (epd2in7.EPD_WIDTH, epd2in7.EPD_HEIGHT), 255)  # 255: clear the frame
    
    # Horizontal
    print "Drawing"
    draw = ImageDraw.Draw(Himage)
    font20 = ImageFont.truetype('/usr/share/fonts/truetype/wqy/wqy-microhei.ttc', 20)
    #draw.text((10, 0), 'hello world', font = font24, fill = 0)
    #draw.text((10, 20), '2.9inch e-Paper', font = font24, fill = 0)
    while True:
        draw.text((10, 70), time.strftime("%c"), font = font20, fill = 0)    
    #draw.line((20, 50, 70, 100), fill = 0)
    #draw.line((70, 50, 20, 100), fill = 0)
    #draw.rectangle((20, 50, 70, 100), outline = 0)
    #draw.line((165, 50, 165, 100), fill = 0)
    #draw.line((140, 75, 190, 75), fill = 0)
    #draw.arc((140, 50, 190, 100), 0, 360, fill = 0)
    #draw.rectangle((80, 50, 130, 100), fill = 0)
    #draw.chord((200, 50, 250, 100), 0, 360, fill = 0)
        epd.display(epd.getbuffer(Himage))
        time.sleep(1)
        
    epd.sleep()
        
except:
    print 'traceback.format_exc():\n%s' % traceback.format_exc()
    exit()

