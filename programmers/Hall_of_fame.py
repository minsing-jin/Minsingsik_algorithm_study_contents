# my sol
def solution(k, score):
    myungye = []
    ans = []
    cnt = 0
    for i in score:
        myungye.append(i)

        if len(myungye) <= k:
            ans.append(min(myungye))

        if len(myungye) > k:
            if min(myungye) > i:
                ans.append(min(myungye))
            else:
                myungye.remove(min(myungye))
                ans.append(min(myungye))


    return ans
  
  
# other sol
def solution(k, score):

    q = []

    answer = []
    for s in score:

        q.append(s)
        if (len(q) > k):
            q.remove(min(q))
        answer.append(min(q))

    return answer
  
  
  
import heapq

def solution(k, score):
    max_heap = []
    answer = []

    for sc in score:
        heapq.heappush(max_heap, (-sc, sc))
        answer.append(max(heapq.nsmallest(k, max_heap))[1])

    return answer
