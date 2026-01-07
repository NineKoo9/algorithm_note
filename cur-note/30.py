def solution():
    N = input()
    
    lst_N = list(map(int, list(N)))
    if "0" not in N or sum(lst_N) % 3 != 0:
        print(-1)
        exit()
    print("".join(map(str, sorted(lst_N, reverse=True))))
    
solution()