'''
Created on Nov 23, 2019

@author: ITAUser
'''

#import the random library

#def a function called pick_random_word():
    #open and read word dictionary/list(words.txt)
    
    #create variable called index = select random word from words.txt
    #create variable called word = strip the randomly selected word
    #return variable 'word'
    
#def a function called ask_for_next_letter():
    #create a variable called letter = input function that asks the user to select a letter.
    #return the letter selected
    
#def a function called generate_word_string(word, letters_guessed):
    #create variable called output = empty list
    #make a for loop that goes through each letter in the variable 'word':
        #if statement that checks if letter is in letters_guessed:
            #append letter to output
        #else:
            #append ("_")
        #return output as a string
        
#create a main module:
    #variable called WORD = pick_random_word()
    
    #variable called letters_to_guess = set of WORD
    #variable called correct_letters_guessed = empty set
    #variable called incorrect_letters_guessed = empty set
    #variable called number_of_guesses = 5
    
    #print statement that welcomes the user to Hangman
    
    #while loop that runs until number_of_guesses is less than one or letters_to_guess is greater than zero:
        #variable called guess = ask_for_next_letter() and turn into lowercase
        
        #if statement that checks if guess is in correct_letters_guessed
            #print statement that says you already guessed that letter
            
        #if statement checks if guess is in letters_to_guess:
            #remove guess from letters_to_guess
            #add guess to correct_letters_guessed
        #else:
            #add guess to incorrect_letters_guessed
            #number_of_guesses goes down by one
        
        #create variable called word_string = generate_word_string(WORD, correct_letters_guessed)
        #print statement that prints word_string
        #print statement that prints how many guesses you have left
        
        #if statement to check if correct_letters_guessed is greater than the value:
            #print Congratulations, you won!
        #else:
            #print You lose! The word was WORD