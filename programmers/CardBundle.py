# my sol
def solution(cards1, cards2, goal):
    tmp_goal = []
    for i in range(len(goal)):
        print("goal: ", goal[i])


        if len(cards1) != 0:
            if goal[i] == cards1[0]:
                tmp_goal.append(goal[i])
                print(tmp_goal)
                cards1.remove(goal[i])


        if len(cards2) != 0:
            if goal[i] == cards2[0]:
                tmp_goal.append(goal[i])
                print(tmp_goal)
                cards2.remove(goal[i])

    if tmp_goal != goal:
        return "No"
    return "Yes"
    
    
 # other sol
def solution(cards1, cards2, goal):
    for g in goal:
        if len(cards1) > 0 and g == cards1[0]:
            cards1.pop(0)       
        elif len(cards2) >0 and g == cards2[0]:
            cards2.pop(0)
        else:
            return "No"
    return "Yes"
