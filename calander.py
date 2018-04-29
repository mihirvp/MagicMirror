from pyicloud import PyiCloudService
import datetime
import numpy as np
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
api = PyiCloudService('mihirpatel358@gmail.com')

def time_string(event_start):
    if(event_start[0] > 12):
        if(event_start[1]<10):
            event_start = (str(event_start[0]-12)+":"+str(event_start[1])+str(0)+"PM")
        else:
            event_start = (str(event_start[0]-12)+":"+str(event_start[1])+str(0)+"PM")
    else: 
        if(event_start[1]<10):
            event_start = (str(event_start[0]-12)+":"+str(event_start[1])+str(0)+"AM")
        else:
            event_start = (str(event_start[0]-12)+":"+str(event_start[1])+str(0)+"AM")
    return event_start




today = datetime.date.today()
tomorrow = today + datetime.timedelta(days=1)
info = np.array([])
for i in range (0,len(api.calendar.events(today, tomorrow))):
    event_name = (api.calendar.events(today, tomorrow)[i]['title'])
    event_end = (api.calendar.events(today, tomorrow)[i]['endDate'][4],api.calendar.events(today, tomorrow)[0]['endDate'][5])
    event_start = (api.calendar.events(today, tomorrow)[i]['startDate'][4],api.calendar.events(today, tomorrow)[0]['startDate'][5])
    loc = (api.calendar.events(today, tomorrow)[i]['location'])
    event_start = time_string(event_start)
    event_end = time_string(event_end)
    if(i == 0):
        info = np.append(info,np.array([event_name,event_start,event_end,loc]))
    else: 
        info = np.vstack((info,np.array([event_name,event_start,event_end,loc])))
    print(event_name)
    print(',')
    print(event_start,'-',event_end)
    print(',')
    print(loc)
    print(',')
    print(',')