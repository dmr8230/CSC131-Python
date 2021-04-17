#==========================================================================
# PROGRAM PURPOSE:... Ch9 - Personal Translation Dictionary 
# AUTHOR:............ Rowe, Danielle
# COURSE:............ CSC 131-006
# TERM:.............. Spring 2019
# COLLABORATION:..... I looked up some of the syntax online, and one of the tutor helped me with a few computing errors 
# WORK TIME(h:mm):... 2:30
#==========================================================================
try:
    m = open('langDict.txt', 'r')
except:
    langDict = {"hello":{"Spanish":"hola","French":"bonjour"}, "goodbye":{"Spanish":"adios"}, "yes":{"Spanish":"si"}}
    p = open('langDict.txt', 'w')
    p.write(str(langDict))
    p.close()
    m = open('langDict.txt', 'r')

m.read()
m.close()
f = open('langDict.txt', 'r')
langDict = eval(f.read())

# create an open key with a few key words and translations
# create a function that has the menu printed out

def MainMenu():
        """ Creates main menu so that the user can chose to either translate, add a word to the dictionary, print the current
            dictionary, or exit the program. Then it makes sure that the user entered the correct number to do one of
            these capabilities, and it creates user input and returns so they can navigate through the menu"""
        
        print("Main Menu")
        print("1 -- translate a word")
        print("2 -- add a word to dict")
        print("3 -- print current translation dictionary")
        print("4 -- exit")
        
        selection = int(input("Please make a selection: "))

        if selection != 1 and selection != 2 and selection != 3 and selection != 4:
            selection = input("Invalid entry, please choose a number between 1-4: ") 

        # make sure it's 1-4 
        return selection

selection1 = 1

while selection1 != 4: 
    
    #try:
    
    #print out please make a selection and then ask for user input
    # do a series of if statements for the user input in order to see what to do

        selection1 = MainMenu()


        #fix upper/lower case problem

        UClangDict = {}
        for s in langDict:
            
            for q in langDict:
                UClangDict[s.upper()] = langDict[s]

        print (UClangDict)
        # for 1

        if selection1 == 1: #this isn't working 
            # then ask for an english word to translate
            tword = input("Provide an English word: ")
            UCtword = tword.upper()
            # if statements so if our user input is in our dictionary print the answer
            if UCtword in UClangDict: 
                print (tword, " -- ", langDict[tword]) 
            else: 
                print("I'm sorry, there is no translation in this dictionary for that word") 

        # for 2

        if selection1 == 2: 
            # ask for user input for a word to translate
            dentry = input("What English word are you providing a translation for (this should be all lowercase): ")
            UCdentry = dentry.upper() 
            ulang = input("What language is the translated word in(your first letter should be capitalized): ")
            UCulang = ulang.upper()
            utrans = input("What is the translated word(this should be all lowercase): ")
            UCutrans = utrans.upper() 
            UCdentry = dentry.upper()
            if dentry in langDict and ulang in langDict[dentry]:
                print("The word already exists in this language:")
                print(dentry, " -- ", langDict[dentry])
            elif dentry in langDict and ulang not in langDict[dentry]: # find a way to make this work so that it asks for a different language
                print("This word exists in the dictionary, the translation for this language has been added:")
                langDict[dentry].update({ulang:utrans})
            else: #this repeats the translation 2 times for some reason 
                langDict.update({dentry:{ulang:utrans}}) #figure out how this works
                
            # ask what language to translate in
            #then ask for the translation
            # if the word is already in the dictionary
                # if word in dictionary:
                    #print(Sorry, this word is already in the dictionary for this language)
                    #print the word and language and translation 
                #else:
                    #dictionary[word].add then somehow add in the language

        # for 3

        if selection1 == 3: 
            # print each different translation
            for n in langDict:
                print(n, " -- ", langDict[n]) 


s = open('langDict.txt', 'w')
s.write(str(langDict))
s.close() 





