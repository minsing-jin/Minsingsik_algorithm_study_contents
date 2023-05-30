def solution(s, skip, index):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    ans = ''
    skip = ''.join(set(skip))
    # skip 알파벳 alpha에서 빼기
    for i in alpha:
        for n in skip:
            if i == n:
                
                alpha = alpha.replace(i, "")
    
    for i in s:
        if alpha.index(i)+index < len(alpha):
            
            ans += alpha[alpha.index(i)+index]
        else:
            n = 1
            while True:
                if len(alpha)*n - (alpha.index(i)+index) >= 0:
                    ans += alpha[len(alpha)*n - (alpha.index(i)+index)]
                    break
                else:
                    n +=1
    return ans
