# Enter your code here. Read input from STDIN. Print output to STDOUT
def isPrime(num):
    flag = True

    for i in range(2, round(num**0.5)+1):
        if (num % i == 0):
            flag = False
    if (num == 1):
        flag = False
    elif (num == 2):
        flag = True

    if (flag):
        print("Prime")
    else:
        print("Not prime")


n = int(input())
for i in range(1, n+1):
    isPrime(int(input()))
