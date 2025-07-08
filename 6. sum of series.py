# Program using function that takes a number as an input from the user and computes its factorial (using recursion).
# then find the sum of the series : 1 - 1/1! + 1/2! - 1/3! + ... + 1/n! .

def factorial(n1):
    if(n1==1):
        return(1)

    else:
        temp = n1*factorial(n1-1)
        return(temp)
        
   
def main():
    n = int(input("Enter the value of n to find the sum of series : 1 - 1/1! + 1/2! - 1/3! + ... + 1/n! : "))
    sign = -1
    sum = 1
    
    for i in range(1,n):
        f = factorial(i)
        sum = sum + sign*(1/f)
        sign = -1*sign

    print("Sum of series upto",n,"is = %.3f" %sum)

    
main()


