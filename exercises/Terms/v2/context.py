from v2.custom_exception import NotBoundException, CannotBeBlankException


class Context:
    def __init__(self,dictionary):
        self.__lookup_table = dictionary

    def bind(self,name:str,value:float):
        if not name:
            raise CannotBeBlankException(name)
        look_up_table_copy = self.__lookup_table.copy()
        look_up_table_copy[name] = value
        return Context(look_up_table_copy)

    def get_value(self,name):
        if not name:
            raise CannotBeBlankException(name)

        if name in self.__lookup_table:
            return self.__lookup_table[name]
        else:
           raise NotBoundException(name)