# my sol
def solution(board, moves):
    tmp = []

    cnt = 0

    for i in moves: # column
        for x in range(len(board)): # row
            if board[x][i-1] == 0:
                continue
            else:
                tmp.append(board[x][i-1])
                board[x][i-1] = 0
                if len(tmp) > 1:
                    print(len(tmp))
                    if tmp[len(tmp)-2] == tmp[len(tmp)-1]:
                        cnt += 1
                        del tmp[len(tmp)-2]
                        del tmp[len(tmp)-1]
                break
    return cnt*2

# other sol
def solution(board, moves):
    cols = list(map(lambda x: list(filter(lambda y: y > 0, x)), zip(*board)))
    a, s = 0, [0]

    for m in moves:
        if len(cols[m - 1]) > 0:
            if (d := cols[m - 1].pop(0)) == (l := s.pop()):
                a += 2
            else:
                s.extend([l, d])

    return a
