# Program using function that takes a number as an input and finds its reverse and computes the sum of its digits.

def revsum(n):  
    n1 = n
    n2 = 0
    count = 0
    
    while(n1>10):
        n1 = n1//10
        count = count+1

    n1 = n

    while(n1>0):
        r = n1%10
        n1 = n1//10
        n2 = r*(10**count)+n2
        count = count-1

    print("The reverse of the number you entered is :",n2)

    sum = n+n2

    print("The sum of the number and the reverse of it is :",sum)
    

def main():
    num = int(input("Enter a number to find its reverse and then sum : "))
    revsum(num)

main()
