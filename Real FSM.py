
#Converts the character input to the column number for the Real FSM
def ch_to_col(c):
    if (c == "."):
        return 1
    elif (c.isdigit()):
        return 0


#2D Array of the Real Finite State Machine.
realarray = [[2,5], [2, 3] , [4,5], [4,5], [5,5]]
#Function that takes in a word and checks if the word is if the statement is a "real" or not.
#Returns True if the statement is a real, false if it is not.
def real(word):
    state = 1
    col = 0
    for i in range(0,len(word)):
        if (word[i].isdigit() or word[i] == "."):  
            print ("Char is: " + str(word[i]) + " and state is: " + str(state))
            state = realarray[state-1][ch_to_col(word[i])]
        else:
            return False
        

    if (state == 4):
        return True    
    else:
        return False
    
print(real("123."))
