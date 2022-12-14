# my sol
def solution(strings, n):
    strings.sort()
    strings.sort(key= lambda x: (x[n]))

    return strings


# other sol
def strange_sort(strings, n):
    '''strings의 문자열들을 n번째 글자를 기준으로 정렬해서 return하세요'''
    return sorted(strings, key=lambda x: x[n])
