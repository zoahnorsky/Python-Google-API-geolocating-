import urllib.request, urllib.parse, urllib.error
import json
import ssl

ctx = ssl.create_default_context() # add these 3 lines for https sites
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

api_key = False

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

while True:
    address = input("enter location: ") # ask for a location name "University of Utah"
    if len(address) < 1: break # make sure entered name is good

    parms = dict() # create dictionary
    parms['address'] = address # add the address to the dict
    if api_key is not False: parms['key'] = api_key # if set key is true, add to dict
    url = serviceurl + urllib.parse.urlencode(parms) # encode dict items and combien with google apis

    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx) # fins and open url
    data = uh.read().decode() # read and decode data
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data) # try to open json data
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK': #
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    print(json.dumps(js, indent=4)) # dump json with 4 indents

    place = js['results'][0]['place_id'] # find 'place_id'
    print('========RESULT========')
    print('')

    print(place)
