# m, k 더해야 하는 수, 제한
m, k = 8, 3
data = [2,4,5,4,6]

data.sort()

def solution1(m, k, data):
    result = 0
    count = 0
    lim = 0
    while True:
        if count < m:
            if lim < k:
                result += data[-1]
                count += 1
                lim += 1
            else:
                result += data[-2]
                lim = 0
                count += 1
        else:
            break
    return result

def solution2(m,k,data):
    result = 0
    dsum = data[-1]*k + data[-2]
    for i in range(m//(k+1)):
        result += dsum
    result += data[-1]*(m%(k+1))
    return result
print(solution2(m, k, data))