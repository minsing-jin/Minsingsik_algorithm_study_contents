# my sol
def solution(name, yearning, photo):
    miss_name = {name: score for name, score in zip(name, yearning)}
    
    
    
    ans = []
    miss_score = 0
    for group in photo:
        for people_name in group:

          for filtering in name:

            if filtering == people_name:
                miss_score += miss_name[people_name]
                print(miss_name[people_name])
        print("저장", miss_score)
        ans.append(miss_score)
        miss_score = 0

        
    
    return ans
  
# others
def solution(이름, 점수, 사진):
    return [sum(점수[이름.index(j)] for j in i if j in 이름) for i in 사진]
