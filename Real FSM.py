#Aaron Gumabong
#Dan Ortiz
#CPSC 323
#Professor Choi


# Variables to keep track of top-down parser
import time
current_lexeme = None
global list_of_lexemes
global position_in_list
global assembly
global memory_address
global current_type

assembly = []
list_of_lexemes = []
list_of_types = [] # by Dan
symbol_table = {} # by Dan


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
keywords = ["if", "while", "for", "whileend", "else", "ifend", "whileend", "get", "put", "and", "true", "false", "int", "function", "return", "boolean", "real"]
operators = ["+","-","*","/","%", "=", "<",">", "|", ":"]
sep = ["(", ")", "[", "]", "{","}", "$$" , ";", ","]
ops = ["+", "-", "*", "/"]

#Lexer 2 parses the text file and only adds valid tokens to the list_of_lexemes function.
def lexer2(file_name):
    global list_of_lexemes

    
    #open the file
    f=open(file_name,"r")
    #Store each line of the file into an array
    content = f.read().split("\n")    
    
    print("Lexeme" + "\t \t \t" + "token")
    print("----------"+"\t \t \t"+ "--------")
    comment = False
    #Loops j amount of times, j being the number of lines in the file.
    for j in range(0,len(content)):     
        
        #Split each individual line into words separated by a space and put it in a list.
        clist = content[j].split(" ")
 
       
        #Parse each line and print out what each token is.
        #print("\n")
       
        for k in range(0, len(clist)):
            
            #Variable used to identify separators. 
            pword = clist[k]
            
            #If there is an empty line skip the line. 
            if len(pword) == 0 or pword == "" or pword == '' or not pword:             
                continue
            #Check if the symbol is a comment. if it is, then every subsequent token will be a comment until "*]" is reached.

            if(pword[-2:] == "*]"):
                #print(pword[-2:] + "\t" + "Comment")
                #print(pword[:-2] + "\t" + "Comment")
                comment = False
                continue
            
            if(pword[:2] == "[*"):
                #print(pword[:2] + "\t" + "Comment")
                #print(pword[2:] + "\t" + "Comment")
                comment = True
                continue

            if (comment == True):
                #print(clist[k] + "\t" + "Comment")
                continue

            
            
            

            #Check to see if there is an seperator at the beginning of the word. If there is, separate it from the word and print out the seperator and then the token that encapsulates it.
            if (pword[0] in sep and pword[len(pword)-1] in sep):
                zled = False
                print(pword[0] + "\t \t \t" + "Seperator")
                fsep = pword[0]
                list_of_lexemes.append(pword[0])
                if (len(pword) ==1 ):
                    continue
                if pword == '' or pword == "":
                    continue
                pword = pword[1:]
                if (pword[len(pword)-1] == ";"):
                    q = len(pword)-1                        
                    zsep = pword[q:]
                    pword = pword[:q]
                    zled = True
                
                z = len(pword)-1
                lsep = pword[z:]
                pword = pword[:z]
                
                if (iden(pword) == True):
                    print(pword + "\t \t \t" + "Identifier")
                    list_of_lexemes.append(pword)
                elif(real(pword) == True):
                    print(pword + "\t \t \t" + "real")
                    list_of_lexemes.append(pword)
                elif(integer(pword) == True):
                    print(pword + "\t \t \t" + "Integer")
                    list_of_lexemes.append(pword)
                if zled == True:
                    list_of_lexemes.append(lsep)
                    print(lsep + "\t \t \t" + "Seperator")
                    list_of_lexemes.append(zsep)
                    print(zsep + "\t \t \t" + "Seperator")

            #######################################    
            if (pword[0] in sep):
                print(pword[0] + "\t \t \t" + "Seperator")
                fsep = pword[0]
                list_of_lexemes.append(pword[0])
                if (len(pword) ==1 ):
                    continue
                if pword == '' or pword == "":
                    continue
                pword = pword[1:]
                if (iden(pword) == True):
                    print(pword + "\t \t \t" + "Identifier")
                    list_of_lexemes.append(pword)
                elif(real(pword) == True):
                    print(pword + "\t \t \t" + "real")
                    list_of_lexemes.append(pword)
                elif(integer(pword) == True):
                    print(pword + "\t \t \t" + "Integer")
                    list_of_lexemes.append(pword)


                
            #Check to see if there is an seperator at the end of the word. If there is, separate it from the word and print out the seperator and then the token that encapsulates it.
            elif(pword[len(pword)-1] in sep):
                print(pword)
                if (pword[len(pword)-1] == ";" and pword[len(pword)-2] in sep):
                    q = len(pword)-1                        
                    zsep = pword[q:]
                    pword = pword[:q]
                pend = pword[len(pword)-1]
                pword = pword[:-1]
                if pword == '' or pword == "":
                    continue
                
                
                if (iden(pword) == True):
                    print(pword + "\t \t \t" + "Identifier")
                    list_of_lexemes.append(pword)
                    list_of_lexemes.append(pend)
                elif(real(pword) == True):
                    print(pword + "\t \t \t" + "real")
                    list_of_lexemes.append(pword)
                    list_of_lexemes.append(pend)
                elif(integer(pword) == True):
                    print(pword + "\t \t \t" + "Integer")
                    list_of_lexemes.append(pword)
                    list_of_lexemes.append(pend)
                print(pend + "\t \t \t" + "Seperator")
                
            #Checks if the word is an operator.
            elif (clist[k] in operators):
                print(clist[k] + "\t \t \t" + "Operator")
                list_of_lexemes.append(clist[k])
                
                
            #Checks if the word is a keyword.
            elif (clist[k] in keywords):
                print(clist[k] + "\t \t \t" + "Keyword")
                list_of_lexemes.append(clist[k])
               
                
            #Checks if the word is an Identifier.
            elif (iden(clist[k]) == True):
                print(clist[k] + "\t \t \t" + "Identifier")
                list_of_lexemes.append(clist[k])
              
                
            #Checks if the word is a real.
            elif(real(clist[k]) == True):
                 print(clist[k] + "\t \t \t" + "Real")
                 list_of_lexemes.append(clist[k])
               
                 
            #Check if the word is an Integer
            elif(integer(clist[k]) == True):                 
                 print(clist[k] + "\t \t \t" + "Integer")
                 list_of_lexemes.append(clist[k])

            #Checks if the word is a Seperator
            elif (clist[k] in sep):
                print (clist[k] + " \t \t \t" + "Separator")
                list_of_lexemes.append(clist[k])
               
            #If the token fits none of the above values, return invalid token.
            else:
                print(clist[k] + "\t \t \t" + "Invalid Token")





#New form of lexer that takes in a token and returns the token type
def lexer(token):
    if (token in keywords):
##        print("keyword")
        return "keyword"
    elif (token in operators):
##        print("operator")
        return "operator"
    elif (token in sep):
##        print("separator")
        return "separator"
    elif (real(token) == True):
##        print("real")
        return "real"
    elif (iden(token) == True):
##        print("identifier")
        return "identifier"
    elif (integer(token) == True):
##        print("integer")
        return "integer"   

def rat18f():
    # Maybe print out the file?
    global current_lexeme
    global position_in_list
    print("<Rat18F> -> <Opt Function Definitions> $$ <Opt Declaration List> <Statement List> $$")
    current_lexeme = list_of_lexemes[position_in_list]
    Opt_Function_Definitions()
    #position_in_list +=1
    current_lexeme = list_of_lexemes[position_in_list]
    print("Current lexeme is: " + current_lexeme)
    #position_in_list+=1
    current_lexeme = list_of_lexemes[position_in_list]
    if (current_lexeme != "$$"):
        print("Error: expected $$ but instead recieved: " + current_lexeme)
    if (current_lexeme == "$$"):
        position_in_list +=1
        current_lexeme = list_of_lexemes[position_in_list]
        print("Current lexeme is: " + current_lexeme)
        print("\n\n\n")
        print ("doing opt dec list")
        print("\n\n\n")
        
        Opt_Declaration_List()
        
        print("Current lexeme is: " + current_lexeme)
        print("\n\n\n")
        print("Doing statement list")
        print("\n\n\n")

        statement_list()
   
        

        if (current_lexeme != "$$"):
            print("Error, expected: '$$' but recieved" + current_lexeme)
        if (current_lexeme == "$$"):
            print("Reached end of file.")

        

def Opt_Function_Definitions():
    global current_lexeme
    global position_in_list
    print("Current lexeme is: " + current_lexeme)
    print("<Opt Function Definitions> -> <Function Definitions> | <Empty>")
    if (current_lexeme != "function"):
        empty()
    else:
        Function_Definitions()

   

def Function_Definitions():
    global current_lexeme
    global position_in_list
    print("Current lexeme is: " + current_lexeme)
    print ("<Function Definitions> -> <Functions> | <Functions> < Function Definitions>")
    Function()

def Function():
    global current_lexeme
    global position_in_list
    print ("<Function> -> function <Identifier> ( <Opt Parameter List> ) <Opt Declaration List> <Body>")
    if (current_lexeme != "function"):
        print("Error: Expected 'function' but instead recieved: " + current_lexeme)
    if (current_lexeme == "function"):
        position_in_list += 1
        current_lexeme = list_of_lexemes[position_in_list]
##        print ("Found function")
        print("Current lexeme is: " + current_lexeme)
        if(lexer(current_lexeme) != "identifier"):
            print("Error: Expected 'identifier' but instead recieved: " + current_lexeme)
        if (lexer(current_lexeme) == "identifier"):
            position_in_list+=1
            current_lexeme = list_of_lexemes[position_in_list]
##            print("Finished with function and identifier, moving to Opt parameter list")
            print("Current lexeme is: " + current_lexeme)
            if (current_lexeme != "("):
                print("Error: Expected '(' but instead recieved: " + current_lexeme)
            if (current_lexeme == "("):
                position_in_list +=1
                current_lexeme = list_of_lexemes[position_in_list]
                Opt_Parameter_List()
                print ("Finished Opt Parameter List")
                print("Current lexeme is: " + current_lexeme)
                if (current_lexeme != ")"):
                    print("Error: Expected ')' but instead recieved: " + current_lexeme)
                if (current_lexeme == ")"):
                    position_in_list +=1
                    current_lexeme = list_of_lexemes[position_in_list]
                    Opt_Declaration_List()
                    print ("Finished with Opt Declaration List")
                    print("Current lexeme is: " + current_lexeme)
                    Body()
                    print("Finished with Body")
                    print("Current lexeme is: " + current_lexeme)
                    position_in_list+=1
                    current_lexeme = list_of_lexemes[position_in_list]
                else:
                    print("Expected ')', but instead recieved" + current_lexeme)
        
        

def Opt_Parameter_List():
    global current_lexeme
    print("Current lexeme is: " + current_lexeme)
    print("<Opt Parameter List> -> <Parameter List> | <Empty>")
    if (current_lexeme == "" or current_lexeme == ''):
        empty()
    else:
        Parameter_List()

def Parameter_List():
    print("Current lexeme is: " + current_lexeme)
    print("<Parameter List> -> <Parameter> | <Parameter> , <Parameter List>")
    Parameter()

    
def Parameter():
    global current_lexeme
    global position_in_list
    print("Current lexeme is: " + current_lexeme)
    print ("<Parameter> -> <IDs> : <Qualifier>")
    print("Inside parameter: before IDs(); current lexeme is " + current_lexeme)
    IDs()
    print("Current lexeme is: " + current_lexeme)
    if (current_lexeme != ":"):
        print("Error: Expected ':' but instead recieved: " + current_lexeme)
    if (current_lexeme == ":"):
        position_in_list +=1
        current_lexeme = list_of_lexemes[position_in_list]
##        print("Finished with IDs, going to qualifier")
##        print ("Current lexeme is: " + current_lexeme)
        qualifier()


def qualifier():
    global current_lexeme
    global position_in_list
    global current_type
    print("Current lexeme is: " + current_lexeme)
    print("<Qualifier -> int | boolean | real")
    if current_lexeme == "int":
        current_type = "int"
        list_of_types.append(current_type)
##        print("int")
        position_in_list += 1
        current_lexeme = list_of_lexemes[position_in_list]
    #elif current_lexeme == "true" or current_lexeme == "false":
    elif current_lexeme == "boolean":
        current_type = "boolean"
        list_of_types.append(current_type)
##        print("boolean")
        position_in_list += 1
        current_lexeme = list_of_lexemes[position_in_list]
    elif current_lexeme == "real":
        current_type = "real"
        list_of_types.append(current_type)
##        print ("real")
        position_in_list += 1
        current_lexeme = list_of_lexemes[position_in_list]
    else:
        print("Error: Expected 'identifier' but instead recieved: " + current_lexeme)
                                         
    


def Body():
    global current_lexeme
    global position_in_list
    global current_type
    print("<Body> -> { <Statement List> }")
    print("Current lexeme is: " + current_lexeme)
    if (len(current_lexeme) == 0):
        position_in_list +=1
        current_lexeme = list_of_lexemes[position_in_list]
##        print("Found empty position, increasing.")
##        print("Current lexeme is: " + current_lexeme)
    if (current_lexeme != "{"):
        print("Error: Expected '{' but instead recieved: " + current_lexeme)
    if (current_lexeme == "{"):
        position_in_list +=1
        current_lexeme = list_of_lexemes[position_in_list]
        statement_list()
        position_in_list += 1
        current_lexeme = list_of_lexemes[position_in_list]
        current_type = None
        if (current_lexeme != "}"):
            print("Error: Expected '}' but instead recieved: " + current_lexeme)     



def Opt_Declaration_List():
    print("Current lexeme is: " + current_lexeme)
    print ("<Opt Declaration List> -> <Declaration List> | <Empty>")    
    if (current_lexeme == "int" or current_lexeme == "boolean" or current_lexeme == "real"):
        Declaration_List()
    else:
        empty()

def Declaration_List():          
    global current_lexeme
    global position_in_list
    print("Current lexeme is: " + current_lexeme)
    print("<Declaration List> -> <Declaration> ; | <Declaration> ; <Declaration List>")
    Declaration()
    if (current_lexeme != ";"):
        print("Error: Expected ';' but instead recieved: " + current_lexeme)
    else:
        print("Current lexeme is: " + current_lexeme)
        position_in_list+=1
        current_lexeme = list_of_lexemes[position_in_list]

        if (current_lexeme == "int" or current_lexeme == "boolean" or current_lexeme == "real"):
            Declaration_List()
        
##    if list_of_lexemes[position_in_list] == ";":
##        position_in_list +=1
##        current_lexeme = list_of_lexemes[position_in_list]

def Declaration():
    global current_lexeme
    global position_in_list
    print("Current lexeme is: " + current_lexeme)
    print("<Declaration> -> <Qualifier> <IDs>")
    qualifier()
##    position_in_list +=1
##    current_lexeme = list_of_lexemes[position_in_list]
    IDs()

def IDs():
    global current_lexeme
    global position_in_list
    global memory_address
    global current_type
    print("Current lexeme is: " + current_lexeme)
    print("<IDs> -> <Identifier> | <Identifier>, <IDs>")
    if (lexer(current_lexeme) != "identifier"):
        print("Error: Expected 'identifier' but instead recieved: " + current_lexeme)
    if (lexer(current_lexeme) == "identifier"):
        if checkSymbolTable(current_lexeme):
            symbol_table[current_lexeme] = memory_address # by Dan
            memory_address += 1 # by Dan
        position_in_list += 1
        current_lexeme = list_of_lexemes[position_in_list]
        print("\n\n\n")
        print("ID Lexeme is" + current_lexeme)
        print("\n\n\n")
        if current_lexeme == ",":
            position_in_list +=1
            current_lexeme = list_of_lexemes[position_in_list]
            list_of_types.append(current_type) # by Dan
            IDs()
        current_type = None
        
        
            
        


def statement_list():
    global current_lexeme
    global position_in_list    
    print("Current lexeme is:" + current_lexeme)
    print("\n\n\n")
    print("<Statement List> -> <Statement> | <Statement> <Statement List>")
    print("\n\n\n")
    statement()
    if (current_lexeme != "}" and current_lexeme != ";" and current_lexeme != "$$"):       
        statement_list()  
   


def statement():
    global current_lexeme
    global position_in_list
    print("Current lexeme is: " + current_lexeme)
    print("<Statement -> <Compound> | <Assign> | <If> |  <Return> | <Print> | <Scan> | <While>")
    current_lexeme = list_of_lexemes[position_in_list]
    # Separate transitions for each case
    if (len(current_lexeme) == 0):
        position_in_list +=1
        current_lexeme = list_of_lexemes[position_in_list]
##        print ("Found empty lexeme, skipping.")
##        print("Current lexeme is: " + current_lexeme)
    if current_lexeme == "{":
        compound()
    elif (current_lexeme == "}"):
            print("Current lexeme is: " + current_lexeme)
    elif (current_lexeme == "if"):
        If()
    elif(current_lexeme == "return"):
        Return()
    elif(current_lexeme == "put"):
        print("found put")
        Print()
    elif(current_lexeme == "get"):
        Scan()
    elif(current_lexeme == "while"):
        While()
    elif lexer(current_lexeme) == "identifier":
        assign()
    else:        
        print("Error: Expected {, if, return, put, get, or 'identifier' but instead recieved: " + current_lexeme)


def compound():
    global current_lexeme
    global position_in_list
    print("<Compound> -> { <Statement List> }")
    print("Current lexeme is: " + current_lexeme)
    if (current_lexeme != "{"):
        print("Error: Expected '{' but instead recieved: " + current_lexeme)
    if (current_lexeme == "{"):        
        position_in_list +=1
        current_lexeme = list_of_lexemes[position_in_list]        
        statement_list()
        position_in_list +=1
        current_lexeme = list_of_lexemes[position_in_list]
        print(" " + current_lexeme)
  


def assign():
    global current_lexeme
    global position_in_list
    print("Current lexeme is: " + current_lexeme)
    print("<Assign> -> <Identifier> = <Expression> ;")
    if (lexer(current_lexeme) != "identifier"):
        print("Error: Expected 'identifier' but instead recieved: " + current_lexeme)
        
    if lexer(current_lexeme) == "identifier":
        if list_of_lexemes[position_in_list + 1] == "=":
            
            position_in_list += 2
            current_lexeme = list_of_lexemes[position_in_list]
            
            expression()
     
            print("" + list_of_lexemes[position_in_list-3])
            
            print("Current lexeme is for ASSIGN is: " + current_lexeme)
            if current_lexeme != "epsilon":
                print("Error: Expected epsilon but instead recieved: " + current_lexeme)
            else:
                current_lexeme = list_of_lexemes[position_in_list]

            if (list_of_lexemes[position_in_list-3] in ops):
                if(lexer(list_of_lexemes[position_in_list-2]) == "identifier"):
                    assembly.append("PUSHM " + list_of_lexemes[position_in_list-2])
                elif(lexer(list_of_lexemes[position_in_list-2]) == "integer"):
                    assembly.append("PUSHI " + list_of_lexemes[position_in_list-2])
                if(lexer(list_of_lexemes[position_in_list-4]) == "identifier"):
                    assembly.append("PUSHM " + list_of_lexemes[position_in_list-4])
                elif(lexer(list_of_lexemes[position_in_list-4]) == "integer"):
                    assembly.append("PUSHI " + list_of_lexemes[position_in_list-4])
                assembly.append("POPM " + list_of_lexemes[position_in_list-6])
            else:
                if(lexer(list_of_lexemes[position_in_list-2]) == "identifier"):
                    assembly.append("PUSHM " + list_of_lexemes[position_in_list-2])
                elif(lexer(list_of_lexemes[position_in_list-2]) == "integer"):
                    assembly.append("PUSHI " + list_of_lexemes[position_in_list-2])
                if(lexer(list_of_lexemes[position_in_list-4]) == "identifier"):
                    assembly.append("POPM " + list_of_lexemes[position_in_list-4])
            
                

            
    else:
        print("There's in error in assign()")

def If():
    global current_lexeme
    global position_in_list
    print("Current lexeme is: " + current_lexeme)
    print("<If> -> if ( <Condition> ) <Statement> ifend | if (<Condition> ) <Statement> else <Statement> ifend")
    if (current_lexeme != "if"):
        print("Error: Expected 'if' but instead recieved: " + current_lexeme)
    if (current_lexeme == "if"):
        position_in_list +=1
        current_lexeme == list_of_lexemes[position_in_list]
        if (current_lexeme != "("):
            print("Error: Expected '(' but instead recieved: " + current_lexeme)        
        if (current_lexeme == "("):
            position_in_list +=1
            current_lexeme == list_of_lexemes[position_in_list]
            Condition()
            position_in_list +=1
            current_lexeme == list_of_lexemes[position_in_list]
            if (current_lexeme != ")"):
                print("Error: Expected ')' but instead recieved: " + current_lexeme)
            if (current_lexeme == ")"):
                 position_in_list +=1
                 current_lexeme == list_of_lexemes[position_in_list]
                 statement()
                 position_in_list +=1
                 current_lexeme == list_of_lexemes[position_in_list]
                 if (current_lexeme == "else"):
                     statement()
                     position_in_list  +=1
                     current_lexeme = list_of_lexemes[position_in_list]
                     
          
          
          
                     
def Return():
    global current_lexeme
    global position_in_list
    print("Current lexeme is: " + current_lexeme)    
    print("<Return> -> return ; | return <Expression>")
    if (current_lexeme == "return"):       
       print("Current lexeme is: " + current_lexeme)
       if (current_lexeme == ";"):
           print ("return ;")
       else:
           position_in_list +=1
           current_lexeme = list_of_lexemes[position_in_list]
           expression()
    else:
        print("Error, expected return but instead recieved: " + current_lexeme)


##for key, value in sorted(symbol_table.iteritems(), key = lambda (k,v): (v,k)):
##    print("%s\t\t%d\t\t\t\t%s" % (key,value,list_of_types[index_in_type]))
##    index_in_type += 1
def Scan():
    global current_lexeme
    global position_in_list
    print("Current lexeme is: " + current_lexeme)
    print("<Scan> -> get (<IDs>);")    
    if (current_lexeme == "get"): 
        assembly.append("STDIN")
        position_in_list +=1
        current_lexeme = list_of_lexemes[position_in_list]
        print ("found get")
        if (current_lexeme == "("):
            position_in_list +=1
            current_lexeme = list_of_lexemes[position_in_list]
            assembly.append("POPM " + current_lexeme)
            IDs()            
            if (current_lexeme != ")"):
                print("Error, expected ) but instead recieved: " + current_lexeme)
            else:
                position_in_list +=1
                current_lexeme = list_of_lexemes[position_in_list]
                print("Current lexeme is: " + current_lexeme + " expecting ;")
                if (current_lexeme == ";"):
                    position_in_list +=1
                    current_lexeme = list_of_lexemes[position_in_list]
                    print("\n")
                    print("Current lexeme is: " + current_lexeme + ", expecting somethin else")
                    
                

def While():
    global current_lexeme
    global position_in_list
    print("Current lexeme is: " + current_lexeme)
    print("<While> -> while (<Condition>) <Statement> whileend")
    if (current_lexeme == "while"):
        position_in_list +=1
        current_lexeme = list_of_lexemes[position_in_list]
        print("Current lexeme is: " + current_lexeme)
        if(current_lexeme == "("):
            position_in_list+=1
            current_lexeme = list_of_lexemes[position_in_list]
            print("Current lexeme is: " + current_lexeme)
            Condition()

            print("Current lexeme is WOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO: " + current_lexeme)            
            if(current_lexeme == ")"):
                position_in_list +=1
                current_lexeme = list_of_lexemes[position_in_list]
                print("Current lexeme is: " + current_lexeme)
                statement()
                position_in_list+=1
                current_lexeme = list_of_lexemes[position_in_list]
                if current_lexeme != "whileend":
                    print("\n\n\n")
                    print("ERROR: expected whileend but instead recieved: " + current_lexeme)
                else:                    
                    print("Current lexeme is: " + current_lexeme)
                    position_in_list+=1
                

def Print():
    global current_lexeme
    global position_in_list
    print("<Print> -> put (<Expression>)")
    print("Current lexeme is: " + current_lexeme)
    if (current_lexeme == "put"):
        position_in_list +=1
        current_lexeme = list_of_lexemes[position_in_list]
        if(current_lexeme == "("):
            position_in_list +=1
            current_lexeme = list_of_lexemes[position_in_list]
            assembly.append("PUSHM " + current_lexeme)
            expression()
            assembly.append("PUSHM " + list_of_lexemes[position_in_list-1])
##            position_in_list +=1
##            current_lexeme = list_of_lexemes[position_in_list]
            print("Current lexeme is: " + current_lexeme)
            if (current_lexeme == "epsilon"):
                current_lexeme = list_of_lexemes[position_in_list]
            if (current_lexeme == ")"):
                position_in_list +=1
                current_lexeme = list_of_lexemes[position_in_list]
                assembly.append("STDOUT")
            else:
                print("Error, expected ) but instead got: " + current_lexeme)
               

def Condition():
    global current_lexeme
    global position_in_list
    print("Current lexeme is: " + current_lexeme)
    print("<Condition> -> <Expresion> < Relop> < Expression>")
    if (lexer(current_lexeme) == "identifier"):
        assembly.append("PUSHM " + current_lexeme)
    elif(lexer(current_lexeme) == "integer"):
         assembly.append("PUSHI " + current_lexeme)
    expression()
    if (current_lexeme != "epsilon"):
        print("ERROR NOT EPSILON IN CONDITION@@@@@@@@@@@@@@@@")
        
    else:
        current_lexeme = list_of_lexemes[position_in_list]
    Relop()
    expression()
    position_in_list +=1
    current_lexeme = list_of_lexemes[position_in_list]
    if (lexer(list_of_lexemes[position_in_list-2]) == "identifier"):
        assembly.insert(len(assembly)-1,"PUSHM " + list_of_lexemes[position_in_list-2])
    elif(lexer(list_of_lexemes[position_in_list-2]) == "integer"):
         assembly.insert(len(assembly)-1,"PUSHI " + list_of_lexemes[position_in_list-2])
    print(assembly)

def Relop():
    global position_in_list
    global current_lexeme
    print("Current lexeme is: " + current_lexeme)
    print("<Relop> -> ")
    if (current_lexeme == "==" or current_lexeme == "^=" or current_lexeme == ">" or current_lexeme == "<" or current_lexeme == "=>" or current_lexeme == "=<"):
        if (current_lexeme == "<"):
            assembly.append("LES")
        elif(current_lexeme == ">"):
            assembly.append("GRT")
        elif(current_lexeme == "=="):
            assembly.append("EQU")
        elif(current_lexeme == "^="):
            assembly.append("NEQ")
        elif(current_lexeme == ">="):
            assembly.append("GEQ")
        elif(current_lexeme == "<="):
            assembly.append("LEQ")
        print (current_lexeme)
        
        
        position_in_list+=1
        current_lexeme = list_of_lexemes[position_in_list]
    
    
          

def expression():
    print("Current lexeme is: " + current_lexeme)
    print("<Expression> -> <Term> <Expression Prime>")
    term()
    expression_prime()


def expression_prime():
    global current_lexeme
##for key, value in sorted(symbol_table.iteritems(), key = lambda (k,v): (v,k)):
##    print("%s\t\t%d\t\t\t\t%s" % (key,value,list_of_types[index_in_type]))
##    index_in_type += 1
    global position_in_list
    print("Current lexeme is: " + current_lexeme)
    print("<Expression Prime> -> + <Term> <Expression Prime> | - <Term> <Expression Prime> | epsilon")    
    if current_lexeme == "+" or current_lexeme == "-":
        if (current_lexeme == "+"):
            assembly.append("ADD")
        elif(current_lexeme == "-"):
            assembly.append("SUB")
        position_in_list += 1
        current_lexeme = list_of_lexemes[position_in_list]
        term()
        expression_prime()
    elif current_lexeme == "epsilon":
        empty()
    else:
        print("Error, expected +, - or epsilon but instead recieved: " + current_lexeme)


def term():
    global current_lexeme
    global position_in_list
    print("Current lexeme is: " + current_lexeme)
    print("<Term> -> <Factor> <Term Prime>")
##    position_in_list +=1
##    current_lexeme = list_of_lexemes[position_in_list]
    factor()
    term_prime()

##for key, value in sorted(symbol_table.iteritems(), key = lambda (k,v): (v,k)):
##    print("%s\t\t%d\t\t\t\t%s" % (key,value,list_of_types[index_in_type]))
##    index_in_type += 1

def term_prime():
    global current_lexeme
    global position_in_list
    print("Current lexeme is: " + current_lexeme)
    print("<Term Prime> -> * <Factor> <Term Prime> | / <Factor> <Term Prime> | epsilon")

    if current_lexeme == "*" or current_lexeme == "/":       
        if current_lexeme == "*":
            assembly.append("MUL")
        elif current_lexeme == "/":
            assembly.append("DIV")
        position_in_list += 1
        current_lexeme = list_of_lexemes[position_in_list]
        print("Current lexeme is: " + current_lexeme)
        factor()
        term_prime()
    elif current_lexeme == "epsilon":
        empty()
    else:
        print("Error, expected '*' or '/' but instead recieved: " + current_lexeme)


def factor():
    global current_lexeme
    global position_in_list
    print("Current lexeme is: " + current_lexeme)
    print("<Factor> -> - <Primary> | <Primary>")

    if current_lexeme == "-":
        position_in_list += 1
        current_lexeme = list_of_lexemes[position_in_list]
        primary()
    else:
        primary()


def primary():
    global current_lexeme
    global position_in_list
    print("Current lexeme is: " + current_lexeme)
    print("<Primary> -> <Identifier> | <Integer> | <Identifier> ( <IDs> ) | ( <Expression> ) | <Real> | true | false")

    if lexer(current_lexeme) == "identifier":
        print("\n")
        print(assembly)
        print("\n")
        if list_of_lexemes[position_in_list + 1] == "(":
            position_in_list += 1
            current_lexeme = list_of_lexemes[position_in_list]
            IDs()
            
            if list_of_lexemes[position_in_list + 1]  != ")":
                print("Error, expected ')'")
        else:
            
            position_in_list += 1
            current_lexeme = list_of_lexemes[position_in_list]
            print("Found Identifier in primary, next thingy is: " + current_lexeme)
            if (current_lexeme == "*" or  current_lexeme == "+" or current_lexeme == "-" or current_lexeme == "/"):
                print("ITS BOUT THAT TIME")
                current_lexeme = list_of_lexemes[position_in_list]                                                                                                            
            elif (current_lexeme == ";"):
                position_in_list+=1
                #current_lexeme = list_of_lexemes[position_in_list]
                print("Found ; finished statement.")
                current_lexeme = "epsilon"
            else:
                current_lexeme = "epsilon"
            
    elif lexer(current_lexeme) == "integer":
        position_in_list += 1
        current_lexeme = list_of_lexemes[position_in_list]
        if (list_of_lexemes[position_in_list] == "*" or list_of_lexemes[position_in_list] == "+" or list_of_lexemes[position_in_list] == "-" or list_of_lexemes[position_in_list] == "/"):
                current_lexeme = list_of_lexemes[position_in_list]
        if (current_lexeme == ";"):
            position_in_list+=1
            #current_lexeme = list_of_lexemes[position_in_list]
            print("Found ; finished statement.")
            current_lexeme = "epsilon"
        
    elif current_lexeme == "(":
        position_in_list +=1
        current_lexeme = list_of_lexemes[position_in_list]
        expression()
        position_in_list +=1
        current_lexeme = list_of_lexemes[position_in_list]
        if list_of_lexemes[position_in_list + 1] != ")":
            print("Missing ')'")
        else:
            position_in_list += 1
            current_lexeme = list_of_lexemes[position_in_list]
            
    elif current_lexeme == "real":
        position_in_list += 1
        current_lexeme = list_of_lexemes[position_in_list]
        
    elif current_lexeme == "false":
        position_in_list += 1
        current_lexeme = list_of_lexemes[position_in_list]
##    elif current_lexeme == "*" or current_lexeme == "/":
##        term_prime()
    else:
        print("Error in primary function")

def empty():
    print("<Empty> -> epsilon")

# by Dan
def checkSymbolTable(identifier):
    for key in symbol_table:
        print("\n\nThis is the key: " + key + " and this is the identifier " + identifier + "\n\n")
        if key == identifier:
            print(identifier + " has already been declared.")
            return False
    return True


file = input("Please enter the name of a file to read.")
position_in_list = 0
memory_address = 5000 # by Dan
current_type = None # by dan
lexer2(file)
print(list_of_lexemes)
rat18f()
for i in range(len(assembly)):
    print(str(i+1) + " " + assembly[i])
print("\n\n\n")
print(list_of_types)
print("\t\t\tSymbol Table\t\t\t")
print("Identifier\tMemory Location\tType")
index_in_type = 0

for key, value in sorted(symbol_table.iteritems(), key = lambda (k,v): (v,k)):
    print("%s\t\t%d\t\t\t\t%s" % (key,value,list_of_types[index_in_type]))
    index_in_type += 1

q = input("Press any key to exit")
