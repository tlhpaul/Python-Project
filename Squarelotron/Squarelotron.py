import copy

def make_squarelotron(numbers):   
    """Given a "flat" list of 25 numbers, make and return a squarelotron. You probably want to represent the
    squarelotron as a list of lists, but that's up to you: Represent it however you like. It could even be
    just the list given as an argument. The first 5 numbers are the top row of the squarelotron, the next 5
    numbers are the second row, etc. Calling this function should not result in any input/output."""

    squarelotron = []
    for i in range(5, len(numbers)+1, 5):
        squarelotron.append(list(numbers[i-5:i]))
        
    return squarelotron

def make_list(squarelotron):   
    """This function is the inverse of make_squarelotron. It returns a list of 25 numbers.
    (Note: Since I have not specified how to represent your squarelotron,
    I will depend heavily on the make_squarelotron and make_list functions to check all the rest of your functions;
    so get them right!) Calling this function should not result in any input/output."""
    squarelotron_list = []
    for i in range(1, len(squarelotron)+1):
        for j in range(1, 6):
            squarelotron_list.append(squarelotron[-i][-j])

    return squarelotron_list


def upside_down_flip(squarelotron, ring):  
    """This function performs the Upside-Down Flip of the squarelotron, as described above,
    and returns the new squarelotron. The original squarelotron should not be modified (I will check for this).
    Calling this function should not result in any input/output."""
    new_squarelotron = copy.deepcopy(squarelotron)
    if ring == "outer":
        new_squarelotron[0], new_squarelotron[4] = new_squarelotron[4], new_squarelotron[0]
        new_squarelotron[1][0], new_squarelotron[3][0] = new_squarelotron[3][0], new_squarelotron[1][0]
        new_squarelotron[1][4], new_squarelotron[3][4] = new_squarelotron[3][4], new_squarelotron[1][4]

    elif ring == "inner":
        for i in range (1, 4):
            new_squarelotron[1][i], new_squarelotron[3][i] = new_squarelotron[3][i], new_squarelotron[1][i]
        
    return new_squarelotron

def left_right_flip(squarelotron, ring):   
    """This function performs the Left-Right Flip of the squarelotron, as described above, and returns the
    new squarelotron. The original squarelotron should not be modified (I will check for this).
    Calling this function should not result in any input/output."""
    new_squarelotron = copy.deepcopy(squarelotron)
    if ring == "outer":
        for i in range(0, 5):
            new_squarelotron[i][0], new_squarelotron[i][4] = new_squarelotron[i][4], new_squarelotron[i][0]
        new_squarelotron[0][1], new_squarelotron[0][3] = new_squarelotron[0][3], new_squarelotron[0][1]
        new_squarelotron[4][1], new_squarelotron[4][3] = new_squarelotron[4][3], new_squarelotron[4][1]
        
    elif ring == "inner":
        for i in range(1, 4):
            new_squarelotron[i][1], new_squarelotron[i][3] = new_squarelotron[i][3], new_squarelotron[i][1]
    
    return new_squarelotron

def inverse_diagonal_flip(squarelotron, ring): 
    """This function performs the Main Inverse Diagonal of the squarelotron, as described above,
    and returns the new squarelotron. The original squarelotron should not be modified (I will check for this).
    Calling this function should not result in any input/output."""
    new_squarelotron = copy.deepcopy(squarelotron)
    if ring == "outer":
        new_squarelotron[0][3], new_squarelotron[1][4] = new_squarelotron[1][4], new_squarelotron[0][3]
        new_squarelotron[0][2], new_squarelotron[2][4] = new_squarelotron[2][4], new_squarelotron[0][2]
        new_squarelotron[0][1], new_squarelotron[3][4] = new_squarelotron[3][4], new_squarelotron[0][1]
        new_squarelotron[0][0], new_squarelotron[4][4] = new_squarelotron[4][4], new_squarelotron[0][0]
        new_squarelotron[1][0], new_squarelotron[4][3] = new_squarelotron[4][3], new_squarelotron[1][0]
        new_squarelotron[2][0], new_squarelotron[4][2] = new_squarelotron[4][2], new_squarelotron[2][0]
        new_squarelotron[3][0], new_squarelotron[4][1] = new_squarelotron[4][1], new_squarelotron[3][0]        
  
    elif ring == "inner":
        new_squarelotron[1][2], new_squarelotron[2][3] = new_squarelotron[2][3], new_squarelotron[1][2]
        new_squarelotron[1][1], new_squarelotron[3][3] = new_squarelotron[3][3], new_squarelotron[1][1]
        new_squarelotron[2][1], new_squarelotron[3][2] = new_squarelotron[3][2], new_squarelotron[2][1]
       
    return new_squarelotron
 
def main_diagonal_flip(squarelotron, ring):
    """This function performs the Main Diagonal Flip of the squarelotron, as described above, and returns
    the new squarelotron. The original squarelotron should not be modified (I will check for this).
    Calling this function should not result in any input/output."""
    new_squarelotron = copy.deepcopy(squarelotron)
    if ring == "outer":
        for i in range(1, 5):
            new_squarelotron[i][0], new_squarelotron[0][i] = new_squarelotron[0][i], new_squarelotron[i][0]
        for j in range(1, 4):
            new_squarelotron[j][4], new_squarelotron[4][j] = new_squarelotron[4][j], new_squarelotron[j][4]
            
    elif ring == "inner":
        for i in range(2, 4):
            new_squarelotron[1][i], new_squarelotron[i][1] = new_squarelotron[i][1], new_squarelotron[1][i]
        new_squarelotron[2][3], new_squarelotron[3][2] = new_squarelotron[3][2], new_squarelotron[2][3]
        
    return new_squarelotron

def rotate_squarelotron(squarelotron, ring, flip):
    """Flip the matrix of number based on flip and ring"""
    if flip == "ud":
        print (*upside_down_flip(squarelotron, ring), sep="\n")
        return upside_down_flip(squarelotron, ring)
        
    elif flip == "lr":
        print (*left_right_flip(squarelotron, ring), sep="\n")
        return left_right_flip(squarelotron, ring)
        
    elif flip == "id":
        print (*inverse_diagonal_flip(squarelotron, ring), sep="\n")
        return inverse_diagonal_flip(squarelotron, ring)
        
    else:
        print (*main_diagonal_flip(squarelotron, ring), sep="\n")
        return main_diagonal_flip(squarelotron, ring)

def keep_rotating():
    """Ask users they want to keep fliping or not"""
    keep_rotating = input("Do you want to flip again (Enter \"Yes\")? or quit(Enter \"No\")? or start over with a new squarelotron?(Enter \"New\")\n")        
    while keep_rotating.lower() != "no" and keep_rotating.lower() != "yes" and keep_rotating.lower() != "new":
        keep_rotating = input("Sorry, I don't understand, could you enter again? Please enter \"yes\", \"no\" or \"new\"\n")
            
    if keep_rotating.lower() == "yes": 
        return True

    elif keep_rotating.lower() == "new":
        return "new"
        
    else:
        print ("Bye!")
        return False

def choose_ring():
    """Choose outer or inner ring to rotate"""
    ring = input("Please choose \"inner\" or \" outer\" ring to flip\n")
    while ring.lower() != "inner" and ring.lower() != "outer":
        ring = input("Sorry you enter wrong answer, please choose \"inner\" or \" outer\" ring\n")
        
    return ring 

def choose_flip():
    """Choose which flip users would like to rotate"""
    flip = input("Please choose how would you like to rotate\n Enter \"UD\" to flip Upside-Down,\n Enter \"LR\" to flip Left-Right,\n Enter \"ID\" to flip Inverse Diagonal,\n Enter \"MD\" to flip \"Main Diagonal\"\n")
    while flip.lower() != "ud" and flip.lower() != "lr" and flip.lower() != "id" and flip.lower() != "md":
        flip = input("Sorry, you enter wrong answer, please choose how would you like to rotate?\n Entering \"UD\" means Upside-Down,\n Entering \"LR\" means Left-Right,\n Entering \"ID\" means Inverse Diagonal,\n Entering \"MD\" means \"Main Diagonal\"\n")
        
    return flip

def print_instruction():
    """Print the instrcution that how to play this game"""
    print ("A Squarelotron consist basically of a matrix of numbers from 1 to 25.\n This matrix can be decomposed as inner and outer ring which can rotate independently in 4 different ways:\n Upside-Down (↕), Left-Right (↔), Inverse Diagonal (↙) and Main Diagonal (↘)")
 
def  main():
    
    print_instruction()  
    squarelotron = make_squarelotron((range(1, 26)))
    print (*squarelotron, sep = "\n")
    while True:
        ring = choose_ring()
        flip = choose_flip()
        squarelotron = rotate_squarelotron(squarelotron, ring, flip)
        play_again_or_not = keep_rotating()
        if play_again_or_not == "new":
            squarelotron = make_squarelotron((range(1, 26)))
            print (*squarelotron, sep = "\n")
        elif not play_again_or_not:
            break
        
if __name__ == "__main__":
    main()
