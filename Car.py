class Car(object):

    def __init__(self, name='General', model='GM', car_type=None):
        super(Car, self).__init__()
        self.name = name
        self.model = model
        self.car_type = car_type
        self.speed = 0

    @property
    def num_of_doors(self):
        if self.name.lower() == 'porshe' or self.name.lower() == 'koenigsegg':
            return 2
        else:
            return 4

    @property
    def num_of_wheels(self):
        if self._car_type.lower() == 'trailer':
            return 8
        else:
            return 4

    @property
    def car_type(self):
        return self._car_type

    @car_type.setter
    def car_type(self, car_type):
        if car_type and car_type.lower() == 'trailer':
            self._car_type = 'trailer'
        elif not car_type:
            self._car_type = 'saloon'

    def is_saloon(self):
        if self._car_type == 'saloon':
            return True
        return False

    def drive(self, gear):
        if self.is_saloon():
            self.speed = (float(1000) / 3) * gear
        else:
            self.speed = (float(77) / 7) * gear

        return self
