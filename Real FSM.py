#Aaron Gumabong
#Dan Ortiz
#CPSC 323
#Professor Choi
 
#Array to hold the integer FSM
intlist = [2,2]
#Function takes in a word and checks if the word is an Integer. 
def integer(word):
    #Intializing starting state and column to default values
    state = 1
    col = 0
    #Loop for the length of the word. If it is anything but a digit, the function will return False.
    for i in range(0,len(word)):
        if(word[i].isdigit()):
            state = intlist[state-1]
        else:
            return False
    return True

#2D array of the Identifier Finite State Machine
idlist = [[2,5],[3,4],[3,4],[3,4],[5,5]]
#Function to determine the column that the FSM goes into. Accepted column states are any digits or alphanumeric letters.
def id_to_col(c):
    if (c.isdigit()):
        return 1
    elif(c.isalpha()):
        return 0

#Function that takes in a word and checks if the word in the statement is an identifier or not. Returns True if it is an identifier, False if it is not.
def iden(word):
    #Initialize starting state and the column to default values
    state = 1
    col = 0
    #Loop for the length of the input
    for i in range(0,len(word)):
        #Check if the input is a letter or digit. Non-valid characters will automatically have the function return False.
        if (word[i].isalpha() or word[i].isdigit()):
            #print ("Char is: " + str(word[i]) + " and state is: " + str(state))
            state = idlist[state-1][id_to_col(word[i])]
        else:
            return False
    #The two accepting states are 3 and 2. Both will verify that the input is an Identifier.
    if (state == 3 or state == 2):
        return True
    #If it is in neither of those states, return False.
    else:
        return False                   
        
    

#Converts the character input to the column number for the Real FSM. Valid inputs are digits and ".".
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
    #Only accepting state is 4. If the state is not 4 then the function will return False.
    if (state == 4):
        return True    
    else:
        return False

#Lists to store the different types of keywords, operators and seperators
keywords = ["if", "while", "for", "whileend", "else", "ifend", "whileend", "get", "put", "and", "true", "false"]
operators = ["+","-","*","/","%", "=", "<",">", "&", "|"]
sep = ["(", ")", "[", "]", "{","}", "$$"]

#New form of lexer that takes in a token and returns the token type
def lexer(token):
    if (token in keywords):
        print("keyword")
        return "keyword"
    elif (token in operators):
        print("operator")
        return "operator"
    elif (token in "sep"):
        print("separator")
        return seperator
    elif (real(token) == True):
        print("real")
        return "real"
    elif (iden(token) == True):
        print("identifier")
        return "identifier"
    elif (integer(token) == True):
        print("integer")
        return "integer"

###Lexer function. Takes in the name of a file and reads each line and separates them into tokens and lexemes. 
##def lexer(file_name):
##
##    
##    #open the file
##    f=open(file_name,"r")
##    #Store each line of the file into an array
##    content = f.read().split("\n")    
##    
##    print("Lexeme" + "\t" + "token")
##    print("----------"+"\t" + "--------")
##    
##    #Loops j amount of times, j being the number of lines in the file.
##    for j in range(0,len(content)):     
##        
##        #Split each individual line into words separated by a space and put it in a list.
##        clist = content[j].split(" ")
##       
##        #Parse each line and print out what each token is.
##        print("\n")
##        comment = False
##        for k in range(0, len(clist)):
##            
##            #Variable used to identify separators. 
##            pword = clist[k]
##            #If there is an empty line skip the line. 
##            if len(pword) == 0:
##                continue
##            #Check if the symbol is a comment. if it is, then every subsequent token will be a comment until "*]" is reached.
##            
##            if(pword[:2] == "[*"):
##                print(pword[:2] + "\t" + "Comment")
##                print(pword[2:] + "\t" + "Comment")
##                comment = True
##                continue
##
##            if(pword[-2:] == "*]"):
##                print(pword[-2:] + "\t" + "Comment")
##                print(pword[:-2] + "\t" + "Comment")
##                comment = False
##                continue
##
##            if (comment == True):
##                print(clist[k] + "\t" + "Comment")
##                continue
##            
##            
##            #Check to see if there is an seperator at the beginning of the word. If there is, separate it from the word and print out the seperator and then the token that encapsulates it.
##            if (pword[0] in sep):
##                print(pword[0] + "\t" + "Seperator")
##                pword = pword[1:]
##                if (iden(pword) == True):
##                    print(pword + "\t" + "Identifier")
##                elif(real(pword) == True):
##                     print(pword + "\t" + "real")
##                elif(integer(pword) == True):
##                     print(pword + "\t" + "Integer")
##            #Check to see if there is an seperator at the end of the word. If there is, separate it from the word and print out the seperator and then the token that encapsulates it.
##            elif(pword[len(pword)-1] in sep):
##                pend = pword[len(pword)-1]            
##                pword = pword[:-1]
##                if (iden(pword) == True):
##                    print(pword + "\t" + "Identifier")
##                elif(real(pword) == True):
##                     print(pword + "\t" + "real")
##                elif(integer(pword) == True):
##                     print(pword + "\t" + "Integer")
##                print(pend + "\t" + "Seperator")
##                
##            #Checks if the word is an operator.
##            elif (clist[k] in operators):
##                print(clist[k] + "\t" + "Operator")
##                
##                
##            #Checks if the word is a keyword.
##            elif (clist[k] in keywords):
##                print(clist[k] + "\t" + "Keyword")
##               
##                
##            #Checks if the word is an Identifier.
##            elif (iden(clist[k]) == True):
##                print(clist[k] + "\t" + "Identifier")
##              
##                
##            #Checks if the word is a real.
##            elif(real(clist[k]) == True):
##                 print(clist[k] + "\t" + "Real")
##               
##                 
##            #Check if the word is an Integer
##            elif(integer(clist[k]) == True):                 
##                 print(clist[k] + "\t" + "Integer")
##               
##            #If the token fits none of the above values, return invalid token.
##            else:
##                print(clist[k] + "\t" + "Invalid Token")


    

##file = input("Please enter a file name: ")
##lexer(file)
##q = (input("\n Press any key to stop."))
