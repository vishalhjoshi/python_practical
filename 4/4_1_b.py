file_name = 'test.txt'
try:
    with open(file_name, 'r') as f:
        lst = []
        for i in f:
            lst.append(i.strip('\n'))
except IOError as e:
    print(">>>",e)


print(f"Total Number of Lines In File {len(lst)}")
print("File Data :")
for line in lst:
    print(line)
word = []
for line in lst:
    words = line.split(' ')
    for w in words:
        word.append(w)

print(f"Total Number of words In File {len(word)}")
print()
print("Seprated Each Sentence In form of list: ")
print(lst)
