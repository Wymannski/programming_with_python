class PhoneKeyboard:
    def __init__(self):
        self.__phoneNumber = ""

    def press(self, digit: int):
        if digit in range(0, 9):
            self.__phoneNumber = self.__phoneNumber + str(digit)

    def backspace(self):
        self.__phoneNumber = self.__phoneNumber[:-1]

    def clear(self):
        self.__phoneNumber = ""

    def dial(self):
        if len(self.__phoneNumber) >= 10:
            print(self.__phoneNumber)

def main():
   phone_keyboard = PhoneKeyboard()
   phone_keyboard.press(1)
   phone_keyboard.press(1)
   phone_keyboard.press(1)
   phone_keyboard.press(1)
   phone_keyboard.press(1)
   phone_keyboard.press(1)
   phone_keyboard.press(1)
   phone_keyboard.press(1)
   phone_keyboard.press(1)
   phone_keyboard.press(1)
   phone_keyboard.dial()
   phone_keyboard.backspace()
   phone_keyboard.dial()
   phone_keyboard.press(2)
   phone_keyboard.dial()

if __name__ == '__main__':
    main()