import urllib2
import json

f = urllib2.urlopen('http://api.wunderground.com/api/ce63f16da1e77cfb/geolookup/conditions/q/IL/Springfield.json')
json_string = f.read()
parsed_json = json.loads(json_string)
location = parsed_json['location']['city']
temp_f = parsed_json['current_observation']['temp_f']
print "Current temperature in %s is: %s" % (location, temp_f)
#print "------------"
#print parsed_json['precip_today_string']
f.close()
