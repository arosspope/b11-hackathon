import requests


class Data():
    """Blah."""

    DATE_FORMAT = "%Y-%m-%dT%I:%M:%S"

    @staticmethod
    def retrieve(startDate, endDate, family, unit, subCode):
        """Will get data."""
        payload = {
            'rFromDate': startDate.strftime(Data.DATE_FORMAT),
            'rToDate': endDate.strftime(Data.DATE_FORMAT),
            'rFamily': family.value,
            'rSensor': unit.value,
            'rSubSensor': subCode.value
        }

        r = requests.post('http://eif-research.feit.uts.edu.au/api/json/', params=payload)

        return (r.status_code, r.json())
