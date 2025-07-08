# Menu driven program to calculate area of square, rectangle, triangle and circle.

def areasq():
    s = float(input("Enter side of square : "))
    ar = s*s
    return(ar)     

def arearec():
    l = float(input("Enter length of rectangle : "))
    b = float(input("Enter breadth of rectangle : "))
    ar = l*b
    return(ar)

def areatri():
    b = float(input("Enter base of triangle : "))
    h = float(input("Enter height of triangle : "))
    ar = 0.5*b*h
    return(ar)
    
def areacir():
    r = float(input("Enter radius of circle : "))
    ar = 3.14*r*r
    return(ar)

def main():
    ch = 'y'
    area = 0

    while(ch=='y' or ch=='Y'):
        print(" 1.Area of square.\n 2.Area of rectangle.\n 3.Area of triangle.\n 4.Area of circle.\n 5.Exit.")
        opt = int(input("Enter your choice = "))
        print()

        if(opt==1):
            area = areasq()
            print("Area of square is %.2f" %area)

        elif(opt==2):
            area = arearec()
            print("Area of rectangle is %.2f" %area)

        elif(opt==3):
            area = areatri()
            print("Area of triangle is %.2f" %area)

        elif(opt==4):
            area = areacir()
            print("Area of circle is %.2f" %area)

        elif(opt==5):
            break
        
        else:
            print("OOPS!! INCORRECT CHOICE, Enter correct choice (1/2/3/4/5)\n")
            continue

        ch = input("Want to enter more (y/n) : ")
        print()

main()



    
