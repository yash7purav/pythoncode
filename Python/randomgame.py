import random
x= input ("insert number here   ")
if x==random.randint(0,100): 
    print ("you win")
else:
    print ("you lose")
    while input=="x":
        input= input("insert number here")
    while input!="x":
        print ("you lose")
        input= int (input("insert number here"))
    print ("you win")


