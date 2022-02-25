from player import *
from sprites import *

def build_map(self, tilemap):
    for i, row in enumerate(tilemap):
        for j, column in enumerate(row):
            Ground(self, j, i)

            if column == 'p':
                self.Player = Player(self, j, i)