import numpy as np
#TODO need to handle/enforce boundary constraints based on pile size and redistribution

class SandPile():
    def __init__(self, x, y, z):
        """Initializes a SandPile instance that consists of a 2D Array and initial pile of sand reresented on the z axis

        Args:
            x (int): array dimension
            y (int): array dimension
            z (int): specifies pile height
        """
        
        self.sandpile = np.zeros((x, y), dtype=np.uint32)
        rows, cols = self.sandpile.shape
        row = rows // 2
        col = cols // 2        
        self.sandpile[row, col] = z

    def apply_gravity(self):
        """Applying gravity will cause qny pile with a height greater than 4 to collapse and be redistributed to adjacent positions in the array

        Returns:
            SandPile: a sandpile to apply gravity constraints to. 
        """
        sandpile = self.sandpile
        #TODO max_height, reduce_pile_by, and distribution_incr should be either inputs or calculatable.
        max_height = 4
        reduce_pile_by = 4
        distribution_incr = 1
        indicies = list(zip(*np.where(sandpile >= max_height)))
        if not indicies:
            sandpile
        else:
            while indicies:
                index = (indicies.pop())
                x = index[0]
                y = index[1]
                indicies_to_incr = [(x-1, y),(x, y-1),(x, y+1),(x+1, y)]
                while sandpile[x, y] >= max_height:
                    sandpile[x, y] -= reduce_pile_by
                    for x, y in indicies_to_incr:
                        sandpile[x, y] += distribution_incr
            self.apply_gravity()            
        return sandpile