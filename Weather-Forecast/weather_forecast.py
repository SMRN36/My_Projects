# -*- coding: utf-8 -*-
"""Weather-Forecast

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Pqi1j-fzUh70jWwMs0Pkc5YFRWxrwS3n
"""

import requests
import json
from PIL import Image, ImageDraw, ImageFont
from datetime import date


api_key = "{API-KEY}"
position = [620, 846, 1069, 1294, 1539, 1748]

uk_list = ["London", "Manchester", "Edinburgh", "Bristol", "Birmingham", "Cambridge"]
india_list = ["Karnataka", "Delhi", "Mumbai", "Kolkata", "Chennai", "Uttar Pradesh"]
us_list = ["New York", "Chicago", "San Francisco", "Los Angeles", "San Diego", "Washington"]
country_list = [uk_list, india_list, us_list]


for country in country_list:
    img = Image.open("Weather.jpg")
    draw = ImageDraw.Draw(img)

    font = ImageFont.truetype('Inter.ttf', size=66)
    content = "Latest Weather Forecast"
    color = 'rgb(0, 0, 0)'
    (x, y) = (357,178)
    draw.text((x, y), content, color, font=font)

    font = ImageFont.truetype('Inter.ttf', size=50)
    content = date.today().strftime("%A - %B %d, %Y")
    color = 'rgb(0, 0 ,0)'
    (x, y) = (400,265)
    draw.text((x, y), content, color, font=font)

    index = 0
    for city in country:
        Url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}".format(city, api_key)
        response = requests.get(Url)
        data = json.loads(response.text)
        
        font = ImageFont.truetype('Inter.ttf', size=50)
        color = 'rgb(0, 0, 0)'
        (x, y) = (142, position[index])
        draw.text((x, y), city, color, font=font)

        font = ImageFont.truetype('Inter.ttf', size=50)
        content = str(data['main']['temp']) + "\u00b0"
        color = 'rgb(0, 0, 0)'
        (x, y) = (780, position[index])
        draw.text((x, y), content, color, font=font)

        font = ImageFont.truetype('Inter.ttf', size=50)
        content = str(data['main']['humidity']) + "%"
        color = 'rgb(0, 0, 0)'
        (x, y) = (1127, position[index])
        draw.text((x, y), content, color, font=font)

        index += 1
       
    img.save(str(date.today()) + country[0] + ".png")
    img_pdf = img.convert('RGB')
    img_pdf.save(str(date.today()) + country[0] + ".pdf")