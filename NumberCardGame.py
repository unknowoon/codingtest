
deck1 = [[3,1,2],
        [4,1,4],
        [2,2,2]]

deck2 = [[7,3,1,8],
        [3,3,3,4]]

def solution(deck):
    result=0
    minList = []
    for row in deck: # whole list means card deck
        minList.append(min(row))
    result = max(minList)
    return result
print(solution(deck2))

# 파이썬 min max는 for loop와 같이 O(n)의 시간 복잡도를 갖는다.
#  하지만 min/max 함수는 바이트코드 인터프리터 오버헤드를 피할 수 있다고 한다.
# 출처 : https://stackoverflow.com/questions/35386546/big-o-of-min-and-max-in-python