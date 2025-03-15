import numpy as np
#TODO need to handle/enforce boundary contraints based on pile size and redistribution

class SandPile():
    def __init__(self, x, y, z):
        self.sandpile = np.zeros((x, y), dtype=np.uint32)
        rows, cols = self.sandpile.shape
        row = rows // 2
        col = cols // 2        
        self.sandpile[row, col] = z

    def apply_gravity(self):
        sandpile = self.sandpile
        indicies = list(zip(*np.where(sandpile >= 4)))
        if not indicies:
            sandpile
        else:
            while indicies:
                index = (indicies.pop())
                x = index[0]
                y = index[1]
                indicies_to_incr = [(x-1, y),(x, y-1),(x, y+1),(x+1, y)]
                while sandpile[x, y] >= 4:
                    sandpile[x, y] -= 4
                    for x, y in indicies_to_incr:
                        sandpile[x, y] += 1
            self.apply_gravity()            
        return sandpile