import requests
import json
import sys
import numpy as np

if __name__ == "__main__":
    key = sys.argv[1]
    ref = sys.argv[2]


    def geturl(key, ref):
        url1 = "http://api.prod.obanyc.com/api/siri/vehicle-monitoring.json?key="
        url2 = "&VehicleMonitoringDetailLevel=calls&LineRef="
        urls = url1 + key + url2 + ref
        requrl = requests.get(urls)
        return requrl.json()


    data = geturl(key, ref)
    businfo = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']
    busnum = np.size(data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'])

    print 'Bus Line : {}'.format(ref)
    print 'Number of Active Buses : {}'.format(busnum)

    for i in range(busnum):
        lat = businfo[i]['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
        lon = businfo[i]['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
        print 'Bus {} is at latitude {} and longitude {}'.format(i, lat, lon)
