def solution():
    N, M = map(int, input().split())  # N, M은 최대 100000
    passwords = [input().split() for _ in range(N)]
    passwords_dict = {site: password for site, password, in passwords}
    
    for _ in range(M):
        target_addr = input()
        print(passwords_dict[target_addr])

solution()