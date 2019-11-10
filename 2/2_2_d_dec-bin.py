n = int(input("Input any number"))
def decToBin(n):
    if n > 0:
        return decToBin(n//2) + str(n%2)
    else:
        return ''
print(decToBin(n))