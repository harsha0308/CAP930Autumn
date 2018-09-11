def func1():
    print("Hello World!!")
    
func1()

def func2():
    print("Hello World!!")
    return
    
func2()

def hello():
    """Prints "Hello World".

    Returns:
        None
    """
    pass

print(hello.__doc__)

def sum1(a,b=2):
    return a+b

print(sum1(2,3))
print(sum1(2))

def sum2(a,b):
    return a+b

print(sum2(2,7))
print(sum2(a=6,b=9))
print(sum2(b=9,a=7))

def add(*args):
    s=0
    for i in args:
        s=s+i
    print("Sum : "+str(s))

add(1,2,3,4,5,6)


s='''harsha'''
print(s)
s1="Harsha"
print(s1)
s2='Harsha'
print(s2)
s3="""Harsha"""
print(s3)
#global vs local variable

gl=10
def func(a):
    s=0
    global gl
    gl=20
    s=a+gl
    print(a)
    print(gl)
    print(s)

func(10)
