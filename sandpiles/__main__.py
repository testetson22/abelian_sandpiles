import sys
from .sandpiles import *

#TODO support proper flags, type handling, etc for args
def main():
    print('in main')
    args = sys.argv[1:]
    x = int(args[0])
    y = int(args[1])
    z = int(args[2])
    print('')

    sand_pile = SandPile(x, y, z)
    print(sand_pile.apply_gravity())

if __name__ == '__main__':
    main()