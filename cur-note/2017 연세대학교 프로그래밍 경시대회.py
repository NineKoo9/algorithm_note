def solution():
    N = int(input())
    count = 0
    for a in [n for n in range(2, 99) if n % 2 == 0]:
        for b in range(1, 99):
            for c in range(1, 99):
                if a + b + c != N:
                    continue
                if c >= b + 2:
                    count += 1
                
    print(count)

solution()