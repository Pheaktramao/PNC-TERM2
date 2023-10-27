# Ex3 - Dictionary or object
studentList = [
  {'id': 1, 'name': 'dara', 'salary': 250, 'province':'Phnom Penh'},
  {'id': 2, 'name': 'kaka', 'salary': 540, 'province': 'Ratanakiri'},
  {'id': 3, 'name': 'bopha', 'salary': 562, 'province': 'Siem Riep'},
  {'id': 4, 'name': 'chompa', 'salary': 330, 'province': 'Battambang'},
  {'id': 5, 'name': 'chompey', 'salary': 455, 'province': 'Siem Riep'},
  {'id': 6, 'name': 'romdul', 'salary': 550, 'province': 'Kratie'},
]
#1 - How many student from "Siem Riep"
StudentName=""
Name=studentList[0]['province']
for student in studentList:
    if student['province']=='Siem Riep':
        Name=student['province']
        StudentName+=student['name'] + "\n"
print(StudentName)
#2 - Find average of student salary
sum=0
average=0
for student in studentList:
    sum+=student['salary']
average=sum/len(studentList)
print(average)
#3 - Who has higher salary in list
highestsalary=studentList[0]['salary']
Name=""
for student in studentList:
    if student['salary']>=highestsalary:
        highestsalary=student['salary']
        Name=student['name']
print(Name)
#4 - Increase salary of Kaka to 670
# 5 - Rename "romdul" to "សុរិយាច័ន្ទ្រាមហាកញ្ញាបទុមកេសរនារីរ៍ត្ន"

# 5 -​ Delete student has id number 5