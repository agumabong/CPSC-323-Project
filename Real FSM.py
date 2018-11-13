#Aaron Gumabong
#Dan Ortiz
#CPSC 323
#Professor Choi


# Variables to keep track of top-down parser
current_lexeme = None
global list_of_lexemes
global position_in_list

list_of_lexemes = []

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
keywords = ["if", "while", "for", "whileend", "else", "ifend", "whileend", "get", "put", "and", "true", "false", "int"]
operators = ["+","-","*","/","%", "=", "<",">", "|", ":"]
sep = ["(", ")", "[", "]", "{","}", "$$" , ";", ","]

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
            if len(pword) == 0 or pword == "" or pword == '':
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
            if (pword[0] in sep):
                print(pword[0] + "\t \t \t" + "Seperator")
                list_of_lexemes.append(pword[0])
                pword = pword[1:]
                if (len(pword) ==1 ):
                    continue
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
                pend = pword[len(pword)-1]
                pword = pword[:-1]
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
        print("keyword")
        return "keyword"
    elif (token in operators):
        print("operator")
        return "operator"
    elif (token in sep):
        print("separator")
        return "separator"
    elif (real(token) == True):
        print("real")
        return "real"
    elif (iden(token) == True):
        print("identifier")
        return "identifier"
    elif (integer(token) == True):
        print("integer")
        return "integer"








    

def rat18f():
    # Maybe print out the file?
    global current_lexeme
    global position_in_list
    print("<Rat18F> -> <Opt Function Definitions> $$ <Opt Declaration List> <Statement List> $$")
    current_lexeme = list_of_lexemes[position_in_list]
    Opt_Function_Definitions()
    position_in_list +=1
    current_lexeme = list_of_lexemes[position_in_list]
    print("Current lexeme is: " + current_lexeme)
    if (len(current_lexeme) == 0):
        position_in_list+=1
        current_lexeme = list_of_lexemes[position_in_list]
        print("Found blank space, removing.")
        print("Current Lexeme is: " + current_lexeme)
    print ("Moving to first $$")
    if (current_lexeme == "$$"):
        position_in_list +=1
        current_lexeme = list_of_lexemes[position_in_list]
        print("Current lexeme is: " + current_lexeme)
        print ("doing opt dec list")
        Opt_Declaration_List()
        
        print("Current lexeme is: " + current_lexeme)
        print("Doing statement list")
        
        while(position_in_list < len(list_of_lexemes)-1):
            statement_list()
            position_in_list +=1
            current_lexeme = list_of_lexemes[position_in_list]
        if (current_lexeme != "$$"):
            print("Error, expected: '$$' but recieved" + current_lexeme)
        if (current_lexeme == "$$"):
            print("reached end of file.")

        

def Opt_Function_Definitions():
    global current_lexeme
    global position_in_list
    print("Current lexeme is: " + current_lexeme)
    print("<Opt Function Definitions> -> <Function Definitions> | <Empty>")
    if (current_lexeme == "" or current_lexeme == ''):
        empty()
    else:
        Function_Definitions()

   

def Function_Definitions():
    global current_lexeme
    global position_in_list
    print("Current lexeme is: " + current_lexeme)
    print ("<Function Definitions> -> <Functions | <Functions> < Function Definitions>")
    Function()

def Function():
    global current_lexeme
    global position_in_list
    print ("<Function> -> function <Identifier> ( <Opt Parameter List> ) <Opt Declaration List> <Body>")
    if (current_lexeme == "function"):
        position_in_list += 1
        current_lexeme = list_of_lexemes[position_in_list]
        print ("Found function")
        print("Current lexeme is: " + current_lexeme)
        if (lexer(current_lexeme) == "identifier"):
            position_in_list+=1
            current_lexeme = list_of_lexemes[position_in_list]
            print("Finished with function and identifier, moving to Opt parameter list")
            print("Current lexeme is: " + current_lexeme)
            if (current_lexeme == "(" or current_lexeme[0] == "("):
                position_in_list +=1
                current_lexeme = list_of_lexemes[position_in_list]
                Opt_Parameter_List()
                print ("Finished Opt Parameter List")
                print("Current lexeme is: " + current_lexeme)
                if (current_lexeme == ")"):
                    position_in_list +=1
                    current_lexeme = list_of_lexemes[position_in_list]
                    print("Current lexeme is: " + current_lexeme)
                    Opt_Declaration_List()
                    print ("Finished with Opt Declaration List")
                    print("Current lexeme is: " + current_lexeme)
                    Body()
                    print("Finished with Body")
                    print("Current lexeme is: " + current_lexeme)
##                else:
##                    print("Expected ')', but instead recieved" + current_lexeme)
        
        

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
    IDs()
    if (current_lexeme == ":"):
        position_in_list +=1
        current_lexeme = list_of_lexemes[position_in_list]
        print("Finished with IDs, going to qualifier")
        print ("Current lexeme is: " + current_lexeme)
        qualifier()
    else:
        print("Expected ':' but instead recieved" + current_lexeme)


def qualifier():
    global current_lexeme
    global position_in_list
    print("Current lexeme is: " + current_lexeme)
    print("<Qualifier -> int | boolean | real")
    if current_lexeme == "int":
        print("int")
        position_in_list += 1
        current_lexeme = list_of_lexemes[position_in_list]
    elif current_lexeme == "true" or current_lexeme == "false":
        print("boolean")
        position_in_list += 1
        current_lexeme = list_of_lexemes[position_in_list]
    elif (lexer(current_lexeme) == "real"):
        print ("real")
        position_in_list += 1
        current_lexeme = list_of_lexemes[position_in_list]
    


def Body():
    global current_lexeme
    global position_in_list
    print("<Body> -> { <Statement List> }")
    print("Current lexeme is: " + current_lexeme)
    if (len(current_lexeme) == 0):
        position_in_list +=1
        current_lexeme = list_of_lexemes[position_in_list]
        print("Found empty position, increasing.")
        print("Current lexeme is: " + current_lexeme)
    if (current_lexeme == "{"):
        position_in_list +=1
        current_lexeme = list_of_lexemes[position_in_list]
        statement_list()
        position_in_list += 1
        current_lexeme = list_of_lexemes[position_in_list]
        
##        if (current_lexeme != "}"  or current_lexeme[len(current_lexeme)] != "}"):
##            print ("Expected '}' but instead recieved " + current_lexeme)     



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
    if list_of_lexemes[position_in_list] == ";":
        position_in_list +=1
        current_lexeme = list_of_lexemes[position_in_list]
        Declaration_List()

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
    print("Current lexeme is: " + current_lexeme)
    print("<IDs> -> <Identifier> | <Identifier>, <IDs>")
    if (lexer(current_lexeme) == "identifier"):
        position_in_list += 1
        current_lexeme = list_of_lexemes[position_in_list]
        if current_lexeme == ",":
            position_in_list +=1
            current_lexeme = list_of_lexemes[position_in_list]
            IDs()
        
            
        


def statement_list():
    print("Current lexeme is: " + current_lexeme)
    print("<Statement List> -> <Statement> | <Statement> <Statement List")
    statement()


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
        print ("Found empty lexeme, skipping.")
        print("Current lexeme is: " + current_lexeme)
    if current_lexeme == "{":
        compound()
    
    if (current_lexeme == "if"):
        If()
    if(current_lexeme == "return"):
        Return()
    if(current_lexeme == "put"):
        Print()
    if(current_lexeme == "get"):
        Scan()
    if(current_lexeme == "while"):
        While()
    if lexer(current_lexeme) == "identifier":
        assign()
        
        print("Error in statement() function")


def compound():
    global current_lexeme
    global position_in_list
    print("<Compound> -> { <Statement List> }")
    print("Current lexeme is: " + current_lexeme)
    if (current_lexeme == "{"):
        position_in_list +=1
        current_lexeme = list_of_lexemes[position_in_list]        
        statement_list()
        position_in_list +=1
        current_lexeme = list_of_lexemes[position_in_list]
  


def assign():
    global current_lexeme
    global position_in_list
    print("Current lexeme is: " + current_lexeme)
    print("<Assign> -> <Identifier> = <Expression> ;")

    if lexer(current_lexeme) == "identifier":
        if list_of_lexemes[position_in_list + 1] == "=":
            position_in_list += 2
            current_lexeme = list_of_lexemes[position_in_list]
            expression()
            position_in_list +=1
            current_lexeme = list_of_lexemes[position_in_list]
            if current_lexeme != ";":
                print("Missing ;")
    else:
        print("There's in error in assign()")

def If():
    global current_lexeme
    global position_in_list
    print("Current lexeme is: " + current_lexeme)
    print("<If> -> if ( <Condition> ) <Statement> ifend | if (<Condition> ) <Statement> else <Statement> ifend")
    if (current_lexeme == "if"):
        position_in_list +=1
        current_lexeme == list_of_lexemes[position_in_list]
        if (current_lexeme == "("):
            position_in_list +=1
            current_lexeme == list_of_lexemes[position_in_list]
            Condition()
            position_in_list +=1
            current_lexeme == list_of_lexemes[position_in_list]
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
       position_in_list +=1
       current_lexeme = list_of_lexemes[position_in_list]
       if (current_lexeme == ";"):
           print ("return ;")
       else:
           position_in_list +=1
           current_lexeme = list_of_lexemes[position_in_list]
           expression()

def Print():
    global current_lexeme
    global position_in_list
    print("Current lexeme is: " + current_lexeme)
    print("<Print> -> put <Expression>);")
    if (current_lexeme == "put"):
        expression()

def Scan():
    global current_lexeme
    global position_in_list
    print("Current lexeme is: " + current_lexeme)
    print("<Scan> -> get (<IDs>);")    
    if (current_lexeme == "get"):
        position_in_list +=1
        current_lexeme = list_of_lexemes[position_in_list]
        print ("found get")
        if (current_lexeme == "("):
            IDs()
            position_in_list +=1
            current_lexeme = list_of_lexemes[position_in_list]

def While():
    global current_lexeme
    global position_in_list
    print("Current lexeme is: " + current_lexeme)
    print("<While> -> while (<Condition>) <Statement> whileend")
    if (current_lexeme == "while"):
        position_in_list +=1
        current_lexeme = list_of_lexemes[position_in_list]
        if(current_lexeme == "("):
            position_in_list+=1
            current_lexeme = list_of_lexemes[position_in_list]
            Condition()
            position_in_list +=1
            current_lexeme = list_of_lexemes[position_in_list]
            if(current_lexeme == ")"):
                position_in_list +=1
                current_lexeme = list_of_lexemes[position_in_list]
                statement()
                position_in_list+=1
                current_lexeme = list_of_lexemes[position_in_list]
                

def Print():
    global current_lexeme
    global position_in_list
    print("<While> -> while ( <Condition> ) <Statement> whileend")
    print("Current lexeme is: " + current_lexeme)
    if (current_lexeme == "while"):
        position_in_list +=1
        current_lexeme = list_of_lexemes[position_in_list]
        if(current_lexeme == "("):
            position_in_list +=1
            current_lexeme = list_of_lexemes[position_in_list]
            Condition()
            position_in_list +=1
            current_lexeme = list_of_lexemes[position_in_list]
            if (current_lexeme == ")"):
                position_in_list +=1
                current_lexeme = list_of_lexemes[position_in_list]
                statement()

def Condition():
    global current_lexeme
    print("Current lexeme is: " + current_lexeme)
    print("<Condition> -> <Expresion> < Relop> < Expression>")
    
    expression()
    Relop()
    expression()

def Relop():
    global current_lexeme
    print("Current lexeme is: " + current_lexeme)
    print("<Relop> -> ")
    if (current_lexeme == ">" or current_lexeme == "<"):
        print (current_lexeme)
    
    
          

def expression():
    print("Current lexeme is: " + current_lexeme)
    print("<Expression> -> <Term> <Expression Prime>")
    term()
    expression_prime()


def expression_prime():
    global current_lexeme
    global position_in_list
    print("Current lexeme is: " + current_lexeme)
    print("<Expression Prime> -> + <Term> <Expression> | - <Term> <Expression> | epsilon")
    
    if current_lexeme == "+" or current_lexeme == "-":
        position_in_list += 1
        current_lexeme = list_of_lexemes[position_in_list]
        term()
        expression()
    else:
        empty()


def term():
    global current_lexeme
    global position_in_list
    print("Current lexeme is: " + current_lexeme)
    print("<Term> -> <Factor> <Term Prime>")
##    position_in_list +=1
##    current_lexeme = list_of_lexemes[position_in_list]
    factor()
    term_prime()


def term_prime():
    global current_lexeme
    global position_in_list
    print("Current lexeme is: " + current_lexeme)
    print("<Term Prime> -> * <Factor> <Term> | / <Factor> <Term> | epsilon")

    if current_lexeme == "*" or current_lexeme == "/":
        position_in_list += 1
        current_lexeme = list_of_lexemes[position_in_list]
        factor()
        term()
    else:
        print("epsilon")


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
        if list_of_lexemes[position_in_list + 1] == "(":
            position_in_list += 1
            current_lexeme = list_of_lexemes[position_in_list]
            IDs()
            if list_of_lexemes[position_in_list + 1]  != ")":
                print("Missing ')'")
        else:
            position_in_list += 1
            current_lexeme = list_of_lexemes[position_in_list]
            
    elif lexer(current_lexeme) == "integer":
        position_in_list += 1
        current_lexeme = list_of_lexemes[position_in_list]
        
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
    elif current_lexeme == "*" or current_lexeme == "/":
        term_prime()
    else:
        print("Error in primary function")

def empty():
    print("<Empty> -> epsilon")    

file = "test2.txt"
position_in_list = 0
lexer2(file)
rat18f()

