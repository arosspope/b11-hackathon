from datetime import datetime
from eif_api import types
from eif_api.data import Data

fromDate = datetime(2017, 3, 9, 11, 32, 27)
toDate = datetime(2017, 3, 11, 11, 32, 27)

#(rc, jsonData) = Data.retrieve(fromDate, toDate, types.SensorFamily.WASP, types.WaspUnit.ES_B_08_422_7BDC, types.WaspSubCode.OXYGEN)

(rc, jsonData) = Data.livePersonCount(types.PeopleUnit.FIRE_1)

print(rc)
print(jsonData)

# The above code simulates hitting the below url on a browser:  http://eif-research.feit.uts.edu.au/api/json/?rFromDate=2017-03-09T11:32:27&rToDate=2017-03-11T11:32:27&rFamily=wasp&rSensor=ES_B_08_422_7BDC&rSubSenor=O2
