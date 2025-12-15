def solution():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    
    A.sort()
    B.sort(reverse=True)
    
    answer_lst = [a * b for a, b in zip(A, B)]
    print(sum(answer_lst))

solution()