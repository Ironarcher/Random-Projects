import urllib2
import json

start = raw_input('Enter starting city: ')
end = raw_input('Enter destination city within driving distance: ')

start = start.replace(' ', '_')
end = end.replace(' ', '_')

search = "https://maps.googleapis.com/maps/api/distancematrix/json?origins=" + start + \
	"&destinations=" + end + "&mode=driving&language=en-US&key=AIzaSyC0w5vbLyY4ZLf0gex7v62gXL7Amgij70g"

contents = urllib2.urlopen(search)
data = json.loads(contents.read())

status = data['rows'][0]['elements'][0]['status']
if status == "NOT_FOUND":
	print("One or more of the cities do not exist")
elif status == "ZERO_RESULTS":
	print("You cannot drive from the first city to the second")
elif status == "OK":
	origin = data['origin_addresses']
	destination = data['destination_addresses']
	distance = data['rows'][0]['elements'][0]['distance']['text']
	time = data['rows'][0]['elements'][0]['duration']['text']
	print "The distance and time traveled from", origin[0], "to", destination[0], "is:"
	print(distance)
	print(time)
else:
	print "Error: ", status