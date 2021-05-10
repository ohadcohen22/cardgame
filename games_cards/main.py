from games_cards.CardGame import CardGame

from games_cards.Player import Player

player1 = Player(input("enter player 1 name,(name must be letters only): "))
player2 = Player(input("enter player 2 name,(name must be letters only): "))
game = CardGame(player1.name, player2.name)
print(game.player1.show())
print(game.player2.show())

for i in range(10):
    print(f"Round {i+1}")
    a = (game.player1.get_card())
    b = (game.player2.get_card())
    print(a)
    print(b)
    if a > b:
        game.player2.add_card(b)
        game.player2.add_card(a)
        print(f"the winner is {player1.name}")

    if a < b:
        game.player1.add_card(b)
        game.player1.add_card(a)
        print(f"the winner is {player2.name}")


print(f" The winner of the game is : {game.get_winner()}")
