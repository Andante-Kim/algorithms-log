# 백준 1018: 체스판 다시 칠하기
n, m = map(int, input().split())
count = 8*8
board = []

def re_color(board):
    w_start = ['WBWBWBWB','BWBWBWBW','WBWBWBWB','BWBWBWBW','WBWBWBWB','BWBWBWBW','WBWBWBWB','BWBWBWBW']
    b_start = ['BWBWBWBW','WBWBWBWB','BWBWBWBW','WBWBWBWB','BWBWBWBW','WBWBWBWB','BWBWBWBW','WBWBWBWB']
    count_w = 0
    count_b = 0

    for k in range(8):
        for t in range(8):
            if w_start[k][t] != board[k][t]:
                count_w += 1
            if b_start[k][t] != board[k][t]:
                count_b += 1
    return min(count_w, count_b)

# 체스판 입력
for _ in range(n):
    line = input()
    board.append(line)

# 살펴봐야 할 범위
search_n = n-7
search_m = m-7

new_board = []

for s_n in range(search_n):
    for s_m in range(search_m):
        part = board[s_n:s_n+8]
        for li in part:
            new_board.append(li[s_m:s_m+8])
        num = re_color(new_board)
        if num < count:
            count = num
        new_board = []
    
print(count)