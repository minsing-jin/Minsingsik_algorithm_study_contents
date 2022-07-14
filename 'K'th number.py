# my solution

def solution(array, commands):
    answer = []

    for i in commands:
        if i[0] != i[1]:
            tmp = array[i[0]-1:i[1]]
            tmp.sort()
            print(tmp)
            answer.append(tmp[i[2]-1])
        else:
            tmp = array[i[0]-1]
            print(tmp)
            answer.append(array[i[0]-1])


    return answer



# answer other people
def solution(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))
# lambda x에 commands가 들어가서 array의 index를 지정해주고, sorted한 녀석의 index를 지정해줌
