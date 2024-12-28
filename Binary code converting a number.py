class Binary:
    def convert(self, number):
        def convert2(number2):
            if number2 == 0:
                return 0
            else:
                return (number2 % 2 + 10 * convert2(number2 // 2))
        return f"1) {convert2(number)}"

    def decimal_to_binary(self, number):
        return bin(number)

    def decimal_to_binary2(self, letter):
        number = ord(letter)
        binary_code = bin(number)
        binary_string = binary_code[2:].zfill(8)
        return binary_string

    def func(self, x):
        def decimal_to_binary3(l):
            n = ord(l)
            b = bin(n)
            c = b[2:].zfill(8)
            return c
        return decimal_to_binary3(x)

try:
    user = int(input("Enter numbers: "))
    decimal_number = 42217502569
    string = "N"
    symbols = "How are you?"

    obj = Binary()

    print(obj.convert(user))
    print("2)", obj.decimal_to_binary(decimal_number))
    print("3)", obj.decimal_to_binary2(string))

    for s in symbols:
        print("4)", obj.func(s))
except ValueError:
    print("ValueError: invalid literal for int()")
