# Menu driven program using function to do list sorting.

def sel_sort(A):
    n = len(A)

    for i in range(0,n-1):
        indx = i
        for j in range(i+1,n):
            if(A[indx]>A[j]):
                indx = j

        A[i],A[indx] = A[indx],A[i]


def in_sort(A):
    n = len(A)

    for i in range(1,n):
        temp = A[i]
        j = i-1
        while(j>=0 and A[j]>temp):
            A[j+1] = A[j]
            j = j-1

        A[j+1] = temp
            
    
def main():
    print()
    lst = eval(input("Enter the numeric list : "))
    print()
    print("  -: MENU :-")
    print("1. Selection sort.")
    print("2. Insertion sort.")
    print("3. Exit.")
    print()
    
    while(1):
        opt = int(input("Enter your choice : "))
        
        if(opt==1):
            sel_sort(lst)
            print("Sorted list by selection sort is :",lst)

        elif(opt==2):
            in_sort(lst)
            print("Sorted list by insertion sort is :",lst)

        elif(opt==3):
            break

        else:
            print("Oops!! INCORRECT CHOICE... Enter correct option (1-3)")

        print()    

main()

