from typing_extensions import override


class CannotBeBlankException(Exception):
    def __init__(self,name:str,message="Variable cannot be blank"):
        self.name = name
        self.message = message
        super().__init__(self.message)

    @override
    def __str__(self):
        return self.message + f"'{self.name}'"

class NotBoundException(Exception):
    def __init__(self,name:str,message="Variable is not bound"):
        self.name = name
        self.message = message
        super().__init__(self.message)

    @override
    def __str__(self):
        return self.message + f"'{self.message}'"