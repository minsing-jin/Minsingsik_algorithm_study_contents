# my sol

def solution(dartResult):
    import math

    # 10,100자릿수 
    tmp = [(dartResult[x] + dartResult[x+1]) if dartResult[x].isdigit() and dartResult[x+1].isdigit() == True else dartResult[x] for x in range(len(dartResult))]




    num_lst = [x for x in dartResult if x.isdigit() == True]



    result_collect = []
    score = 0


    for i in range(len(tmp)):


        if tmp[i].isdigit() == True:
            score += int(tmp[i])
            print(score)

    # s d t 숫자 제곱들
        elif tmp[i] == 'S':
            #print(score)
            result_collect.append(score)
            score = 0
        elif tmp[i] == 'D':
            score = score**2
            result_collect.append(score)
            score = 0
        elif tmp[i] == 'T':
            score = int(math.pow(score,3))
            result_collect.append(score)
            score = 0

    # 샾이랑 별로 특수효과 부여하는 line
        elif tmp[i] == '#':
            result_collect[num_lst.index(tmp[i-2])] = result_collect[num_lst.index(tmp[i-2])]*(-1)
            print(result_collect)
        elif tmp[i] == '*':
            if len(result_collect) <= 1:

                result_collect[num_lst.index(tmp[i-2])] = result_collect[num_lst.index(tmp[i-2])]*(2)

            else:
                result_collect[num_lst.index(tmp[i-2])] = result_collect[num_lst.index(tmp[i-2])]*(2)
                result_collect[num_lst.index(tmp[i-2])-1] = result_collect[num_lst.index(tmp[i-2])-1]*(2)

    ans = int(sum(result_collect))


    return ans
  
  
  # other sol
  import re


def solution(dartResult):
    bonus = {'S' : 1, 'D' : 2, 'T' : 3}
    option = {'' : 1, '*' : 2, '#' : -1}
    p = re.compile('(\d+)([SDT])([*#]?)')
    dart = p.findall(dartResult)
    for i in range(len(dart)):
        if dart[i][2] == '*' and i > 0:
            dart[i-1] *= 2
        dart[i] = int(dart[i][0]) ** bonus[dart[i][1]] * option[dart[i][2]]

    answer = sum(dart)
    return answer

