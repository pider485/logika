class Student():
    def __init__(self, surname, name, grade):
        self.surname = surname
        self.name = name
        self.garde = grade

students = []

with open ('students_large.txt', 'r', encoding='utf-8') as file:
    for line in file:
        data = line.split(' ')
        obj = Student(data[0], data[1], int(data[2]))
        students.append(obj)
mark=0
num=0
for i in students:
    mark=mark + i.garde
    num=num+ 1

mark=mark/num
print(mark)