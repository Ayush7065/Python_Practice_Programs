# Menu driven program using in-built string functions.

st = input("Enter your string = ")

while(1):
    print()
    print("MENU")
    print("1. Look for a substring in the given string and return its position.")
    print("2. Replace substring 'good' with 'best' in the given string.")
    print("3. Find all the substring in the string which are separated by delimiter ;")
    print("4. Convert the given text into title form.")
    print("5. Convert lowercase to uppercase and uppercase to lowercase in the given string.")
    print("6. Exit.\n")

    opt = int(input("Enter your choice = "))

    if(opt==1):
        substr = input("Enter substring for which you are looking for : ")

        if(substr in st):
            n = st.count(substr)
            pos = st.find(substr)+1
            print("Position of",substr,"in the string is :")

            for i in range(n): 
                print(pos,end='')
                pos = st.find(substr,pos)+1
                if(pos!=0):
                    print(',',end='')
                                    
            print()    

        else:
            print(substr,"not found in the string.")

    elif(opt==2):
        if('good' in st):
            st1 = st.replace('good','best')
            print("Replaced string is : ",st1)

        else:
            print("'good' is not in the string.")

    elif(opt==3):
        if(';' in st):
            st1 = st.split(';')
            print("Substrings seperated by delimiter ; are :")
            for i in range(len(st1)):
                print(st1[i])

        else:
            print("No substring is seperated by delimiter ;")

    elif(opt==4):
        st1 = st.title()
        print("Title form : ",st1)

    elif(opt==5):
        st1 = st.swapcase()
        print("String after swaping lowercase and uppercase letters is : ",st1)

    elif(opt==6):
        break

    else:
        print("Oops! Wrong choice, enter correct choice(1-6)")

        
