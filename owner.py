class Owner:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def find_my_cars(self):
        from car import Car
        cars = Car.all()
        my_cars = [f'{car.make} {car.model}' for car in cars if car.owner.name == self.name]
        return my_cars

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name
    
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, age):
        self._age = age


############