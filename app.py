#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return app.send_static_file("index.html")

#define constants to define the options rock, paper or scissors
ROCK = "rock"
PAPER = "paper"
SCISSORS = "scissors"

#set a list of options
OPTIONS = [ROCK, PAPER, SCISSORS]

#define rules for the game: rock beats scissors, paper beats rock, scissors beats paper
RULES = {
    ROCK: SCISSORS,
    PAPER: ROCK,
    SCISSORS: PAPER
}

#function to determine the winner
def determine_winner(user_choice, computer_choice):
    #if the user and computer choice are the same, it's a tie
    if user_choice == computer_choice:
        return "tie"
    #if the user choice beats the computer choice, the user wins
    elif RULES[user_choice] == computer_choice:
        return "user"
    #otherwise the computer wins
    else:
        return "computer"
    
#function to play the game
def play_game(user_choice):
    #import the random module
    import random
    #get the computer choice from the list of options
    computer_choice = random.choice(OPTIONS)
    #determine the winner
    winner = determine_winner(user_choice, computer_choice)
    #print the winner
    result = "You chose " + user_choice + ", the computer chose " + computer_choice + "."

    #if the result is a tie, print that it's a tie
    if winner == "tie":
        result += " It's a tie."
    else:
        result += " The winner is " + winner + "."

    print( result )
    #return the winner
    return winner

#function to keep the score of the game and another function to return the score
def main():
    #set the initial score to 0
    score = 0
    round = 0
    #play the game while the user wants to play using a do while
    while True:
        #ask the user if they want to play the game
        play_again = input("Would you like to play rock, paper, scissors? ")
        while play_again not in ["yes", "no"]:
            #if the user says no, break out of the loop
            if play_again == "no":
                break
            #if the user says yes, continue the loop
            elif play_again == "yes":
                continue
            #if the user enters anything else, ask them again
            else:
                play_again = input("Invalid choice. Please enter yes or no: ")
        
        #if the user says no, break out of the loop
        if play_again == "no" :
            #print the final score, if the user played at least one round
            if round > 0:
                print("After "+ str(round) +" round(s). You won " + str(score) + " times.")
                
            break
        
        round += 1
        #show the current round number
        print("Round " + str(round) )
        #the user choice is entered by the user
        user_choice = input("Enter rock, paper, or scissors: ")
        #validate the user choice
        while user_choice not in OPTIONS:
            user_choice = input("Invalid choice. Please enter rock, paper, or scissors: ")
        #determine the winner
        winner = play_game(user_choice)
        #if the user wins, add 1 to the score
        if winner == "user":
            score += 1


main()