def solutiuon():
    from collections import defaultdict
    
    N = int(input())
    tmp = list(map(int, input().split()))
    having_cards = defaultdict(int)
    for num in tmp:
        having_cards[num] = 1
    
    
    M = int(input())
    compare_cards = list(map(int, input().split()))
    answer = []
    for card in compare_cards:
        if card in having_cards:
            answer.append(1)
        else:
            answer.append(0)
    
    return " ".join(map(str, answer))


print(solutiuon())
