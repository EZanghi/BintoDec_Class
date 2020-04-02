#Intented convert a binary number to your decimal equivalent.

class Binary:

    def __init__(self, binary_number):
        #Intented convert a binary number to your decimal equivalent.
        self.binary_number = binary_number
        self.check_character()
        self.check_qty_character()
        self.bin_length = len(self.binary_number)
        #print("{} binary number is created!".format(binary_number))

    def __str__(self):
        return self.binary_number

    def decimal(self):
        #Function to convert binary number to decimal
        self.bin_to_dec = 0
        for i in self.binary_number:
            self.bin_to_dec += int(i) * (2 ** (self.bin_length - 1))
            self.bin_length -= 1
        return print(self.bin_to_dec)
        #return print("The converted binary number to decimal is: {}".format(self.bin_to_dec))

    def hexadecimal(self):
        #Function to convert a binary number to hexadecimal
        pass

    def check_character(self):
        for char in self.binary_number:
            if (char != "0" or char != "1"):
                return True
            else:
                raise ValueError("O número só pode ter 0's and 1's")

    def check_qty_character(self):
        self.bin_length = len(self.binary_number)
        if self.bin_length <= 8:
            return True
        else:
            raise ValueError("The number entered must be less than 8 digits!")