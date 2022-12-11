# my sol
def solution(answers):
    A_score = 0
    B_score = 0
    C_score = 0

    # 필요한만큼 abc 찍는 방식 만들기
    a = [1,2,3,4,5]
    b = [2, 1, 2, 3, 2, 4, 2, 5]
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    a_rule = [a[i%len(a)] for i in range(len(answers))]
    b_rule = [b[i%len(b)] for i in range(len(answers))]
    c_rule = [c[i%len(c)] for i in range(len(answers))]
    print(a_rule)


    for i in range(len(answers)):
        if answers[i] == a_rule[i]:
            A_score += 1
        if answers[i] == b_rule[i]:
            B_score += 1
        if answers[i] == c_rule[i]:
            C_score += 1


    ans_arr = [A_score, B_score, C_score]

    ans = [i+1 for i in range(len(ans_arr)) if ans_arr[i] == max(ans_arr)]



    return ans  


# other sol
def solution(answers):
    pattern1 = [1,2,3,4,5]
    pattern2 = [2,1,2,3,2,4,2,5]
    pattern3 = [3,3,1,1,2,2,4,4,5,5]
    score = [0, 0, 0]
    result = []

    for idx, answer in enumerate(answers):
        if answer == pattern1[idx%len(pattern1)]:
            score[0] += 1
        if answer == pattern2[idx%len(pattern2)]:
            score[1] += 1
        if answer == pattern3[idx%len(pattern3)]:
            score[2] += 1

    for idx, s in enumerate(score):
        if s == max(score):
            result.append(idx+1)

    return result
