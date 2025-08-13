def solution():
    N = int(input())
    # n 팩토리얼을 어떻게 구하지?
    answer = 1
    while N > 1:
        answer *= N
        N -= 1
    print(answer)
    
solution()