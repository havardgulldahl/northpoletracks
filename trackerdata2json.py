#encoding: utf-8

# TrackerData2json.py 
#
# <TrackerData>
#<device serial="20258">
#<position id="14444707" momsn="5" at="2015-02-24T12:24:06Z" lat="59.93567" lon="10.72155" source="GPS" sog="0.2" cog="000" alt="62" temp="24.0" batt="99" alert="false"/>
#<position id="14444708" momsn="6" at="2015-02-24T12:24:06Z" lat="59.93567" lon="10.72155" source="GPS" sog="0.2" cog="000" alt="62" temp="24.0" batt="99" alert="false"/>



import sys, urllib, json
from xml.etree import ElementTree as ET

# get file 
data = urllib.urlopen('http://secure.rock7mobile.com/API2/GetPositions/20258?username=gulldahl-api&password=9898lance')
xml = ET.parse(data)
root = xml.getroot()
positions = [ p.attrib for p in root.iter('position' ) ]

sys.stdout.write(json.dumps(positions))
	
	