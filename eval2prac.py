#loops

#for loop

l=[1,2,3,4,5]
for i in l:
    print(i)

d={"one":1,"two":2,"three":3}
for i in d.items():
    print(i)

for i in d.values():
    print(i)

for i in d.keys():
    print(i)


for i in range(len(l)):
    print(l[i])

c=0
while(c<=10):
    print(c)
    c=c+1
else:
    print("Loop over")
    
c=0
while(c<=10):
    if(c==5):
        break
    print(c)
    c=c+1
else:
    print("Loop over")


c=0
while(c<=10):
    c=c+1
    if c % 2==0:
        continue
    print(c)
    
else:
    print("Loop over")

print("-------------")




for i in range(1,6,1):
    for j in range(1,i):
        print(j, end='')
    print()

c=0
while(c<=5):
    d=0
    while(d<=2):
        print(d,end='')
        d=d+1
    print(c)
    c=c+1
    
