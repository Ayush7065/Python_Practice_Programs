# Program to implement a class for finding area and perimeter of a rectangular playground.
# Write constructor, destructor and functions for calculating area and perimeter.

class rec:
    def __init__(self,l,b):
        self.l = l
        self.b = b

    def area(self):
        a = self.l * self.b
        return(a)

    def perimeter(self):
        p = 2*(self.l + self.b)
        return(p)

    def __del__(self):
        print("Details of rectangular playground deleted !!")
        print()


def main():
    print()
    print("Enter sides of rectangular playground :-")

    length = int(input("Enter length of the playground = "))
    breadth = int(input("Enter breadth of the playground = "))
    pg = rec(length,breadth)

    ch = 'y'
    while(ch=='y' or ch=='Y'):
        print()
        print("  -: MENU :-")
        print("1. Area of the playground.")
        print("2. Perimeter of the playground.")
        print()

        opt = int(input("Enter your choice = "))

        if(opt==1):
            ar = pg.area()
            print("Area of the playground is :",ar)

        elif(opt==2):
            pr = pg.perimeter()
            print("Perimeter of the playground is :",pr)

        else:
            print()
            print("Oops !! INCORRECT CHOICE... Enter correct option (1-2)")

        print()
        ch = input("Want to view menu again ? (y/n) : ")

    print()

main()


