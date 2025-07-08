# Program using function that reads a text file and calculates the frequency of vowels.
# Use a variable of dictionary type to maintain the count.

f = open("file13.txt","a")
f.close()

def freqvowel_func(st1):
    freqvow = {}
    freqvow['a'] = 0
    freqvow['e'] = 0
    freqvow['i'] = 0
    freqvow['o'] = 0
    freqvow['u'] = 0

    st1 = st1.lower()
    for i in st1:
        if(i=='a'):
            freqvow[i] = st1.count(i)

        elif(i=='e'):
            freqvow[i] = st1.count(i)

        elif(i=='i'):
            freqvow[i] = st1.count(i)

        elif(i=='o'):
            freqvow[i] = st1.count(i)

        elif(i=='u'):
            freqvow[i] = st1.count(i)    

    return(freqvow)

def main():
    with open("file13.txt", "r") as f:
        txt = f.read()

        if(len(txt)==0):
           print("File is empty !!")

        else:   
            freqvowel = freqvowel_func(txt)
            print()
            print('Text file is :- "file13.txt"')
            print()
            print("VOWELS  :  FREQUENCY")
            
            for key,value in freqvowel.items():
                print(" '",end='')
                print(key,end='')
                print("'    :    ",value)


main()

