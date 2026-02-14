import sys

from matrix2Dim import Matrix2Dim


class Maze:
    def __init__(self,file_path:str):
        self.row_count = 0
        self.column_count = 0
        self.matrix = self.__read_file(file_path)
        self.result = ''

    def __str__(self):
        output = ""
        for i in range(self.row_count):
            for j in range(self.column_count):
                output += self.__int_to_character(self.matrix.get_element(i, j))
            output += '\n'
        return output

    def __read_file(self, file_path: str):
        try:
            with open(f'./{file_path}') as file:
                lines = file.readlines()
        except FileNotFoundError:
            raise FileNotFoundError('File does not exist')

        self.row_count = len(lines)
        self.column_count = len(lines[0])
        matrix = Matrix2Dim((self.row_count, self.column_count))
        for x, line in enumerate(lines):
            for y, character in enumerate(line):
                matrix.set_element(x, y, self.__character_to_int(character))

        return matrix

    def solve(self):
        if self.__findPathRec__(1, 1):
            path = self.result[::-1]
            print('Path:',path)
            print('Path length:',len(path))
            print(self)
        else:
            print('No path exists')

    def __is_valid_move__(self, i: int, j: int) -> bool:
        return self.matrix.get_element(i, j) == 1 or self.matrix.get_element(i, j) == 2

    def __findPathRec__(self, i: int, j: int) -> bool:
        if self.matrix.get_element(i, j) == 3:
            # B reached
            return True

        if self.__is_valid_move__(i, j):
            if self.matrix.get_element(i, j) != 2:
                # set already visited
                self.matrix.set_element(i, j, 4)
            if self.__findPathRec__(i - 1, j):
                if self.matrix.get_element(i - 1, j) != 3:
                    self.result += 'N'
                    self.matrix.set_element(i - 1, j, 5)
                return True
            elif self.__findPathRec__(i + 1, j):
                if self.matrix.get_element(i + 1, j) != 3:
                    self.result += 'S'
                    self.matrix.set_element(i + 1, j, 6)
                return True
            elif self.__findPathRec__(i, j - 1):
                if self.matrix.get_element(i + 1, j) != 3:
                    self.result += 'W'
                    self.matrix.set_element(i + 1, j, 7)
                return True
            elif self.__findPathRec__(i, j + 1):
                if self.matrix.get_element(i, j + 1) != 3:
                    self.result += 'E'
                    self.matrix.set_element(i, j + 1, 8)
                return True

            return False

        return False

    def __int_to_character(self, number: int) -> str:
        character_map = {0: '*', 1: ' ', 2: 'A', 3: 'B', 5: 'N', 6: 'S', 7: 'W', 8: 'E'}
        return character_map.get(number,' ')

    def __character_to_int(self, character: str) -> int:
        int_map = {'*':0,' ':1,'A':2,'B':3}
        # 9 helps to encode \n
        return int_map.get(character,9)


def main():
    file_path = sys.argv[1]
    try:
        maze = Maze(file_path)
        maze.solve()
    except FileNotFoundError:
        print('File not found')


if __name__ == '__main__':
    main()
