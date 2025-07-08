# pRint no And its cube in a dictionary
def dictcube():
    dc = {}
    no=[]
    total_ele=int(input("Enter the no of elements you want in the list:-"))
    for i in range(total_ele):
        num=int(input("Enter the no. you want in the list:- "))
        no.append(num)
    cube = list(map(lambda x : x**3,no))   
    for k in range(len(no)):
        dc[no[k]] = cube[k]
    print(dc)
    print(cube)
    print(type(cube))
    
def main():
    a = input("Press enter to print the dictionary.\n")
    dictcube()
main()

