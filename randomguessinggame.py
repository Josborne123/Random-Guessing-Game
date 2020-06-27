import random
import time
tries = 0

num = random.randint(1, 101)
while True: #tries < 5:
    print ('Guess a number between 1 and 100')
    guess = input()
    i = int(guess)
    if i == num:
        print('You guessed right')
        tries += 1
        print('\nYou took ' + str(tries) + ' tries')
        print('\nWindow will close now')
        time.sleep(3)
        break   
    elif i < num:
        print('You guessed too low')
        tries += 1
    elif i > num:
        print('You guessed to high')	
        tries += 1	
 
    # If you want the player to only have 5 tries put this into the while loop
    # if tries == 5:
        # print("Sorry, too many guesses you have lost. Window will close now")
        # time.sleep(3) 

        
