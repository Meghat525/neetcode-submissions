class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_seen = defaultdict(set)
        column_seen = defaultdict(set)
        grid_seen = defaultdict(set)
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] != ".":
                    if (board[i][j] in row_seen[i]) or (board[i][j] in column_seen[j]) or (board[i][j] in grid_seen[(i // 3 , j // 3)]):
                        return False
                    row_seen[i].add(board[i][j])
                    column_seen[j].add(board[i][j])
                    grid_seen[(i//3, j//3)].add(board[i][j])
        return True
        