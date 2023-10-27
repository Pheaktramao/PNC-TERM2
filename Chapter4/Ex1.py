# Ex1 - Dictionary or object
studentList=[
  {'id': 1, 'name': 'dara', 'age': 20},
  {'id': 2, 'name': 'kaka', 'age': 20},
  {'id': 3, 'name': 'bopha', 'age': 12},
  {'id': 4, 'name': 'chompa', 'age': 40},
  {'id': 5, 'name': 'chompey', 'age': 30},
  {'id': 6, 'name': 'romdul', 'age': 60},
]
#1 - who is younger in list

minAge=studentList[0]['age']
studentName=""
for student in studentList:
    if student['age']<=minAge:
        minAge=student['age']
        studentName=student['name']
print(studentName)
# 2 - who  is older in list
maxAge=studentList[0]['age']
studentName=""
for student in studentList:
    if student['age']>maxAge:
        maxAge=student['age']
        studentName=student['name']
print(studentName)
#3 - how many student has the same age
Age=studentList[0]['age']
for student in studentList:
    if student['age']==Age:
        Age=student['age']
        print(student['name'])
# 4 - how many student older than "kaka"
Age=studentList[0]['age']
count=0
for student in studentList:
    if student['name']=="kaka":
            Age=student['age']
    elif student['age']>Age:
          count+=1
print(count)
#5 - remove student name "romdul" from the list
index=None
for i in range(len(studentList)):
    if studentList[i]['name']=="romdul":
        index=i
studentList.pop(index)
print(studentList)