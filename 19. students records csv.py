# Program to maintain student records using CSV files.

import csv

f = open("student.csv","a")
f.close()

fname = "student.csv"

def s_add():
    rno = int(input("Enter student's roll number : "))
    name = input("Enter student's name : ")
    m1 = int(input("Enter marks in subject 1 :"))
    m2 = int(input("Enter marks in subject 2 :"))
    m3 = int(input("Enter marks in subject 3 :"))
    marks = m1+m2+m3
    
    std = []
    std.append(rno)
    std.append(name)
    std.append(marks)

    with open(fname,"a",newline="") as f:
        writer = csv.writer(f)
        writer.writerow(std)

    print("Student's details added successfully !!")


def s_read():
    with open(fname,"r") as f:
        reader = csv.reader(f)
        
        stdlst = []
        for i in reader:
            std = []
            for j in i:
                std.append(j)

            stdlst.append(std)

    return(stdlst)


def s_disp(rn):
    stdlist = s_read()

    for s in stdlist:
        if(s[0]==rn):
            print()
            print("Roll number :",s[0])
            print("Student's name :",s[1])
            print("Total marks :",s[2])
            

def s_disp3():
    stdlist = s_read()
    if(len(stdlist)==0):
        print("No students details found in the file !! Add some student's details first.")

    else:
        print("Details of every 3rd student in the file are :-")
        for i in range(len(stdlist)):
            if((i+3)%3==0):
                s_disp(stdlist[i][0])


def menu():
    print()
    print("  -: STUDENT'S RECORDS :-")
    print("1. Add new student details.")
    print("2. Display details of every 3rd student from the file.")
    print()


def main():
    ch = 'y'
    while(ch=='y' or ch=='Y'):
        menu()
        opt = int(input("Enter your choice : "))
        print()

        if(opt==1):
            s_add()

        elif(opt==2):
            s_disp3()

        else:
            print("Oops !! INCORRECT CHOICE...Enter correct option (1-2)")

        print()
        ch = input("Want to view menu again (y/n) : ")


if(__name__ == "__main__"):
    main()
