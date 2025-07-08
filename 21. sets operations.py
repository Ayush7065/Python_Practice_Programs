# Program that accepts two strings and performs some operations using sets.

print()
str1 = input("Enter the first string : ")
str2 = input("Enter the second string : ")

set1 = set(str1.lower())
set2 = set(str2.lower())

ch = 'y'
while(ch=='y' or ch=='Y'):
    print()
    print("  -: MENU :-")
    print("1. Display the common characters between the two strings.")
    print("2. Display the distinct characters between the two strings.")
    print()

    opt = int(input("Enter your choice = "))

    if(opt==1):
        set3 = set1 & set2
        print("Common characters :", ','.join(set3))

    elif(opt==2):
        set3 = set1 ^ set2
        print("Distinct characters :", ','.join(set3))

    else:
        print()
        print("Oops !! INCORRECT CHOICE... Enter correct option (1-2)")

    print()
    ch = input("Want to view menu again ? (y/n) : ")

print()

