# XML and JSON

# 13.1 - Change either geojson.py or geoxml.py to print out the two-character country code from
# the retrieved data. Add error checking so your program does not traceback if the country code is
# not there. Once you have it working, search for “Atlantic Ocean” and make sure it can
# handle locations that are not in any country.

# geojson.py
import urllib.request, urllib.parse, urllib.error
import json
import ssl

api_key = False

# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro
if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else:
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location: ')
    if len(address) < 1: break
    parms = dict()
    parms['address'] = address
    if api_key is not False: parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)
    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')
    try:
        js = json.loads(data)
    except:
        js = None
    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue
    print(json.dumps(js, indent=4))
    lat = js['results'][0]['geometry']['location']['lat']
    lng = js['results'][0]['geometry']['location']['lng']
    print('lat', lat, 'lng', lng)
    location = js['results'][0]['formatted_address']
    print(location)

    # change to program to include country code & proper error for natural_features
    aclist = len(js['results'][0]['address_components'])
    print('ADDRESS COMPONENTS LIST:', aclist)
    if aclist < 4:
        print('===No country code for this location===')
        continue
    tccc = js['results'][0]['address_components'][3]['short_name']
    print('Two-character country code:', tccc)
quit()

# JSON lectures and textbook

# data as a list of dictionaries
import json
data1 = '''[
    { "id" : "001",
      "x" : "2",
      "name" : "Chuck"
    } ,
    { "id" : "009",
      "x" : "7",
      "name" : "Brent"
    }
]'''
info1 = json.loads(data1)
count = 0
for d in info1:
    count += 1
    print('DICTIONARY', count)
    print('Name:', d["name"])
    print('ID:', d["id"])
    print('Attribute:', d["x"], '\n')
quit()


# data as a dictionary of pairs & dictionaries
import json
data = '''{
    "name" : "Chuck",
    "phone" : {
        "type" : "intl",
        "number" : "+1 734 303 4456"
    },
    "email" : {
        "hide" : "yes"
    }
}'''
info = json.loads(data)
print('Name:', info["name"])
print('Email hidden:', info["email"]["hide"])
quit()



# XML lectures and textbook

# complex tag with mult. child tags
# looping through a list of trees [tree, tree]
import xml.etree.ElementTree as ET
data1 = '''
<stuff>
    <users>
        <user x="2">
            <id>001</id>
            <name>Chuck</name>
        </user>
        <user x="7">
            <id>009</id>
            <name>Brent</name>
        </user>
    </users>
</stuff>'''
stuff = ET.fromstring(data1)
lst = stuff.findall('users/user')
print('User count:', len(lst))
# print(lst)
for item in lst:
    print('Name:', item.find('name').text)
    print('ID:', item.find('id').text)
    print('Attr:', item.get('x'))
quit()



# simple tag with one child tag (no nested children/ grandchildren)
# sequentially following one tree
import xml.etree.ElementTree as ET
data = '''<person>
    <name>Chuck</name>
    <phone type="intl">
        +1 734 303 4456
    </phone>
    <email hide="yes"/>
    </person>'''
tree = ET.fromstring(data)
print('Name:', tree.find('name').text)
print('Atrr:', tree.find('email').get('hide'))
print('Phone attr:', tree.find('phone').get('type'))