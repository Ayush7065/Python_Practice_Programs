# Program using function to return nth term of fibonacci sequence using iteration and recursion.

def itfibonacci(no):
    n1 = 0
    n2 = 1
    sum = 0

    if(no==1):
        return(n1)

    elif(no==2):
        return(n2)

    else:
        for i in range(1,no-1):
            sum = n1+n2
            n1 = n2
            n2 = sum
            
        return(sum)

def recfibonacci(no):
    if(no==1):
        return(0)

    elif(no==2):
        return(1)

    else:
        return(recfibonacci(no-1) + recfibonacci(no-2))
    

def main():
    n = int(input("Enter the value of n for the nth term of Fibonacci sequence = "))
    
    term = itfibonacci(n)
    print("Using Iteration :",term)

    term = recfibonacci(n)
    print("Using Recursion :",term)

    
main()



