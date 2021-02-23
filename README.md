# random-winner
''' random number divide 2 times until 1
it takes input of number of players
and then the name for each player.
Those names are stored in the .txt file,
that later is modified according to code.

#program can be modified that it doesnt need user input, but can use already prepered .txt file

If the input for the number of players is 10, 
then it takes this number and divide it by two each time until reaches 1.
If the number is the odd number, then one of the player would lose because of that based on the score.

Based on a number of players there is calculationg players that supposed to be in each round.
Those number are collected into list, and then the length of rounds is determeined (len(list)).

Each score for player is a random number from 0 to 1000.
There is dictionary for player name and players score and based on that information 
the first half of player on top of the list goes into next tour. 


'''
