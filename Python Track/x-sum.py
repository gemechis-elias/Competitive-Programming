import sys
input = sys.stdin.readline
 
#        ---- Input Functions ----      #
def inp():
    return int(input())
def inlt():
    return list(map(int, input().split()))
def insr():
    s = input()
    return list(s[:len(s) - 1])
def invr():
    return map(int, input().split())
 
if __name__ == "__main__":
    t = inp()
 
    for i in range(t):
        ans = 0
        chess = []
        n,m = inlt()
        for _ in range(n):
            row = inlt()
            chess.append(row)
        right_diagonal = {}
        left_diagonal = {}
        for i in range(len(chess)):
            for j in range(len(chess[i])):
                right_diagonal[i + j] = right_diagonal.get(i + j, 0) + chess[i][j]
                left_diagonal[i - j] = left_diagonal.get(i - j,0) + chess[i][j]
        for i in range(len(chess)):
            for j in range(len(chess[i])):
                ans = max(ans, right_diagonal[i + j ] + left_diagonal[i - j] - chess[i][j])
        print(ans)
