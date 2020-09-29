byte_array = "Converting to Binary to ASCII characters is really not that hard. Now you can send binary coded messages to your friends. Imagine passing a note to a friend and when it gets intercepted; it turns out to be just a piece of paper full of 1's and 0's.".encode()

binary_int = int.from_bytes(byte_array, "big")
binary_string = bin(binary_int)

print(binary_string)