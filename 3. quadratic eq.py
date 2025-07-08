# program to calculate the roots of a quadratic equation.

eq = input("Enter quadratic equation in the format ax^2+bx+c = ")

a1 = eq[0]

if(a1=='-'):
    a = -int(eq[1])
    b1 = eq[5]
    c1 = eq[8]

    if(b1=='+'):
        b = int(eq[6]) 
    else:
        b = -int(eq[6])

    if(c1=='+'):
        c = int(eq[9])
    else:
        c = -int(eq[9])

else:
    a = int(eq[0])
    b1 = eq[4]
    c1 = eq[7]

    if(b1=='+'):
        b = int(eq[5]) 
    else:
        b = -int(eq[5])

    if(c1=='+'):
        c = int(eq[8])
    else:
        c = -int(eq[8])    
     
d = ((b*b)-(4*a*c))**(1/2)

z1 = (-b+d)/(2*a)
z2 = (-b-d)/(2*a)

print("Zeroes of the quadraric equation are = %.2f" %z1,"and %.2f" %z2)














