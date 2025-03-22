# my sol
def solution(s, n):

    A = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    a = 'abcdefghijklmnopqrstuvwxyz'
    tmp = [i for i in s]

    for i in range(len(tmp)):
        if tmp[i].isalpha() == True:
            A.find(s[i])
            a.find(s[i])
        if A.find(s[i]) != -1:

            tmp[i] = A[((A.find(s[i])+n)%len(A))]

        if a.find(s[i]) != -1:

            tmp[i] = a[((a.find(s[i])+n)%len(a))]


    return ''.join(tmp)


# other sol
def caesar(s, n):
    s = list(s)
    for i in range(len(s)):
        if s[i].isupper():
            s[i]=chr((ord(s[i])-ord('A')+ n)%26+ord('A'))
        elif s[i].islower():
            s[i]=chr((ord(s[i])-ord('a')+ n)%26+ord('a'))

    return "".join(s)
    # 주어진 문장을 암호화하여 반환하세요.


# 실행을 위한 테스트코드입니다.
print('s는 "a B z", n은 4인 경우: ' + caesar("a B z", 4))




def solution(s, n):
    return ''.join([chr(ord(i) + (not ord(i)==32)*((n%26) -26*((90<(ord(i)+(n%26))*(ord(i)<91)) + (122<(ord(i)+(n%26)))))) for i in s])
