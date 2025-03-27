n, m = map(int,input().split())
board = []
answer_B = ['BWBWBWBW','WBWBWBWB','BWBWBWBW','WBWBWBWB','BWBWBWBW','WBWBWBWB','BWBWBWBW','WBWBWBWB']
answer_W = ['WBWBWBWB','BWBWBWBW','WBWBWBWB','BWBWBWBW','WBWBWBWB','BWBWBWBW','WBWBWBWB','BWBWBWBW']
for i in range(n):
    board.append(list(str(input())))


cnt = []

for i in range(n-8+1):
    for j in range(m-8+1):
        
        tmp = 0
        for k in range(i,i+8):      
            for l in range(j,j+8):
                if board[k][l] == answer_B[k-i][l-j]:
                    continue
                else:
                    tmp +=1
        cnt.append(tmp)

        tmp = 0
        for k in range(i,i+8):
            for l in range(j,j+8):
                if board[k][l] == answer_W[k-i][l-j]:
                    continue
                else:
                    tmp +=1
        cnt.append(tmp)

print(min(cnt))