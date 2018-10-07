#2D array of the Identifier Finite State Machine
idlist = [[2,5],[3,4],[3,4],[3,4],[5,5]]
def id_to_col(c):
    if (c.isdigit()):
        return 1
    elif(c.isalpha()):
        return 0

#Function that takes in a word and checks if the word in the statement is an identifier or not
def iden(word):
    state = 1
    col = 0
    for i in range(0,len(word)):
        if (word[i].isalpha() or word[i].isdigit()):
            #print ("Char is: " + str(word[i]) + " and state is: " + str(state))
            state = idlist[state-1][id_to_col(word[i])]
        else:
            return False
    if (state == 3 or state == 2):
        return True
    else:
        return False                   
        
    

#Converts the character input to the column number for the Real FSM
def ch_to_col(c):
    if (c == "."):
        return 1
    elif (c.isdigit()):
        return 0


#2D Array of the Real Finite State Machine.
realarray = [[2,5], [2, 3] , [4,5], [4,5], [5,5]]
#Function that takes in a word and checks if the word in if the statement is a "real" or not.
#Returns True if the statement is a real, false if it is not.
def real(word):
    state = 1
    col = 0
    for i in range(0,len(word)):
        #Checks if the current letter is a number or "."
        #If it is not, then automatically return False
        if (word[i].isdigit() or word[i] == "."):  
            #print ("Char is: " + str(word[i]) + " and state is: " + str(state))
            state = realarray[state-1][ch_to_col(word[i])]
        else:
            return False
        
    
    if (state == 4):
        return True    
    else:
        return False

keywords = ["if", "while", "for", "whileend", "else", "ifend", "whileend", "get", "put", "and"]
operators = ["+","-","*","/","%", "=", "<",">"]
sep = ["(", ")", "[", "]", "{","}"]

#open the file
f=open("test.txt","r")
#Store each line of the file into an array
content = f.read().split("\n")
content.remove('')
        
print("Lexeme" + "\t" + "token")
print("----------"+"\t" + "--------")
for j in range(0,len(content)):
    
    #Split each individual line into words separated by a space and put it in a list
    clist = content[j].split(" ")
    #print (clist)
    #Parse each line and print out what each identifier is
    for k in range(0, len(clist)):
        pword = clist[k]
        #Check to see if there is an seperator at the beginning of the word
        if (pword[0] in sep):
            print(pword[0] + "\t" + "Seperator")
            pword = pword[1:]
            if (iden(pword) == True):
                print(pword + "\t" + "Identifier")
            elif(real(pword) == True):
                 print(pword + "\t" + "real")                
        #Check to see if there is a seperator at the end of the word
        elif(pword[len(pword)-1] in sep):
            pend = pword[len(pword)-1]            
            pword = pword[:-1]
            if (iden(pword) == True):
                print(pword + "\t" + "Identifier")
            elif(real(pword) == True):
                 print(pword + "\t" + "real")
            print(pend + "\t" + "Seperator")
        #Checks if the word is an operator
        elif (clist[k] in operators):
            print(clist[k] + "\t" + "Operator")
        #Checks if the word is a keyword
        elif (clist[k] in keywords):
            print(clist[k] + "\t" + "Keyword")
        #Checks if the word is an Identifier
        elif (iden(clist[k]) == True):
            print(clist[k] + "\t" + "Identifier")
        #Checks if the word is a real
        elif(real(clist[k]) == True):
             print(clist[k] + "\t" + "real")
        
        
       
   
       
            
        
                   
                   
  
    





        
        
    
