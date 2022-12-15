def solution(number):
    
    minus = [i for i in number if i < 0]
    plus = [i for i in number if i > 0]

    m_ans = 0
    # 1번 case
    for m in range(len(minus)):
        for p_1 in range(len(plus)):
            tmp_plus = plus[:p_1] + plus[p_1+1:]
            for p_2 in tmp_plus:
                if (minus[m]+plus[p_1]+p_2) == 0:
                    m_ans += 1

                else:
                    continue


    p_ans = 0
    # 2번 case
    for p in range(len(plus)):
        for m_1 in range(len(minus)):
            tmp_minus = minus[:m_1] + minus[m_1+1:]
            for m_2 in tmp_minus:
                if (plus[p]+minus[m_1]+m_2) == 0:
                    p_ans += 1
                
                else:
                    continue


    # 3번 case:
    z_ans = 0
    if 0 in number:
        for i in minus:
            for n in plus:
                if i + n == 0:
                    z_ans += 1
    
    # 4번 case:
    tmp_zero = 0
    z2_ans = 0
    for i in number:
        if i == 0:
            tmp_zero += 1
    
    z2_ans += tmp_zero // 3
    
    
    ans = (p_ans+m_ans)/2 + (z_ans) + z2_ans




    return int(ans)


'''
1. 음수인 수를 하나 뽑아서 양수인 두녀석을 더해보며 체크
2. 양수인 수 한개를 뽑아서 음수인 두녀석을 더해보며 체크
3. 0이 있을경우 음수 양수 같은 숫자가 있어야함
4. 0만 가지고 있는 경우 혹은 0이 압도적으로 많은 경우
'''
