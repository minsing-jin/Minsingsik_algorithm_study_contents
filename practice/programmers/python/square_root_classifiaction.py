# my
def solution(n):
    sqrt_n = n**0.5

    if sqrt_n - int(n**0.5) == 0:  
        return (n**0.5 + 1)**2

    return -1


  # other
def nextSqure(n):
    sqrt = n ** (1/2)

    if sqrt % 1 == 0:
        return (sqrt + 1) ** 2
    return 'no'
