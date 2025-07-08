# Program to perform the functions on lists.

print()
n = int(input("Enter size of list : "))
lst = []

for i in range(n):
    print("Enter element",(i+1),"= ",end='')
    el = (input())
    lst.append(el)

print("Your list is : ",lst)

typelist = 1
for i in lst:
    for j in i:
        if not(j>='0' and j<='9'):
            typelist = 0
            break

if(typelist==0):
    typelist = 2
    for i in lst:
        for j in i:
            if not((j>='A' and j<='Z')or(j>='a' and j<='z')):
                typelist = 0
                break
    
ch = 'y'
while(ch=='y' or ch=='Y'):
    print()
    print("  -: MENU :-")
    print("1. Check all elements in list are numbers or not.")
    print("2. If numeric list then count number of odd values in it.")
    print("3. If string list then display the largest string in the list.")
    print("4. If all elements are string then count numeric string and string with alphabets only.")
    print()

    opt = int(input("Enter your choice = "))

    if(opt==1):
        if(typelist==1):
            print("All elements in the list are numbers.")

        else:
            print("All elements in the list are not numbers.")

    elif(opt==2):
        if(typelist==1):
            count = 0
            for i in lst:
                if(int(i)%2!=0):
                    count = count+1

            print("Number of odd values in the list are :",count)        

        else:
            print("The list is not numeric list.")

    elif(opt==3):
        if(typelist==2):
            largest = lst[0]
            for i in lst[1:]:
                if(len(i)>len(largest)):
                    largest = i

            print("Largest string in the list is :",largest)        

        else:
            print("The list is not string list.")

    elif(opt==4):
        num = 0
        al = 0
        for i in lst:
            if(i.isdigit()):
                num = num + 1

            elif(i.isalpha()):
                al = al + 1

        print("Numeric strings :",num)
        print("Strings with alphabets only :",al)

    else:
        print("Oops !! INCORRECT CHOICE... Enter correct option (1-4)")
        
    print()
    ch = input("Want to view menu again ? (y/n) : ")

print()

