from abc import ABC,abstractmethod
from datetime import datetime


class Person:
    def __init__(self, name:str, reservations=None):
        if reservations is None:
            reservations = []
        self.__name = name
        self.__reservations = reservations

    def make_reservation(self,start_date:str,end_date:str,resource):
        reservation = Reservation(start_date,end_date,resource)
        self.__reservations.append(reservation)

class Reservation:
    def __init__(self,resource,start_date: str,end_date:str):
        self.__resource = resource
        self.__start_date = start_date
        self.__end_date = end_date


class Resource(ABC):
    @property
    @abstractmethod
    def resource_id(self):
        pass

class Resource_1(Resource):
    @property
    def resource_id(self):
        return 1

class Resource_2(Resource):
    @property
    def resource_id(self):
        return 2

class Resource_3(Resource):
    @property
    def resource_id(self):
        return 3

def main():
    person = Person('Max')
    resource_1 = Resource_1()
    person.make_reservation("1.1.2003","1.2.2003",resource_1)
    print('success')

if __name__ == '__main__':
    main()

