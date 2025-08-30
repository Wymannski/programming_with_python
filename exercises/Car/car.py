

class Car:
    def __init__(self,gas_consumption:float,tank_size:float):
        self.__gas_consumption = gas_consumption
        self.__tank_size = tank_size
        self.__gas_level = 0

    def fill(self,liters:float):
        if liters + self.__gas_level <= self.__tank_size:
            self.__gas_level += liters
        else:
            print("To much fuel")

    def drive(self,km:float):
        if self.__gas_consumption * km / 100 <= self.__gas_level:
            self.__gas_level -= (self.__gas_consumption / 100 * km)
        else:
            print("Not enough fuel")

    @property
    def gas_level(self):
        return self.__gas_level

def main():
    car = Car(2,30)
    car.fill(10)
    print(car.gas_level)
    car.drive(5)
    print(car.gas_level)
    car.fill(100)
    car.drive(1000)

if __name__ == '__main__':
    main()


