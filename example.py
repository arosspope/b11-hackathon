import requests
from datetime import datetime


fromDate = datetime(2017, 3, 9, 11, 32, 27)
toDate = datetime(2017, 3, 11, 11, 32, 27)
dateFormat = "%Y-%m-%dT%I:%M:%S"

payload = {
    'rFromDate': fromDate.strftime(dateFormat),
    'rToDate': toDate.strftime(dateFormat),
    'rFamily': 'wasp',
    'rSensor': 'ES_B_08_422_7BDC',
    'rSubSensor': 'O2'
}

r = requests.post('http://eif-research.feit.uts.edu.au/api/json/', params=payload)

if(r.status_code == requests.codes.ok):
    print(r.json())  # r.json is a dictonary of dates and values
    print(r.url)


# The above code simulates hitting the below url on a browser:  http://eif-research.feit.uts.edu.au/api/json/?rFromDate=2017-03-09T11:32:27&rToDate=2017-03-11T11:32:27&rFamily=wasp&rSensor=ES_B_08_422_7BDC&rSubSenor=O2
