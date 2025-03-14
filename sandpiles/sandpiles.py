import numpy as np
#TODO need to handle/enforce boundary contraints based on pile size and redistribution

class SandPile():
    def __init__(self, x, y, z):
        self.sandpile = np.zeros((x, y), dtype=np.uint32)
        #TODO calculate centerpoint
        self.sandpile[2, 2] = z
        
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
                while sandpile[x, y] >= 4:
                    sandpile[x, y] -= 4
                    sandpile[x-1, y] += 1
                    sandpile[x, y-1] += 1
                    sandpile[x, y+1] += 1
                    sandpile[x+1, y] += 1
            self.apply_gravity(sandpile)
            
        return sandpile