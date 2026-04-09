def addBinary(a, b):
    result = bin(int(a, 2) + int(b, 2))
    return result[2:]

a = input("Enter first binary: ")
b = input("Enter second binary: ")

print("Result:", addBinary(a, b))
