class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        hash_map = defaultdict(set)
        column = defaultdict(set)
        for i in range(9):
            bucket = set()
            for j in range(9):
                if board[i][j] == '.':
                    continue
                el = board[i][j]
                if el in bucket or el in column[j] or el in hash_map[str(i//3)+str(j//3)]:
                    return False
                bucket.add(el)
                column[j].add(el)
                hash_map[str(i//3)+str(j//3)].add(el)
        return True

                