import requests
import json
import sys
import pandas as pd
import numpy as np


if __name__ == "__main__":
    key=sys.argv[1]
    ref=sys.argv[2]
    filename=sys.argv[3]

    def geturl(key, ref):
        url1 = "http://api.prod.obanyc.com/api/siri/vehicle-monitoring.json?key="
        url2 = "&VehicleMonitoringDetailLevel=calls&LineRef="
        urls = url1 + key + url2 + ref
        requrl = requests.get(urls)
        return requrl.json()



    data = geturl(key, ref)
    businfo = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']
    busnum = np.size(data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'])

    bus_info = pd.DataFrame(columns=['Latitude', 'Longitude', 'Stop Name', 'Stop Status'])

    for i in range(busnum):
        lat = businfo[i]['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
        lon = businfo[i]['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
        stopflag = businfo[i]['MonitoredVehicleJourney']['OnwardCalls']
        if 'OnwardCall' in stopflag:
            stopflag2 = businfo[i]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall']
            if (np.size(stopflag2) > 1):
                stopname = businfo[i]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][1]['StopPointName']
                stopstatus = businfo[i]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][1]['Extensions']['Distances'][
                    'PresentableDistance']
            else:
                stopname = 'N/A'
                stopstatus = 'N/A'
        else:
            stopname = 'N/A'
            stopstatus = 'N/A'
        df = pd.DataFrame({'Latitude': [lat], 'Longitude': [lon], 'Stop Name': stopname, 'Stop Status': stopstatus})
        bus_info = bus_info.append(df)
        df = df.reset_index(drop=True)
    bus_info.to_csv(filename+'.csv',index=False)
