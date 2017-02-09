# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
from urllib2 import urlopen
import re

from django.db import models
from models import Hostel, City, Country, Service

rus = Country.objects.get(pk=1)
msk = City.objects.get(pk=1)
wifi = Service.objects.get(pk=1)

URL = 'http://anti-hostel.ru/hostely-moskvy/hostel-real-time-school-slavyanskiy-bulvar/'

html_doc = urlopen(URL).read()
soup = BeautifulSoup(html_doc)

# Ищем название

h1 = soup.find('h1')
name = h1.string.replace(u', МОСКВА', '')
name = name.capitalize()

# Формируем символьный код

symbol_code = URL.replace('http://anti-hostel.ru/hostely-moskvy/', '')
symbol_code = symbol_code.replace('/', '')

# Ищем адрес

address = soup.find(text=re.compile(u'Адрес'))
address = address.replace(u'Адрес: ', '')

# Ищем URL Booking

booking = soup.find('a', 'wpb_button_a')
if booking:
    booking_url = booking.get('href')

# Ищем главное описание

h1 = soup.find('h1')
desc = findAllPs(h1)

def findAllPs(tag):
    next = tag.find_next_sibling()
    if not hasattr(next, 'name') or next.name != 'p':
        return ''
    else:    
        try:
            next = next.a.extact()
        except AttributeError:
            next
        finally:
            if not re.match(u'^Адрес', next.string):
                return next.string + ' ' + findAllPs(next)
            else:
                return '' + findAllPs(next)
        
        

# Ищем описание услуг и номеров

h2 = soup.find_all('h2')
for header in h2:
    if u'НОМЕР' in header.string:
        room_desc = findAllPs(header)
    elif u'УСЛУГ' in header.string:
        serv_desc = findAllPs(header)

# Ищем описание мест

h3 = soup.select('h3[dir]')
for header in h3:
    if header['dir'] == 'ltr':
        places_desc = findAllPs(header)

# Создание элемента БД

def addHostel(country, city, serv, desc, serv_desc, places_desc, room_desc):
    h = Hostel(
    active = True,
    entry_type = 'hotel',
    name = 'People',
    symbol_code = 'hostel-people-pipl-smolenskaya',
    address = u'Москва, Новинский бульвар, дом 11',
    url_booking = 'http://www.booking.com/hotel/ru/people-novinsky.html?aid=801609',
    country = country,
    city = city,
    desc = desc,
    serv_desc = serv_desc,
    places_desc = places_desc,
    room_desc = room_desc)
    h.save()
    h.services.add(serv)

addHostel(rus, msk, wifi, desc, serv_desc, places_desc, room_desc)