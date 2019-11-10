name = input("Enter Student Name : >>")
roll_no = input("Enter Roll Number : >>")
sub1 = int(input("Enter marks of  Maths : >>"))
sub2 = int(input("Enter marks of History : >>"))
sub3 = int(input("Enter marks of  Science : >>"))
sub4 = int(input("Enter marks of  Marathi : >>"))
sub5 = int(input("Enter marks of  English : >>"))


avg = (sub1+sub2+sub3+sub4+sub4) * 100 // 500

if avg >= 90:
    grade = 'A'
elif avg >= 80 and avg < 90:
    grade = 'B'
elif avg >= 70 and avg < 80:
    grade = 'C'
elif avg >= 60 and avg < 70:
    grade = 'D'
else:
    grade = 'F'

if grade == 'F':
    result = 'Fail'
else:
    result = 'Pass'

print("------------------------RESULT-----------------------")
# print("-----------------------------------------------------")
print(f"NAME : {name}                   ROll NO : {roll_no} ")
print("-----------------------------------------------------")
print("SUB NAME                                    MARKS")
print("-----------------------------------------------------")
print(f"MATHS                                        {sub1}")
print(f"HISTORY                                      {sub2}")
print(f"SCIENCE                                      {sub3}")
print(f"MARATHI                                      {sub4}")
print(f"ENGLISH                                      {sub5}")
print("-----------------------------------------------------")
print(f"RESULT : {result}                  GRADE: {grade} ")



