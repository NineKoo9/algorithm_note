def solution():
    from collections import defaultdict
    
    N = int(input())
    my_cards = defaultdict(int)
    for card in list(map(int, input().split())):
        my_cards[card] += 1
        
    M = int(input())
    ur_cards = list(map(int, input().split()))
    answer = []
    for ur_card in ur_cards:
        if ur_card in my_cards:
            answer.append(my_cards[ur_card])
        else:
            answer.append(0)
    print(" ".join(map(str, answer)))

solution()