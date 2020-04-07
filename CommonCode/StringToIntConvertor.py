# https://tio.run/

class StringToIntConverter:

    def convert(self, string):
        mybytes = string.encode('utf-8')
        myint = int.from_bytes(mybytes, 'little')
        return myint

    def reverseConvert(self, integer):
        recoveredbytes = integer.to_bytes((integer.bit_length() + 7) // 8, 'little')
        recoveredstring = recoveredbytes.decode('utf-8')
        return recoveredstring
