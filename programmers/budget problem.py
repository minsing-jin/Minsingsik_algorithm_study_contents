# my solution
def solution(d, budget):
    d.sort()
    #print(d)
    Department = []
    default = 0
    for i in d:
        default += i
        print(default)
        if budget < default:
            return len(Department)


        Department.append(i)

    return len(Department)
    
  
  
# other solution
def solution(d, budget):
    d.sort()
    while budget < sum(d):
        d.pop()
    return len(d)
