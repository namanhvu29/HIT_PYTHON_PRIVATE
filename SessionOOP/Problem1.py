class Manufacturer:
    def __init__(self, identity, location):
        self.__identity = identity
        self.__location = location

    def describe(self):
        """
        Print the details of the manufacturer.
        """
        print(f"Manufacturer ID: {self.__identity} - Location: {self.__location}")


class Device:
    def __init__(self, name, price, identity, location):
        self.__name = name
        self.__price = price
        
        self.__manufacturer = Manufacturer(identity, location)

    def describe(self):
        """
        Print the details of the device, including its manufacturer.
        """
        print(f"Device Name: {self.__name} - Price: {self.__price}")
        self.__manufacturer.describe()

device1 = Device("Mouse", 2.5, 9725, "Vietnam")
device2 = Device("Monitor", 12.5, 11, "Germany")

device1.describe()
device2.describe()
