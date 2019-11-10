n = int(input("Input any number"))
def decToHex(n):
    hex_values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'b', 'c', 'd', 'e', 'f']
    reversed_number = ""
    while n > 0:
        remainder = n % 16
        n -= remainder
        n //= 16
        reversed_number += str(hex_values[remainder])
    return reversed_number


print(decToHex(n))