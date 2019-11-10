#Given Number is armstrong or not
#num  = 153
n = input("Enter Number : >> ")

def checkArmstrong(n):
    number = str(n)
    result = number
    sum  = 0
    for i in number:
        sum += int(i) ** len(number)

    if result == str(sum):
        return True
    else:
        return False


if checkArmstrong(n):
    print(f'Yes! given Number({n}) is armstrong number')
else:
    print(f'NO! given Number({n}) is NOT armstrong number')
