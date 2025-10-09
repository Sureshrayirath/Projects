def play_higher_lower():
    
    # infinite loop to make user play 
    # game again and again.
    playing_game = True
    while playing_game:
        
        # variable to keep track fo suer's score, 
        # i.e., how many times he answers correctly
        score = 0
        
        # infinite loop to continue the current game play
        still_guessing = True
        while still_guessing:
            
            # print the logo after clearing the screen.
            clear()
            print(logo)
            
            # assign two account names to display
            person1 = assign()
            person2 = assign()
            
            # if we are not in first iteration, and user
            # input corret answer to previous iteration,
            # in that case, make account1 become account2
            # and randomly asing account2 some other account.
            if score > 0:
                person1 = person2
                person2 = assign()
                
                # we need to make sure that the two accounts
                # are not same.
                if person1 == person2:
                    person2 = assign()
            
            # display account1 name and description
            print(f"Name: {person1['name']}, Desc: {person1['description']}")
            
            # display the "VS" art
            print(vs)
            
            # display account2 name and description
            print(f"Name: {person2['name']}, Desc: {person2['description']}")
            
            # display current score
            print("----------------------------------------------")
            print(f"Your current score is: {score}")
            print("----------------------------------------------")
            
            # ask for user input
            guess = input("Enter name of person with Higher Followers: ")
            
            # see if user is correct
            if compare(person1, person2, guess):
              
                  # if user is correct continue to next iteration
                # and increase score by 1
                score += 1
            else:
                # if user is wrong, the current game play loop stops
                still_guessing = False
                
        # since the user was wrong in previous iteration and 
        # the game ended, ask him if he want to play again.
                
        play_again = input("Want to Play Again? (y/n): ").lower()
        
        # if he want to, continue, otherwise end the outer 
        # loop as well. also check if the user entered some
        # other input than what is allowed
        if play_again == 'y':
            continue
        elif play_again == 'n':
            playing_game = False
            clear()
            print("Game Exited Successfully")
        else:
            playing_game = False
            print("Invalid Input Taken as no.")
