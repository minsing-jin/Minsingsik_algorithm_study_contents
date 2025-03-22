input_num = int(input())


for i in range(2, int(input_num**(1/2)) + 1):
    while True:
        if input_num % i ==0:
            print(i)
            input_num //= i
        else:
            break

if input_num > 1:
    print(input_num)
