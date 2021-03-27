import random
turncount=0
secretnum=random.randint(0,5)
secretnum=str(secretnum)
#print (type(secretnum))
#print (secretnum)
x=  input ("insert number here   ")
turncount= turncount+1
if secretnum==x:
    print ("you win")
    print ("the number of turns " + str(turncount))
    quit
while secretnum!=x:
    turncount=turncount+1
    print ("you lose")
    x= input("insert number here  ")
print ("you win")
print ("the number of turns " + str(turncount))









