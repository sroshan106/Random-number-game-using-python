from random import randint
from threading import Timer
import sys
from Tools.scripts.treesync import raw_input

i=0
count=0
q=0

def tty():
    print("\nGame Over\n")
    print("No of correct answers ", count)
    global q
    q=1
    sys.exit()

t = Timer(10,tty)
t.start()


print("""                                   Maths Game                                  """)
print("""                         Press enter to skip an operation                      """)
while(q==0):
    a = randint(0,10)
    print(a)
    b = randint(1,10)
    print(b)
    c = randint(1,5)

    if (c==1) :
        print("+")
    elif(c==2):
        print("-")
    elif(c==3):
        print("/")
    elif(c==4):
        print("*")
    elif(c==5):
        print("%")


    if (c==1) :
        d=a+b;
    elif(c==2):
        d=a-b;
    elif(c==3):
        d=a/b;
    elif(c==4):
        d=a*b;
    elif(c==5):
        d=a%b;

    d = int(d)


    e = input("Enter your answer")

    if e != "":
        e = int(e)

        if(e==d):
            count=count+1
        else:
            print("wrong answer")

        i=i+1


