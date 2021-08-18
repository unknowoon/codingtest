def solution(n, lost, reserve):
    answer = 0
    reserve1 = list(set(reserve)-set(lost))
    lost1 = list(set(lost)-set(reserve))
    answer = n - len(lost1)
    for i in lost1:
        if i-1 in reserve1:
            answer += 1
            reserve1.remove(i-1)
        elif i+1 in reserve1:
            answer += 1
            reserve1.remove(i+1)
    return answer