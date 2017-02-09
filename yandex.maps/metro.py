# -*- coding: utf-8 -*-

import json, urllib, urllib2

f = open('address.txt')
list = f.read()
f.close()
list = list.split('\n')
print list 

for line in list:
	hostel = line.split(';')
	address = hostel[2]
	url = 'http://geocode-maps.yandex.ru/1.x/?format=json&'
	params = urllib.urlencode({'geocode':address})
	fullUrl = url+params
	response = urllib2.urlopen(fullUrl)
	pyObj = json.load(response)
	try:
		coords = pyObj["response"]['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos']
		url = 'http://geocode-maps.yandex.ru/1.x/?format=json&kind=metro&'
		params = urllib.urlencode({'geocode':coords})
		fullUrl = url+params
		response = urllib2.urlopen(fullUrl)
		pyObj = json.load(response)
		f = open('test.txt', 'a')
		try:
			metro = pyObj["response"]['GeoObjectCollection']['featureMember'][0]['GeoObject']['metaDataProperty']['GeocoderMetaData']['AddressDetails']['Country']['AdministrativeArea']['SubAdministrativeArea']['Locality']['Thoroughfare']['Premise']['PremiseName']
			f.write(hostel[0] + ';' + hostel[1] + ';' + address + ';' + metro.encode('utf-8') + ' \n')
		except IndexError:
			f.write(hostel[0] + ';' + hostel[1] + ';' + address + ';' + '' + '\n')
	except IndexError:
		f = open('test.txt', 'a')
		f.write(hostel[0] + ';' + hostel[1] + ';' + address + ';' + '' + '\n')
	
	#f.write(address.encode('utf-8') + ' ' + pyObj["response"]['GeoObjectCollection']['featureMember'][0]['GeoObject']['metaDataProperty']['GeocoderMetaData']['AddressDetails']['Country']['AdministrativeArea']['SubAdministrativeArea']['Locality']['Thoroughfare']['Premise']['PremiseName'].encode('utf-8'))
	f.close()

# 1. Прогоняем адреса, получаем координаты
# 2. Прогоняем координаты, получаем метро	


