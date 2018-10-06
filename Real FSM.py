#2D Array of the Real Finite State Machine.
realarray = [[2,5], [2, 3] , [4,5], [4,5], [5,5]]
#Function that takes in a word and checks if the word is if the statement is a "real" or not.
#Returns True if the statement is a real, false if it is not.
def real(word):
    state = 1
    for i in range(0,len(word)):
        print ("Char is: " + str(word[i]) + " and state is: " + str(state))
        if (state == 5):
            return False
        #State 1 statements
        elif (state == 1 and word[i].isdigit()):
            state = realarray[state-1][0]
        elif (state == 1 and word[i] == "."):
            state = realarray[state-1][1]
        #State 2 Statements
        elif (state == 2 and word[i].isdigit()):
            state = realarray[state-1][0]
        elif (state == 2 and word[i] == "."):
            state = realarray[state-1][1]
        #State 3 Statements
        elif (state == 3 and word[i].isdigit()):
            state = realarray[state-1][0]
        elif(state == 3 and word[i] == "."):
            state = realarray[state-1][1]
        #State 4 Statements
        elif (state == 4 and word[i].isdigit()):
            state = realarray[state-1][0]
        elif(state ==4 and word[i] == "."):
            state = realarray[state-1][1]
        else:
            state = 5
    if (state == 4):
        return True    
    else:
        return False
    
print(real("123.w4"))
        
        
    
