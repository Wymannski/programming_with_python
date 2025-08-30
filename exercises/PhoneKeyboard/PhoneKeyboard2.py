class Keyboard:
    def __init__(self):
        self.__phone_number = ""

    def press(self,digit:int):
        if digit in range(10):
            self.__phone_number += str(digit)

    def backspace(self):
        self.__phone_number = self.__phone_number[:-1]

    def clear(self):
        self.__phone_number = ""

    def dial(self):
        if len(self.__phone_number) >= 10:
            print(self.__phone_number)


def main():
    keyboard = Keyboard()
    keyboard.press(1)
    keyboard.press(1)
    keyboard.press(1)
    keyboard.press(1)
    keyboard.press(1)
    keyboard.press(1)
    keyboard.press(1)
    keyboard.press(1)
    keyboard.press(1)
    keyboard.dial()
    keyboard.press(1)
    keyboard.dial()
    keyboard.backspace()
    keyboard.press(1)
    keyboard.dial()


if __name__ == '__main__':
    main()