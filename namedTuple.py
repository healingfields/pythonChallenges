from collections import namedtuple

student_number = int(input())
columns = input()
total = 0
Student = namedtuple('student', columns)


for i in range(student_number):
    std = Student(*input().split())
    total += int(std.MARKS)
print('{:.2f}'.format(total/student_number))
   
