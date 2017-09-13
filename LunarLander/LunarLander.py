""" Name: Tse-Lun Hsu, Student ID: 61737979"""


def main():
    
    a = 50.0 #altitiude
    v = 0.0 #velocity
    f = 1000.0 #fuel left
    b = 0.0 # fuel to burn
    
    def lunar_lander(a, v, f, b):
        
        while a > 0:

            print ("Altitude above the moon is", a)

            print ("Velocity is", v)

            print ("Fuel you remain is", f)

            b = input("How much fuel you would like to burn? ")

            if f >= b > 0 :

                f = f - b

            elif b > f >= 0:

                b = f

                f = b - f

            else :

                b = 0

            v = v + 1.6 - 0.15 * b 

            a = a - v 
                
        if v < 10:

            a = 0 
            
            print ("Your altitude is 0 now, You have landed, Congrats!")
            
        else:

            print ("You just blasted a", -a, "-meters deep crater...")      
            
    
    def play_again():
        
        play_again = raw_input("Do you want to play again? Please enter \"yes\" or \"no\"\n") 
        
        while play_again[:1].lower() != "n" and play_again[:1].lower() != "y":

            play_again = raw_input("Sorry, I don't understand, could you enter again? Please enter \"yes\" or \"no\"\n")   
                                  
        
        if play_again[:1].lower() == "y":
  
            return True
        
        else:
            print ("Bye")
            return False
    
    while True:   
 
        lunar_lander(a, v, f, b)
        if not play_again():
            break
    
if __name__ == "__main__":
    main()
