# Program to define a class STUDENT to store student's details and define user-defined function members.

class Student:
    maxavg = 0
    
    def __init__(self,nm,rn,m1,m2,m3):
        self.nm = nm
        self.rn = rn
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
        self.avg = (self.m1+self.m2+self.m3)/3

        if(self.avg>Student.maxavg):
            Student.maxavg = self.avg

    def display(self):
        print("Student's name :",self.nm)
        print("Student's roll number :",self.rn)
        print("Student's marks in subject 1 :",self.m1)
        print("Student's marks in subject 2 :",self.m2)
        print("Student's marks in subject 3 :",self.m3)
        print("Student's average marks :",self.avg)

    def disp_maxavg():
        print("Maximum average marks among all students is :",Student.maxavg)

    def __del__(self):
        print()


def main():
    print()
    print("Enter details of the students :-")
    print()
    stdlist = []

    ch = 'y'
    while(ch=='y' or ch=='Y'):
        name = input("Enter name of the student : ")
        rollno = int(input("Enter roll number of the student : "))
        marks1 = int(input("Enter marks in subject 1 : "))
        marks2 = int(input("Enter marks in subject 2 : "))
        marks3 = int(input("Enter marks in subject 3 : "))

        s1 = Student(name,rollno,marks1,marks2,marks3)
        stdlist.append(s1)
        print("Average marks :",s1.avg)
        print()
        ch = input("Want to add more student details (y/n) : ")
        print()
                
    again='y'
    while(again=='y' or again=='Y'):
        print("        -: MENU :-")
        print("1. Display details of particular students.")
        print("2. Display maximum average marks of student.")
        print()

        opt = int(input("Enter your choice = "))
        
        if(opt==1):
            print()
            rno = int(input("Enter student's roll number whose details you want to display : "))
            flag = 1
            for i in range(len(stdlist)):
                if(rno==stdlist[i].rn):
                    print()
                    print("Student's details are :-")
                    stdlist[i].display()
                    flag = 1
                    break

                else:
                    flag = 0

            if(flag==0):
                print("Student's details not found !!")

        elif(opt==2):    
            Student.disp_maxavg()

        else:
            print("Oops! INCORRECT CHOICE. Enter correct choice(1-2)")

        print()
        again = input("Want to view menu again ? (y/n) : ")
        print()

    print("All student's details deleted !!")    


main()
        
