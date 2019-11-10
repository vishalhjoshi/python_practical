lst = [12,12,33,55,89,55,69,45,75]
print(lst)
new_lst = []

for num in lst:
    if num not in new_lst:
        new_lst.append(num)

lst = new_lst
print(lst)