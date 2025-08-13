def solution():
    N = int(input())
    
    count = 0
    for b in range(1, 501):
        for a in range(b, 501):
            if (a - b) * (a + b) == N:
                count += 1
    print(count)

solution()