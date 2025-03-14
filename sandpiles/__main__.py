import sys
from .sandpiles import *

#TODO support proper flags for args
def main():
    print('in main')
    args = sys.argv[1:]
    x = args[0]
    y = args[1]
    z = args[2]
    print('')

    sand_pile = SandPile(x, y, z)
    sand_pile.apply_gravity()

if __name__ == '__main__':
    main()