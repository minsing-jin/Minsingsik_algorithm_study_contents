# my sol
def solution(price, money, count):
    tmp = [(price*i) for i in range(1,count+1)]

    if money >= sum(tmp):
        return 0
    else:
        return sum(tmp) - money

      
      
      
# other sol
def solution(price, money, count):
    return max(0,price*(count+1)*count//2-money)
  


def solution(price, money, count):
    return abs(min(money - sum([price*i for i in range(1,count+1)]),0))
