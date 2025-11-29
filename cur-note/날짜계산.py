def solution():
    E, S, M = map(int, input().split())
    
    year = 0
    while 1:
        if 1 + (year % 15) == E and 1 + (year % 28) == S and 1 + (year % 19) == M:
            print(year + 1)
            exit()
        year += 1
        
solution()