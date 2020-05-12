import sys, random

#variables to keep track of wins, losses, and ties


wins = 0
losses = 0
ties = 0



while True:
    print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties))
    while True:
        print('Enter your move: (r)ock, (p)aper, (s)cissors or (q)uit')
        playerMove = input()
        if playerMove == 'q':
            sys.exit()
        if playerMove == 'r' or playerMove == 'p' or playerMove == 's':
            break #break out of player input loop
        print('Type one of r, p, s, or q.')

    #display player selection
    if playerMove == 'r':
        print('Rock vs......')
    elif playerMove == 'p':
        print('Paper vs......')
    elif playerMove == 's':
        print('Scissors vs......')
        
        
    #display computer selection
    randomNumber = random.randint(1,3)
    if randomNumber == 1:
        computerMove = 'r'
        print('Rock')
    elif randomNumber == 2:
        computerMove = 'p'
        print('Paper')
    elif randomNumber == 3:
        computerMove = 's'
        print('Scissors')

    #display results comparing playerMove vs computerMove
    if playerMove == computerMove:
        print("It's a tie!")
        ties = ties + 1
    elif playerMove == 'r' and computerMove == 's': 
        print('You win!')
        wins = wins + 1
    elif playerMove == 'p' and computerMove == 'r':
        print ('You win!')
        wins = wins + 1
    elif playerMove == 's' and computerMove == 'p':
        print('You win!')
        wins = wins + 1
    elif computerMove == 'r' and playerMove == 's':
        print('You lose :(')
        losses = losses + 1
    elif computerMove == 'p' and playerMove == 'r':
        print('You Lose :(')
        losses = losses + 1
    elif computerMove == 's' and playerMove == 'p':
        print('You lose:(')
        losses = losses + 1