from custom_exception import CannotBeBlankException, NotBoundException


class Context:
    def __init__(self):
        self.__lookupTable: dict[str,float] = {}

    def bind(self, name : str, value: float):
        if not name:
            raise CannotBeBlankException(name)
        self.__lookupTable[name] = value

    def get_value(self, name: str) -> float:
        if not name:
            raise CannotBeBlankException(name)
        if name in self.__lookupTable:
            return self.__lookupTable[name]
        else:
            raise NotBoundException(name)