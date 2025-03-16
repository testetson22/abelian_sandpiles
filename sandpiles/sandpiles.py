import numpy as np

class SandPile():
    def __init__(self, x, y, z):
        """Initializes a SandPile instance that consists of a 2D Array and initial pile of sand reresented on the z axis

        Args:
            x (int): array dimension
            y (int): array dimension
            z (int): specifies pile height
        """
        
        #TODO consider separating some of this stuff out into functions for testability
        if not all(isinstance(i, int) for i in [x, y, z]):
            raise TypeError("Sandpile array dimensions and pile height must be int type")
        if not all(i > 0 for i in [x, y]):
            raise ValueError("Sandpile array dimensions must be greater than zero")
        
        self.sandpile = np.zeros((x, y), dtype=np.uint32)
        rows, cols = self.sandpile.shape
        self.center_row = rows // 2
        self.center_col = cols // 2
        self.sandpile[self.center_row, self.center_col] = z
        
    def get_sandpile_center_point(self):
        return (self.center_row, self.center_col)

    def apply_gravity(self):
        """Applying gravity will cause any pile with a height greater than 4 to collapse and be redistributed to adjacent positions in the array

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
                    for incx, incy in indicies_to_incr:
                        try:
                            sandpile[incx, incy] += distribution_incr
                        except IndexError:
                            raise IndexError(f"Sandpile height was too high to distribute within the array dimensions")
            self.apply_gravity()            
        return sandpile