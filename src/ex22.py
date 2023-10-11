"""
Exercise 22 : Rock Paper Scissor
"""


def rps_check(player1, player2):
    """
    Check the result of a rock-paper-scissors game between two players.

    Parameters:
        p1 (str): The choice of player one. It can be 'rock', 'paper', or 'scissor'.
        p2 (str): The choice of player two. It can be 'rock', 'paper', or 'scissor'.

    Returns:
        str: The result of the game. It can be 'player one', 'player two', or 'tie'.
    """
    # TODO : complete this
    if player1 == 'rock' and player2 == 'scissors':
        return 'player one'
    elif player1 == 'rock' and player2 == 'paper':
        return 'player two'
    elif player1 == 'scissors' and player2 == 'paper':
        return 'player one'
    elif player1 == 'scissors' and player2 == 'rock':
        return 'player two'
    elif player1 == 'paper' and player2 == 'rock':
        return 'player one'
    elif player1 == 'paper' and player2 == 'scissors':
        return 'player two'
    else:
        return 'tie'
