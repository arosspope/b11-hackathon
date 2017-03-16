from datetime import datetime
from eif_api import types
from eif_api.data import Data

class FloorPlan():

    def __init__(self, fireExits, rooms, fireSensors):
        self.fireExits = fireExits
        self.rooms = rooms
        self.fireSensors = fireSensors
        self.hazards = []
        self.exitMap = [[0 for x in range(12)] for y in range(4)]  # TODO: Don't use hardcoded range
        self.roomMap = [[0 for x in range(12)] for y in range(4)]
        self.fireSensorMap = [[0 for x in range(12)] for y in range(4)]

        # Update map with interesting places
        for(exit in self.fireExits):
            x, y = exit.location
            self.exitMap[x][y] = exit

        for(room in self.rooms):
            x, y = room.location
            self.roomMap[x][y] = room

        for(sensor in self.fireSensors):
            x, y = sensor.location
            self.fireSensorMap[x][y] = sensor

    def updateExits(self):
        # TODO: For each exit, poll live people counter and determine which one needs to be blocked
        # Also need to check if any of these exists are blocked


class FireExit():

    def __init__(self, peopleUnit, location):
        self.peopleUnit = peopleUnit
        self.blocked = False
        self.location = location


class Room():

    def __init__(self, location, fireExit):
        self.location = location
        self.fireExit = fireExit


class FireSensor():

    def __init__(self, sensor, location):
        self.sensor = sensor
        self.location = location

    def isFire(self):
        currentTime = datetime.datetime.now()
        fiveMinutesAgo = currentTime - datetime.timedelta(minutes=5)
        (rc, json) = Data.retrieve(fiveMinutesAgo, currentTime, self.sensor.family, self.sensor.unit, self.sensor.subCode)

        for (attr, value) in json.iteritems():
            print attr
            print value

        # Add all values and find the average and see if its over a certain value and return boolean
        return false
