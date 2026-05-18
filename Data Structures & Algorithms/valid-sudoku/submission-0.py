class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        row_check = [set() for i in range(9)]
        col_check = [set() for i in range(9)]
        box_check = [set() for i in range(9)]
        for r in range(9):
            for c in range(9):

                curr_val = board[r][c]
                box_index = (r // 3) * (3) + (c // 3)

                if curr_val == ".":
                    continue

                if (curr_val in row_check[r]) or (curr_val in col_check[c]) or (curr_val in box_check[box_index]):
                    return False
                else:
                    row_check[r].add(curr_val)
                    col_check[c].add(curr_val)
                    box_check[box_index].add(curr_val)
        return True
                 

        