from typing import Tuple

SHIPS = [
  ('Patrol Boat', 2),
  ('Submarine', 3),
  ('Destroyer', 3),
  ('Battleship', 4),
  ('Carrier', 5)
]


class Player:
  def __init__(self, name):
    self.name = name
    self.ships = self.create_ships()
    self.guesses = set()
    self.remaining_ships = len(SHIPS)
    
  def create_ships(self):
    pass

  def ship_placed(self) -> bool:
    pass


class Ship:
  def __init__(self, name, length):
    self.name = name
    self.length = length
    self.parts_intact = length
    self.placed = False
  

class Cell:
  def __init__(self):
    self.ships = {'computer': None, 'human': None}
    self.guesses = {'computer': False, 'human': False}


class Board:
  def __init__(self):
    self.size = 10
    self.cells = [[Cell() for i in range(self.size)] for i in range(self.size)]
    
  def attack_cell(self, coord: Tuple[int, int]) -> str:
    pass

  def valid_ship_placement(self, coord: Tuple[int, int], direction: str, player: str, ship: str) -> bool:
    pass

  def add_ship(self, coord: Tuple[int, int], direction: str, player: str, ship: str):
    pass

class Game:
  def __init__(self):
    self.board = Board()
    self.player = self.create_player()
    self.computer = Player('computer')

  def play_game(self):
    pass

  def initialize(self):
    # TODO add ships to board: computer
    # TODO add ships to board: player
    pass

  def start(self):
    pass

  def check_game_status(self):
    pass

  def add_ships(self, player: Player):
    pass

  def new_guess(self, coord: Tuple[int, int], player: Player) -> bool:
    pass

  def create_player(self):
    pass

  def display_board(self):
    pass

if __name__ == '__main__':
  game = Game()

  
  
  
  
