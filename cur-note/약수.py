def solution():
    N = int(input())
    yaks = list(map(int, input().split()))
    yaks.sort()
    print(max(yaks) * min(yaks) if len(yaks) > 1 else yaks[0]**2)
    
solution()