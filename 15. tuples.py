# Program to perform some operations on tuples.

print()
t1 = (1,2,5,7,9,2,4,6,8,10)
print("The given tuple is :",t1)

ch = 'y'
while(ch=='y' or ch=='Y'):
    print()
    print("  -: MENU :-")
    print("1. Print half the values in one line and the other half in the next line.")
    print("2. Print another tuple whose values are even numbers in the given tuple.")
    print("3. Concatenate a tuple t2=(11,13,15) with the given tuple.")
    print("4. Return maximum and minimum value from the given tuple.")
    print()

    opt = int(input("Enter your choice : "))

    if(opt==1):
        print("First half : ", end='')
        for i in range(len(t1)):
            if(i==len(t1)/2):
                print()
                print("Other half : ", end='')

            print(t1[i],end=' ')

        print()    

    elif(opt==2):
        t3 = []
        for i in t1:
            if(i%2==0):
                t3.append(i)

        t3 = tuple(t3)        
        print("Another tuple with the even numbers from the given tuple is :",t3)        

    elif(opt==3):
        t2 = (11,13,15)
        t4 = t1 + t2
        print("Concatenated tuple is :",t4)

    elif(opt==4):
        maxval = max(t1)
        minval = min(t1)
        print("Maximum value is :",maxval)
        print("Minimum value is :",minval)

    else:
        print()
        print("Oops !! INCORRECT CHOICE... Enter correct option (1-4)")

    print()
    ch = input("Want to view menu again ? (y/n) : ")    
