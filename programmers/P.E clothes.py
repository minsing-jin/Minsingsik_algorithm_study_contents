# my sol

import copy
def solution(n, lost, reserve):
    #    lost, reserve 오름차순 가공
    lost.sort()
    reserve.sort()

    lost_copy = copy.deepcopy(lost)
    reserve_copy = copy.deepcopy(reserve)


        # 체육가능 students list 생성
    students = [i for i in range(1,n+1)]
    students_copy = copy.deepcopy(students)

    # reserve와 lost 비교 --> reserve중에서 lost한 사람 걸러내기--> 같으면 reserve remove
    for i in lost_copy:
        for n in reserve_copy:
            if i == n:
                reserve.remove(n)
                lost.remove(n)

    reserve_copy2 = reserve
    lost_copy2 = lost

    # 뭔가 복사에 오류가 생김 -> 깊은복사 얇은복사 메모리만 참고하는지 check

    # 가공된 reserve와 lost 비교해서 체육 불가능 students 걸러내기
    for n in reserve_copy2:
        for x in lost_copy2:
            try:
                if x-1 == n:
                    lost.remove(x)
                elif x+1 == n:
                    lost.remove(x)

                else:
                    continue
            except:
                continue
    # print(len(lost))
    print(lost)


    # 체육 쌉가능 students만 걸러내기
    if len(lost) == 0:
        return(len(students))

    else:
        for i in lost:
            for n in students_copy:
                if i == n:
                    students.remove(i)
        print(len(students))
        return len(students)

    
    
 # ohter sol 1.
def solution(n, lost, reserve):
    new_lost = list(set(lost) - set(reserve))
    new_reserve = list(set(reserve) - set(lost))

    for r in new_reserve:
        if r - 1 in new_lost:
            new_lost.remove(r - 1)
        elif r + 1 in new_lost:
            new_lost.remove(r + 1)
    return n - len(new_lost)


# other sol 2.

def solution(n, lost, reserve):
    _reserve = [r for r in reserve if r not in lost]
    _lost = [l for l in lost if l not in reserve]
    for r in _reserve:
        f = r - 1
        b = r + 1
        if f in _lost:
            _lost.remove(f)
        elif b in _lost:
            _lost.remove(b)
    return n - len(_lost)

# 주로 답에서는 students를 카운팅하기보다는 원래 인원에서 lost한 인원을 빼는 아이디어를 생각함.
# 내 아이디어로 할려면 copy본이 손상되지 않도록 depp copy와 shallow copy 개념을 알아야했음!
    
