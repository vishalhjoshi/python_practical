def sum_of_digit(digit):
    digit = str(digit)
    sod = 0
    for i in digit:
        sod = sod + int(i)
    return sod


try:
    d = int(input("Enter any digit : >>"))
    print(f'sum of "{d}" is {sum_of_digit(d)}')
except ValueError:
    print('Invalid Input')
