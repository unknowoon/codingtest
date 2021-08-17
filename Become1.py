n = 25
k = 5

def solution(n, k):
    count = 0
    while True:
        if n == 1:
            break
        else:
            if n % k == 0:
                n = n/k
                count += 1
            else:
                n -= 1
                count += 1
    return count

def solution2(n, k):
    count = 0
    count = n%k
    n -= count
    while True:
        if n <= 1:
            break
        else:
            n = n /k
            count += 1
    return count
print(solution2(n, k))