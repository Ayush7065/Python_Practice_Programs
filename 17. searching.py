# Menu driven program using function to do list searching.

def lin_search(A,n):
    for i in range(len(A)):
        if(A[i]==n):
            return(i+1)

    return(-1)


def bin_search(A,n):
    lb = 0
    ub = len(A)-1

    while(lb<=ub):
        mid = (lb+ub)//2
        if(n==A[mid]):
            return(mid+1)

        elif(n<A[mid]):
            ub = mid-1

        elif(n>A[mid]):
            lb = mid+1

    if(lb>ub):
        return(-1)


def main():
    print()
    lst = eval(input("Enter the numeric list : "))
    print()
    print("  -: MENU :-")
    print("1. Linear search.")
    print("2. Binary search.")
    print("3. Exit.")
    print()
    
    while(1):
        opt = int(input("Enter your choice : "))
        
        if(opt==1):
            n = int(input("Enter element you want to search in the list : "))
            p = lin_search(lst,n)
            if(p==-1):
                print(n,"not found in the list!!")

            else:    
               print(n,"found in the list at position",p)

        elif(opt==2):
            ln = len(lst)
            flag = 1
            for i in range(ln-1):
                if(lst[i]>lst[i+1]):
                    print("List must be sorted in ascending order for binary search!!")
                    flag = 0
                    break

            if(flag==1):
                n = int(input("Enter element you want to search in the list : "))
                p = bin_search(lst,n)
                if(p==-1):
                    print(n,"not found in the list!!")

                else:    
                   print(n,"found in the list at position",p)

        elif(opt==3):
            break

        else:
            print("Oops!! INCORRECT CHOICE... Enter correct option (1-3)")

        print()    


main()
