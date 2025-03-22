def solution(X, Y):

  ans = ''
  for i in X:
    ans_idx = Y.find(i)
    if ans_idx != -1:
      ans += Y[ans_idx]
      Y = Y[:ans_idx] + Y[ans_idx+1:]
  print(ans)
  sorted(ans)
  print(type(ans))
  if len(ans) == 0:
    return '-1'

  if ans[0] == '0':
    return '0'
  
  # print(ans)
  return ans[::-1]


def solution(X, Y):
  X = sorted(X)
  Y = sorted(Y)
  copy_X = X
  copy_Y = Y
  ans = []
  for i in range(len(X)):
    for n in Y:
      if X[i] == n:
        ans.append(X[i])
        Y.remove(n)
  
  ans.sort(reverse = True)   
  
  if len(ans) == 0:
    return '-1'

  if ans[0] == '0':
    return '0'
  
  # print(ans)
  return ''.join(ans)





# 2번째 trial
def solution(X, Y):

    ans = ''
    tmp = []
    n = 0
    for i in X:
    
        while True:
            if n == len(Y) - 1:
                if i == Y[n]:

                    tmp.append(Y[n])
                    Y = Y[:n] + Y[n+1:]
                n = 0


                break


            if i == Y[n]:

                tmp.append(Y[n])
                Y = Y[:n] + Y[n+1:]
                break
            else:
                n += 1



    tmp.sort(reverse = True)
    
    if len(tmp) == 0:
        return '-1'
    if sum([int(i) for i in tmp]) == 0:
        return '0'

    return ''.join(tmp)

