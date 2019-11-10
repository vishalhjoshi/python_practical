file_name = 'test.txt'
#handling file exception
try:
    open(file_name)
    # creating file if not exists
    # data = f.read() not readable
    # print(data)
    # open file in writing mode
    with open(file_name, 'w') as f:
        for i in range(1, 11):
            f.write(f"This is line number {i}\n")
    # reading file :
    with open(file_name, 'a') as f:
        f.write('This line is appended !')
    # reading file :
    with open(file_name, 'r') as f:
        data = f.read()
        print(data)
except IOError as e:
    print(f"Something Went Wrong - ERROR:{e}")







