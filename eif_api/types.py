from enum import Enum


class SensorFamily(Enum):
    """Sensor Types avaialble through the api."""

    WASP = 'Waspmote'
    EMBED = 'Embedded Sensors'
    WEATHER = 'Weather Station'
    LOGINS = 'PCLabs Logins'


class SensorCode(Enum):
    """List of Sensor codes available through the api."""

    ESD00_1 = ''
    ESD06_2 = ''
    ESD12_1 = ''
    ESD12_2 = ''
    ESD13_1 = ''
    ESDB3_2 = ''

class SubSensorCode(Enum):
    """List of Sub Sensor codes avalialbe through the api."""
