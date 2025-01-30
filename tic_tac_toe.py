"""
ana 2ly h3ml win gdid ya 3m
"""

class Player:
    def __init__(self) :
        self.name = ""
        self.symbol = ""
        self.number_of_wins = 0

    def choose_name(self) :
        while True:
            self.name =input("Please, enter your name using only letters.\n")
            if self.name.isalpha() :
                self.name = self.name.capitalize()
                break
            print("Invalid Name.")

    def choose_symbol(self):
        while True:
            self.symbol = input(f"enter the symbol you want to play with {self.name.capitalize()}. \n").capitalize()
            if len(self.symbol) == 1:
                self.symbol.capitalize()
                break
            print(f"Invalid Symbol {self.name.capitalize()}.")

class Menu :

    def main_menu(self):
        main_menu = """
1- Start 
2- Quit :(
(1 or 2):
"""
        while True :
            choice = input(main_menu)
            if choice.isdigit() and int(choice) > 0 and int(choice) < 3:
                return int(choice) 
            else :
                print("Invalid input You must enter 1 or 2.")

    def restart_menu(self):
        restart_menu = """
        Good Game Body
1- Play Again :)
2- Quit :( 
(1 or 2):
"""
        while True :
            choice = input(restart_menu)
            if choice.isdigit() and int(choice) > 0 and int(choice) < 3:
                return int(choice) 
            else :
                print("Invalid input You must enter 1 or 2.")

class Board:
    def __init__(self) :
        self.board = [str(i) for i in range(1,10)]

    def display_board(self):
        for i in range(0,9,3):
            print(" | ".join(self.board[i:i+3]))
            print( "-" * 9 )

    def update_board(self,pos,symbol): 
        if self.is_valid( pos):
            self.board[pos-1] = symbol
            return True
        return False

    def reset_board(self):
            self.board = [str(i) for i in range(1,10)]

    def is_valid(self,pos):
        return self.board[pos-1].isdigit()

class Game:
    def __init__(self) :
        self.players = [Player(),Player()]
        self.board = Board()
        self.menu = Menu()
        self.current_player_index = 0
        self.x =0 

    def game_start(self):
        clear_Screen()
        choice = self.menu.main_menu()
        if choice == 1:
            self.setup_players()
            self.new_game()
        else :
            self.quit_game_first_menu()

    def new_game(self):
        while True:
            self.play_turn()
            clear_Screen()
            if self.check_win() or self.check_draw() :

                choice = self.menu.restart_menu()
                if (choice) == 2 :
                    clear_Screen() 
                    self.quit_game()
                    break
                else:
                    self.restart_game()
                    clear_Screen() 

    def play_turn(self):
        self.board.display_board()
        while True :
            pos = input(f"{self.players[self.current_player_index].name} enter your move\n")
            if not pos.isdigit():
                print("you should only write integers")
                
            elif  int(pos) > 0 and int(pos) < 10:
                    self.board.board[int(pos)-1].isdigit()
                    break
            else :
                    print("Invaild Move already used.")
        clear_Screen()
        
        self.board.update_board(int(pos),self.players[self.current_player_index].symbol)
        self.current_player_index = 1 - self.current_player_index

    def setup_players(self):

        for p in self.players:
        
            print(f"player {self.current_player_index+1}")
            p.choose_name()
            p.choose_symbol()
            self.current_player_index = 1 - self.current_player_index
        clear_Screen()

    def check_win(self) :

        winning_combinations = [
            [0,1,2],[3,4,5],[6,7,8],
            [0,3,6],[1,4,7],[2,5,8],
            [0,4,8],[2,4,6]
        ]

        for combo in winning_combinations:
            if self.board.board[combo[0]] == self.board.board[combo[1]] == self.board.board[combo[2]]:
                self.board.display_board()
                self.players[self.current_player_index - 1 ].number_of_wins +=1
                if self.players[self.current_player_index - 1 ].number_of_wins == 1 :
                        print(f"{self.players[self.current_player_index - 1 ].name} Won {self.players[self.current_player_index - 1 ].number_of_wins} time ")
                else : 
                        print(f"{self.players[self.current_player_index - 1 ].name} Won {self.players[self.current_player_index - 1 ].number_of_wins} times ")

                return  True

        
        return False

    def check_draw(self) : 
        for n in self.board.board:
            if n.isdigit():
                return False
        self.board.display_board()
        print("Game has gone to it's end guys \nDraw   ")
        return True

    def restart_game(self):
        self.board.reset_board()
        self.current_player_index = 0
        self.new_game()

    def quit_game_first_menu(self):
        clear_Screen() 
    
    def quit_game(self):
        clear_Screen() 
        print("Thank you for playing","\nit was fun")

import os
def clear_Screen():
    return os.system("cls" if os.name=="nt" else "clear")

x = Game()
x.game_start()
