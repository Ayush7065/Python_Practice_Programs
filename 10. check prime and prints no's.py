# Program using function that takes a number as an input and determine whether it is prime or not.
# Use this function to display all prime numbers till the provided number n.

def prime(n1):
    fact = 1
    i =2

    while(i<n1):
        if(n1%i==0):
            fact = fact+1
            break

        i = i+1
       
    if(fact==1):
        return(fact)

    else:
        return(fact)


def main():
    n = int(input("Enter number you want to check whether it is prime or not = "))
    check = prime(n)

    if(check==1):
        print(n,"is a prime number. \n")

    else:
        print(n,"is not a prime number. \n")

    print("Prime numbers till",n,"are : \n 2")

    for i in range(3,n+1,2):
        check = prime(i)

        if(check==1):
            print("",i)


main()


