def solution(n, lost, reserve):
#    lost, reserve 오름차순 가공
    lost.sort()
    reserve.sort()
    lost_copy = lost
    reserve_copy = reserve
    
        # 체육가능 students list 생성
    students = [i for i in range(1,n+1)]
    students_copy = students
    
    # reserve와 lost 비교 --> 같으면 reserve remove
    for i in lost:
        for n in reserve:
            if i == n:
                reserve_copy.remove(n)

    # 가공된 reserve와 lost 비교해서 체육 불가능 students 걸러내기
    for n in reserve_copy:
        for x in lost:
            if x-1 == n:
                lost_copy.remove(x)
         
            elif x+1 == n:
                lost_copy.remove(x)
             
            else:
                continue



# 체육 쌉가능 students만 걸러내기
    if len(lost_copy) == 0:
        return len(students)

    else:
        for i in lost_copy:
            for n in students:
                if i == n:
                    students_copy.remove(i)
    return len(students_copy)
