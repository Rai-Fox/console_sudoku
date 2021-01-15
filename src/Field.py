class Field:
    BLOCK_SIZE = 3
    SIZE = BLOCK_SIZE ** 2

    def __init__(self, cells=None):
        if cells is None:
            self.cells = [['.'] * Field.SIZE for _ in range(Field.SIZE)]
        else:
            self.cells = cells

    def print(self):
        for block in range(Field.BLOCK_SIZE):
            for j in range(Field.BLOCK_SIZE):
                self.__print_row(block * Field.BLOCK_SIZE + j)
            print()

    def __print_row(self, i):
        for block in range(Field.BLOCK_SIZE):
            for j in range(Field.BLOCK_SIZE):
                print(self.cells[i][block * Field.BLOCK_SIZE + j], end=" ")
            print(" ", end="")
        print()


