class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [set() for _ in range(9)]
        column = [set() for _ in range(9)]
        square = [set() for _ in range(9)]
        for i in range(9):
            for j in range(9):
                if (board[i][j] == "."):
                    continue
                num = board[i][j]
                square_index = int((i/3)) * 3 + int((j/3))
                if num in row[i] or num in column[j] or num in square[square_index]:
                    return False
                else:
                    row[i].add(num)
                    column[j].add(num)
                    square[square_index].add(num)
        return True