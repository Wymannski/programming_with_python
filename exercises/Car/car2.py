class Car2:
    def __init__(self,gas_consumption,tank_size = 30):
        self.__gas_consumption = gas_consumption
        self.__tank_size = tank_size
        self.__gas_level = 0

    def fill(self,liters:float):
        if self.gas_level + liters <= self.__tank_size:
            self.__gas_level += liters

    def drive(self,km:float):
        if (self.__gas_consumption /100 * km) <= self.gas_level:
            self.__gas_level -= (self.__gas_consumption / 100 * km)

    @property
    def gas_level(self):
        return self.__gas_level



def main():
    pass

if __name__ == '__main__':
    main()