class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        hash_map = defaultdict(list)
        hash_column = defaultdict(list)
        for i in range(9):
            bucket = set()
            for j in range(9):
                if board[i][j] == '.':
                    continue
                el = board[i][j]
                if bucket:
                    if el in bucket:
                        return False
                if hash_column[j]:
                    if el in hash_column[j]:
                        return False
                if hash_map[str(i//3)+str(j//3)]:
                    if el in hash_map[str(i//3)+str(j//3)]:
                        return False
                bucket.add(el)
                hash_column[j].append(el)
                hash_map[str(i//3)+str(j//3)].append(el)
        return True

                