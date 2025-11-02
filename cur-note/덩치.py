def solution():
    N = int(input())
    persons = [list(map(int, input().split())) + [idx] for idx in range(N)]
    
    persons.sort()
    
    orders = [-1] * N
    for i in range(N):
        # 몸무게가 큰 사람을 기준으로 키를 비교한다.
        count = 0
        for j in range(i + 1, N):
            if persons[i][0] < persons[j][0] and persons[i][1] < persons[j][1]:
                count += 1
        orders[persons[i][2]] = count + 1
    print(*orders)
        
solution()