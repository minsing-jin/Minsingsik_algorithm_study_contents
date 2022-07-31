answers = [1,2,3,4,5]


A_1 = []
B_2 = []
C_3 = []
a_rule = [1,2,3,4,5]
b_rule = [2, 1, 2, 3, 2, 4, 2, 5]
c_rule = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

x = 0
# A
for i in range(len(answers)):

# 0/5 ==0 이라는 예외 발생
    if i%5==0:
        x = 0
        A_1.append(a_rule[x])
        print(a_rule[x])
        print(A_1[x])
  
    else:
        A_1.append(a_rule[x])
        x += 1
        print(a_rule[x])
        print(A_1[x])
print(A_1)  

"""
    elif i == 0:
        A_1.append(a_rule[x])
        x += 1
"""     
"""
    if i%5==0:
        x = 0
        A_1.append(a_rule[x])
    else:
        A_1.append(a_rule[x])
        x += 1
"""
"""
# B

    if i%8==0:
        x = 0
        B_2.append(b_rule[x])
    else:
        B_2.append(b_rule[x])
        x += 1
        
# C

    if i%10==0:
        x = 0
        C_3.append(c_rule[x])
    else:
        C_3.append(c_rule[x])
        x += 1
        """

score_a = 0
score_b = 0
score_c = 0

for i in range(len(answers))
    if answer[i] == A_3[i]:
        score_a += 1
    elif answer[i] == B_2[i]:
        score_b += 1
    elif answer[i] == C_3[i]:
        score_c += 1
        
rank = [score_a,score_b,score_c]
# 동점자 처리
if rank[0] == rank[1]:
    return [1,2]
elif rank[1] == rank[2]:
    return [2,3]
elif rank[0] == rank[2]:
    return [1,3]
elif rank[0] == rank[1] == rank[2]:
    return [1,2,3]

# 동점자 없을 경우
tmp = max[rank]
answer = rank.index(tmp)

return answer


