# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 13:32:29 2015

@author: 577342
"""

import xml.etree.ElementTree as ET
tree = ET.parse('Documents\\Data Science Projects\\Tale of 2 Cities\\Tale of Two Cities.kml')
root = tree.getroot()
root.tag
root.attrib
for child in root[0][4][2][2][1][0]:
    print child.tag, child.attrib, child.text

for child in tree.findall('.//{http://www.opengis.net/kml/2.2}coordinates'):
    print child.tag, child.attrib, child.text

for placemark in tree.findall('.//{http://www.opengis.net/kml/2.2}Placemark'):
    name = placemark.find('.//{http://www.opengis.net/kml/2.2}name')
    print name.text
    coordinates = placemark.find('.//{http://www.opengis.net/kml/2.2}coordinates')
    for coord in coordinates.text.strip().split(' '):
        print coord.split(',')

kml_text = """<?xml version="1.0" encoding="UTF-8"?>
<kml xmlns="http://www.opengis.net/kml/2.2" 
     xmlns:gx="http://www.google.com/kml/ext/2.2" 
     xmlns:kml="http://www.opengis.net/kml/2.2" 
     xmlns:atom="http://www.w3.org/2005/Atom">
    <actor>
        <name>John Cleese</name>
        <gx:character>Lancelot</gx:character>
        <gx:character>Archie Leach</gx:character>
    </actor>
    <actor>
        <name>Eric Idle</name>
        <gx:character>Sir Robin</gx:character>
        <gx:character>Gunther</gx:character>
        <gx:character>Commander Clement</gx:character>
    </actor>
</kml>
"""
root = ET.fromstring(kml_text)

for actor in root.findall('{http://www.opengis.net/kml/2.2}actor'):
    name = actor.find('{http://www.opengis.net/kml/2.2}name')
    print name.text
    for char in actor.findall('{http://www.google.com/kml/ext/2.2}character'):
        print ' |-->', char.text

import lxml
import pykml
from pykml import parser