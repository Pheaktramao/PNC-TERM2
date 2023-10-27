
teacherlist=[ 
 {"subject": "html", "class": "WEP-B",'teacher-id':45}, 
 {"subject": " algorithm ", "class": "WEP-A",'teacher-id': 68},  
 {"subject": "algorithm", "class": "WEP-B",'teacher-id': 39},
  
]
teachersubject=[ 
    {"teacher-id": 39, "first-name": "Mengheang", "last-name": "Pho"},  
    {"teacher-id": 45, "first-name": "ronan", "last-name": "the best"},  
    {"teacher-id": 68, "first-name": "him", "last-name": 'Hey'}
]
nameTeacher=""
Subject=teachersubject[0]['teacher-id']
for i in teacherlist:
    if teacherlist['teacher-id']==teachersubject['teachersubject:']:
            nameTeacher=teachersubject['last-name']+teachersubject['first-name']
            print(nameTeacher)
    else:
        print("No teacher in algorithm subject")