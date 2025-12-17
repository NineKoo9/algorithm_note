def solution():
    s = input() # 서로다른 부분 문자열이라.. 확실한것은 연속되어야 한다는 것이다. 단순한 조합은 아니다. 솔직히 1000 이하이면 n * n/2 의 시간복잡도로 가능하다.
    answer = set()
    for i in range(len(s)):
        answer.add(s[i:])
        for j in range(i, len(s)):
            if s[i:j]:
                answer.add(s[i:j])    
    print(len(answer))

solution()