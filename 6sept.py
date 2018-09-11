l=[]
d={}
t={}
def personal_details():
    name=input("Enter your name : ")
    regno=int(input("Enter your Registration number : "))
    degree=input("Enter your degree : ")
    l.append(name)
    l.append(regno)
    l.append(degree)
    
    

    
def academic_details():
    subjectname=input("Enter Subject name : ")
    ca1=int(input("Enter CA1 marks out of 20 : "))
    ca2=int(input("Enter CA2 marks out of 20 : "))
    mte=int(input("Enter MTE marks out of 25 : "))
    ete=int(input("Enter ETE marks out of 50 : "))
    att=int(input("Enter your attendance % : "))
    if(att>=90):
        attendance=5
    elif (att>=85 and att<90):
        attendance=4
    elif (att>=80 and att<85):
        attendance=3
    elif (att>=75 and att<80):
        attendance=2
    else:
        attendance=0
    avgca=float(ca1+ca2)/2
    total=avgca+mte+ete+attendance
    d['sname']=subjectname
    d['ca1']=ca1
    d['ca2']=ca2
    d['mte']=mte
    d['ete']=ete
    d['attndnce']=attendance
    t['subject']=subjectname
    t['total_marks']=total

print("Student details")
personal_details()
for i in l:
    print(i)

while True:
    ch=str(input("Do you wish to continue ? Y/N"))
    if(ch=='Y' or ch=='y'):
        academic_details()
        for i in d.items():
            print(i)
    else:
        for i in t.items():
            print(i)
        break
    
    
        
    

    
    

'''A = personal_details()
B=academic_details()
def display():
    print(A)
    print(B)

print(l)
print(d)
display()'''
