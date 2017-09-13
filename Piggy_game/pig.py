""" Name: Tse-Lun Hsu, Student ID: 61737979"""

import random 

def ask_yes_or_no():
            # ask user to roll again or not
            answer = raw_input("Roll again? Please enter \"yes\" or \"no\"\n")
            while answer[:1].lower() != "y" and answer[:1].lower() != "n":
                        answer = raw_input("I am sorry, I don't understand, could you enter again? Please enter \"yes\" or \"no\"\n")
            if answer[:1].lower() == "y": 
                        return True          
            else:
                        return False
             
        
def instructions(): 
            #Tell the use the rules of game
            print ("You are palying \"PIG!\", This game is a game between you and the computer.\n Each turn, you and computer will roll a six-sided die, as many as you wish or until\n you roll a \"1\". Each number you roll will be added to the bank as your score,\n but if you roll a \"1\", that means this turn is over and the score for this turn is \"0\".\n The first one to reach or exceed 100 wins! Computer will go first! ")
            raw_input("Press Enter to continue...")    
            
            
def show_results(computer_score, human_score):
            #tells who won or lost, and by how much
            print "Your score is", human_score
            print "Computer's score is", computer_score                   
            if human_score > computer_score:
                        print "Yon won by ", human_score - computer_score, ", congrats!"
            else :       
                        print "I am sorry, you lost by ", computer_score - human_score
                                      
                        
def roll():
            #roll a number from 1 to 6
            return random.randint(1, 6)
             

def human_move(computer_score, human_score): 
            #Tell user his or her current score and computer's score, and ahead or behind by how much, and roll the dice
            print "Your score is ", human_score
            print "Computer's score is ", computer_score
            if human_score > computer_score:
                        print "You are ahead by ", human_score - computer_score                    
            elif computer_score > human_score:
                        print "You are behind by ", computer_score - human_score
            else:
                        print "You are tied with computer"            
            sub_human_score = 0
            number_player_get = 0            

            while True :                 
                        number_player_get = roll()                                
                        if number_player_get != 1 :               
                                    sub_human_score += number_player_get
                                    print "The number you get is", number_player_get                                    
                                    print "Your score for this turn is", sub_human_score, "now"
                                    if not ask_yes_or_no():                                    
                                                return sub_human_score
                        else: 
                                    print "The number you get is", number_player_get                              
                                    print "Unfortunately, you got 0 for this turn"                               
                                    raw_input("Press Enter to continue...")                  
                                    return 0
                                    
                                    
def computer_move(computer_score, human_score):
            #Computer rolls few times, and display the number for computer's turn, my strategy is computer will try to roll as many as possible to 
            #get higher score if computer is losing
            sub_computer_score = 0 
            number_computer_get = 0
            all_the_number_computer_get = []    

            while True :                    
                        number_computer_get = roll()
                        all_the_number_computer_get.append(number_computer_get)
                        sub_computer_score += number_computer_get                               
                        computer_score += sub_computer_score
                        if number_computer_get == 1 :
                                    print "Computer got \"1\" "
                                    print "Computer's individual score for this turn is", all_the_number_computer_get,",\nand total for this turn is 0"
                                    raw_input("Press Enter to continue...")
                                    return 0                        
                        if computer_score - human_score > 0 :                         
                                    print "Computer's individual score for this turn is", all_the_number_computer_get,",\nand total for this turn is",sub_computer_score
                                    raw_input("Press Enter to continue...")
                                    return sub_computer_score
                                             
def is_game_over(computer_score, human_score):
            #the condition when the game is over
            if (computer_score >= 100 or human_score >= 100) and computer_score != human_score:
                        return True
            else:
                        return False



def main():  
            #start execeution
    
            from piggy import *
         
            instructions()
            human_score =  0 
            computer_score = 0
            
            
            
            while not is_game_over(computer_score, human_score): 
               
                        computer_score += computer_move(computer_score, human_score)
                        
                  
                        human_score += human_move(computer_score, human_score)
                
        
                
                
            show_results(computer_score, human_score)



if __name__ == "__main__" :
            main()
    
    
    
    
