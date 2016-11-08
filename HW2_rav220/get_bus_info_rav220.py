# Author: Richard Vecsler, NYU, September 2016

# Principals in Urban Informatics
# HW 2
# Assignment 2
# Python Script to scrape and parse MTA Bus data

#####################

from __future__ import print_function
import sys
import urllib
import json
import csv

# test number of inputs

if not len(sys.argv) == 4:
        print("Invalid number of arguments.  Run as python show_bus_locations.py <MTA_KEY> <BUS_LINE>")
        sys.exit()

# scrape MTA site

MTA_key = sys.argv[1]
Bus_line = sys.argv[2]

bus_json_url="http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=" + MTA_key + "&VehicleMonitoringDetailLevel=calls&LineRef=" + Bus_line
response = urllib.urlopen(bus_json_url)
bus_data = response.read().decode("utf-8")
data = json.loads(bus_data)

fout = csv.writer(open(sys.argv[3], "wb+"))

fout.writerow(['Latitude','Longitude','Stop Time','Stop Status'])


for it in data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']:

        if len(it['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['StopPointName']) == 0:
                stop = 'N/A'

        else:
                stop = it['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['StopPointName']

        if len(it['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['Extensions']['Distances']['PresentableDistance']) == 0:
                dist = 'N/A'
        else:
                dist = it['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['Extensions']['Distances']['PresentableDistance']

        lat = it['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
        lon = it['MonitoredVehicleJourney']['VehicleLocation']['Longitude']


        fout.writerow([lat,lon,stop,dist])
