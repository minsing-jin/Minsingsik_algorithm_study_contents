strings = ["abce", "abcd", "cdx"]
n = 1

tmp = []


for i in strings:
    tmp.append(i[n])

tmp.sort()
    
for i in strings:
    for x in tmp:
        if i[n] == x:
            tmp[tmp.index(x)] = i

ans
# tmp 요소들의 n번째 알파벳이 몇번째부터 몇번째까지 같은지 조사 -> sort
for i in range(1, len(tmp)):
    if tmp[i-1] == tmp[i]:
        idx = i-1 #번복되는 구간 찾기 마지막 녀석을 어떻게 count해야할지 아직 모르겠음
        
        
       
    
