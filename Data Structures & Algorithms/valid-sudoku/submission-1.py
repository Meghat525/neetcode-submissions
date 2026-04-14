class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(len(board)):
            seen_set = set()
            for j in range(len(board[i])):
                if board[i][j] != ".":
                    if board[i][j] in seen_set:
                        return False
                    seen_set.add(board[i][j])

        j = 0
        while j < 9:
            seen_set = set()
            for i in range(len(board)):
                if board[i][j] != ".":
                    if board[i][j] in seen_set:
                        return False
                    seen_set.add(board[i][j])
            j += 1

        i = j = 0
        row_grid_count = 0
        seen_set = set()
        while i < 9:
            while row_grid_count < 3:
                for j in range(row_grid_count * 3, 3 * row_grid_count+3):
                    if board[i][j] != ".":
                        if board[i][j] in seen_set:
                            return False
                        seen_set.add(board[i][j])
                i += 1
                if i % 3 == 0:
                    row_grid_count += 1
                    seen_set = set()
                if i % 3 ==0 and j != 8:
                    i = i - 3 
            row_grid_count = 0
            
        return True
        