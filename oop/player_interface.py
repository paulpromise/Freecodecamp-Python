from abc import ABC, abstractmethod
import random

class Player(ABC):
    def __init__(self):
        self.moves = []
        self.position = (0,0)
        self.path = [(0,0)]
        self.path = [self.position]
    
    def make_move(self):
        dx, dy = random.choice(self.moves)
        x, y = self.position
        self.position = (x + dx, y + dy)
        self.path.append(self.position)
        return self.position
    
    @abstractmethod
    def level_up(self):
        pass
    
class Pawn(Player):
    def __init__(self):
        super().__init__()
        self.moves = [
            (0, 1),    # up
            (0, -1),   # down
            (-1, 0),   # left
            (1, 0)     # right
        ]
    
   
    def level_up(self):
        diagonal_moves = [
            (1, 1),
            (1, -1),
            (-1, 1),
            (-1, -1)
        ]
        self.moves.extend(diagonal_moves)