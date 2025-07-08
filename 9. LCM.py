# Program using function that takes two numbers as input parameters and returns their least common multiple.

def lcmfn(num1,num2):
    if(num1>num2):
        n1 = num1
        n2 = num2

    else:
        n1 = num2
        n2 = num1
    
    for i in range(n1,(n1*n2)+1):
        if(i%n1==0 and i%n2==0):
            res = i
            break

    return(res)    
            
def main():
    no1 = int(input("Enter 1st number : "))
    no2 = int(input("Enter 2nd number : "))

    lcm = lcmfn(no1,no2)
    print("LCM of",no1,"and",no2,"is =",lcm)


main()



