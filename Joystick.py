def solution(name):
    # 대문자는 26개 문자 아스키에서 뺀 값과 여기서 뒤로 갔을 때를 계산해야한다
    # 파이썬 절대값 함수 abs()
    # 파이썬 아스키 함수 ord()
    answer = 0
    
    A = ord('A')
    
    for i in range(len(name)):
        rev = A-ord(name[i])+26
        seq = ord(name[i])-A
        
        #앞 뒤 중 짧은 걸로 알파벳 변경
        if rev > seq:
            answer += seq+1
        else:
            answer += rev+1
        
    if len(name) == 3 and name[1]=='A':
        answer-=1
    return answer-1
name = "JAZ"
print(solution(name))