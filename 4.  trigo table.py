# program to generate table of sines, cosines and tangents.

import math

ch = 'y'

while(ch=='y'):
    print("What would like to print?")
    print("1. Sine table. \n2. Cosine table. \n3. Tangent table. \n")

    opt = int(input("Enter your choice = "))
    print()
    a = 0
    
    if(opt==1):
        print("Table of Sines : ")
        while(a<=360):
            print("Sin(",a,")= %.2f" %math.sin(a),sep='')
            a = a+45

    elif(opt==2):
         print("Table of Cosines : ")
         while(a<=360):
            print("Cos(",a,")= %.2f" %math.cos(a),sep='')
            a = a+45


    elif(opt==3):
        print("Table of Tangents : ")
        while(a<=360):
            print("Tan(",a,")= %.2f" %math.tan(a),sep='')
            a = a+45

    else:
        print("Enter correct choice (1/2/3)")

    ch = input("Want to print more (y/n) : ")
    print()

    


    

    


        
