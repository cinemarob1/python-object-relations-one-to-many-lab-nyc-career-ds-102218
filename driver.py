from trip import Trip

class Driver:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name
    
    def my_trips(self):
        my_trips = []
        all_trips = Trip.all()
        my_trips = [f'{trip.start} to {trip.destination}' for trip in all_trips if trip.driver.name == self.name]
        return my_trips

    def my_trip_summaries(self):
        pass
