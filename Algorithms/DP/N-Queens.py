# https://leetcode.com/problems/n-queens/

def n_queens(size):
    def dfs(queens, xy_dif, xy_sum):
        lng = len(queens)
        if lng == size:
            result.append(queens)
            return None
        for i in range(size):
            if i not in queens and lng-i not in xy_dif and lng+i not in xy_sum:
                dfs(queens+[i], xy_dif+[lng-i], xy_sum+[lng+i])
    result = []
    dfs([],[],[])
    return [["."*i + "Q"+"."*(size-i-1) for i in sol] for sol in result]


if __name__ == "__main__":
    print(n_queens(4))
    
"""
[['.Q..', '...Q', 'Q...', '..Q.'], ['..Q.', 'Q...', '...Q', '.Q..']]

Solution #1:    Solution #2:
.Q..            ..Q.
...Q            Q...
Q...            ...Q
..Q.            .Q..
"""