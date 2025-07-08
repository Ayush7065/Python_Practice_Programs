# Hollow Cylnder

def dollar():
    r=int(input("Enter no. of Rows you want to print:- "))
    c =int(input("Enter no. of Collumns you want to print:- "))

    for i in range(1,r+1):
        for j in range(1,c+1):
            if(i!=1 and i!=r):
                if(j!=1 and j!=c):
                    print(" ",end='')
                else:
                    print("$",end='')
            else:
                print("$",end='')
        print()
dollar()





            
