studentlist=[ 
    {'name': 'dyna','subject' :'Algorithm' ,'score' :10}, 
    {'name': 'sokheang','subject' :'Html' ,'score' :45}, 
    {'name': 'sreynang','subject' :'Algorithm' ,'score' :89}, 
    {'name': 'phanit','subject' :'Algorithm' ,'score':49}
]
OBJECT={}
Name=""
array=[] 
count=0
min=studentlist[0]['score']
for student in studentlist:
    if student['subject']=='Algorithm' and student['score']<=min:
        count+=1
        Name+=student['name']
        array.append(Name)
    Name=""
    OBJECT['number']=count 
    OBJECT['name']=array
print(OBJECT)