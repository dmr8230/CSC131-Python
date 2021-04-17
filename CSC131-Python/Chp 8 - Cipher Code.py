#==========================================================================
# PROGRAM PURPOSE:... Ch8 - Decryption Using Letter Frequency 
# AUTHOR:............ Rowe, Danielle
# COURSE:............ CSC 131-006
# TERM:.............. Spring 2019
# COLLABORATION:..... I looked at past code for referencing, also Aaron helped me from tutoring
# WORK TIME(h:mm):... 7 
#==========================================================================




from csc131Helper import getFile # calls the function from getFile()
import operator
test1 = getFile()
print(test1) 


cipher = "etaoinshrdlcumwfgypbvkjxqz"
freqcounter = {}
freqcountersort = []


ofname = test1[0].replace('.','solved.')
ofile = open(ofname,'w') 

wordsr = test1[1].readlines()
for line in wordsr:
    line = line.lower().strip('\n') 
    
    for i in line:
        if i in 'abcdefghijklmnopqrstuvwxyz':
            if i in freqcounter:
                freqcounter[i] += 1
            else:
                freqcounter[i] = 1

for letter in 'abcdefghijklmnopqrstuvwxyz':
    if letter not in freqcounter:
        freqcounter[letter] = 0 
    
for keys in freqcounter:
    sortmeth = [keys, freqcounter[keys]]
    freqcountersort.append(sortmeth)
freqcountersort.sort(key=operator.itemgetter(1))


print(freqcountersort)
string2 = ''
for m in freqcountersort[::-1]:
    string2 += m[0]
    

for line in wordsr:
    line = line.lower().strip('\n')
    estring = ''
    for char in line:
        if char in 'abcdefghijklmnopqrstuvwxyz':
            x = string2.find(char)
            estring += cipher[x] 
        else:
            estring += char

    print(estring + '\n')  
    ofile.write(estring + '\n')
            
        

ofile.close()

    
        
