def outer():
    print("Hi")
    def inner():
        print("Hello")

    inner()
    print("Hi again")

outer()


def prime():
    c=0
    for i in range(2,20):
        c=0
        for j in range(2,i):
            if i%j==0:
                c=c+1
                break
        if(c==0):
            print(i)

prime()


def fibo():
    a=0
    b=1
    print(a)
    print(b)
    for i in range(18):
        c=a+b
        print(c)
        a=b
        b=c

fibo()
