# Author: Richard Vecsler, NYU, September 2016


# Principals in Urban Informatics
# HW 2
# Assignment 1
# Python Script to scrape and parse MTA Bus data


#####################


from __future__ import print_function
import sys
import urllib
import json

# test number of inputs

if not len(sys.argv) == 3:
	print("Invalid number of arguments.  Run as python show_bus_locations.py <MTA_KEY> <BUS_LINE>")
	sys.exit()


# scrape MTA site

MTA_key = sys.argv[1]
Bus_line = sys.argv[2]


bus_json_url="http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=" + MTA_key + "&VehicleMonitoringDetailLevel=calls&LineRef=" + Bus_line
response = urllib.urlopen(bus_json_url)
bus_data = response.read().decode("utf-8")
data = json.loads(bus_data)


print ("Bus Line :", Bus_line)

num_buses = 0

for it in data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']:
	num_buses = num_buses + 1
print ("Number of Active Buses :", num_buses)

bus_num = 0

for it in data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']:
	print("bus", bus_num, "is at latitude", it['MonitoredVehicleJourney']['VehicleLocation']['Latitude'], "and longitude", it['MonitoredVehicleJourney']['VehicleLocation']['Longitude'])
	bus_num = bus_num + 1

